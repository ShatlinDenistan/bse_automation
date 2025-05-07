import random
from string import ascii_letters, digits
from pos.order_credit_po import OrderCreditPO


class OrderCreditPage(OrderCreditPO):
    """Page class for Order Credit functionality"""

    def expand_customer_credit_section_and_click_allocate_credit(self):
        """Expand the customer credit section and click the allocate credit button"""
        self.step("Expanding the customer credit section and clicking allocate credit button")
        self.click(self.btn_customer_credit)
        self.wait_for_seconds(1)
        self.click(self.btn_allocate_credit)

    def select_credit_reason(self, reason):
        """Select a credit reason from the dropdown"""
        self.step("Selecting credit reason")
        self.click(self.dropdown_credit_reason)

        # Determine which reason locator to use based on the input
        reason_locator = None
        if reason == "Goodwill":
            reason_locator = self.reason_goodwill
        elif reason == "Late delivery fee":
            reason_locator = self.reason_late_delivery_fee
        elif reason == "Subscription late delivery fee":
            reason_locator = self.reason_sub_late_delivery
        elif reason == "Credit breach":
            reason_locator = self.reason_credit_breach
        elif reason == "B2B bulk orders":
            reason_locator = self.reason_b2b_bulk_order
        elif reason == "Failed EFT refunds":
            reason_locator = self.reason_failed_eft_refunds
        elif reason == "System error: Credit removal failed":
            reason_locator = self.reason_system_error
        elif reason == "Duplicate payment":
            reason_locator = self.reason_duplicate_payment
        elif reason == "COD return":
            reason_locator = self.reason_cod_return
        elif reason == "Credit error":
            reason_locator = self.reason_credit_error

        if reason_locator:
            self.expect_to_be_visible(reason_locator)
            self.click(reason_locator)
        else:
            raise ValueError(f"Credit reason '{reason}' not supported")

    def enter_amount_and_admin_note(self):
        """Enter a random amount and admin note for order credit"""
        self.step("Entering credit amount and admin note")
        # Generate random amount (single digit number)
        order_credit_amount = str(random.randint(1, 9))

        # Clear and fill the fields
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, order_credit_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

        return order_credit_amount

    def enter_invalid_min_amount(self, min_amount):
        """Enter an invalid minimum amount and admin note"""
        self.step(f"Entering invalid minimum amount: {min_amount}")
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, min_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

        return min_amount

    def enter_invalid_max_amount(self, max_amount):
        """Enter an invalid maximum amount and admin note"""
        self.step(f"Entering invalid maximum amount: {max_amount}")
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, max_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

        return max_amount

    def verify_validation_error(self):
        """Verify validation error message is displayed"""
        self.step("Verifying validation error message")
        self.expect_to_be_visible(self.validation_error)
        error_text = self.get_text(self.validation_error)

        return error_text == "Validation Error"

    def enter_jira_number_for_credit_breach(self):
        """Enter a JIRA number for credit breach reason"""
        self.step("Entering JIRA number for credit breach")
        self.fill(self.txt_jira_number, "Automation-Jira-Number-123")

    def expand_order_items_and_click_credit_item(self):
        """Expand order items section and click the credit item option"""
        self.step("Expanding order items section and clicking credit item option")
        self.click(self.btn_order_item_menu)
        self.click(self.credit_item_option)

    def enter_negative_amount_and_admin_note(self):
        """Enter a negative amount and admin note"""
        self.step("Entering negative amount and admin note")
        order_credit_amount = "-3"

        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, order_credit_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

        return order_credit_amount

    def enter_rfn_for_system_error(self):
        """Enter RFN number for system error reason"""
        self.step("Entering RFN number for system error")
        self.fill(self.txt_rfn_number, "Automation-RFN-Number-1")

    def enter_calculated_amount_and_admin_note(self, order_total, order_shipping, order_discount):
        """Calculate and enter amount plus admin note"""
        self.step("Entering calculated amount and admin note")

        # Convert string values to numbers
        order_total_amount = float(order_total)
        order_shipping = float(order_shipping)
        order_discount = float(order_discount)

        # Calculate auth total
        calculated_auth_total = order_total_amount + order_shipping - order_discount + 10000
        calculated_auth_total_str = "{:,}".format(calculated_auth_total)

        # Fill the form
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, calculated_auth_total_str)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

        return calculated_auth_total_str

    def get_return_cancelled_amount(self):
        """Get return cancelled amount from order financials"""
        self.step("Getting return cancelled amount from order financials")

        # Open order financials accordion
        self.expect_to_be_visible(self.accordion_order_financials)
        self.click(self.accordion_order_financials)

        # Get return cancelled amount
        return_cancelled_amount = self.get_text(self.order_financials_return_cancelled)
        # Remove currency symbol and spaces
        return_cancelled_amount = return_cancelled_amount.replace("R ", "")

        # Calculate amount
        return_cancelled_amount_number = float(return_cancelled_amount)
        calculated_amount = return_cancelled_amount_number + 10000

        return return_cancelled_amount, calculated_amount

    def enter_return_cancelled_amount_and_admin_note(self, return_cancelled_amount):
        """Enter the return cancelled amount and admin note"""
        self.step("Entering return cancelled amount and admin note")
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, return_cancelled_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

    def get_cancelled_amount(self):
        """Get cancelled amount from order financials"""
        self.step("Getting cancelled amount from order financials")

        # Open order financials accordion
        self.expect_to_be_visible(self.accordion_order_financials)
        self.click(self.accordion_order_financials)

        # Get cancelled amount
        cancelled_amount = self.get_text(self.order_financials_cancelled)
        # Remove currency symbol and spaces
        cancelled_amount = cancelled_amount.replace("R ", "")

        # Calculate amount
        cancelled_amount_number = float(cancelled_amount)
        calculated_amount = cancelled_amount_number + 10000

        return cancelled_amount, calculated_amount

    def enter_cancelled_amount_and_admin_note(self, cancelled_amount):
        """Enter the cancelled amount and admin note"""
        self.step("Entering cancelled amount and admin note")
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, cancelled_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")
