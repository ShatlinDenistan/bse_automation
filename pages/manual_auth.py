from playwright.sync_api import Page
from base.page_base import PageBase
from pages.manual_override import ManualOverridePage


# Locators
payments_ledger_accordion = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[7]", "Payments Ledger Accordion")
authorize_now_button = ("//button[contains(text(),'Authorise Now')]", "Authorize Now Button")
auth_success_message = ("//div[contains(text(),'Successfully processed 1 item(s)')]", "Auth Success Message")
close_success_message = ("//i[@aria-invalid='true' and @class='close icon']", "Close Success Message Button")
verify_manual_auth_logs = ("//div[contains(text(),'by Test en-gcs: ManualAuth: Reason=Manual, Amount ')]", "Manual Auth Logs")
ebucks_amount_cell = ("//tbody/tr[2]/td[9]", "eBucks Amount Cell")

# Credit button and form locators
credit_button = ("//button[contains(text(),'Add Credit')]", "Add Credit Button")
amount_input = ("//input[@aria-invalid='true' and @name='amount']", "Amount Input")
comment_input = ("//textarea[@aria-invalid='true' and @name='comment']", "Comment Input")
ok_button = ("//button[contains(text(),'OK')]", "OK Button")

# Dynamic locators with format strings
refund_type_option = ("//span[contains(text(),'{}')]", "Refund Type Option")


class ManualAuthPage(PageBase):
    """Page object for Manual Authorization functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        # Initialize locators
        self.payments_ledger_accordion = self.locator(payments_ledger_accordion)
        self.authorize_now_button = self.locator(authorize_now_button)
        self.auth_success_message = self.locator(auth_success_message)
        self.close_success_message = self.locator(close_success_message)
        self.verify_manual_auth_logs = self.locator(verify_manual_auth_logs)
        self.ebucks_amount_cell = self.locator(ebucks_amount_cell)
        self.credit_button = self.locator(credit_button)
        self.amount_input = self.locator(amount_input)
        self.comment_input = self.locator(comment_input)
        self.ok_button = self.locator(ok_button)

    def click_payments_ledger_accordion(self):
        """Click the payments ledger accordion in the order view."""
        self.click(self.payments_ledger_accordion)
        self.wait_for_seconds(2)

    def click_authorize_now_button_and_close_notification(self):
        """Click authorize now button and handle the success notification."""
        self.click(self.authorize_now_button)
        self.wait_for_seconds(2)
        self.expect_to_be_visible(self.auth_success_message)
        self.click(self.close_success_message)
        self.expect_to_be_visible(self.verify_manual_auth_logs)

    def get_refund_amount_for_ebucks(self):
        """Get the refund amount for eBucks payment."""
        amount_text = self.get_text(self.ebucks_amount_cell)
        # Remove 'R ' prefix from amount
        amount = amount_text.replace("R ", "")
        return amount

    def click_credit_button_and_add_credit_amount(self, order_total):
        """Click the credit button and add credit amount."""
        self.click(self.credit_button)
        self.fill(self.amount_input, order_total)
        self.fill(self.comment_input, "Added credit amount test")
        self.click(self.credit_button)
        self.click(self.ok_button)

    def get_refund_type_locator(self, refund_type: str):
        """Get locator for a specific refund type option."""
        return self.locator((refund_type_option[0].format(refund_type), f"{refund_type} Option"))

    def click_manual_auth_override_button_and_complete_form(self, select_payment_method: str):
        """Complete the manual auth override form with the specified payment method."""
        manual_override = ManualOverridePage(self.page)

        # Click the manual override button
        manual_override.click(manual_override.btn_manual_override)
        self.wait_for_seconds(2)

        # Select payment method
        manual_override.click(manual_override.ddl_refund_method)
        payment_option = manual_override.get_payment_method_option(select_payment_method)
        manual_override.click(payment_option)

        # Get refund amount for eBucks if needed
        refund_amount = self.get_refund_amount_for_ebucks()

        # Fill form with refund amount and reason
        manual_override.fill(manual_override.txt_refund_amount, refund_amount)
        manual_override.fill(manual_override.txt_override_reason, "Test Override for Manual Auth")

        # Click refund override button
        manual_override.click(manual_override.btn_refund_override)
