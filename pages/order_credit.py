import random
from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
btn_customer_credit = ("//span[contains(text(),'Customer Credit')]", "Customer Credit Button")
btn_allocate_credit = ("//*[contains(text(),'Allocate credit')]", "Allocate Credit Button")
txt_credit_amount = ("//input[@name='amount']", "Credit Amount Input")
txt_credit_comments = ("//textarea[@name='adminNote']", "Credit Comments Textarea")
dropdown_credit_reason = ("//*[@name='reason']", "Credit Reason Dropdown")
reason_goodwill = ("//*[@role='option']/span[contains(text(),'Goodwill')]", "Goodwill Reason")
reason_late_delivery_fee = ("//*[@role='option']/span[contains(text(),'Late delivery fee')]", "Late Delivery Fee Reason")
reason_sub_late_delivery = ("//*[@role='option']/span[contains(text(),'Subscription late delivery fee')]", "Subscription Late Delivery Fee")
reason_credit_breach = ("//*[@role='option']/span[contains(text(),'Credit breach')]", "Credit Breach Reason")
txt_jira_number = ("//input[@name='extra']", "JIRA Number Input")
reason_b2b_bulk_order = ("//*[@role='option']/span[contains(text(),'B2B bulk orders')]", "B2B Bulk Orders Reason")
reason_failed_eft_refunds = ("//*[@role='option']/span[contains(text(),'Failed EFT refunds')]", "Failed EFT Refunds Reason")
accordion_order_items = ("//span[contains(text(),'Order Items')]", "Order Items Accordion")
btn_order_item_menu = ("//div[@class='accordion ui']//*[@class='ui simple dropdown']/i", "Order Item Menu Button")
credit_item_option = ("//*[contains(text(),'Credit Item')]", "Credit Item Option")
reason_system_error = ("//*[@role='option']/span[contains(text(),'System error: Credit removal failed')]", "System Error Reason")
txt_rfn_number = ("//*[@placeholder='Please enter a RFN number']", "RFN Number Input")
reason_duplicate_payment = ("//*[@role='option']/span[contains(text(),'Duplicate payment')]", "Duplicate Payment Reason")
reason_cod_return = ("//*[@role='option']/span[contains(text(),'COD return')]", "COD Return Reason")
accordion_order_financials = ("//*[contains(text(),'Order Financials')]", "Order Financials Accordion")
order_financials_return_cancelled = ("//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Return Cancelled')]//following-sibling::td", "Order Financials Return Cancelled")
order_financials_cancelled = ("//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Cancelled')]//following-sibling::td", "Order Financials Cancelled")
reason_credit_error = ("//*[@role='option']/span[contains(text(),'Credit error')]", "Credit Error Reason")
validation_error = ("//*[@class='ui negative message']/div/div", "Validation Error Message")

# Dynamic locator with format string
credit_reason_option = ("//*[@role='option']/span[contains(text(),'{}')]", "Credit Reason Option")


