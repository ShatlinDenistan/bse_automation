from base.page_base import PageBase


class ReinstateOrderPO(PageBase):
    """Page Object class for Reinstate Order functionality."""

    # region Reinstate Buttons

    @property
    def btn_reinstate(self):
        selector = "//button[contains(text(),'Reinstate')]"
        return self.locator(selector, "Reinstate button")

    @property
    def reinstate_btn(self):
        selector = "//*[@class='ui small modal transition visible active']//button[contains(text(),'Reinstate')]"
        return self.locator(selector, "Confirm reinstate button")

    # endregion

    # region Order Status Indicators

    @property
    def admin_note(self):
        selector = "//div[contains(text(),'Order reinstated')]"
        return self.locator(selector, "Admin note for reinstated order")

    @property
    def order_page_canceled_by_badge(self):
        selector = "//*[@class='ten wide column label-container']/span/div[1]"
        return self.locator(selector, "Order page canceled by badge")

    # endregion

    # region Reinstate Modal Amounts

    @property
    def reinstate_staff_discount_amount(self):
        selector = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Staff Discount')]//following-sibling::td"
        return self.locator(selector, "Reinstate staff discount amount")

    @property
    def reinstate_order_items_amount(self):
        selector = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Items')]//following-sibling::td"
        return self.locator(selector, "Reinstate order items amount")

    @property
    def reinstate_delivery_amount(self):
        selector = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Delivery')]//following-sibling::td"
        return self.locator(selector, "Reinstate delivery amount")

    @property
    def reinstate_coupon_discount_amount(self):
        selector = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Coupon Discount')]//following-sibling::td"
        return self.locator(selector, "Reinstate coupon discount amount")

    @property
    def reinstate_order_total_amount(self):
        selector = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Total')]//following::td"
        return self.locator(selector, "Reinstate order total amount")

    # endregion

    # region Order Financials Section

    @property
    def order_financials_accordion(self):
        selector = "//div[contains(text(),'Order Financials')]//i"
        return self.locator(selector, "Order financials accordion")

    @property
    def order_financials_staff_discount_amount(self):
        selector = "//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Staff Discount')]//following-sibling::td"
        return self.locator(selector, "Order financials staff discount amount")

    # endregion
