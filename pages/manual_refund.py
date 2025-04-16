import datetime
from playwright.sync_api import Page

from base.page_base import PageBase

# Locator tuples with descriptive names
customer_credit_accordion = ("//div[contains(text(),' available credit')]", "Customer Credit Accordion")
refund_page_url_pattern = ("http://fin-portal.master.env/refund/{}", "Refund Page URL")
refund_amount_text = ("//div[text()='Amount to be refunded']", "Refund Amount Text")
btn_refund = ("//button[contains(text(),'Refund')]", "Refund Button")
btn_submitting_refund_req = ("//button[contains(text(),'Submitting refund request')]", "Submitting Refund Request Button")
btn_okay = ("//button[contains(text(),'Okay')]", "Okay Button")
view_refund_log_link = ("//a[contains(text(),'View Refund Log')]", "View Refund Log Link")
refund_text = ("//div[contains(text(),'Refund')]", "Refund Text")
test_en_gcs_text = ("//div[contains(text(),'Test en-gcs')]", "Test en-gcs Text")
order_not_eligible_message = ("//li[contains(text(),'Order {} is not eligible for refund.')]", "Order Not Eligible Message")
bank_account_input = ("//input[@autocomplete='off' and @name='bankAccount' and @type='text']", "Bank Account Input")
bank_dropdown = ("//div[@name='bank' and @role='listbox' and @class='ui fluid selection dropdown']", "Bank Dropdown")
bank_option = ("//span[contains(text(),'{}')]", "Bank Option")
branch_dropdown = ("//div[contains(text(),'- - Select branch - -')]", "Branch Dropdown")
branch_option = ("//span[contains(text(),'{}')]", "Branch Option")
proceed_button = ("//button[contains(text(),'Proceed')]", "Proceed Button")
refund_amount_cell = ("//html/body/div[1]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/table/tbody/tr/td[2][contains(text(),'{}')]", "Refund Amount Cell")
payment_method_text = ("//div[contains(text(),'{}')]", "Payment Method Text")


