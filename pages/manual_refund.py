from datetime import datetime
from pos.manual_refund_po import ManualRefundPO


class ManualRefundPage(ManualRefundPO):
    """Page class for Manual Refund functionality"""

    def expand_customer_credit_accordion(self):
        """Expands the customer credit accordion under customer info"""
        self.wait_for_seconds(1)  # MIN_TIMEOUT equivalent
        self.click(self.customer_credit_accordion)
        self.wait_for_seconds(1)  # SLEEP equivalent

    def navigate_to_refund_page(self, order_id):
        """Navigates to the refund page for a specific order"""
        self.page.goto(f"http://fin-portal.master.env/refund/{order_id}")
        self.wait_for_text("Amount to be refunded")

    def click_refund_button_and_submit_request(self):
        """Clicks refund button and submits refund request"""
        self.wait_till_element_visible(self.refund_button)
        self.click(self.refund_button)
        self.wait_till_element_visible(self.submit_refund_request_button)
        self.click(self.okay_button)
        # Store current date and time for verification
        date_time = datetime.now().strftime("%d-%b-%Y @ %H:%M")
        return date_time

    def click_view_refund_log_and_verify_details(self, payment_method):
        """Clicks view refund log button and verifies refund details"""
        self.click(self.view_refund_log_button)
        self.wait_for_text(payment_method)
        self.wait_for_text("Refund")
        self.wait_for_text("Test en-gcs")
        # Note: Commented out in original file
        # self.wait_for_text(get_date_time)

    def click_view_refund_log_and_verify_part_payment_details(self, payment_method, payment_methods):
        """Clicks view refund log button and verifies part-payment refund details"""
        self.click(self.view_refund_log_button)
        self.wait_for_text(payment_method)
        self.wait_for_text(payment_methods)
        self.wait_for_text("fin_portal")
        self.wait_for_text("Refund")
        self.wait_for_text("Test en-gcs")
        # Note: This was not commented out in original
        # self.wait_for_text(get_date_time)

    def verify_order_not_eligible_for_manual_refund(self, order_id):
        """Verifies that order is not eligible for manual refund"""
        locator = self.not_eligible_for_refund.replace("${order_ids[0]}", order_id)
        self.wait_till_element_visible(locator)

    def click_refund_button_and_enter_banking_details(self):
        """Clicks refund button and enters banking details"""
        self.wait_for_text("Amount to be refunded")
        self.fill(self.bank_account_input, "96696696")
        self.click(self.bank_dropdown)
        self.click(self.capitec_bank_option)
        self.click(self.branch_dropdown)
        self.click(self.capitec_bank_cpc_option)

    def click_eft_refund_button_and_submit_request(self):
        """Clicks EFT refund button and submits refund request"""
        self.click(self.refund_button)
        self.wait_for_text("Bank account number 96696696 is associated with")
        self.click(self.proceed_button)
        self.click(self.okay_button)
        # Store current date and time for verification
        date_time = datetime.now().strftime("%d-%b-%Y @ %H:%M")
        return date_time

    def verify_refund_amount_excludes_coupon_amount(self, order_total, order_discount, order_shipping):
        """Verifies that refund amount excludes coupon amount"""
        total_converted = float(order_total)
        discount_converted = float(order_discount)
        shipping_converted = float(order_shipping)
        refund_amount = total_converted + shipping_converted - discount_converted
        refund_amount_text = f"{refund_amount:,}"

        # Wait for the refund amount text to be visible in the display
        self.wait_till_element_visible(f"{self.refund_amount_display}[contains(text(),'{refund_amount_text}')]")

    def verify_refund_not_available(self, order_id):
        """Verifies that refund is not available"""
        locator = self.not_eligible_for_refund.replace("${order_ids[0]}", order_id)
        self.wait_till_element_visible(locator)
