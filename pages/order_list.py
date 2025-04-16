import random

from playwright.sync_api import Page, expect

from base.page_base import PageBase

# Locators
btn_menu = ("//i[@class='content large icon' and @aria-hidden='true']", "Menu Button")
order_list_menu_option = ("//*[contains(text(),'Order List')]", "Order List Menu Option")
clear_date_range_today = ("//div[@class='ui checked checkbox']//label[text()='Today']", "Clear Date Range Today")
order_list_apply_filter_button = ("//button[contains(text(), 'Apply Filter')]", "Apply Filter Button")
past_10_days = ("//label[text()='Past 10 Days']", "Past 10 Days Option")
apply_filter = ("//button[contains(text(), 'Apply Filter')]", "Apply Filter Button")
first_row_with_order_status_new_order_checkbox = (
    "//tr[td[9]/div[contains(text(), 'New Order')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "First New Order Checkbox",
)
second_row_with_order_status_new_order_checkbox = (
    "//tr[td[9]/div[contains(text(), 'New Order')]][2]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "Second New Order Checkbox",
)
third_row_with_order_status_new_order_checkbox = (
    "//tr[td[9]/div[contains(text(), 'New Order')]][3]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "Third New Order Checkbox",
)
order_id_column = ("//tr[td[9]/div[contains(text(), 'New Order')]][1]//a[contains(@href, '/order/')]", "First Order ID")
order_id_column2 = ("//tr[td[9]/div[contains(text(), 'New Order')]][2]//a[contains(@href, '/order/')]", "Second Order ID")
order_id_column3 = ("//tr[td[9]/div[contains(text(), 'New Order')]][3]//a[contains(@href, '/order/')]", "Third Order ID")
order_list_authorise_order_button = ("//button[contains(text(), 'Authorise Order(s)')]", "Authorise Order Button")
authorise_orders_modal = ("//div[contains(@class, 'ui large modal transition visible active')]", "Authorise Orders Modal")
authorise_orders_modal_close_icon = ("//*[@class= 'close icon']", "Authorise Orders Modal Close Icon")
fin_portal_global_search_field = ("//*[@name='searchText' and @type='text']", "Global Search Field")
fin_portal_global_search_icon = ("//*[@class='search icon']", "Search Icon")
authed_by_order_page_badge = ("//div[contains(text(), 'Auth by')]", "Auth By Badge")
order_list_cancel_order_button = ("//button[contains(text(), 'Cancel Order(s)')]", "Cancel Order Button")
cancel_orders_modal_header = ("//div[contains(text(),'Please confirm')]", "Cancel Orders Modal Header")
cancellation_reason_dropdown = ("//div[@name='cancelReason']", "Cancellation Reason Dropdown")
cancel_orders_modal_cancel_button = ("//button[contains(text(), 'Cancel Orders')]", "Cancel Orders Button")
cancel_orders_modal = ("//div[contains(@class, 'ui large modal transition visible active')]", "Cancel Orders Modal")
cancel_orders_modal_close_icon = ("//*[@class= 'close icon']", "Cancel Orders Modal Close Icon")
canceled_by_order_page_badge = ("//div[contains(text(), 'Canceled by')]", "Canceled By Badge")
order_item_cancellation_reason = ("//div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]", "Cancellation Reason")
first_row_with_order_status_cancelled_checkbox = (
    "//tr[td[9]/div[contains(text(), 'Canceled')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]",
    "First Canceled Order Checkbox",
)
order_id_column_canceled = ("//tr[td[9]/div[contains(text(), 'Canceled')]][1]//a[contains(@href, '/order/')]", "Canceled Order ID")
order_list_clear_filter_button = ("//button[contains(text(), 'Clear Filter')]", "Clear Filter Button")
daily_deals_checkbox = ("//label[text()='Daily Deals']", "Daily Deals Checkbox")
all_order_id_columns = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]", "All Order ID Columns")
auth_status_dropdown = ("//div[@name='authStatus']", "Auth Status Dropdown")
auth_status_new = ("//span[contains(text(), 'New')]", "Auth Status New Option")
auth_status_auth = ("//span[text()='Auth']", "Auth Status Auth Option")
all_auth_status_columns = ("//td[position() = (count(//th[text()='Auth Status']/preceding-sibling::th) + 1)]", "All Auth Status Columns")
payment_method_dropdown = ("//div[@name='paymentMethod']", "Payment Method Dropdown")
payment_method_credit_card = ("//span[text()='Credit Card']", "Payment Method Credit Card Option")
payment_method_credit = ("//span[text()='Credit']", "Payment Method Credit Option")
payment_method_payfast = ("//span[text()='PayFast']", "Payment Method PayFast Option")
payment_method_deposit = ("//span[text()='Deposit']", "Payment Method Deposit Option")
all_payment_method_columns = ("//td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 1)]", "All Payment Method Columns")
shipping_method_dropdown = ("//div[@name='shippingMethod']", "Shipping Method Dropdown")
shipping_method_collect = ("//span[text()='Collect']", "Shipping Method Collect Option")
shipping_method_courier = ("//span[text()='Courier']", "Shipping Method Courier Option")
minimum_order_total_dropdown = ("//div[@name='minimumTotal']", "Minimum Order Total Dropdown")
minimum_order_total_r500 = ("//div[@name='minimumTotal']//span[text()='R 500']", "Minimum Order Total R500 Option")
minimum_order_total_r0 = ("//div[@name='minimumTotal']//span[text()='R 0']", "Minimum Order Total R0 Option")
maximum_order_total_dropdown = ("//div[@name='maximumTotal']", "Maximum Order Total Dropdown")
maximum_order_total_r500 = ("//div[@name='maximumTotal']//span[text()='R 500']", "Maximum Order Total R500 Option")
all_order_total_columns = ("//td[position() = (count(//th[text()='Order Total']/preceding-sibling::th) + 1)]", "All Order Total Columns")
order_list_table = ("//table[@class='ui small celled compact table']", "Order List Table")
all_table_rows = ("//table[@class='ui small celled compact table']//tbody//tr", "All Table Rows")

