from playwright.sync_api import Playwright
import os
from dotenv import load_dotenv

load_dotenv(override=True)


class TestLogin:

    def test_login_negative_test(self, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        home_page = os.getenv("HOME_PAGE")
        page.goto(f"{home_page}/login")
        user_name = os.getenv("USER_NAME")
        password = os.getenv("PASSWORD")
        page.get_by_role("textbox", name="Email").fill(user_name)
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Login").nth(1).click()
        page.get_by_text("Incorrect username or password").click()
        page.get_by_role("button", name="Login").click()
        # ---------------------
        context.close()
        browser.close()
