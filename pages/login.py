from playwright.sync_api import Page, expect

from base.page_base import PageBase


class LoginPage(PageBase):
    """Page methods and elements for login page"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.email_textbox = self.page.get_by_role("textbox", name="Email")
        self.password_textbox = self.page.get_by_role("textbox", name="Password")
        self.login_button = self.page.get_by_role("button", name="Login").nth(1)

    def confirm_if_in_page(self):
        """Confirm if in login page"""
        expect(self.email_textbox).to_be_visible()

    def login(self, username, password):
        """login into the system"""
        self.fill(self.email_textbox, username)
        self.fill(self.password_textbox, password)
        self.click(self.login_button)
