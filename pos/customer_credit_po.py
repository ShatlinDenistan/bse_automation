"""Customer Credit Page Object file."""

from base.page_base import PageBase

# Module-level constants
CUSTOMER_CREDIT_BTN = "//span[contains(text(),'Customer Credit')]"
ADD_CREDIT_BTN = "//button[contains(text(),'Add Credit')]"
CONFIRM_CREDIT_BTN = "//button[contains(text(),'OK')]"
CONFIRM_DIALOG = "//div[contains(text(),'Please confirm')]"
VERIFY_CUSTOMER_CREDIT = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]"
VERIFY_DATE_CREATED = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]"
ADD_CREDIT_CUSTOMER_BTN = '//button[@class="ui small primary button"][2]'


class CustomerCreditPO(PageBase):
    """Page Object for Customer Credit functionality."""

    def __init__(self, page):
        """Initialize the Customer Credit Page Object with elements."""
        super().__init__(page)
        self.customer_credit_btn = self.locator(CUSTOMER_CREDIT_BTN, "Customer Credit Button")
        self.add_credit_btn = self.locator(ADD_CREDIT_BTN, "Add Credit Button")
        self.confirm_credit_btn = self.locator(CONFIRM_CREDIT_BTN, "Confirm Credit Button")
        self.confirm_dialog = self.locator(CONFIRM_DIALOG, "Confirmation Dialog")
        self.verify_customer_credit = self.locator(VERIFY_CUSTOMER_CREDIT, "Verify Customer Credit")
        self.verify_date_created = self.locator(VERIFY_DATE_CREATED, "Verify Date Created")
        self.add_credit_customer_btn = self.locator(ADD_CREDIT_CUSTOMER_BTN, "Add Credit Customer Button")
