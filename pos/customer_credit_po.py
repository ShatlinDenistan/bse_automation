"""Customer Credit Page Object file."""

from base.page_base import PageBase


class CustomerCreditPO(PageBase):

    # region Customer Credit Section

    @property
    def customer_credit_btn(self):
        selector = "//span[contains(text(),'Customer Credit')]"
        return self.locator(selector, "Customer Credit Button")

    @property
    def add_credit_btn(self):
        selector = "//button[contains(text(),'Add Credit')]"
        return self.locator(selector, "Add Credit Button")

    @property
    def confirm_credit_btn(self):
        selector = "//button[contains(text(),'OK')]"
        return self.locator(selector, "Confirm Credit Button")

    @property
    def confirm_dialog(self):
        selector = "//div[contains(text(),'Please confirm')]"
        return self.locator(selector, "Confirmation Dialog")

    @property
    def verify_customer_credit(self):
        selector = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]"
        return self.locator(selector, "Verify Customer Credit")

    @property
    def verify_date_created(self):
        selector = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]"
        return self.locator(selector, "Verify Date Created")

    @property
    def add_credit_customer_btn(self):
        selector = '//button[@class="ui small primary button"][2]'
        return self.locator(selector, "Add Credit Customer Button")

    # endregion
