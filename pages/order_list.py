from playwright.sync_api import Page, expect


class OrderListPage:
    def __init__(self, page: Page):
        self.page = page
        self.auth_status_label = page.locator("//label[.='Auth Status']")

    def confirm_if_in_page(self):
        expect(self.auth_status_label).to_be_visible(timeout=5000)
