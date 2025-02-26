from playwright.sync_api import Playwright


class TestLogin:

    def test_login_negative_test(self, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://fin-portal.master.env/login")
        page.get_by_role("textbox", name="Email").fill("shatlin.denistan@takealot.com")
        page.get_by_role("textbox", name="Password").fill("testststs")
        page.get_by_role("button", name="Login").nth(1).click()
        page.get_by_text("Incorrect username or password").click()
        page.get_by_role("button", name="Login").click()
        # ---------------------
        context.close()
        browser.close()