class ManualRefundPage(PageBase):
    """Page object for Manual Refund functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Initialize all locators
        self.customer_credit_accordion = self.locator(customer_credit_accordion)
        self.refund_amount_text = self.locator(refund_amount_text)
        self.btn_refund = self.locator(btn_refund)
        self.btn_submitting_refund_req = self.locator(btn_submitting_refund_req)
        self.btn_okay = self.locator(btn_okay)
        self.view_refund_log_link = self.locator(view_refund_log_link)
        self.refund_text = self.locator(refund_text)
        self.test_en_gcs_text = self.locator(test_en_gcs_text)
        self.bank_account_input = self.locator(bank_account_input)
        self.bank_dropdown = self.locator(bank_dropdown)
        self.branch_dropdown = self.locator(branch_dropdown)
        self.proceed_button = self.locator(proceed_button)

        # Common bank and branch options
        self.capitec_bank_option = self.locator((bank_option[0].format("Capitec Bank"), "Capitec Bank Option"))
        self.capitec_branch_option = self.locator((branch_option[0].format("Capitec Bank CPC"), "Capitec Bank CPC Branch Option"))

    def expand_the_customer_credit_accordion_under_customer_info(self):
        """Expand the customer credit accordion under customer info"""
        self.wait_for_seconds(3)  # Equivalent to ${MIN_TIMEOUT}
        self.click(self.customer_credit_accordion)
        self.wait_for_seconds(2)  # Equivalent to ${SLEEP}

    def on_order_view_page_expand_the_order_items_accordion_and_click_refund(self, order_id):
        """Navigate to the refund page for a specific order"""
        refund_url = refund_page_url_pattern[0].format(order_id)
        self.page.goto(refund_url)
        self.expect_to_be_visible(self.refund_amount_text)

    def click_the_refund_button_and_submit_refund_request(self):
        """Click the refund button and submit the refund request"""
        self.expect_to_be_visible(self.btn_refund)
        self.click(self.btn_refund)
        self.expect_to_be_visible(self.btn_submitting_refund_req)
        self.click(self.btn_okay)
        # Set date time in the same format as the Robot Framework file
        date_time = datetime.datetime.now().strftime("%d-%b-%Y @ %H:%M")
        return date_time

    def click_the_view_refund_log_button_and_verify_details(self, payment_method):
        """Click the view refund log button and verify details for the specified payment method"""
        self.click(self.view_refund_log_link)
        payment_method_locator = self.locator((payment_method_text[0].format(payment_method), f"{payment_method} Text"))
        self.expect_to_be_visible(payment_method_locator)
        self.expect_to_be_visible(self.refund_text)
        self.expect_to_be_visible(self.test_en_gcs_text)

    def click_the_view_refund_log_button_and_verify_part_payment_details(self, payment_method, payment_methods, date_time):
        """Click the view refund log button and verify part-payment details"""
        self.click(self.view_refund_log_link)

        # Verify primary payment method
        primary_payment_method_locator = self.locator((payment_method_text[0].format(payment_method), f"{payment_method} Text"))
        self.expect_to_be_visible(primary_payment_method_locator)

        # Verify secondary payment method
        secondary_payment_method_locator = self.locator((payment_method_text[0].format(payment_methods), f"{payment_methods} Text"))
        self.expect_to_be_visible(secondary_payment_method_locator)

        # Verify standard elements
        fin_portal_locator = self.locator((payment_method_text[0].format("fin_portal"), "fin_portal Text"))
        self.expect_to_be_visible(fin_portal_locator)
        self.expect_to_be_visible(self.refund_text)
        self.expect_to_be_visible(self.test_en_gcs_text)

        # Verify date time (this would need parsing the date from the page which isn't
        # directly implemented in the original robot file)

    def verify_that_order_is_not_eligible_for_manual_refund(self, order_id):
        """Verify that the order is not eligible for manual refund"""
        not_eligible_message = self.locator((order_not_eligible_message[0].format(order_id), f"Order {order_id} Not Eligible Message"))
        self.expect_to_be_visible(not_eligible_message)

    def click_the_refund_button_and_enter_banking_details(self):
        """Click the refund button and enter banking details"""
        self.expect_to_be_visible(self.refund_amount_text)
        self.fill(self.bank_account_input, "96696696")
        self.click(self.bank_dropdown)
        self.click(self.capitec_bank_option)
        self.click(self.branch_dropdown)
        self.click(self.capitec_branch_option)

    def click_the_eft_refund_button_and_submit_refund_request(self):
        """Click the EFT refund button and submit refund request"""
        self.click(self.btn_refund)
        bank_account_confirmation_text = self.locator("//div[contains(text(),'Bank account number 96696696 is associated with')]", "Bank Account Confirmation Text")
        self.expect_to_be_visible(bank_account_confirmation_text)
        self.click(self.proceed_button)
        self.click(self.btn_okay)
        # Set date time in the same format as the Robot Framework file
        date_time = datetime.datetime.now().strftime("%d-%b-%Y @ %H:%M")
        return date_time

    def verify_that_refund_amount_excludes_coupon_amount(self, order_total, order_discount, order_shipping):
        """Verify that the refund amount excludes coupon amount"""
        # Convert strings to numbers
        total_converted = float(order_total)
        discount_converted = float(order_discount)
        shipping_converted = float(order_shipping)

        # Calculate refund amount
        refund_amount = total_converted + shipping_converted - discount_converted

        # Format the refund amount with commas as in the Robot Framework
        refund_amount_text = f"{refund_amount:,}"

        # Verify the refund amount is displayed correctly
        refund_amount_cell_locator = self.locator((refund_amount_cell[0].format(refund_amount_text), f"Refund Amount Cell {refund_amount_text}"))
        self.expect_to_be_visible(refund_amount_cell_locator)

    def verify_that_refund_not_available(self, order_id):
        """Verify that refund is not available for the order"""
        not_eligible_message = self.locator((order_not_eligible_message[0].format(order_id), f"Order {order_id} Not Eligible Message"))
        self.expect_to_be_visible(not_eligible_message)