# Dynamic locators with format strings
cancellation_reason_option = ("//span[contains(text(), '{}')]", "Cancellation Reason Option")


class OrderListPage(PageBase):
    """Page object for Order List functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Basic navigation locators
        self.btn_menu = self.locator(btn_menu)
        self.order_list_menu_option = self.locator(order_list_menu_option)

        # Filter locators
        self.clear_date_range_today = self.locator(clear_date_range_today)
        self.order_list_apply_filter_button = self.locator(order_list_apply_filter_button)
        self.past_10_days = self.locator(past_10_days)
        self.apply_filter = self.locator(apply_filter)
        self.order_list_clear_filter_button = self.locator(order_list_clear_filter_button)
        self.daily_deals_checkbox = self.locator(daily_deals_checkbox)

        # Order selection locators
        self.first_row_with_order_status_new_order_checkbox = self.locator(first_row_with_order_status_new_order_checkbox)
        self.second_row_with_order_status_new_order_checkbox = self.locator(second_row_with_order_status_new_order_checkbox)
        self.third_row_with_order_status_new_order_checkbox = self.locator(third_row_with_order_status_new_order_checkbox)
        self.first_row_with_order_status_cancelled_checkbox = self.locator(first_row_with_order_status_cancelled_checkbox)

        # Order ID column locators
        self.order_id_column = self.locator(order_id_column)
        self.order_id_column2 = self.locator(order_id_column2)
        self.order_id_column3 = self.locator(order_id_column3)
        self.order_id_column_canceled = self.locator(order_id_column_canceled)
        self.all_order_id_columns = self.locator(all_order_id_columns)

        # Authorise order locators
        self.order_list_authorise_order_button = self.locator(order_list_authorise_order_button)
        self.authorise_orders_modal = self.locator(authorise_orders_modal)
        self.authorise_orders_modal_close_icon = self.locator(authorise_orders_modal_close_icon)

        # Cancel order locators
        self.order_list_cancel_order_button = self.locator(order_list_cancel_order_button)
        self.cancel_orders_modal_header = self.locator(cancel_orders_modal_header)
        self.cancellation_reason_dropdown = self.locator(cancellation_reason_dropdown)
        self.cancel_orders_modal_cancel_button = self.locator(cancel_orders_modal_cancel_button)
        self.cancel_orders_modal = self.locator(cancel_orders_modal)
        self.cancel_orders_modal_close_icon = self.locator(cancel_orders_modal_close_icon)

        # Order status badges
        self.canceled_by_order_page_badge = self.locator(canceled_by_order_page_badge)
        self.authed_by_order_page_badge = self.locator(authed_by_order_page_badge)
        self.order_item_cancellation_reason = self.locator(order_item_cancellation_reason)

        # Search locators
        self.fin_portal_global_search_field = self.locator(fin_portal_global_search_field)
        self.fin_portal_global_search_icon = self.locator(fin_portal_global_search_icon)

        # Filter dropdown locators
        self.auth_status_dropdown = self.locator(auth_status_dropdown)
        self.auth_status_new = self.locator(auth_status_new)
        self.auth_status_auth = self.locator(auth_status_auth)
        self.all_auth_status_columns = self.locator(all_auth_status_columns)

        self.payment_method_dropdown = self.locator(payment_method_dropdown)
        self.payment_method_credit_card = self.locator(payment_method_credit_card)
        self.payment_method_credit = self.locator(payment_method_credit)
        self.payment_method_payfast = self.locator(payment_method_payfast)
        self.payment_method_deposit = self.locator(payment_method_deposit)
        self.all_payment_method_columns = self.locator(all_payment_method_columns)

        self.shipping_method_dropdown = self.locator(shipping_method_dropdown)
        self.shipping_method_collect = self.locator(shipping_method_collect)
        self.shipping_method_courier = self.locator(shipping_method_courier)

        self.minimum_order_total_dropdown = self.locator(minimum_order_total_dropdown)
        self.minimum_order_total_r500 = self.locator(minimum_order_total_r500)
        self.minimum_order_total_r0 = self.locator(minimum_order_total_r0)
        self.maximum_order_total_dropdown = self.locator(maximum_order_total_dropdown)
        self.maximum_order_total_r500 = self.locator(maximum_order_total_r500)
        self.all_order_total_columns = self.locator(all_order_total_columns)

        # Table locators
        self.order_list_table = self.locator(order_list_table)
        self.all_table_rows = self.locator(all_table_rows)

        # Pre-initialized cancellation reason options
        self.cancellation_reason_customer_request = self.locator((cancellation_reason_option[0].format("Customer request"), "Customer Request Option"))
        self.cancellation_reason_supplier_out_of_stock = self.locator((cancellation_reason_option[0].format("Supplier out of stock"), "Supplier Out of Stock Option"))
        self.cancellation_reason_fraud = self.locator((cancellation_reason_option[0].format("Fraud"), "Fraud Option"))
        self.cancellation_reason_damaged = self.locator((cancellation_reason_option[0].format("Damaged"), "Damaged Option"))
        self.cancellation_reason_incorrect_packaging = self.locator((cancellation_reason_option[0].format("Incorrect Packaging"), "Incorrect Packaging Option"))

    def get_cancellation_reason_option(self, reason: str):
        """Get locator for a specific cancellation reason option"""
        return self.locator((cancellation_reason_option[0].format(reason), f"{reason} Option"))

    def navigate_to_order_list_page(self):
        """Navigate to Order List Page"""
        self.click(self.btn_menu)
        self.click(self.order_list_menu_option)

    def clear_today_filter(self):
        """Clear Today Filter"""
        self.click(self.clear_date_range_today)
        self.click(self.order_list_apply_filter_button)

    def authorise_single_order(self):
        """Authorise Single Order"""
        self.click(self.past_10_days)
        self.click(self.apply_filter)

        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)
        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)
        self.click(self.first_row_with_order_status_new_order_checkbox)
        order_id = self.get_text(self.order_id_column)

        self.click(self.order_list_authorise_order_button)
        self.wait_for_seconds(5)

        self.expect_to_be_visible(self.authorise_orders_modal)
        authorise_orders_modal_text = self.get_text(self.authorise_orders_modal)

        # Perform assertions
        assert "Authorizing Orders" in authorise_orders_modal_text
        self.wait_for_seconds(3)
        assert "Successfully processed 1 item(s)" in authorise_orders_modal_text
        assert f"Successfully processed item: {order_id}" in authorise_orders_modal_text

        self.click(self.authorise_orders_modal_close_icon)

        self.fill(self.fin_portal_global_search_field, order_id)
        self.click(self.fin_portal_global_search_icon)
        self.click(self.authed_by_order_page_badge)

        auth_by = self.get_text(self.authed_by_order_page_badge)
        assert "Auth by Test en-gcs" in auth_by

        return order_id

    def authorise_multiple_orders(self):
        """Authorise Multiple Orders"""
        self.click(self.past_10_days)
        self.click(self.apply_filter)

        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)
        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)

        self.click(self.first_row_with_order_status_new_order_checkbox)
        self.click(self.second_row_with_order_status_new_order_checkbox)
        self.click(self.third_row_with_order_status_new_order_checkbox)

        order_id_1 = self.get_text(self.order_id_column)
        order_id_2 = self.get_text(self.order_id_column2)
        order_id_3 = self.get_text(self.order_id_column3)

        self.click(self.order_list_authorise_order_button)
        self.wait_for_seconds(5)

        self.expect_to_be_visible(self.authorise_orders_modal)
        authorise_orders_modal_text = self.get_text(self.authorise_orders_modal)

        # Perform assertions
        assert "Authorizing Orders" in authorise_orders_modal_text
        self.wait_for_seconds(12)
        assert "Successfully processed 3 item(s)" in authorise_orders_modal_text
        assert f"Successfully processed item: {order_id_1}" in authorise_orders_modal_text
        assert f"Successfully processed item: {order_id_2}" in authorise_orders_modal_text
        assert f"Successfully processed item: {order_id_3}" in authorise_orders_modal_text

        self.click(self.authorise_orders_modal_close_icon)

        # Verify the first order
        self.fill(self.fin_portal_global_search_field, order_id_1)
        self.click(self.fin_portal_global_search_icon)
        self.wait_for_seconds(5)
        self.click(self.authed_by_order_page_badge)

        auth_by = self.get_text(self.authed_by_order_page_badge)
        assert "Auth by Test en-gcs" in auth_by

        # Verify the second order
        self.reload()
        self.wait_for_seconds(5)
        self.fill(self.fin_portal_global_search_field, order_id_2)
        self.click(self.fin_portal_global_search_icon)
        self.wait_for_seconds(5)
        self.click(self.authed_by_order_page_badge)

        auth_by = self.get_text(self.authed_by_order_page_badge)
        assert "Auth by Test en-gcs" in auth_by

        # Verify the third order
        self.reload()
        self.wait_for_seconds(5)
        self.clear(self.fin_portal_global_search_field)
        self.fill(self.fin_portal_global_search_field, order_id_3)
        self.click(self.fin_portal_global_search_icon)
        self.wait_for_seconds(5)
        self.click(self.authed_by_order_page_badge)

        auth_by = self.get_text(self.authed_by_order_page_badge)
        assert "Auth by Test en-gcs" in auth_by

        return order_id_1, order_id_2, order_id_3

    def cancel_single_order(self):
        """Cancel Single Order"""
        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)
        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)
        self.click(self.first_row_with_order_status_new_order_checkbox)
        order_id = self.get_text(self.order_id_column)

        self.click(self.order_list_cancel_order_button)
        self.wait_for_seconds(2)

        self.expect_to_be_visible(self.cancel_orders_modal_header)
        cancel_orders_header_text = self.get_text(self.cancel_orders_modal_header)
        assert "Please confirm if you would like to cancel selected orders." in cancel_orders_header_text

        # Select random cancellation reason
        self.click(self.cancellation_reason_dropdown)
        random_number = random.randint(1, 5)

        if random_number == 1:
            self.click(self.cancellation_reason_customer_request)
        elif random_number == 2:
            self.click(self.cancellation_reason_supplier_out_of_stock)
        elif random_number == 3:
            self.click(self.cancellation_reason_fraud)
        elif random_number == 4:
            self.click(self.cancellation_reason_damaged)
        elif random_number == 5:
            self.click(self.cancellation_reason_incorrect_packaging)

        selected_reason = self.get_text(self.cancellation_reason_dropdown)

        self.click(self.cancel_orders_modal_cancel_button)

        self.expect_to_be_visible(self.cancel_orders_modal)
        cancel_orders_modal_text = self.get_text(self.cancel_orders_modal)

        # Perform assertions
        assert "Cancelling Orders" in cancel_orders_modal_text
        assert "Successfully processed 1 item(s)" in cancel_orders_modal_text
        assert f"Successfully processed item: {order_id}" in cancel_orders_modal_text

        self.click(self.cancel_orders_modal_close_icon)

        self.fill(self.fin_portal_global_search_field, order_id)
        self.click(self.fin_portal_global_search_icon)
        self.click(self.canceled_by_order_page_badge)

        canceled_by = self.get_text(self.canceled_by_order_page_badge)
        assert "Canceled by Test en-gcs" in canceled_by

        order_item_reason = self.get_text(self.order_item_cancellation_reason)
        assert selected_reason in order_item_reason
        assert "Test en-gcs" in order_item_reason

        return order_id, selected_reason

    def cancel_multiple_orders(self):
        """Cancel Multiple Orders"""
        self.click(self.past_10_days)
        self.click(self.apply_filter)

        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)
        self.expect_to_be_visible(self.first_row_with_order_status_new_order_checkbox)

        self.click(self.first_row_with_order_status_new_order_checkbox)
        self.click(self.second_row_with_order_status_new_order_checkbox)
        self.click(self.third_row_with_order_status_new_order_checkbox)

        order_id_1 = self.get_text(self.order_id_column)
        order_id_2 = self.get_text(self.order_id_column2)
        order_id_3 = self.get_text(self.order_id_column3)

        self.click(self.order_list_cancel_order_button)
        self.wait_for_seconds(5)

        self.click(self.cancellation_reason_dropdown)
        self.click(self.cancellation_reason_customer_request)
        self.click(self.cancel_orders_modal_cancel_button)
        self.wait_for_seconds(5)

        self.expect_to_be_visible(self.cancel_orders_modal)
        cancel_orders_modal_text = self.get_text(self.cancel_orders_modal)

        # Perform assertions
        assert "Cancelling Orders" in cancel_orders_modal_text
        self.wait_for_seconds(12)
        assert "Successfully processed 3 item(s)" in cancel_orders_modal_text
        assert f"Successfully processed item: {order_id_1}" in cancel_orders_modal_text
        assert f"Successfully processed item: {order_id_2}" in cancel_orders_modal_text
        assert f"Successfully processed item: {order_id_3}" in cancel_orders_modal_text

        self.wait_for_seconds(5)
        self.click(self.cancel_orders_modal_close_icon)

        # Verify the first order
        self.fill(self.fin_portal_global_search_field, order_id_1)
        self.click(self.fin_portal_global_search_icon)
        self.wait_for_seconds(5)
        self.click(self.canceled_by_order_page_badge)

        canceled_by = self.get_text(self.canceled_by_order_page_badge)
        assert "Canceled by Test en-gcs" in canceled_by

        # Verify the second order
        self.reload()
        self.wait_for_seconds(5)
        self.fill(self.fin_portal_global_search_field, order_id_2)
        self.click(self.fin_portal_global_search_icon)
        self.wait_for_seconds(5)
        self.click(self.canceled_by_order_page_badge)

        canceled_by = self.get_text(self.canceled_by_order_page_badge)
        assert "Canceled by Test en-gcs" in canceled_by

        # Verify the third order
        self.reload()
        self.wait_for_seconds(5)
        self.fill(self.fin_portal_global_search_field, order_id_3)
        self.click(self.fin_portal_global_search_icon)
        self.wait_for_seconds(5)
        self.click(self.canceled_by_order_page_badge)

        canceled_by = self.get_text(self.canceled_by_order_page_badge)
        assert "Canceled by Test en-gcs" in canceled_by

        order_item_reason = self.get_text(self.order_item_cancellation_reason)
        assert "Customer request" in order_item_reason
        assert "Test en-gcs" in order_item_reason

        return order_id_1, order_id_2, order_id_3

    def cancel_already_cancelled_order(self):
        """Cancel Already Cancelled Order"""
        self.expect_to_be_visible(self.first_row_with_order_status_cancelled_checkbox)
        self.expect_to_be_visible(self.first_row_with_order_status_cancelled_checkbox)
        self.click(self.first_row_with_order_status_cancelled_checkbox)
        order_id = self.get_text(self.order_id_column_canceled)

        self.click(self.order_list_cancel_order_button)
        self.wait_for_seconds(2)

        self.click(self.cancellation_reason_dropdown)
        self.click(self.cancellation_reason_customer_request)
        self.click(self.cancel_orders_modal_cancel_button)

        self.wait_for_seconds(5)
        self.expect_to_be_visible(self.cancel_orders_modal)
        cancel_orders_modal_text = self.get_text(self.cancel_orders_modal)

        # Perform assertions
        assert "Cancelling Orders" in cancel_orders_modal_text
        assert "Failed to process 1 item(s)" in cancel_orders_modal_text
        assert f"Failed to process item: {order_id} , Unable to process service request" in cancel_orders_modal_text

        return order_id

    def filter_by_daily_deal(self):
        """Filter By Daily Deal"""
        self.click(self.order_list_clear_filter_button)
        self.wait_for_seconds(2)
        self.expect_to_be_visible(self.daily_deals_checkbox)
        self.click(self.daily_deals_checkbox)
        self.click(self.order_list_apply_filter_button)

        order_id_elements = self.all_order_id_columns
        all_elements = order_id_elements.all()

        # Verify all rows contain "Daily Deal"
        for element in all_elements:
            assert "Daily Deal" in self.get_text(element)

    def filter_by_auth_status(self):
        """Filter By Auth Status"""
        self.click(self.order_list_clear_filter_button)
        self.wait_for_seconds(2)
        self.expect_to_be_visible(self.order_list_table)
        self.click(self.auth_status_dropdown)

        # Select random auth status
        random_number = random.randint(1, 2)
        if random_number == 1:
            self.click(self.auth_status_new)
            selected_status = "New"
        else:
            self.click(self.auth_status_auth)
            selected_status = "Auth"

        self.click(self.order_list_apply_filter_button)

        auth_status_elements = self.all_auth_status_columns
        all_elements = auth_status_elements.all()

        # Verify all rows contain the selected auth status
        for element in all_elements:
            assert selected_status in self.get_text(element)

    def filter_by_payment_method(self):
        """Filter By Payment Method"""
        self.click(self.order_list_clear_filter_button)
        self.expect_to_be_visible(self.order_list_table)
        self.click(self.payment_method_dropdown)

        # Select random payment method
        random_number = random.randint(1, 2)
        if random_number == 1:
            self.click(self.payment_method_credit_card)
            selected_payment_method = "Credit Card"
        else:
            self.click(self.payment_method_payfast)
            selected_payment_method = "PayFast"

        self.click(self.order_list_apply_filter_button)

        payment_method_elements = self.all_payment_method_columns
        all_elements = payment_method_elements.all()

        # Verify all rows contain the selected payment method
        for element in all_elements:
            assert selected_payment_method in self.get_text(element)

    def filter_by_shipping_method(self):
        """Filter By Shipping Method"""
        self.click(self.order_list_clear_filter_button)
        self.expect_to_be_visible(self.order_list_table)
        self.click(self.shipping_method_dropdown)

        self.click(self.shipping_method_collect)

        self.click(self.order_list_apply_filter_button)

        order_id_elements = self.all_order_id_columns
        all_elements = order_id_elements.all()

        # Verify all rows contain "Collection"
        for element in all_elements:
            assert "Collection" in self.get_text(element)

    def filter_by_minimum_order_total(self):
        """Filter By Minimum Order Total"""
        self.click(self.order_list_clear_filter_button)
        self.expect_to_be_visible(self.order_list_table)

        self.click(self.minimum_order_total_dropdown)
        self.click(self.minimum_order_total_r500)

        self.click(self.order_list_apply_filter_button)

        # Get all rows in the table
        row_count = self.get_locator_count(self.all_table_rows)

        # Check that all order totals are > R500
        for row_index in range(row_count):
            table_row = self.page.locator(f"//table[@class='ui small celled compact table']//tbody//tr[{row_index + 1}]//td[7]")
            order_total = self.get_text(table_row)
            numeric_value = float(order_total.replace("R", "").replace(",", ""))
            assert numeric_value > 500, f"{numeric_value} should be greater than 500"

    def filter_by_maximum_order_total(self):
        """Filter By Maximum Order Total"""
        self.click(self.order_list_clear_filter_button)
        self.expect_to_be_visible(self.order_list_table)

        self.click(self.minimum_order_total_dropdown)
        self.click(self.minimum_order_total_r0)

        self.click(self.maximum_order_total_dropdown)
        self.click(self.maximum_order_total_r500)

        self.click(self.order_list_apply_filter_button)

        # Get all rows in the table
        row_count = self.get_locator_count(self.all_table_rows)

        # Check that all order totals are < R500
        for row_index in range(row_count):
            table_row = self.page.locator(f"//table[@class='ui small celled compact table']//tbody//tr[{row_index + 1}]//td[7]")
            order_total = self.get_text(table_row)
            numeric_value = float(order_total.replace("R", "").replace(",", ""))
            assert numeric_value < 500, f"{numeric_value} should be less than 500"

    def filter_by_multiple_filters(self):
        """Filter By Multiple Filters"""
        self.click(self.order_list_clear_filter_button)
        self.expect_to_be_visible(self.order_list_table)

        # Set Auth Status to New
        self.click(self.auth_status_dropdown)
        self.click(self.auth_status_new)

        # Set Payment Method to Credit Card
        self.click(self.payment_method_dropdown)
        self.click(self.payment_method_credit_card)

        # Set Shipping Method to Collect
        self.click(self.shipping_method_dropdown)
        self.click(self.shipping_method_collect)

        self.click(self.order_list_apply_filter_button)

        # Verify Auth Status is New for all rows
        auth_status_elements = self.all_auth_status_columns
        all_auth_elements = auth_status_elements.all()
        for element in all_auth_elements:
            assert "New" in self.get_text(element), "All Auth status rows should be New"

        # Verify Payment Method is Credit Card for all rows
        payment_method_elements = self.all_payment_method_columns
        all_payment_elements = payment_method_elements.all()
        for element in all_payment_elements:
            assert "Credit Card" in self.get_text(element), "All Payment method rows should be Credit Card"

        # Verify Shipping Method is Collect for all rows
        shipping_method_elements = self.all_order_id_columns
        all_shipping_elements = shipping_method_elements.all()
        for element in all_shipping_elements:
            assert "Collection" in self.get_text(element), "All Shipping method rows should be Collect"
