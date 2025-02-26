"""login tests"""

import os
from playwright.sync_api import Playwright, expect
from dotenv import load_dotenv

load_dotenv(override=True)


class TestLogin:
    """login tests"""

    def test_login_positive_test(self, playwright: Playwright):
        """positive login test with valid user name and password"""
        # arrange
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        home_page = os.getenv("HOME_PAGE")
        page.goto(f"{home_page}/login")
        user_name = os.getenv("USER_NAME")
        password = os.getenv("PASSWORD")

        # act
        page.get_by_role("textbox", name="Email").fill(user_name)
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Login").nth(1).click()

        # assert
        logout_button = page.get_by_role("button", name="Sign Out")
        expect(logout_button).to_be_visible()

        context.close()
        browser.close()

    def test_login_negative_test(self, playwright: Playwright):
        """positive login test with valid user name and password"""
        # arrange
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        home_page = os.getenv("HOME_PAGE")
        page.goto(f"{home_page}/login")
        user_name = os.getenv("USER_NAME")
        password = "wrong_password"

        # act
        page.get_by_role("textbox", name="Email").fill(user_name)
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Login").nth(1).click()

        # assert
        logout_button = page.get_by_role("button", name="Sign Out")
        expect(logout_button).to_be_hidden()

        context.close()
        browser.close()

    # SLI
    # login with empty username
    # login with invalid username and invalid password

    # THANDEKA
    # login with empty password
    # login with empty username and password
