from playwright.sync_api import Page, expect


class TopNav:
    def __init__(self, page: Page):
        self.driver = page
        self.expand_side_bar_link = page.get_by_text("Finance Portal")

    def expand_side_bar(self):
        self.expand_side_bar_link.click()
