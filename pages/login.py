from playwright.sync_api import Page, expect
import time

from base.page_base import PageBase


class LoginPage(PageBase):
    """Page methods and elements for login page"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        # General login elements
        self.email_textbox = self.page.get_by_role("textbox", name="Email")
        self.password_textbox = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name="Login").nth(1)

        # Fin-Portal specific elements
        self.fin_portal_login_heading = self.page.locator("xpath=//div[contains(text(),'Log In User')]")
        self.fin_portal_username_input = self.page.locator("xpath=//body/div[2]/div[1]/div[2]/form[1]/div[1]/input[1]")
        self.fin_portal_password_input = self.page.locator("xpath=//body/div[2]/div[1]/div[2]/form[1]/div[2]/input[1]")
        self.fin_portal_login_button = self.page.locator("xpath=//body/div[2]/div[1]/div[3]/button[1]")

        # CS-Admin specific elements
        self.cs_admin_email_input = self.page.locator("xpath=//input[@name='email']")
        self.cs_admin_password_input = self.page.locator("xpath=//input[@name='password']")
        self.cs_admin_login_button = self.page.locator("xpath=//*[@class='ui green basic button']")

    def confirm_if_in_page(self):
        """Confirm if in login page"""
        expect(self.email_textbox).to_be_visible()

    def login(self, username, password):
        """login into the system"""
        self.fill(self.email_textbox, username)
        self.fill(self.password_textbox, password)
        self.click(self.login_button)

    def login_fin_portal(self, username, password):
        """
        Login to Fin-Portal

        Args:
            username: Username for Fin-Portal
            password: Password for Fin-Portal
        """
        # Wait for the login element to be visible
        self.fin_portal_login_heading.wait_for(state="visible")

        # Fill in credentials
        self.fin_portal_username_input.fill(username)
        self.fin_portal_password_input.fill(password)

        # Click login button
        self.fin_portal_login_button.click()

        # Wait for login to complete
        time.sleep(5)

    def login_cs_admin(self, username, password):
        """
        Login to CS-Admin

        Args:
            username: Username for CS-Admin
            password: Password for CS-Admin
        """
        # Wait for the login element to be visible
        self.cs_admin_email_input.wait_for(state="visible")

        # Fill in credentials
        self.cs_admin_email_input.fill(username)
        self.cs_admin_password_input.fill(password)

        # Click login button
        self.cs_admin_login_button.click()

        # Wait for login to complete
        time.sleep(5)
