import random

from playwright.sync_api import Page

from base.page_base import PageBase

# Locators
btn_manual_override = ("//a[contains(text(),'Manual Override')]", "Manual Override Button")
ddl_refund_method = ("//div[contains(text(),'- - Select a refund method - -')]", "Refund Method Dropdown")
lst_credit_card = ("//span[contains(text(),'Credit Card')]", "Credit Card Option")
lst_ebucks = ("//span[contains(text(),'eBucks')]", "eBucks Option")
lst_payfast = ("//span[contains(text(),'PayFast')]", "PayFast Option")
lst_eft = ("//span[contains(text(),'EFT')]", "EFT Option")
lst_discovery_miles = ("//span[contains(text(),'Discovery Miles')]", "Discovery Miles Option")
txt_refund_amount = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[2]/div[1]/input[1]", "Refund Amount Input")
txt_eft_refund_amount = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[3]/div[1]/input[1]", "EFT Refund Amount Input")
txt_override_reason = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[3]/textarea[1]", "Override Reason Textarea")
txt_eft_override_reason = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[7]/textarea[1]", "EFT Override Reason Textarea")
btn_refund_override = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[4]/button[1]", "Refund Override Button")
btn_eft_refund_override = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[8]/button[1]", "EFT Refund Override Button")
btn_confirm_override = ("//body/div[2]/div[1]/div[2]/button[2]", "Confirm Override Button")
verification_message = ("//div[contains(text(),'Successfully processed 1 item(s)')]", "Success Message")
close_success_message = ("//i[@aria-hidden='true' and @class='close icon']", "Close Success Message Button")
original_payment_method = ("//div[contains(text(),'- - Select an original payment - -')]", "Original Payment Method Dropdown")
select_eft_originate_pay_meth = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]", "EFT Original Payment Method Option")
txt_bank_account = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]", "Bank Account Input")
ddl_bank_name = ("//div[contains(text(),'- - Select a bank - -')]", "Bank Name Dropdown")
select_bank_name = ("//span[contains(text(),'ABSA Bank')]", "ABSA Bank Option")
ddl_branch = ("//div[contains(text(),'- - Select branch - -')]", "Branch Dropdown")
select_branch = ("//span[contains(text(),'ABSA Electronic Settlement CNT')]", "ABSA Electronic Settlement Branch Option")
btn_okay = ("//a[contains(text(),'Okay')]", "Okay Button")
txt_credit_amount = ("//input[@name='amount']", "Credit Amount Input")
txt_credit_comments = ("//textarea[@name='adminNote']", "Credit Comments Textarea")
search_input = ("//input[@name='search']", "Search Input")
search_button = ("//button[@type='submit']", "Search Button")
failed_override_note = ("//div[contains(text(),'by Test en-gcs: Refund request submission failed (')]", "Failed Override Note")
cc_amount_cell = ("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]", "Credit Card Amount Cell")
ebucks_amount_cell = ("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]", "eBucks Amount Cell")
refund_amount_cell_pattern = ("//td[2][contains(text(),'{}')]", "Refund Amount Cell")

# Dynamic locators with format strings
payment_method_option = ("//span[contains(text(),'{}')]", "Payment Method Option")
payment_method_text = ("//div[contains(text(),'{}')]", "Payment Method Text")
refund_text = ("//div[contains(text(),'Refund')]", "Refund Text")
processed_by_text = ("//div[contains(text(),'Test en-gcs')]", "Processed By Text")
bank_option = ("//span[contains(text(),'{}')]", "Bank Option")
branch_option = ("//span[contains(text(),'{}')]", "Branch Option")
admin_note_pattern = ("//li[contains(text(),'Refund by {}, Amount: ')]", "Admin Note Pattern")


