import re
import time
from pos.reinstate_order_po import ReinstateOrderPO


class ReinstateOrderPage(ReinstateOrderPO):
    """Page class for Reinstate Order functionality."""

    def __init__(self, page):
        super().__init__(page)
        self.reinstate_staff_discount_amount_value = None
        self.reinstate_order_items_amount_value = None
        self.reinstate_delivery_amount_value = None
        self.reinstate_coupon_discount_amount_value = None
        self.reinstate_order_total_amount_value = None
        self.order_financials_staff_discount_amount_value = None

    def reinstate_order(self):
        """Reinstate a canceled order and capture financial amounts."""
        self.wait_for_element_to_be_visible(self.btn_reinstate)
        self.click(self.btn_reinstate)
        time.sleep(1)  # Equivalent to Sleep ${SLEEP}
        self.wait_for_element_to_be_visible(self.btn_reinstate)

        # Get and store all financial values
        self.reinstate_staff_discount_amount_value = self._get_amount_value(self.reinstate_staff_discount_amount)
        self.reinstate_order_items_amount_value = self._get_amount_value(self.reinstate_order_items_amount)
        self.reinstate_delivery_amount_value = self._get_amount_value(self.reinstate_delivery_amount)
        self.reinstate_coupon_discount_amount_value = self._get_amount_value(self.reinstate_coupon_discount_amount)
        self.reinstate_order_total_amount_value = self._get_amount_value(self.reinstate_order_total_amount)

        # Click the Reinstate button to confirm
        self.click(self.reinstate_btn)

    def verify_admin_note_for_reinstatement(self):
        """Verify that an admin note for order reinstatement was created."""
        self.wait_for_element_to_be_visible(self.admin_note)
        return self.is_visible(self.admin_note)

    def get_order_financials_amounts(self):
        """Get order financials amounts by opening the accordion."""
        self.wait_for_element_to_be_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)
        self.order_financials_staff_discount_amount_value = self._get_amount_value(self.order_financials_staff_discount_amount, remove_minus=True)

    def verify_staff_discount_match(self):
        """Verify that staff discount on reinstate matches staff discount on order financials."""
        return self.reinstate_staff_discount_amount_value == self.order_financials_staff_discount_amount_value

    def verify_reinstate_order_amounts(self, order_shipping, order_discount):
        """Verify that reinstate order amounts are correct."""
        # Calculate expected total
        expected_total = self.reinstate_order_items_amount_value + self.reinstate_delivery_amount_value - self.reinstate_coupon_discount_amount_value

        # Verify delivery and discount match the ones from the database
        delivery_match = self.reinstate_delivery_amount_value == float(order_shipping[0])
        coupon_match = self.reinstate_coupon_discount_amount_value == float(order_discount[0])
        total_match = self.reinstate_order_total_amount_value == expected_total

        return delivery_match and coupon_match and total_match

    def verify_reinstate_button_not_available(self, order_id):
        """Verify that reinstate button is not available for orders not auto-canceled."""
        button_not_visible = not self.is_visible(self.btn_reinstate)

        if button_not_visible:
            canceled_by_text = self.get_text(self.order_page_canceled_by_badge)
            print(f"{order_id} {canceled_by_text}")

        return button_not_visible

    def _get_amount_value(self, element, remove_minus=False):
        """Helper method to get and clean amount values."""
        text = self.get_text(element)
        # Remove 'R ' and optionally '-' from the text
        if remove_minus:
            text = re.sub(r"R\s|-", "", text)
        else:
            text = re.sub(r"R\s", "", text)

        return float(text)
