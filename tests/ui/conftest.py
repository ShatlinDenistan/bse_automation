import pytest

import os
from playwright.sync_api import Playwright
from dotenv import load_dotenv
from pages.login import LoginPage
from pages.side_nav import SideNav
from pages.top_nav import TopNav
from pages.order_list import OrderListPage

load_dotenv(override=True)


def init_page_objects(page, request):
    request.cls.login_page = LoginPage(page)
    request.cls.side_nav = SideNav(page)
    request.cls.top_nav = TopNav(page)
    request.cls.order_list_page = OrderListPage(page)


@pytest.fixture(scope="function", autouse=True)
def test_setup(playwright: Playwright, request: pytest.FixtureRequest):
    """Test set up method"""
    # start up code
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    request.cls.page = page
    request.cls.context = context
    request.cls.browser = browser
    login_page = LoginPage(page)
    page.goto(f"{os.getenv('HOME_PAGE')}/login")
    login_page.confirm_if_in_page()
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    login_page.login(user_name, password)
    init_page_objects(page, request)
    yield page

    # tear down code
    context.close()
    browser.close()