class OrderCreditPage(PageBase):
    """Page object for Order Credit functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        # Standard button, input and dropdown locators
        self.btn_customer_credit = self.locator(btn_customer_credit)
        self.btn_allocate_credit = self.locator(btn_allocate_credit)
        self.txt_credit_amount = self.locator(txt_credit_amount)
        self.txt_credit_comments = self.locator(txt_credit_comments)
        self.dropdown_credit_reason = self.locator(dropdown_credit_reason)

        # Credit reason options
        self.reason_goodwill = self.locator(reason_goodwill)
        self.reason_late_delivery_fee = self.locator(reason_late_delivery_fee)
        self.reason_sub_late_delivery = self.locator(reason_sub_late_delivery)
        self.reason_credit_breach = self.locator(reason_credit_breach)
        self.reason_b2b_bulk_order = self.locator(reason_b2b_bulk_order)
        self.reason_failed_eft_refunds = self.locator(reason_failed_eft_refunds)
        self.reason_system_error = self.locator(reason_system_error)
        self.reason_duplicate_payment = self.locator(reason_duplicate_payment)
        self.reason_cod_return = self.locator(reason_cod_return)
        self.reason_credit_error = self.locator(reason_credit_error)

        # Additional input fields
        self.txt_jira_number = self.locator(txt_jira_number)
        self.txt_rfn_number = self.locator(txt_rfn_number)

        # Order sections and menus
        self.accordion_order_items = self.locator(accordion_order_items)
        self.btn_order_item_menu = self.locator(btn_order_item_menu)
        self.credit_item_option = self.locator(credit_item_option)
        self.accordion_order_financials = self.locator(accordion_order_financials)
        self.order_financials_return_cancelled = self.locator(order_financials_return_cancelled)
        self.order_financials_cancelled = self.locator(order_financials_cancelled)
        self.validation_error = self.locator(validation_error)

    def get_credit_reason_option(self, reason: str):
        """Get locator for a specific credit reason option"""
        return self.locator((credit_reason_option[0].format(reason), f"{reason} Option"))

    def expand_the_customer_credit_section_and_click_the_allocate_credit_button(self):
        """Expand the customer credit section and click the allocate credit button"""
        self.click(self.btn_customer_credit)
        self.wait_for_seconds(1)
        self.click(self.btn_allocate_credit)

    def select_a_credit_reason(self, reason: str):
        """Select a credit reason from the dropdown"""
        self.click(self.dropdown_credit_reason)
        reason_option = self.get_credit_reason_option(reason)
        self.expect_to_be_visible(reason_option)
        self.click(reason_option)

    def enter_an_amount_and_enter_an_admin_note_for_order_credit(self):
        """Enter a random amount and admin note for order credit"""
        order_credit_amount = str(random.randint(1, 35))
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, order_credit_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")
        return order_credit_amount

    def enter_invalid_min_amount(self, min_amount: str):
        """Enter an invalid minimum amount"""
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, min_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

    def enter_invalid_max_amount(self, max_amount: str):
        """Enter an invalid maximum amount"""
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, max_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

    def verify_validation_error(self):
        """Verify validation error message is displayed"""
        error_text = self.get_text(self.validation_error)
        assert error_text == "Validation Error", f"Expected 'Validation Error' but got '{error_text}'"

    def enter_jira_number_for_credit_breach_reason(self):
        """Enter JIRA number for credit breach reason"""
        self.fill(self.txt_jira_number, "Automation-Jira-Number-123")

    def expand_order_items_section_and_click_the_credit_item_option(self):
        """Expand order items section and click the credit item option"""
        self.click(self.btn_order_item_menu)
        self.click(self.credit_item_option)

    def enter_a_negative_amount_and_enter_an_admin_note_for_order_credit(self):
        """Enter a negative amount and admin note for order credit"""
        order_credit_amount = "-3"
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, order_credit_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")
        return order_credit_amount

    def enter_rfn_for_system_error_reason(self):
        """Enter RFN number for system error reason"""
        self.fill(self.txt_rfn_number, "Automation-RFN-Number-1")

    def enter_calculated_amount_and_enter_an_admin_note_for_order_credit(self, order_total: str, order_shipping: str, order_discount: str):
        """Calculate and enter amount based on order values"""
        # Calculate Auth Total
        order_total_amount = float(order_total)
        order_shipping_amount = float(order_shipping)
        order_discount_amount = float(order_discount)

        calculated_auth_total = order_total_amount + order_shipping_amount - order_discount_amount + 10000
        formatted_auth_total = f"{calculated_auth_total:,}"

        # Enter Credit Amount and Admin Note
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, formatted_auth_total)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

        return formatted_auth_total

    def get_return_cancelled_amount_from_order_financials(self):
        """Get return cancelled amount from order financials"""
        # Expand Order Financials section if needed
        self.expect_to_be_visible(self.accordion_order_financials)
        self.click(self.accordion_order_financials)

        # Get amount and cleanup
        return_cancelled_amount = self.get_text(self.order_financials_return_cancelled)
        return_cancelled_amount_clean = return_cancelled_amount.replace("R ", "")

        # Convert to number for calculation
        return_cancelled_amount_number = float(return_cancelled_amount_clean)
        calculated_amount = return_cancelled_amount_number + 10000

        return return_cancelled_amount_clean, calculated_amount

    def enter_return_canceled_amount_and_enter_an_admin_note_for_order_credit(self, return_cancelled_amount: str):
        """Enter return cancelled amount and admin note for order credit"""
        # Enter Credit Amount and Admin Note
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, return_cancelled_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")

    def get_cancelled_amount_from_order_financials(self):
        """Get cancelled amount from order financials"""
        # Expand Order Financials section if needed
        self.expect_to_be_visible(self.accordion_order_financials)
        self.click(self.accordion_order_financials)

        # Get amount and cleanup
        cancelled_amount = self.get_text(self.order_financials_cancelled)
        cancelled_amount_clean = cancelled_amount.replace("R ", "")

        # Convert to number for calculation
        cancelled_amount_number = float(cancelled_amount_clean)
        calculated_amount = cancelled_amount_number + 10000

        return cancelled_amount_clean, calculated_amount

    def enter_canceled_amount_and_enter_an_admin_note_for_order_credit(self, cancelled_amount: str):
        """Enter cancelled amount and admin note for order credit"""
        # Enter Credit Amount and Admin Note
        self.clear(self.txt_credit_amount)
        self.fill(self.txt_credit_amount, cancelled_amount)
        self.fill(self.txt_credit_comments, "Automation Test Admin Note")
