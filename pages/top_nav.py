from playwright.sync_api import Page

from base.page_base import PageBase


class TopNav(PageBase):
    def __init__(self, page: Page):
        self.driver = page
        super().__init__(page)
        self.expand_side_bar_link = page.get_by_text("Finance Portal")

    def expand_side_bar(self):
        """Expand side bar"""
        self.step("Expanding the side bar")
        self.click(self.expand_side_bar_link)
