from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
btn_customer_credit = "xpath=//span[contains(text(),'Customer Credit')]"
btn_allocate_credit = "xpath=//*[contains(text(),'Allocate credit')]"
txt_credit_amount = "xpath=//input[@name='amount']"
txt_credit_comments = "xpath=//textarea[@name='adminNote']"
dropdown_credit_reason = "xpath=//*[@name='reason']"
validation_error = "xpath=//*[@class='ui negative message']/div/div"


class OrderCreditPage(PageBase):
    """Page object for Order Credit functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.btn_customer_credit = self.locator(btn_customer_credit)
        self.btn_allocate_credit = self.locator(btn_allocate_credit)
        self.txt_credit_amount = self.locator(txt_credit_amount)
        self.txt_credit_comments = self.locator(txt_credit_comments)
        self.dropdown_credit_reason = self.locator(dropdown_credit_reason)
        self.validation_error = self.locator(validation_error)

    def expand_customer_credit_section_and_allocate_credit(self):
        self.btn_customer_credit.click()
        self.page.wait_for_timeout(2000)
        self.btn_allocate_credit.click()

    def select_credit_reason(self, reason: str):
        self.dropdown_credit_reason.click()
        self.page.click(f"xpath=//*[@role='option']/span[contains(text(),'{reason}')]")

    def enter_credit_amount_and_admin_note(self, amount: str, note: str):
        self.txt_credit_amount.fill(amount)
        self.txt_credit_comments.fill(note)

    def verify_validation_error(self, expected_error: str):
        error_text = self.validation_error.text_content()
        assert error_text == expected_error, f"Expected '{expected_error}', but got '{error_text}'"
