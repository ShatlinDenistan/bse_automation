"""login tests"""

import os
import time
from playwright.sync_api import Playwright, expect
from dotenv import load_dotenv
import pytest

load_dotenv(override=True)


class TestHomePage:
    """login tests"""

    @pytest.mark.customer_search
    @pytest.mark.regression
    def test_customer_search(self, playwright: Playwright):
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

        search_textbox = page.locator("//input [@name='searchText']")
        search_filter = page.locator("//div[.='-- all --']").first
        customer_option = page.locator("//span[.='Customer']")
        search_button = page.locator("//button[@type='submit']")
        customer_info_button = page.locator("//button[.='Customer Info']")
        expect(search_textbox).to_be_visible(timeout=5000)
        search_textbox.fill("100")
        search_filter.click()
        customer_option.click()
        search_button.click()
        expect(customer_info_button).to_be_visible(timeout=5000)
        context.close()
        browser.close()

    # SLI Order Number
    # Thandeka RRN
