from playwright.sync_api import Page
from datetime import datetime
import random

from base.page_base import PageBase

# Locators
btn_customer_credit = ("//span[contains(text(),'Customer Credit')]", "Customer Credit Button")
btn_add_credit = ("//button[contains(text(),'Add Credit')]", "Add Credit Button")
btn_confirm_credit = ("//button[contains(text(),'OK')]", "Confirm Credit Button")
lbl_confirm_dialog = ("//div[contains(text(),'Please confirm')]", "Confirm Dialog Label")
lbl_verify_customer_credit = ("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]", "Verify Customer Credit Label")
lbl_verify_date_created = ("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]", "Verify Date Created Label")
btn_add_credit_customer = ("//button[@class='ui small primary button'][2]", "Add Credit Customer Button")


class CustomerCreditPage(PageBase):
    """Page object for Customer Credit functionality"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.btn_customer_credit = self.locator(btn_customer_credit)
        self.btn_add_credit = self.locator(btn_add_credit)
        self.btn_confirm_credit = self.locator(btn_confirm_credit)
        self.lbl_confirm_dialog = self.locator(lbl_confirm_dialog)
        self.lbl_verify_customer_credit = self.locator(lbl_verify_customer_credit)
        self.lbl_verify_date_created = self.locator(lbl_verify_date_created)
        self.btn_add_credit_customer = self.locator(btn_add_credit_customer)

    def expand_customer_credit_section_and_click_credit_button(self):
        """Expand the Customer Credit section and click the Credit button."""
        self.page.wait_for_timeout(1000)  # Wait for 1 second
        self.click(self.btn_customer_credit)
        self.click(self.btn_add_credit_customer)

    def enter_amount_and_comment(self):
        """Enter a random amount and a comment."""
        self.customer_credit_amount = str(random.randint(100, 999))
        self.type(self.btn_add_credit, self.customer_credit_amount)

    def select_add_credit_button(self):
        """Click the Add Credit button and wait for the confirmation dialog."""
        self.click(self.btn_add_credit)
        self.page.wait_for_selector(self.lbl_confirm_dialog)

    def select_ok_on_dialog(self):
        """Click OK on the confirmation dialog."""
        self.click(self.btn_confirm_credit)

    def verify_customer_credit_applied(self):
        """Verify that the customer credit is applied."""
        current_date = datetime.now().strftime("%d-%b-%Y @ %H:%M")
        if "@ 0" in current_date:
            current_date = current_date.replace("@ 0", "@ ")
        print(current_date)  # Log to console
        self.page.locator(self.lbl_verify_customer_credit).wait_for()
        assert self.customer_credit_amount in self.page.locator(self.lbl_verify_customer_credit).inner_text()
        assert "Not linked to an order" in self.page.locator(self.lbl_verify_customer_credit).inner_text()

    def verify_order_credit_applied(self):
        """Scroll until the credit amount is visible and verify that the credit was added."""
        self.page.evaluate("window.scrollTo(0, 250)")
        self.page.locator(self.lbl_verify_customer_credit).wait_for()
        assert self.customer_credit_amount in self.page.locator(self.lbl_verify_customer_credit).inner_text()
