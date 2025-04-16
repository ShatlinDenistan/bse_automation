from playwright.sync_api import Page, expect

from base.page_base import PageBase

first_order_checkbox = ("//tr[td[9]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]", "First Order Checkbox")
auth_status_label = ("//label[.='Auth Status']", "Authorization Status")
auth_button = ("//button[contains(.,'Authorise')]", "Authorise Button")

# New locators added from orOrderList.robot
clear_date_range_today = ("//div[@class='ui checked checkbox']//label[text()='Today']", "Clear Date Range Today Checkbox")
order_list_apply_filter_button = ("//button[contains(text(), 'Apply Filter')]", "Order List Apply Filter Button")
past_10_days = ("//label[text()='Past 10 Days']", "Past 10 Days Checkbox")
first_row_with_order_status_new_order_checkbox = (
    "//tr[td[9]/div[contains(text(), 'New Order')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "First Row with New Order Checkbox",
)
second_row_with_order_status_new_order_checkbox = (
    "//tr[td[9]/div[contains(text(), 'New Order')]][2]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "Second Row with New Order Checkbox",
)
third_row_with_order_status_new_order_checkbox = (
    "//tr[td[9]/div[contains(text(), 'New Order')]][3]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "Third Row with New Order Checkbox",
)
order_id_column = ("//tr[td[9]/div[contains(text(), 'New Order')]][1]//a[contains(@href, '/order/')", "Order ID Column")
order_list_authorise_order_button = ("//button[contains(text(), 'Authorise Order(s)')", "Order List Authorise Order Button")
authorise_orders_modal = ("//div[contains(@class, 'ui large modal transition visible active')", "Authorise Orders Modal")
authorise_orders_modal_close_icon = ("//*[@class= 'close icon']", "Authorise Orders Modal Close Icon")
fin_portal_global_search_field = ("//*[@name='searchText' and @type='text']", "Fin Portal Global Search Field")
fin_portal_global_search_icon = ("//*[@class='search icon']", "Fin Portal Global Search Icon")
authed_by_order_page_badge = ("//div[contains(text(), 'Auth by')", "Authed By Order Page Badge")
order_list_cancel_order_button = ("//button[contains(text(), 'Cancel Order(s)')", "Order List Cancel Order Button")
cancel_orders_modal_header = ("//div[contains(text(),'Please confirm')", "Cancel Orders Modal Header")
cancellation_reason_dropdown = ("//div[@name='cancelReason']", "Cancellation Reason Dropdown")


class OrderListPage(PageBase):
    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.auth_status_label = self.locator(auth_status_label)
        self.first_order_checkbox = self.locator(first_order_checkbox)
        self.cancel_button = page.get_by_text("Cancel Order(s)")
        self.authorise_button = self.locator(auth_button)

        self.cancellation_reasons_dropdown = page.get_by_role("listbox").filter(has_text="-- none --Stock accuracy (")
        self.cancellation_reason = page.get_by_text("Stock accuracy (pick fails")
        self.modal_cancel_button = page.get_by_role("button", name="Cancel Orders")
        self.confirmation_message = page.get_by_text("Successfully processed 1 item")
        self.selected_order = "//table//td//a[.='{}']//ancestor::tr//div"
        self.table_xpath = "//table"

    def confirm_if_in_page(self):
        """Confirm if the user is on the Order List page"""
        expect(self.auth_status_label).to_be_visible(timeout=5000)

    def authorize_order(self):
        """Authorie the first available order in the list"""
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
        self.click(selected_order_checkbox)
        self.click(self.authorise_button)

        expect(self.confirmation_message).to_be_visible(timeout=50000)
        return True

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
        self.click(selected_order_checkbox)
        self.click(self.cancel_button)
        self.click(self.cancellation_reasons_dropdown)
        self.click(self.cancellation_reason)
        self.click(self.modal_cancel_button)

        expect(self.confirmation_message).to_be_visible(timeout=50000)
        return True
