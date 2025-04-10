from playwright.sync_api import Page, expect

from base.page_base import PageBase


class SideNav(PageBase):
    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.deposit_match_link = page.get_by_role("link", name="Deposit Match")
        self.risk_queue_link = page.get_by_role("link", name="Risk Queue")
        self.home_link = page.get_by_role("link", name="Home")
        self.order_list_link = page.get_by_role("link", name="Order List")
        self.financial_orders_link = page.get_by_role("link", name="Financial Orders")
        self.eft_refunds_link = page.get_by_role("link", name="EFT Refunds")
        self.escalated_refunds_link = page.get_by_role("link", name="Escalated Refunds")

    def click_deposit_match(self):
        self.click(self.deposit_match_link)

    def click_risk_queue(self):
        self.click(self.risk_queue_link)

    def click_home(self):
        self.click(self.home_link)

    def click_order_list(self):
        self.click(self.order_list_link)

    def click_financial_orders(self):
        self.click(self.financial_orders_link)

    def click_eft_refunds(self):
        self.click(self.eft_refunds_link)

    def click_escalated_refunds(self):
        self.click(self.escalated_refunds_link)
