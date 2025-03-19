from playwright.sync_api import Page, expect


class SideNav:
    def __init__(self, page: Page):
        self.page = page
        self.deposit_match_link = page.get_by_role("link", name="Deposit Match")
        self.risk_queue_link = page.get_by_role("link", name="Risk Queue")
        self.home_link = page.get_by_role("link", name="Home")
        self.order_list_link = page.get_by_role("link", name="Order List")
        self.financial_orders_link = page.get_by_role("link", name="Financial Orders")
        self.eft_refunds_link = page.get_by_role("link", name="EFT Refunds")
        self.escalated_refunds_link = page.get_by_role("link", name="Escalated Refunds")

    def click_deposit_match(self):
        self.deposit_match_link.click()

    def click_risk_queue(self):
        self.risk_queue_link.click()

    def click_home(self):
        self.home_link.click()

    def click_order_list(self):
        self.order_list_link.click()

    def click_financial_orders(self):
        self.financial_orders_link.click()

    def click_eft_refunds(self):
        self.eft_refunds_link.click()

    def click_escalated_refunds(self):
        self.escalated_refunds_link.click()
