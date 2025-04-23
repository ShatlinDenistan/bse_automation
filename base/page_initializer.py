from playwright.sync_api import Page

from pages.login import LoginPage
from pages.side_nav import SideNav
from pages.top_nav import TopNav


class PageInitializer:
    """Handles page object initialization"""

    def initialize_pages(self, page: Page):
        """Test base functionality."""
        self.login_page = LoginPage(page)
        self.side_nav = SideNav(page)
        self.top_nav = TopNav(page)
