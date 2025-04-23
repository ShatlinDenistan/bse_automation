from base.page_base import PageBase

# Module-level constants for locators
BTN_REINSTATE = "//button[contains(text(),'Reinstate')]"
REINSTATE_BTN = "//*[@class='ui small modal transition visible active']//button[contains(text(),'Reinstate')]"
ADMIN_NOTE = "//div[contains(text(),'Order reinstated')]"
REINSTATE_STAFF_DISCOUNT_AMOUNT = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Staff Discount')]//following-sibling::td"
REINSTATE_ORDER_ITEMS_AMOUNT = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Items')]//following-sibling::td"
REINSTATE_DELIVERY_AMOUNT = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Delivery')]//following-sibling::td"
REINSTATE_COUPON_DISCOUNT_AMOUNT = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Coupon Discount')]//following-sibling::td"
REINSTATE_ORDER_TOTAL_AMOUNT = "//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Total')]//following::td"
ORDER_FINANCIALS_ACCORDION = "//div[contains(text(),'Order Financials')]//i"
ORDER_FINANCIALS_STAFF_DISCOUNT_AMOUNT = "//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Staff Discount')]//following-sibling::td"
ORDER_PAGE_CANCELED_BY_BADGE = "//*[@class='ten wide column label-container']/span/div[1]"


class ReinstateOrderPO(PageBase):
    """Page Object class for Reinstate Order functionality."""

    def __init__(self, page):
        super().__init__(page)
        # Initialize locators
        self.btn_reinstate = self.locator(BTN_REINSTATE, "Reinstate button")
        self.reinstate_btn = self.locator(REINSTATE_BTN, "Confirm reinstate button")
        self.admin_note = self.locator(ADMIN_NOTE, "Admin note for reinstated order")
        self.reinstate_staff_discount_amount = self.locator(REINSTATE_STAFF_DISCOUNT_AMOUNT, "Reinstate staff discount amount")
        self.reinstate_order_items_amount = self.locator(REINSTATE_ORDER_ITEMS_AMOUNT, "Reinstate order items amount")
        self.reinstate_delivery_amount = self.locator(REINSTATE_DELIVERY_AMOUNT, "Reinstate delivery amount")
        self.reinstate_coupon_discount_amount = self.locator(REINSTATE_COUPON_DISCOUNT_AMOUNT, "Reinstate coupon discount amount")
        self.reinstate_order_total_amount = self.locator(REINSTATE_ORDER_TOTAL_AMOUNT, "Reinstate order total amount")
        self.order_financials_accordion = self.locator(ORDER_FINANCIALS_ACCORDION, "Order financials accordion")
        self.order_financials_staff_discount_amount = self.locator(ORDER_FINANCIALS_STAFF_DISCOUNT_AMOUNT, "Order financials staff discount amount")
        self.order_page_canceled_by_badge = self.locator(ORDER_PAGE_CANCELED_BY_BADGE, "Order page canceled by badge")
