from base.page_base import PageBase
from playwright.sync_api import expect


# Locator tuples with xpath and descriptions
REINSTATE_BUTTON = ("//button[contains(text(),'Reinstate')]", "Reinstate button")
REINSTATE_CONFIRM_BUTTON = ("//*[@class='ui small modal transition visible active']//button[contains(text(),'Reinstate')]", "Reinstate confirm button")
ADMIN_NOTE = ("//div[contains(text(),'Order reinstated')]", "Admin note for reinstated order")
STAFF_DISCOUNT_AMOUNT = ("//*[@class='ui small modal transition visible active']//*[contains(text(),'Staff Discount')]//following-sibling::td", "Staff discount amount")
ORDER_ITEMS_AMOUNT = ("//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Items')]//following-sibling::td", "Order items amount")
DELIVERY_AMOUNT = ("//*[@class='ui small modal transition visible active']//*[contains(text(),'Delivery')]//following-sibling::td", "Delivery amount")
COUPON_DISCOUNT_AMOUNT = ("//*[@class='ui small modal transition visible active']//*[contains(text(),'Coupon Discount')]//following-sibling::td", "Coupon discount amount")
ORDER_TOTAL_AMOUNT = ("//*[@class='ui small modal transition visible active']//*[contains(text(),'Order Total')]//following::td", "Order total amount")
ORDER_FINANCIALS_ACCORDION = ("//div[contains(text(),'Order Financials')]//i", "Order financials accordion")
ORDER_FINANCIALS_STAFF_DISCOUNT = ("//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Staff Discount')]//following-sibling::td", "Order financials staff discount")
CANCELED_BY_BADGE = ("//*[@class='ten wide column label-container']/span/div[1]", "Canceled by badge")


class ReinstateOrderPage(PageBase):
    """Page object for reinstating orders and verifying financial amounts."""
    
    def __init__(self, page):
        super().__init__(page)
        # Initialize locators
        self.reinstate_button = self.locator(REINSTATE_BUTTON)
        self.reinstate_confirm_button = self.locator(REINSTATE_CONFIRM_BUTTON)
        self.admin_note = self.locator(ADMIN_NOTE)
        self.staff_discount_amount = self.locator(STAFF_DISCOUNT_AMOUNT)
        self.order_items_amount = self.locator(ORDER_ITEMS_AMOUNT)
        self.delivery_amount = self.locator(DELIVERY_AMOUNT)
        self.coupon_discount_amount = self.locator(COUPON_DISCOUNT_AMOUNT)
        self.order_total_amount = self.locator(ORDER_TOTAL_AMOUNT)
        self.order_financials_accordion = self.locator(ORDER_FINANCIALS_ACCORDION)
        self.order_financials_staff_discount = self.locator(ORDER_FINANCIALS_STAFF_DISCOUNT)
        self.canceled_by_badge = self.locator(CANCELED_BY_BADGE)

        # Store amounts as instance variables
        self.reinstate_staff_discount = None
        self.reinstate_order_items = None
        self.reinstate_delivery = None
        self.reinstate_coupon_discount = None
        self.reinstate_order_total = None
        self.order_financials_staff_discount_value = None

    def reinstate_order(self):
        """Reinstate an order and capture all financial amounts."""
        expect(self.reinstate_button).to_be_visible()
        self.click(self.reinstate_button)
        self.page.wait_for_timeout(1000)  # Replace SLEEP variable
        expect(self.reinstate_button).to_be_visible()

        # Get and store all amounts, removing 'R ' prefix
        self.reinstate_staff_discount = self._get_amount(self.staff_discount_amount)
        self.reinstate_order_items = self._get_amount(self.order_items_amount)
        self.reinstate_delivery = self._get_amount(self.delivery_amount)
        self.reinstate_coupon_discount = self._get_amount(self.coupon_discount_amount)
        self.reinstate_order_total = self._get_amount(self.order_total_amount)

        self.click(self.reinstate_confirm_button)

    def verify_admin_note_created(self):
        """Verify that an admin note was created for the order reinstatement."""
        expect(self.admin_note).to_be_visible()
        return self.get_text(self.admin_note)

    def get_order_financials_amounts(self):
        """Get order financials amounts after reinstatement."""
        expect(self.order_financials_accordion).to_be_visible()
        self.click(self.order_financials_accordion)
        
        # Get and store staff discount amount, removing 'R ' and '-' prefixes
        text = self.get_text(self.order_financials_staff_discount)
        self.order_financials_staff_discount_value = text.replace('R ', '').replace('-', '').strip()

    def verify_staff_discount_matches(self):
        """Verify that staff discount on reinstate matches staff discount on order financials."""
        assert self.reinstate_staff_discount == self.order_financials_staff_discount_value, \
            f"Staff discount mismatch: Reinstate={self.reinstate_staff_discount}, Financials={self.order_financials_staff_discount_value}"

    def verify_order_amounts_correct(self, order_shipping, order_discount):
        """Verify that reinstate order amounts are correct."""
        # Calculate total
        calculated_total = float(self.reinstate_order_items) + float(self.reinstate_delivery) - float(self.reinstate_coupon_discount)
        
        # Verify amounts match
        assert float(self.reinstate_delivery) == float(order_shipping[0]), "Delivery amount mismatch"
        assert float(self.reinstate_coupon_discount) == float(order_discount[0]), "Coupon discount mismatch"
        assert float(self.reinstate_order_total) == calculated_total, "Order total mismatch"

    def verify_reinstate_button_not_available(self):
        """Verify that the reinstate button is not available."""
        expect(self.reinstate_button).not_to_be_visible()
        canceled_by_text = self.get_text(self.canceled_by_badge)
        return canceled_by_text

    def _get_amount(self, locator):
        """Helper method to get amount text and remove 'R ' prefix."""
        text = self.get_text(locator)
        return text.replace('R ', '').strip()
