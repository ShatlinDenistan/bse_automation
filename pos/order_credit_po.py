from base.page_base import PageBase


class OrderCreditPO(PageBase):
    """Page Object class for Order Credit functionality"""

    # region Customer Credit Section

    @property
    def btn_customer_credit(self):
        selector = "//span[contains(text(),'Customer Credit')]"
        return self.locator(selector, "Customer Credit button")

    @property
    def btn_allocate_credit(self):
        selector = "//*[contains(text(),'Allocate credit')]"
        return self.locator(selector, "Allocate Credit button")

    # endregion

    # region Credit Form Section

    @property
    def txt_credit_amount(self):
        selector = "//input[@name='amount']"
        return self.locator(selector, "Credit amount field")

    @property
    def txt_credit_comments(self):
        selector = "//textarea[@name='adminNote']"
        return self.locator(selector, "Credit comments field")

    @property
    def dropdown_credit_reason(self):
        selector = "//*[@name='reason']"
        return self.locator(selector, "Credit reason dropdown")

    @property
    def validation_error(self):
        selector = "//*[@class='ui negative message']/div/div"
        return self.locator(selector, "Validation error message")

    # endregion

    # region Credit Reasons

    @property
    def reason_goodwill(self):
        selector = "//*[@role='option']/span[contains(text(),'Goodwill')]"
        return self.locator(selector, "Goodwill reason option")

    @property
    def reason_late_delivery_fee(self):
        selector = "//*[@role='option']/span[contains(text(),'Late delivery fee')]"
        return self.locator(selector, "Late delivery fee reason option")

    @property
    def reason_sub_late_delivery(self):
        selector = "//*[@role='option']/span[contains(text(),'Subscription late delivery fee')]"
        return self.locator(selector, "Subscription late delivery fee reason option")

    @property
    def reason_credit_breach(self):
        selector = "//*[@role='option']/span[contains(text(),'Credit breach')]"
        return self.locator(selector, "Credit breach reason option")

    @property
    def reason_b2b_bulk_order(self):
        selector = "//*[@role='option']/span[contains(text(),'B2B bulk orders')]"
        return self.locator(selector, "B2B bulk orders reason option")

    @property
    def reason_failed_eft_refunds(self):
        selector = "//*[@role='option']/span[contains(text(),'Failed EFT refunds')]"
        return self.locator(selector, "Failed EFT refunds reason option")

    @property
    def reason_system_error(self):
        selector = "//*[@role='option']/span[contains(text(),'System error: Credit removal failed')]"
        return self.locator(selector, "System error reason option")

    @property
    def reason_duplicate_payment(self):
        selector = "//*[@role='option']/span[contains(text(),'Duplicate payment')]"
        return self.locator(selector, "Duplicate payment reason option")

    @property
    def reason_cod_return(self):
        selector = "//*[@role='option']/span[contains(text(),'COD return')]"
        return self.locator(selector, "COD return reason option")

    @property
    def reason_credit_error(self):
        selector = "//*[@role='option']/span[contains(text(),'Credit error')]"
        return self.locator(selector, "Credit error reason option")

    # endregion

    # region Additional Fields

    @property
    def txt_jira_number(self):
        selector = "//input[@name='extra']"
        return self.locator(selector, "JIRA number field")

    @property
    def txt_rfn_number(self):
        selector = "//*[@placeholder='Please enter a RFN number']"
        return self.locator(selector, "RFN number field")

    # endregion

    # region Order Items Section

    @property
    def accordion_order_items(self):
        selector = "//span[contains(text(),'Order Items')]"
        return self.locator(selector, "Order Items accordion")

    @property
    def btn_order_item_menu(self):
        selector = "//div[@class='accordion ui']//*[@class='ui simple dropdown']/i"
        return self.locator(selector, "Order Item menu button")

    @property
    def credit_item_option(self):
        selector = "//*[contains(text(),'Credit Item')]"
        return self.locator(selector, "Credit Item option")

    # endregion

    # region Order Financials Section

    @property
    def accordion_order_financials(self):
        selector = "//*[contains(text(),'Order Financials')]"
        return self.locator(selector, "Order Financials accordion")

    @property
    def order_financials_return_cancelled(self):
        selector = "//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Return Cancelled')]//following-sibling::td"
        return self.locator(selector, "Order Financials Return Cancelled amount")

    @property
    def order_financials_cancelled(self):
        selector = "//*[contains(text(),'Order Financials')]/parent::div//*[contains(text(),'Cancelled')]//following-sibling::td"
        return self.locator(selector, "Order Financials Cancelled amount")

    # endregion
