from playwright.sync_api import Page

from base.page_base import PageBase

# Locators
black_ellipsis = ("//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']", "Black Ellipsis Icon")
edit_order_menu_option = ("//*[contains(text(),'Edit Order')]", "Edit Order Menu Option")
payment_method_dropdown = ("//*[@name='paymentMethod']", "Payment Method Dropdown")
update_button = ("//button[contains(text(),'Update')]", "Update Button")
payment_method_update_admin_note = ("//div[contains(text(),'Payment method updated ')]", "Payment Method Update Admin Note")


class EditOrderPage(PageBase):
    """Page object for Edit Order functionality"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.black_ellipsis = self.locator(black_ellipsis)
        self.edit_order_menu_option = self.locator(edit_order_menu_option)
        self.payment_method_dropdown = self.locator(payment_method_dropdown)
        self.update_button = self.locator(update_button)
        self.payment_method_update_admin_note = self.locator(payment_method_update_admin_note)
