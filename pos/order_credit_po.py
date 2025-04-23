from base.page_base import PageBase

# Module-level constants for all XPath selectors
BTN_CUSTOMER_CUDION = "//span[contains(text(),'Customer Credit')]"
BTN_CREDIT = "//*[contains(text(),'Allocate credit')]"
TXT_CREDIT_AMOUNT = "//input[@name='amount']"
TXT_CREDIT_COMMENTS = "//textarea[@name='adminNote']"
DROPDOWN_CREDIT_REASON = "//*[@name='reason']"
REASON_GOODWILL = "//*[@role='option']/span[contains(text(),'Goodwill')]"
REASON_LATE_DELIVERY_FEE = "//*[@role='option']/span[contains(text(),'Late delivery fee')]"
VALIDATION_ERROR = "//*[@class='ui negative message']/div/div"
REASON_SUB_LATE_DELIVERY = "//*[@role='option']/span[contains(text(),'Subscription late delivery fee')]"
REASON_CREDIT_BREACH = "//*[@role='option']/span[contains(text(),'Credit breach')]"
TXT_JIRA_NUMBER = "//input[@name='extra']"
REASON_B2B_BULK_ORDER = "//*[@role='option']/span[contains(text(),'B2B bulk orders')]"
REASON_FAILED_EFT_REFUNDS = "//*[@role='option']/span[contains(text(),'Failed EFT refunds')]"
ACCORDION_ORDER_ITEMS = "//span[contains(text(),'Order Items')]"
BTN_ORDER_ITEM_MENU = "//div[@class='accordion ui']//*[@class='ui simple dropdown']/i"
CREDIT_ITEM_OPTION = "//*[contains(text(),'Credit Item')]"
REASON_SYSTEM_ERROR = "//*[@role='option']/span[contains(text(),'System error: Credit removal failed')]"
TXT_RFN_NUMBER = "//*[@placeholder='Please enter a RFN number']"
REASON_DUPLICATE_PAYMENT = "//*[@role='option']/span[contains(text(),'Duplicate payment')]"
REASON_COD_RETURN = "//*[@role='option']/span[contains(text(),'COD return')]"
ACCORDION_ORDER_FINANCIALS = "//*[contains(text(),'Order Financials')]"
ORDER_FINANCIALS_RETURN_CANCELLED = "//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Return Cancelled')]//following-sibling::td"
ORDER_FINANCIALS_CANCELLED = "//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Cancelled')]//following-sibling::td"
REASON_CREDIT_ERROR = "//*[@role='option']/span[contains(text(),'Credit error')]"


class OrderCreditPO(PageBase):
    """Page Object class for Order Credit functionality"""

    def __init__(self, page):
        """Initialize the OrderCreditPO class with locators"""
        super().__init__(page)

        # Customer credit section locators
        self.btn_customer_credit = self.locator(BTN_CUSTOMER_CUDION, "Customer Credit button")
        self.btn_allocate_credit = self.locator(BTN_CREDIT, "Allocate Credit button")

        # Credit form locators
        self.txt_credit_amount = self.locator(TXT_CREDIT_AMOUNT, "Credit amount field")
        self.txt_credit_comments = self.locator(TXT_CREDIT_COMMENTS, "Credit comments field")
        self.dropdown_credit_reason = self.locator(DROPDOWN_CREDIT_REASON, "Credit reason dropdown")

        # Credit reasons
        self.reason_goodwill = self.locator(REASON_GOODWILL, "Goodwill reason option")
        self.reason_late_delivery_fee = self.locator(REASON_LATE_DELIVERY_FEE, "Late delivery fee reason option")
        self.reason_sub_late_delivery = self.locator(REASON_SUB_LATE_DELIVERY, "Subscription late delivery fee reason option")
        self.reason_credit_breach = self.locator(REASON_CREDIT_BREACH, "Credit breach reason option")
        self.reason_b2b_bulk_order = self.locator(REASON_B2B_BULK_ORDER, "B2B bulk orders reason option")
        self.reason_failed_eft_refunds = self.locator(REASON_FAILED_EFT_REFUNDS, "Failed EFT refunds reason option")
        self.reason_system_error = self.locator(REASON_SYSTEM_ERROR, "System error reason option")
        self.reason_duplicate_payment = self.locator(REASON_DUPLICATE_PAYMENT, "Duplicate payment reason option")
        self.reason_cod_return = self.locator(REASON_COD_RETURN, "COD return reason option")
        self.reason_credit_error = self.locator(REASON_CREDIT_ERROR, "Credit error reason option")

        # Additional fields
        self.txt_jira_number = self.locator(TXT_JIRA_NUMBER, "JIRA number field")
        self.txt_rfn_number = self.locator(TXT_RFN_NUMBER, "RFN number field")
        self.validation_error = self.locator(VALIDATION_ERROR, "Validation error message")

        # Order items section
        self.accordion_order_items = self.locator(ACCORDION_ORDER_ITEMS, "Order Items accordion")
        self.btn_order_item_menu = self.locator(BTN_ORDER_ITEM_MENU, "Order Item menu button")
        self.credit_item_option = self.locator(CREDIT_ITEM_OPTION, "Credit Item option")

        # Order financials section
        self.accordion_order_financials = self.locator(ACCORDION_ORDER_FINANCIALS, "Order Financials accordion")
        self.order_financials_return_cancelled = self.locator(ORDER_FINANCIALS_RETURN_CANCELLED, "Order Financials Return Cancelled amount")
        self.order_financials_cancelled = self.locator(ORDER_FINANCIALS_CANCELLED, "Order Financials Cancelled amount")
