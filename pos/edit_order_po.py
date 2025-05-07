from base.page_base import PageBase


class EditOrderPO(PageBase):

    # region Menu Options

    @property
    def black_ellipsis(self):
        selector = "//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']"
        return self.locator(selector, "Black ellipsis menu")

    @property
    def edit_order_menu_option(self):
        selector = "//*[contains(text(),'Edit Order')]"
        return self.locator(selector, "Edit order menu option")

    @property
    def audit_log_menu_option(self):
        selector = "//*[contains(text(),'Audit log')]"
        return self.locator(selector, "Audit log menu option")

    # region Input Fields

    @property
    def payment_method_dropdown(self):
        selector = "//*[@name='paymentMethod']"
        return self.locator(selector, "Payment method dropdown")

    @property
    def discount_amount(self):
        selector = "//*[@name='discountAmount']"
        return self.locator(selector, "Discount amount input")

    @property
    def shipping_amount(self):
        selector = "//*[@name='shippingAmount']"
        return self.locator(selector, "Shipping amount input")

    # region Buttons

    @property
    def update_button(self):
        selector = "//button[contains(text(),'Update')]"
        return self.locator(selector, "Update button")

    @property
    def update_to_shipped_button(self):
        selector = "//div[@class='ui tiny modal transition visible active']//button[contains(text(),'Update to shipped')]"
        return self.locator(selector, "Update to shipped button")

    # region Admin Notes

    @property
    def payment_method_update_admin_note(self):
        selector = "//div[contains(text(),'Payment method updated ')]"
        return self.locator(selector, "Payment method update admin note")

    @property
    def discount_applied_admin_note(self):
        selector = "//div[contains(text(),'Discount applied:')]"
        return self.locator(selector, "Discount applied admin note")

    @property
    def shipping_fee_applied_admin_note(self):
        selector = "//div[contains(text(),'Shipping fee applied:')]"
        return self.locator(selector, "Shipping fee applied admin note")

    @property
    def update_to_shipped_admin_note(self):
        selector = "//div[contains(text(),'status updated from Return Canceled to Shipped')]"
        return self.locator(selector, "Update to shipped admin note")

    # region Warnings and Errors

    @property
    def payment_method_warning_banner(self):
        selector = "//*[@class='banner-container']"
        return self.locator(selector, "Payment method warning banner")

    @property
    def invalid_discount_amount(self):
        selector = "//*[@class='ui error message']/div/p/li"
        return self.locator(selector, "Invalid discount amount message")

    # region Order Financials

    @property
    def order_financials_accordion(self):
        selector = "//div[contains(text(),'Order Financials')]//i"
        return self.locator(selector, "Order financials accordion")

    @property
    def order_financials_shipping_amount(self):
        selector = "//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Shipping')]//following-sibling::td"
        return self.locator(selector, "Order financials shipping amount")

    @property
    def order_financials_discount_amount(self):
        selector = "//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Discount')]//following-sibling::td"
        return self.locator(selector, "Order financials discount amount")

    # region Order Items and Status

    @property
    def return_canceled_order_item_menu(self):
        selector = "//div[@class='accordion ui fluid styled']//*[@role='listbox']"
        return self.locator(selector, "Return canceled order item menu")

    @property
    def update_to_shipped_menu_option(self):
        selector = "//*[contains(text(),'Update to shipped')]"
        return self.locator(selector, "Update to shipped menu option")

    @property
    def update_to_shipped_modal_message(self):
        selector = "//div[@class='ui tiny modal transition visible active']//*[@class='ui form']/p"
        return self.locator(selector, "Update to shipped modal message")

    @property
    def order_item_status(self):
        selector = "//div[@class='accordion ui']//table[@class='ui table']//td[8]/div"
        return self.locator(selector, "Order item status")

    # region Disabled Fields

    @property
    def discount_amount_disabled_field(self):
        selector = "//*[contains(text(),'Discount')]/parent::div//parent::div/div/p"
        return self.locator(selector, "Discount amount disabled field")

    @property
    def shipping_fee_disabled_field(self):
        selector = "//*[contains(text(),'Shipping')]/parent::div//parent::div/div/p"
        return self.locator(selector, "Shipping fee disabled field")

    # region Audit Log

    @property
    def audit_log_edit_order_action_type(self):
        selector = "//*[@class='ui striped basic very compact table']/tbody/tr/td[3]"
        return self.locator(selector, "Audit log edit order action type")

    @property
    def audit_log_edit_order_data(self):
        selector = "//*[@class='ui striped basic very compact table']/tbody/tr/td[5]"
        return self.locator(selector, "Audit log edit order data")
