"""Test init and tear down methods"""

import fnmatch
import json
import logging as logger
import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, Page, Playwright
from config.config import TestConfig as test_config
from config.pages import PAGES
from pages.login import LoginPage
from utils.common import CommonUtils as common_utils

load_dotenv(override=True)


RECORD_VIDEO = os.getenv("RECORD_VIDEO") == "TRUE"
ARGS = ["--start-maximized"]


@pytest.fixture(scope="session", autouse=True)
def _init_session_for_test():
    video_folder = f"{test_config.VIDEOS_PATH}{common_utils.get_date_month_year_string()}"
    setup_video_folder(video_folder)  # Uncomment if setup is needed
    yield video_folder
    clean_up_video_folder(video_folder)  # Uncomment if cleanup is needed


def _get_browser(playwright: Playwright, request: pytest.FixtureRequest) -> Browser:
    _browser = common_utils.get_env("BROWSER")
    if not _browser:
        _browser = request.config.getoption("browser_name")
    _browser = _browser.upper()
    _headless = request.config.getoption("--headless")
    headless = _headless.upper() == "TRUE"
    _slow_mo = request.config.getoption("--slow-mo")
    slow_mo = int(_slow_mo) if _slow_mo else int(os.getenv("SLOW_MO", "100"))

    browser_launchers = {
        "CHROME": lambda: playwright.chromium.launch(channel="chrome", headless=headless, slow_mo=slow_mo, args=ARGS),
        "CHROMIUM": lambda: playwright.chromium.launch(headless=headless, slow_mo=slow_mo, args=ARGS),
        "EDGE": lambda: playwright.chromium.launch(channel="msedge", headless=headless, slow_mo=slow_mo, args=ARGS),
        "SAFARI": lambda: playwright.webkit.launch(headless=headless, slow_mo=slow_mo),
        "FIREFOX": lambda: playwright.firefox.launch(headless=headless, slow_mo=slow_mo),
        "WEBKIT": lambda: playwright.webkit.launch(headless=headless, slow_mo=slow_mo),
    }

    browser_launcher = browser_launchers.get(_browser, lambda: playwright.chromium.launch(headless=headless, slow_mo=slow_mo, args=ARGS))

    return browser_launcher()


def new_page(browser: Browser, video_folder, headless):
    # Set viewport size based on headless mode
    viewport_size = {"width": 1920, "height": 1080} if headless else None
    page_options = {"ignore_https_errors": True}

    if viewport_size:
        page_options["viewport"] = viewport_size
    else:
        page_options["no_viewport"] = True

    if RECORD_VIDEO:
        page_options["record_video_dir"] = video_folder
        page_options["record_video_size"] = {"width": 1920, "height": 1080}

    page = browser.new_page(**page_options)
    page.set_default_timeout(8000)

    # Load the storage state after the page is created
    if os.getenv("SAVE_CONTEXT", "True").upper() == "TRUE":
        if not common_utils.file_is_empty(test_config.CONTEXT_FILE):
            with open(test_config.CONTEXT_FILE, "r", encoding="utf-8") as f:
                storage_state = json.load(f)
                page.context.add_cookies(storage_state["cookies"])
    return page


@pytest.fixture(scope="function", autouse=True)
def _init_test(playwright: Playwright, _init_session_for_test, _api_session, request: pytest.FixtureRequest):
    """Fixture to initialize test without logging in."""
    browser = _get_browser(playwright, request)
    video_folder = f"{_init_session_for_test}/{get_test_class_name()}"
    headless = request.config.getoption("--headless").upper() == "TRUE"
    page: Page = new_page(browser, video_folder, headless)
    context = browser.contexts[0]
    start_trace(context)
    page.goto(f"{test_config.HOME_PAGE}/{PAGES.home}", wait_until="domcontentloaded")
    login_page = LoginPage(page)
    login_page.confirm_if_in_page()
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    login_page.login(user_name, password)
    request.cls.page = page
    request.cls.browser = browser
    request.cls.context = context
    yield page

    end_trace(context)
    _close_context(context, page, video_folder)
    browser.close()


def _close_context(context: BrowserContext, page: Page, video_folder):
    try:
        if os.getenv("SAVE_CONTEXT", "True").upper() == "TRUE":
            context.storage_state(path=test_config.CONTEXT_FILE)
        if RECORD_VIDEO:
            existing_video_name = page.video.path()
            new_video_name = set_video_name(video_folder)
            if os.path.exists(existing_video_name):
                if os.path.exists(new_video_name):
                    os.remove(new_video_name)
                os.rename(existing_video_name, new_video_name)
    except FileNotFoundError:
        logger.warning("Video file not found; skipping renaming.")
    except Exception as e:
        logger.error(f"Exception while closing context for test {get_test_class_name()}: {str(e)}")


def get_test_class_name():
    """Extract and return the class name of the current test."""
    return os.getenv("PYTEST_CURRENT_TEST", "").split("::")[1].replace("Test", "")


def get_test_name():
    """Extract and return the name of the current test, removing specific browser markers."""
    current_test = os.getenv("PYTEST_CURRENT_TEST", "")
    test_name = current_test.split(":")[-1].split(" ")[0]
    return test_name.replace("[chromium]", "").lower()


def set_video_name(video_folder):
    """Generate a path for the video file based on the test name."""
    return os.path.join(video_folder, f"{get_test_name()}.webm")


def clean_up_video_folder(folder):
    """Clean up the video folder by removing files that don't contain 'test_' in their names."""
    try:
        if os.path.isdir(folder):
            for dirpath, _, filenames in os.walk(folder):
                for file in filenames:
                    if "test_" not in file:
                        os.remove(os.path.join(dirpath, file))
    except Exception as e:
        logger.error(f"Exception while cleaning up video folder: {str(e)}")


def start_trace(context: BrowserContext):
    """Start tracing in the given context if tracing is enabled."""
    if test_config.TRACE_ENABLED:
        try:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
        except Exception as e:
            logger.error(f"Exception while starting trace: {str(e)}")


def end_trace(context: BrowserContext):
    """Stop tracing and save the trace file to a specified path."""
    if test_config.TRACE_ENABLED:
        try:
            trace_folder = os.path.join(test_config.TRACE_PATH, get_test_class_name())
            os.makedirs(trace_folder, exist_ok=True)
            trace_path = os.path.join(trace_folder, f"{get_test_name()}.zip")
            if os.path.exists(trace_path):
                os.remove(trace_path)
            context.tracing.stop(path=trace_path)
        except Exception as e:
            logger.error(f"Exception while ending trace: {str(e)}")


def setup_video_folder(folder):
    """This is no longer required. we will not clear all files in the folder before starting a test"""
    try:
        if os.path.isdir(folder):
            for dirpath, _, filenames in os.walk(folder):
                for file in filenames:
                    if fnmatch.fnmatch(file, "*.webm"):
                        os.remove(os.path.join(dirpath, file))
    except FileNotFoundError:
        logger.info("exception while cleaning up video folder")
