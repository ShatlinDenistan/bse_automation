from playwright.sync_api import Page, expect

from base.page_base import PageBase


class OrderListPage(PageBase):
    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.auth_status_label = page.locator("//label[.='Auth Status']")
        self.first_order_checkbox = page.locator("//tr[td[9]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]")
        self.cancel_button = page.get_by_text("Cancel Order(s)")
        self.cancellation_reasons_dropdown = page.get_by_role("listbox").filter(has_text="-- none --Stock accuracy (")
        self.cancellation_reason = page.get_by_text("Stock accuracy (pick fails")
        self.modal_cancel_button = page.get_by_role("button", name="Cancel Orders")
        self.confirmation_message = page.get_by_text("Successfully processed 1 item")
        self.selected_order = "//table//td//a[.='{}']//ancestor::tr//div"
        self.table_xpath = "//table"

    def confirm_if_in_page(self):
        """Confirm if the user is on the Order List page"""
        expect(self.auth_status_label).to_be_visible(timeout=5000)

    def cancel_order(self):
        """Cancel the first order in the list"""
        self.confirm_if_in_page()
        self.set_page_size(page_size=50)
        table_data = self.get_table_data(table_xpath=self.table_xpath)
        for row in table_data:
            if row[8] == "New Order":
                order_number = row[1].split(" ")[0]
                break
        else:
            return False
        self.selected_order = self.selected_order.format(order_number)
        selected_order_checkbox = self.page.locator(self.selected_order).first
        selected_order_checkbox.click()
        self.cancel_button.click()
        self.cancellation_reasons_dropdown.click()
        self.cancellation_reason.click()
        self.modal_cancel_button.click()
        expect(self.confirmation_message).to_be_visible(timeout=50000)
        return True
