from base.page_base import PageBase

# Module-level constants from orEditOrder.robot
BLACK_ELLIPSIS = "//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']"
EDIT_ORDER_MENU_OPTION = "//*[contains(text(),'Edit Order')]"
PAYMENT_METHOD_DROPDOWN = "//*[@name='paymentMethod']"
UPDATE_BUTTON = "//button[contains(text(),'Update')]"
PAYME_METHOD_UPDATE_ADMIN_NOTE = "//div[contains(text(),'Payment method updated ')]"
PAYME_METHOD_WARNING_BANNER = "//*[@class='banner-container']"
DISCOUNT_AMOUNT = "//*[@name='discountAmount']"
INVALID_DISCOUNT_AMOUNT = "//*[@class='ui error message']/div/p/li"
SHIPPING_AMOUNT = "//*[@name='shippingAmount']"
DISCOUNT_APPLIED_ADMIN_NOTE = "//div[contains(text(),'Discount applied:')]"
SHIPPING_FEE_APPLIED_ADMIN_NOTE = "//div[contains(text(),'Shipping fee applied:')]"
AUDIT_LOG_MENU_OPTION = "//*[contains(text(),'Audit log')]"
AUDIT_LOG_EDIT_ORDER_ACTION_TYPE = "//*[@class='ui striped basic very compact table']/tbody/tr/td[3]"
AUDIT_LOG_EDIT_ORDER_DATA = "//*[@class='ui striped basic very compact table']/tbody/tr/td[5]"
ORDER_FINANCIALS_ACCORDION = "//div[contains(text(),'Order Financials')]//i"
ORDER_FINANCIALS_SHIPPING_AMOUNT = "//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Shipping')]//following-sibling::td"
ORDER_FINANCIALS_DISCOUNT_AMOUNT = "//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Discount')]//following-sibling::td"
RETURN_CANCELED_ORDER_ITEM_MENU = "//div[@class='accordion ui fluid styled']//*[@role='listbox']"
UPDATE_TO_SHIPPED_MENU_OPTION = "//*[contains(text(),'Update to shipped')]"
UPDATE_TO_SHIPPED_MODAL_MESSAGE = "//div[@class='ui tiny modal transition visible active']//*[@class='ui form']/p"
UPDATE_TO_SHIPPED_BUTTON = "//div[@class='ui tiny modal transition visible active']//button[contains(text(),'Update to shipped')]"
ORDER_ITEM_STATUS = "//div[@class='accordion ui']//table[@class='ui table']//td[8]/div"
UPDATE_TO_SHIPPED_ADMIN_NOTE = "//div[contains(text(),'status updated from Return Canceled to Shipped')]"
DISCOUNT_AMOUNT_DISABLED_FIELD = "//*[contains(text(),'Discount')]/parent::div//parent::div/div/p"
SHIPPING_FEE_DISABLED_FIELD = "//*[contains(text(),'Shipping')]/parent::div//parent::div/div/p"


class EditOrderPO(PageBase):
    def __init__(self, page):
        super().__init__(page)
        # Initialize locators using self.locator() method
        self.black_ellipsis = self.locator(BLACK_ELLIPSIS, "Black ellipsis menu")
        self.edit_order_menu_option = self.locator(EDIT_ORDER_MENU_OPTION, "Edit order menu option")
        self.payment_method_dropdown = self.locator(PAYMENT_METHOD_DROPDOWN, "Payment method dropdown")
        self.update_button = self.locator(UPDATE_BUTTON, "Update button")
        self.payment_method_update_admin_note = self.locator(PAYME_METHOD_UPDATE_ADMIN_NOTE, "Payment method update admin note")
        self.payment_method_warning_banner = self.locator(PAYME_METHOD_WARNING_BANNER, "Payment method warning banner")
        self.discount_amount = self.locator(DISCOUNT_AMOUNT, "Discount amount input")
        self.invalid_discount_amount = self.locator(INVALID_DISCOUNT_AMOUNT, "Invalid discount amount message")
        self.shipping_amount = self.locator(SHIPPING_AMOUNT, "Shipping amount input")
        self.discount_applied_admin_note = self.locator(DISCOUNT_APPLIED_ADMIN_NOTE, "Discount applied admin note")
        self.shipping_fee_applied_admin_note = self.locator(SHIPPING_FEE_APPLIED_ADMIN_NOTE, "Shipping fee applied admin note")
        self.audit_log_menu_option = self.locator(AUDIT_LOG_MENU_OPTION, "Audit log menu option")
        self.audit_log_edit_order_action_type = self.locator(AUDIT_LOG_EDIT_ORDER_ACTION_TYPE, "Audit log edit order action type")
        self.audit_log_edit_order_data = self.locator(AUDIT_LOG_EDIT_ORDER_DATA, "Audit log edit order data")
        self.order_financials_accordion = self.locator(ORDER_FINANCIALS_ACCORDION, "Order financials accordion")
        self.order_financials_shipping_amount = self.locator(ORDER_FINANCIALS_SHIPPING_AMOUNT, "Order financials shipping amount")
        self.order_financials_discount_amount = self.locator(ORDER_FINANCIALS_DISCOUNT_AMOUNT, "Order financials discount amount")
        self.return_canceled_order_item_menu = self.locator(RETURN_CANCELED_ORDER_ITEM_MENU, "Return canceled order item menu")
        self.update_to_shipped_menu_option = self.locator(UPDATE_TO_SHIPPED_MENU_OPTION, "Update to shipped menu option")
        self.update_to_shipped_modal_message = self.locator(UPDATE_TO_SHIPPED_MODAL_MESSAGE, "Update to shipped modal message")
        self.update_to_shipped_button = self.locator(UPDATE_TO_SHIPPED_BUTTON, "Update to shipped button")
        self.order_item_status = self.locator(ORDER_ITEM_STATUS, "Order item status")
        self.update_to_shipped_admin_note = self.locator(UPDATE_TO_SHIPPED_ADMIN_NOTE, "Update to shipped admin note")
        self.discount_amount_disabled_field = self.locator(DISCOUNT_AMOUNT_DISABLED_FIELD, "Discount amount disabled field")
        self.shipping_fee_disabled_field = self.locator(SHIPPING_FEE_DISABLED_FIELD, "Shipping fee disabled field")
