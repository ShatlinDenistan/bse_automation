from playwright.sync_api import Page

from base.page_base import PageBase

# Locators
btn_reinstate = "//button[contains(text(),'Reinstate')]"
reinstate_btn = "//*[@class='ui small modal transition visible active']//button[contains(text(),'Reinstate')]"
admin_note = "//div[contains(text(),'Order reinstated')]"
reinstate_staff_discount_amount = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Staff Discount')]//following-sibling::td"
reinstate_order_items_amount = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Items')]//following-sibling::td"


class ReinstateOrderPage(PageBase):
    """Page object for Reinstate Order functionality"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.btn_reinstate = self.locator(btn_reinstate)
        self.reinstate_btn = self.locator(reinstate_btn)
        self.admin_note = self.locator(admin_note)
        self.reinstate_staff_discount_amount = self.locator(reinstate_staff_discount_amount)
        self.reinstate_order_items_amount = self.locator(reinstate_order_items_amount)