class ManualOverridePage(PageBase):
    """Page object for Manual Override functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        # Standard button, input and dropdown locators
        self.btn_manual_override = self.locator(btn_manual_override)
        self.ddl_refund_method = self.locator(ddl_refund_method)
        self.lst_credit_card = self.locator(lst_credit_card)
        self.lst_ebucks = self.locator(lst_ebucks)
        self.lst_payfast = self.locator(lst_payfast)
        self.lst_eft = self.locator(lst_eft)
        self.lst_discovery_miles = self.locator(lst_discovery_miles)
        self.txt_refund_amount = self.locator(txt_refund_amount)
        self.txt_eft_refund_amount = self.locator(txt_eft_refund_amount)
        self.txt_override_reason = self.locator(txt_override_reason)
        self.txt_eft_override_reason = self.locator(txt_eft_override_reason)
        self.btn_refund_override = self.locator(btn_refund_override)
        self.btn_eft_refund_override = self.locator(btn_eft_refund_override)
        self.btn_confirm_override = self.locator(btn_confirm_override)
        self.verification_message = self.locator(verification_message)
        self.close_success_message = self.locator(close_success_message)
        self.original_payment_method = self.locator(original_payment_method)
        self.select_eft_originate_pay_meth = self.locator(select_eft_originate_pay_meth)
        self.txt_bank_account = self.locator(txt_bank_account)
        self.ddl_bank_name = self.locator(ddl_bank_name)
        self.select_bank_name = self.locator(select_bank_name)
        self.ddl_branch = self.locator(ddl_branch)
        self.select_branch = self.locator(select_branch)
        self.btn_okay = self.locator(btn_okay)
        self.refund_text = self.locator(refund_text)
        self.processed_by_text = self.locator(processed_by_text)

        # Credit-related locators
        self.txt_credit_amount = self.locator(txt_credit_amount)
        self.txt_credit_comments = self.locator(txt_credit_comments)

        # Search and table locators
        self.search_input = self.locator(search_input)
        self.search_button = self.locator(search_button)
        self.cc_amount_cell = self.locator(cc_amount_cell)
        self.ebucks_amount_cell = self.locator(ebucks_amount_cell)
        self.failed_override_note = self.locator(failed_override_note)

        # Pre-initialize dynamic locators for commonly used options
        self.ebucks_note = self.locator((admin_note_pattern[0].format("eBucks"), "eBucks Admin Note"))
        self.credit_card_note = self.locator((admin_note_pattern[0].format("CreditCard"), "Credit Card Admin Note"))

        # Create a dictionary of payment method options for common payment types
        self.payment_method_options = {
            "Credit Card": self.locator((payment_method_option[0].format("Credit Card"), "Credit Card Option")),
            "eBucks": self.locator((payment_method_option[0].format("eBucks"), "eBucks Option")),
            "PayFast": self.locator((payment_method_option[0].format("PayFast"), "PayFast Option")),
            "EFT": self.locator((payment_method_option[0].format("EFT"), "EFT Option")),
            "Discovery Miles": self.locator((payment_method_option[0].format("Discovery Miles"), "Discovery Miles Option")),
        }

        # Create a dictionary of payment method text for verification
        self.payment_method_texts = {
            "Paygate": self.locator((payment_method_text[0].format("Paygate"), "Paygate Text")),
            "eBucks": self.locator((payment_method_text[0].format("eBucks"), "eBucks Text")),
            "PayFast": self.locator((payment_method_text[0].format("PayFast"), "PayFast Text")),
            "EFT": self.locator((payment_method_text[0].format("EFT"), "EFT Text")),
            "iPay": self.locator((payment_method_text[0].format("iPay"), "iPay Text")),
            "Discovery Miles": self.locator((payment_method_text[0].format("Discovery Miles"), "Discovery Miles Text")),
            "Deposit": self.locator((payment_method_text[0].format("Deposit"), "Deposit Text")),
        }

        # Common bank options
        self.bank_options = {"ABSA Bank": self.locator((bank_option[0].format("ABSA Bank"), "ABSA Bank Option"))}

        # Common branch options
        self.branch_options = {"ABSA Electronic Settlement CNT": self.locator((branch_option[0].format("ABSA Electronic Settlement CNT"), "ABSA Electronic Settlement Branch Option"))}

    def get_payment_method_option(self, payment_method: str):
        """Get locator for a specific payment method option"""
        # Use dictionary if available, otherwise create dynamically
        if payment_method in self.payment_method_options:
            return self.payment_method_options[payment_method]
        return self.locator((payment_method_option[0].format(payment_method), f"{payment_method} Option"))

    def get_payment_method_text(self, payment_method: str):
        """Get locator for a specific payment method text"""
        # Use dictionary if available, otherwise create dynamically
        if payment_method in self.payment_method_texts:
            return self.payment_method_texts[payment_method]
        return self.locator((payment_method_text[0].format(payment_method), f"{payment_method} Text"))

    def get_bank_option(self, bank_name: str):
        """Get locator for a specific bank option"""
        # Use dictionary if available, otherwise create dynamically
        if bank_name in self.bank_options:
            return self.bank_options[bank_name]
        return self.locator((bank_option[0].format(bank_name), f"{bank_name} Option"))

    def get_branch_option(self, branch_name: str):
        """Get locator for a specific branch option"""
        # Use dictionary if available, otherwise create dynamically
        if branch_name in self.branch_options:
            return self.branch_options[branch_name]
        return self.locator((branch_option[0].format(branch_name), f"{branch_name} Option"))

    def complete_override_form(self, payment_method: str, refund_amount: str, reason: str):
        """Complete the override form with the given payment method, amount and reason"""
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.click(self.ddl_refund_method)
        payment_option = self.get_payment_method_option(payment_method)
        self.click(payment_option)
        self.fill(self.txt_refund_amount, refund_amount)
        self.fill(self.txt_override_reason, reason)
        self.click(self.btn_refund_override)

    def confirm_override(self):
        """Confirm the override and close the success message"""
        self.click(self.btn_confirm_override)
        self.expect_to_be_visible(self.verification_message)
        self.click(self.close_success_message)

    def select_payment_method(self, payment_method: str):
        """Select a payment method from the dropdown."""
        self.click(self.ddl_refund_method)
        payment_option = self.get_payment_method_option(payment_method)
        self.click(payment_option)

    def fill_override_form(self, refund_amount: str, reason: str):
        """Fill the override form with refund amount and reason."""
        self.fill(self.txt_refund_amount, refund_amount)
        self.fill(self.txt_override_reason, reason)

    def complete_override_form_with_payment_method(self, payment_method: str, refund_amount: str, reason: str):
        """Complete the override form with a specific payment method."""
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.select_payment_method(payment_method)
        self.fill_override_form(refund_amount, reason)
        self.click(self.btn_refund_override)

    def complete_override_form_exceeding_amount(self, payment_method: str, refund_amount: str, reason: str):
        """Complete the override form with an amount exceeding the total."""
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.select_payment_method(payment_method)
        self.fill_override_form(refund_amount, reason)
        self.click(self.btn_refund_override)

    def complete_override_form_efb(self, payment_method: str, refund_amount: str, reason: str):
        """Complete the override form for eBucks or Credit Card."""
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.select_payment_method(payment_method)
        self.fill_override_form(refund_amount, reason)
        self.click(self.btn_refund_override)
        self.click(self.btn_confirm_override)
        self.expect_to_be_visible(self.btn_okay)
        self.click(self.btn_okay)

    def capture_efb_banking_details(self, account_number: str, bank_name: str, branch_name: str, reason: str):
        """Capture EFT banking details."""
        self.fill(self.txt_bank_account, account_number)
        self.click(self.ddl_bank_name)
        bank = self.get_bank_option(bank_name)
        self.click(bank)
        self.click(self.ddl_branch)
        branch = self.get_branch_option(branch_name)
        self.click(branch)
        self.fill(self.txt_eft_override_reason, reason)
        self.click(self.btn_eft_refund_override)

    def confirm_override_and_view_logs(self, order_id: str):
        """Confirm the override and view logs."""
        self.click(self.btn_confirm_override)
        self.expect_to_be_visible(self.btn_okay)
        self.click(self.btn_okay)
        self.go_to_page(f"order/{order_id}/refunds_logs")
        self.wait_for_seconds(2)

    def verify_override_details(self, payment_method: str):
        """Verify override details on the page."""
        payment_text = self.get_payment_method_text(payment_method)
        self.expect_to_be_visible(payment_text)
        self.expect_to_be_visible(self.refund_text)
        self.expect_to_be_visible(self.processed_by_text)

    def complete_override_form_eft(self, payment_method: str, refund_amount: str):
        """Complete the override form for EFT."""
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.click(self.ddl_refund_method)
        payment_option = self.get_payment_method_option(payment_method)
        self.click(payment_option)
        self.click(self.original_payment_method)
        self.click(self.select_eft_originate_pay_meth)
        self.fill(self.txt_eft_refund_amount, refund_amount)

    def complete_override_form_for_credit_card_and_ebucks(self, credit_card_amount: str, ebucks_amount: str):
        """Complete the override form for both Credit Card and eBucks payment methods."""
        # Handle eBucks first
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.click(self.ddl_refund_method)
        self.click(self.lst_ebucks)
        self.fill(self.txt_refund_amount, ebucks_amount)
        self.fill(self.txt_override_reason, "Test eBucks Override")
        self.click(self.btn_refund_override)
        self.click(self.btn_confirm_override)
        self.expect_to_be_visible(self.btn_okay)
        self.click(self.btn_okay)

        # Handle Credit Card next
        self.click(self.btn_manual_override)
        self.wait_for_seconds(2)
        self.click(self.ddl_refund_method)
        self.click(self.lst_credit_card)
        self.fill(self.txt_refund_amount, credit_card_amount)
        self.fill(self.txt_override_reason, "Test Credit Card Override")
        self.click(self.btn_refund_override)

    def verify_dual_payment_admin_notes(self):
        """Verify that admin notes for both eBucks and Credit Card refunds exist."""
        self.expect_to_be_visible(self.ebucks_note)
        self.expect_to_be_visible(self.credit_card_note)

    def verify_failed_override_admin_note(self):
        """Verify that a failed override admin note exists."""
        self.expect_to_be_visible(self.failed_override_note)

    def enter_donation_credit(self, amount: str, comment: str):
        """Enter donation credit amount and comment."""
        self.fill(self.txt_credit_amount, amount)
        self.fill(self.txt_credit_comments, comment)

    def verify_refund_amount_excludes_donation(self, original_amount: str, donation_amount: str):
        """Verify that the refund amount excludes the donation amount."""
        expected_refund = float(original_amount) - float(donation_amount)
        formatted_refund = f"{expected_refund:,}"
        refund_cell = self.locator((refund_amount_cell_pattern[0].format(formatted_refund), f"Refund Amount Cell ({formatted_refund})"))
        self.expect_to_be_visible(refund_cell)

    def get_refund_amounts_for_payment_methods(self):
        """Get refund amounts for Credit Card and eBucks payment methods."""
        # Get Credit Card amount
        cc_cell = self.locator(cc_amount_cell)
        ebucks_cell = self.locator(ebucks_amount_cell)

        cc_amount = self.get_text(cc_cell).replace("R ", "")
        ebucks_amount = self.get_text(ebucks_cell).replace("R ", "")

        return cc_amount, ebucks_amount

    def search_for_order(self, order_id: str):
        """Search for an order by ID."""
        search_input_locator = self.locator(search_input)
        search_button_locator = self.locator(search_button)

        self.fill(search_input_locator, order_id)
        self.click(search_button_locator)

    def generate_random_account_number(self):
        """Generate a random 8-digit account number."""

        return "".join([str(random.randint(0, 9)) for _ in range(8)])

    def complete_override_form_with_amount_exceeding_total(self, payment_method: str, base_amount: str):
        """Complete the override form with an amount exceeding the total."""
        exceeded_amount = float(base_amount) + 700
        self.complete_override_form(payment_method, str(exceeded_amount), "Test Override")

    def click_manual_override_button_and_complete_override_form_eft(self):
        """
        Click manual override button and complete the form for EFT payment method
        """
        self.click(self.btn_manual_override)
        self.wait_for_seconds(1)

        # Select EFT refund method
        self.click(self.ddl_refund_method)
        self.click(self.lst_eft)

        # Select original payment method
        self.click(self.original_payment_method)
        self.click(self.select_eft_originate_pay_meth)

        # Fill in the amount (using the amount from database)
        self.fill(self.txt_eft_refund_amount, self.utils.get_env("REFUND_AMOUNT", "100"))

        # No need to continue here, the next method will handle banking details

    def capture_eft_banking_details(self):
        """
        Fill in the EFT banking details form
        """
        # Generate random account number
        account_number = self.generate_random_account_number()

        # Fill in account number
        self.fill(self.txt_bank_account, account_number)

        # Select bank name
        self.click(self.ddl_bank_name)
        self.click(self.select_bank_name)

        # Select bank branch
        self.click(self.ddl_branch)
        self.click(self.select_branch)

        # Fill in reason
        self.fill(self.txt_eft_override_reason, "Test EFT Refund")

        # Click refund button
        self.click(self.btn_eft_refund_override)

    def confirm_manual_override_and_view_logs(self):
        """
        Confirm the manual override and view logs
        """
        self.click(self.btn_confirm_override)
        self.expect_to_be_visible(self.verification_message)
        self.wait_for_seconds(1)
