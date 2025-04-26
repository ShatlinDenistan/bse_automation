import datetime
import logging as logger
import os
from typing import Dict
from dotenv import find_dotenv, load_dotenv

import pytest
import requests
from pytest import CollectReport, StashKey
from jira import JIRA

from config.config import TestConfig as test_config
from utils.common import CommonUtils as common_utils


load_dotenv(find_dotenv(usecwd=True), override=True)

phase_report_key = StashKey[Dict[str, CollectReport]]()

overall_summary = {}


def pytest_addoption(parser):
    """Add custom CLI options for browser configuration"""
    parser.addoption("--browser_name", action="store", default="chromium")
    parser.addoption("--headless", action="store", default="False")
    parser.addoption("--slow-mo", action="store", default=None)


@pytest.fixture(scope="session", autouse=True)
def session_setup_and_teardown():
    """Set up before all tests and log the summary after all tests"""
    session_start_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    start_time = common_utils.start_tracking_time()

    if not os.path.isfile(test_config.CONTEXT_FILE):
        open(test_config.CONTEXT_FILE, mode="w", encoding="UTF-8")

    yield

    logger.info(_construct_log_header_and_footer_line("Test Summary"))
    for key, value in overall_summary.items():
        if "pass" in value:
            logger.info("%s : %s", key, value)
    for key, value in overall_summary.items():
        if "skip" in value:
            logger.info("%s : %s", key, value)
    for key, value in overall_summary.items():
        if "fail" in value:
            logger.info("%s : %s", key, value)

    passed = len([x for x in overall_summary.values() if "pass" in x])
    failed = len([x for x in overall_summary.values() if "fail" in x])
    skipped = len([x for x in overall_summary.values() if "skip" in x])

    summary = f"passed = {passed} , failed = {failed} , skipped = {skipped}"
    logger.info("%s", summary)
    current_datetime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logger.info("Test run started at: %s", session_start_time)
    logger.info("Test run completed at: %s", current_datetime)
    common_utils.end_tracking_time(start_time)


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    """Hook to store test reports for each phase"""
    outcome = yield
    item.stash.setdefault(phase_report_key, {})[outcome.when] = outcome
    return outcome


@pytest.hookimpl
def pytest_exception_interact(_, call):
    """Hook to log exception info"""
    exception = call.excinfo.exconly()
    logger.info("%s", exception)


def update_jira(request, result, duration):
    """Update test result in JIRA if enabled"""
    if not test_config.UPDATE_JIRA:
        return
    try:
        duration = duration.replace("s", "")
        duration = float(duration)
    except Exception:
        duration = -1

    test_result = result.upper()
    if test_result == "PASS" or test_result == "SKIP":
        test_result = 10711
    elif test_result == "FAIL":
        test_result = 10712
    else:
        return

    jiraOptions = {"server": test_config.JIRA}
    jira = JIRA(options=jiraOptions, basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_TOKEN")))
    markers = [mark.name.upper() for mark in request.node.iter_markers() if mark.name.upper().startswith("PC_")]
    if "MP_UI" in markers:
        markers.remove("MP_UI")
    for marker in markers:
        if "MP_UI" in marker:
            continue
        key = marker.replace("_", "-")
        try:
            ticket = jira.issue(key)
            ticket.update(
                fields={
                    "customfield_11491": {"id": f"{test_result}"},
                    "customfield_11492": request.node.name,
                    "customfield_11530": test_config.HOME_PAGE,
                    "customfield_11531": duration,
                }
            )
        except Exception as e:
            logger.info("Error while trying update JIRA: %s in %s", e, key.strip())


@pytest.fixture(autouse=True)
def log_test_name(request):
    """Log test name and result before and after each test"""
    result = "unknown"
    test_name = request.node.nodeid.split("::")[-1]
    logger.info(_construct_log_header_and_footer_line(f" {test_name} "))
    if test_config.LOG_DETAIL is True:
        scenario = request.function.__doc__
        if scenario:
            scenario = scenario.replace("\n", " ")
        common_utils.log(f"Scenario: {scenario if scenario else 'Scenario / docstring not provided'}")
    yield

    report = request.node.stash[phase_report_key]
    duration = f'{report["call"].duration:.4f}s'

    if ("call" not in report) or report["call"].failed:
        result = "fail"
    elif report["call"].skipped:
        result = "skip"
    elif report["call"].passed:
        result = "pass"

    comment = f"{result} : duration: {duration}"
    if test_name in overall_summary:
        comment += f" : {overall_summary[test_name]}"
    overall_summary[test_name] = comment

    logger.info("Test result: %s         Test run time: %s\n", result, duration)


def _construct_log_header_and_footer_line(text):
    """Construct a header or footer line with text centered"""
    filler_full_length = 70
    filler_length = (filler_full_length - len(text)) // 2
    filler_left = filler_length
    if filler_length % 2 == 1:
        filler_left = filler_length + 1
    return f'{"=" * filler_left}{text}{"=" * filler_length}'


def pytest_configure(config):
    """Configure logging per worker for parallel test execution"""
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id is not None:
        worker_id = worker_id.replace("gw", "")
        logger.basicConfig(
            format=config.getini("log_file_format"),
            filename=f"./output/logs/takealot_automation_{worker_id}.log",
        )


@pytest.fixture(scope="session", autouse=True)
def _api_session():
    """Create the one-time API session for all tests"""

    session = requests.Session()
    session.base_url = test_config.BFF_URL
    session.test_data_service = test_config.TEST_DATA_SERVICE
    auth_data = {
        "email": os.getenv("USER_NAME"),
        "password": os.getenv("PASSWORD"),
    }
    auth_url = f"{session.base_url}/authenticate"
    header = {"Content-Type": "application/json"}
    response = session.post(url=auth_url, json=auth_data, headers=header, verify=False)
    response = response.json()
    token = response.get("token", "")
    session.headers = {"Content-Type": "application/json", "Authorization": token}
    pytest.session = session
    yield session


@pytest.fixture(scope="class")
def get_api_session(_api_session, request):
    """fixture for setting up json api session"""
    session = _api_session

    if "endpoint" in request.cls.__dict__.keys():
        session.url = f"{session.base_url}/{request.cls.endpoint_base}"
    else:
        session.url = session.base_url
    request.cls.session = session
    yield session
