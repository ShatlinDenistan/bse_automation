from playwright.sync_api import Page
from base.page_base import PageBase
import random
from datetime import datetime

# Locators
btn_customer_credit = ("//span[contains(text(),'Customer Credit')]", "Customer Credit Button")
btn_add_credit = ("//button[contains(text(),'Add Credit')]", "Add Credit Button")
btn_confirm_credit = ("//button[contains(text(),'OK')]", "OK Button")
lbl_confirm_dialog = ("//div[contains(text(),'Please confirm')]", "Confirm Dialog")
lbl_verify_customer_credit = ("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]", "Customer Credit Verification")
lbl_verify_date_created = ("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]", "Date Created Verification")
btn_add_credit_customer = ("//button[@class='ui small primary button'][2]", "Add Credit Customer Button")
btn_credit = ("//*[contains(text(),'Allocate credit')]", "Allocate Credit Button")
txt_credit_amount = ("//input[@name='amount']", "Credit Amount Input")
txt_comment = ("//textarea[@name='comment']", "Comment Textarea")

# Dynamic locators with format strings
credit_amount_text = ("//div[contains(text(),'R {}')]", "Credit Amount Text")
not_linked_text = ("//div[contains(text(),'Not linked to an order')]", "Not Linked Text")
date_created_text = ("//td[contains(text(),'{}')]", "Date Created Text")


class CustomerCreditPage(PageBase):
    """Page object for Customer Credit functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.btn_customer_credit = self.locator(btn_customer_credit)
        self.btn_add_credit = self.locator(btn_add_credit)
        self.btn_confirm_credit = self.locator(btn_confirm_credit)
        self.lbl_confirm_dialog = self.locator(lbl_confirm_dialog)
        self.lbl_verify_customer_credit = self.locator(lbl_verify_customer_credit)
        self.lbl_verify_date_created = self.locator(lbl_verify_date_created)
        self.btn_add_credit_customer = self.locator(btn_add_credit_customer)
        self.btn_credit = self.locator(btn_credit)
        self.txt_credit_amount = self.locator(txt_credit_amount)
        self.txt_comment = self.locator(txt_comment)
        self.not_linked_text = self.locator(not_linked_text)

    def get_credit_amount_text(self, amount: str):
        """Get locator for credit amount text with specific amount"""
        return self.locator((credit_amount_text[0].format(amount), f"Credit Amount {amount} Text"))

    def get_date_created_text(self, date: str):
        """Get locator for date created text with specific date"""
        return self.locator((date_created_text[0].format(date), f"Date Created {date} Text"))

    def expand_customer_credit_section_and_click_credit_button(self):
        """Expand the customer credit section and click the credit button"""
        self.wait_for_seconds(1)
        self.click(self.btn_credit)

    def enter_amount_and_comment(self):
        """Enter a random amount and comment for customer credit"""
        # Generate a random 3-digit number for credit amount
        customer_credit_amount = "".join(random.choices("123456789", k=3))
        self.fill(self.txt_credit_amount, customer_credit_amount)
        self.fill(self.txt_comment, f"Test comment for customer credit {customer_credit_amount}")
        # Return the generated amount for later verification
        return customer_credit_amount

    def select_add_credit_button(self):
        """Click the add credit button and wait for confirmation dialog"""
        self.click(self.btn_add_credit)
        self.expect_to_be_visible(self.lbl_confirm_dialog)

    def select_ok_on_dialog(self):
        """Click OK on the confirmation dialog"""
        self.click(self.btn_confirm_credit)

    def verify_customer_credit_is_applied(self, credit_amount):
        """Verify that customer credit is applied correctly"""
        # Format current date and time for verification
        date = datetime.now().strftime("%d-%b-%Y @ %H:%M")
        date = date.replace("@ 0", "@ ")

        # Check that credit amount and "Not linked to an order" text is visible
        credit_amount_locator = self.get_credit_amount_text(credit_amount)
        self.expect_to_be_visible(credit_amount_locator)
        self.expect_to_be_visible(self.not_linked_text)

        # Optionally check the date (commented out in original implementation)
        # date_locator = self.get_date_created_text(date)
        # self.expect_to_be_visible(date_locator)

    def verify_order_credit_is_applied(self, credit_amount):
        """Verify that order credit is applied correctly"""
        # Scroll down to make the credit amount visible
        self.page.evaluate("window.scrollTo(0, 250)")

        # Check that credit amount is visible on the page
        credit_amount_locator = self.get_credit_amount_text(credit_amount)
        self.expect_to_be_visible(credit_amount_locator)

    def add_customer_credit(self):
        """Complete the customer credit addition workflow"""
        self.expand_customer_credit_section_and_click_credit_button()
        credit_amount = self.enter_amount_and_comment()
        self.select_add_credit_button()
        self.select_ok_on_dialog()
        self.verify_customer_credit_is_applied(credit_amount)
        return credit_amount

    def expand_customer_credit_accordion(self):
        """
        Expand the customer credit accordion under customer info
        """
        # Define the customer credit accordion locator
        customer_credit_accordion = self.locator("//div[@class='accordion ui fluid styled']//div[contains(text(),'Customer Credit')]", "Customer Credit Accordion")
        self.expect_to_be_visible(customer_credit_accordion)
        self.click(customer_credit_accordion)
        self.wait_for_seconds(1)
