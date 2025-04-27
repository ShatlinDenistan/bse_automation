from base.page_base import PageBase


class ManualRefundPO(PageBase):
    """Page Object for Manual Refund functionality"""

    # region UI Section Elements

    @property
    def customer_credit_accordion(self):
        selector = "//div[contains(text(),' available credit')]"
        return self.locator(selector, "Customer credit accordion")

    @property
    def refund_amount_display(self):
        selector = "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/table/tbody/tr/td[2]"
        return self.locator(selector, "Refund amount display")

    @property
    def not_eligible_for_refund(self):
        selector = "//li[contains(text(),'Order ${order_ids[0]} is not eligible for refund.')]"
        return self.locator(selector, "Not eligible for refund message")

    # endregion

    # region Button Elements

    @property
    def refund_button(self):
        selector = "${btnRefund}"
        return self.locator(selector, "Refund button")

    @property
    def submit_refund_request_button(self):
        selector = "${btnSubmittingRefundReq}"
        return self.locator(selector, "Submit refund request button")

    @property
    def okay_button(self):
        selector = "${btnOkay}"
        return self.locator(selector, "Okay button")

    @property
    def view_refund_log_button(self):
        selector = "//a[contains(text(),'View Refund Log')]"
        return self.locator(selector, "View refund log button")

    @property
    def proceed_button(self):
        selector = "//button[contains(text(),'Proceed')]"
        return self.locator(selector, "Proceed button")

    # endregion

    # region Input Field Elements

    @property
    def bank_account_input(self):
        selector = "//input[@autocomplete='off' and @name='bankAccount' and @type='text']"
        return self.locator(selector, "Bank account input")

    @property
    def txt_jira_number(self):
        selector = "//input[@name='extra']"
        return self.locator(selector, "JIRA number field")

    # endregion

    # region Dropdown Elements

    @property
    def bank_dropdown(self):
        selector = "//div[@name='bank' and @role='listbox' and @class='ui fluid selection dropdown']"
        return self.locator(selector, "Bank dropdown")

    @property
    def branch_dropdown(self):
        selector = "//div[contains(text(),'- - Select branch - -')]"
        return self.locator(selector, "Branch dropdown")

    @property
    def capitec_bank_option(self):
        selector = "//span[contains(text(),'Capitec Bank')]"
        return self.locator(selector, "Capitec Bank option")

    @property
    def capitec_bank_cpc_option(self):
        selector = "//span[contains(text(),'Capitec Bank CPC')]"
        return self.locator(selector, "Capitec Bank CPC option")

    # endregion
