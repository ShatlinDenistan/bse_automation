from base.page_base import PageBase


# Module-level constants for locators
CUSTOMER_CREDIT_ACCORDION = "//div[contains(text(),' available credit')]"
REFUND_BUTTON = "${btnRefund}"
SUBMIT_REFUND_REQUEST_BUTTON = "${btnSubmittingRefundReq}"
OKAY_BUTTON = "${btnOkay}"
VIEW_REFUND_LOG_BUTTON = "//a[contains(text(),'View Refund Log')]"
NOT_ELIGIBLE_FOR_REFUND = "//li[contains(text(),'Order ${order_ids[0]} is not eligible for refund.')]"
BANK_ACCOUNT_INPUT = "//input[@autocomplete='off' and @name='bankAccount' and @type='text']"
BANK_DROPDOWN = "//div[@name='bank' and @role='listbox' and @class='ui fluid selection dropdown']"
CAPITEC_BANK_OPTION = "//span[contains(text(),'Capitec Bank')]"
BRANCH_DROPDOWN = "//div[contains(text(),'- - Select branch - -')]"
CAPITEC_BANK_CPC_OPTION = "//span[contains(text(),'Capitec Bank CPC')]"
PROCEED_BUTTON = "//button[contains(text(),'Proceed')]"
REFUND_AMOUNT_DISPLAY = "/html/body/div[1]/div[3]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/table/tbody/tr/td[2]"


class ManualRefundPO(PageBase):
    """Page Object for Manual Refund functionality"""

    def __init__(self, page):
        super().__init__(page)

        # Initialize elements using self.locator
        self.customer_credit_accordion = self.locator(CUSTOMER_CREDIT_ACCORDION, "Customer credit accordion")
        self.refund_button = self.locator(REFUND_BUTTON, "Refund button")
        self.submit_refund_request_button = self.locator(SUBMIT_REFUND_REQUEST_BUTTON, "Submit refund request button")
        self.okay_button = self.locator(OKAY_BUTTON, "Okay button")
        self.view_refund_log_button = self.locator(VIEW_REFUND_LOG_BUTTON, "View refund log button")
        self.not_eligible_for_refund = self.locator(NOT_ELIGIBLE_FOR_REFUND, "Not eligible for refund message")
        self.bank_account_input = self.locator(BANK_ACCOUNT_INPUT, "Bank account input")
        self.bank_dropdown = self.locator(BANK_DROPDOWN, "Bank dropdown")
        self.capitec_bank_option = self.locator(CAPITEC_BANK_OPTION, "Capitec Bank option")
        self.branch_dropdown = self.locator(BRANCH_DROPDOWN, "Branch dropdown")
        self.capitec_bank_cpc_option = self.locator(CAPITEC_BANK_CPC_OPTION, "Capitec Bank CPC option")
        self.proceed_button = self.locator(PROCEED_BUTTON, "Proceed button")
        self.refund_amount_display = self.locator(REFUND_AMOUNT_DISPLAY, "Refund amount display")
