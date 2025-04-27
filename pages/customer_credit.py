"""Customer Credit Page class file."""

import random
import string
from datetime import datetime
from pos.customer_credit_po import CustomerCreditPO


class CustomerCreditPage(CustomerCreditPO):
    """Page class for Customer Credit functionality."""

    def __init__(self, page):
        """Initialize the Customer Credit Page with elements."""
        super().__init__(page)
        self.customer_credit_amount = None

    def expand_credit_section_and_click_credit_button(self):
        """Expand the customer credit section and click the credit button."""
        self.wait_for_seconds(1)  # Using dynamic sleep equivalent
        self.click(self.customer_credit_btn)

    def enter_amount_and_comment(self):
        """Enter a random amount and comment for credit."""
        self.customer_credit_amount = "".join(random.choices(string.digits, k=3))
        self.fill(self.credit_amount_input, self.customer_credit_amount)

    def select_add_credit_button(self):
        """Click the Add Credit button."""
        self.click(self.add_credit_btn)
        self.wait_till_element_visible(self.confirm_dialog)

    def select_ok_on_dialog(self):
        """Click OK on the confirmation dialog."""
        self.click(self.confirm_credit_btn)

    def verify_customer_credit_applied(self):
        """Verify that customer credit is applied correctly."""
        current_date = datetime.now().strftime("%d-%b-%Y @ %H:%M")
        if current_date.startswith("@ 0"):
            current_date = current_date.replace("@ 0", "@ ")

        self.wait_for_text(f"R {self.customer_credit_amount}")
        self.wait_for_text("Not linked to an order")
        # Datetime verification is commented out as in the original
        # self.expect_to_be_visible(f"//td[contains(text(),'{current_date}')]")
        return True

    def verify_order_credit_applied(self):
        """Verify that order credit is applied correctly."""
        self.evaluate("window.scrollTo(0, 250)")
        self.wait_for_text(self.customer_credit_amount)
        return True
