from playwright.sync_api import Page
import random
from base.page_base import PageBase

# Static locators
menu_btn = ("//i[@aria-hidden='true' and @class='content large icon']", "Menu Button")
risk_queue_menu_option = ("//body/div[@id='root']/div[1]/a[4]", "Risk Queue Menu Option")
results_table = ("//*[@class='ui small celled compact table']", "Results Table")
item_list_ddl = ("//div[contains(text(),'Show 15 Items')]", "Items Per Page Dropdown")
list_filter_10 = ("//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[1]", "10 Items Filter")
next_page = ("//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[2]/a[2]", "Next Page Button")
order_checkbox = ("//body/div[@id='root']/div[3]/div/div/table/tbody/tr[1]/td[1]/div", "First Order Checkbox")
clear_risk_btn = ("//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[1]", "Clear Risk Button")
clear_filter_btn = ("//button[contains(text(), 'Clear Filter')]", "Clear Filter Button")

# Filter locators
payment_method_dropdown = ("//div[@name='paymentMethod']", "Payment Method Dropdown")
shipping_method_dropdown = ("//div[@name='shippingMethod']", "Shipping Method Dropdown")
shipping_method_delivery = ("//span[text()='Courier']", "Courier Shipping Option")
minimum_total_dropdown = ("//div[@name='minimumTotal']", "Minimum Total Dropdown")
maximum_total_dropdown = ("//div[@name='maximumTotal']", "Maximum Total Dropdown")
apply_filter_btn = ("//button[contains(text(), 'Filter')]", "Apply Filter Button")
virtual_items_checkbox = ("//*[@id='root']/div[3]/div/div/form/div/div/div[1]/div/div/div[2]/div", "Virtual Items Checkbox")
daily_deals_checkbox = ("//*[@id='root']/div[3]/div/div/form/div/div/div[1]/div/div/div[1]/div", "Daily Deals Checkbox")
date_range_checkbox = ("//*[@id='root']/div[3]/div/div/form/div/div/div[2]/div/div[3]/div", "Date Range Checkbox")
date_filter = ("//input[@name='dateRange']", "Date Range Filter")

# Email template locators
send_email_btn = ("//table/tfoot/tr/th/div/div[3]/button", "Send Email Button")
email_templates_dropdown = ("//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]", "Email Templates Dropdown")
send_emails_confirm_btn = ("//button[contains(text(),'Send Emails')]", "Send Emails Confirm Button")
email_sent_modal = ("//div[contains(text(),'Successfully processed')]", "Email Sent Success Modal")
email_sent_close_icon = ("//body/div[2]/div[1]/i[1]", "Email Modal Close Icon")

# Cancel order locators
risk_queue_cancel_order_btn = ("//button[contains(text(), 'Cancel Order(s)')]", "Cancel Order Button")
cancel_orders_modal_header = ("//div[contains(text(),'Please confirm')]", "Cancel Orders Modal Header")
cancellation_reason_dropdown = ("//div[@name='cancelReason']", "Cancellation Reason Dropdown")
cancel_orders_modal_cancel_btn = ("//button[contains(text(), 'Cancel Orders')]", "Cancel Orders Confirm Button")
cancel_orders_modal = ("//div[contains(@class, 'ui large modal transition visible active')]", "Cancel Orders Modal")
cancel_success_message = ("//div[contains(@class, 'ui success message')]/div/div", "Cancel Success Message")
cancel_modal_close_icon = ("//*[@class= 'close icon']", "Cancel Modal Close Icon")

# Order details locators
order_id_hyperlink = ("//*[@id='root']/div[3]/div/div/table/tbody/tr[1]/td[2]/a", "Order ID Link")
global_search_field = ("//*[@name='searchText' and @type='text']", "Global Search Field")
global_search_icon = ("//*[@class='search icon']", "Global Search Icon")
canceled_by_badge = ("//div[contains(text(), 'Canceled by')]", "Canceled By Badge")
cancellation_reason = ("//div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]", "Cancellation Reason")

# Dynamic locators with format strings
payment_method_option = ("//span[text()='{}']", "Payment Method Option")
all_payment_method_columns = ("//td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 7)]", "All Payment Method Columns")
all_order_id_columns = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]", "All Order ID Columns")
email_template_option = ("//span[contains(text(),'{}')]", "Email Template Option")
cancellation_reason_option = ("//span[contains(text(), '{}')]", "Cancellation Reason Option")


class RiskQueuePage(PageBase):
    """Page object for Risk Queue functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Initialize locators
        self.menu_btn = self.locator(menu_btn)
        self.risk_queue_menu_option = self.locator(risk_queue_menu_option)
        self.results_table = self.locator(results_table)
        self.item_list_ddl = self.locator(item_list_ddl)
        self.list_filter_10 = self.locator(list_filter_10)
        self.next_page = self.locator(next_page)
        self.order_checkbox = self.locator(order_checkbox)
        self.clear_risk_btn = self.locator(clear_risk_btn)
        self.clear_filter_btn = self.locator(clear_filter_btn)

        # Filter locators
        self.payment_method_dropdown = self.locator(payment_method_dropdown)
        self.shipping_method_dropdown = self.locator(shipping_method_dropdown)
        self.shipping_method_delivery = self.locator(shipping_method_delivery)
        self.minimum_total_dropdown = self.locator(minimum_total_dropdown)
        self.maximum_total_dropdown = self.locator(maximum_total_dropdown)
        self.apply_filter_btn = self.locator(apply_filter_btn)
        self.virtual_items_checkbox = self.locator(virtual_items_checkbox)
        self.daily_deals_checkbox = self.locator(daily_deals_checkbox)
        self.date_range_checkbox = self.locator(date_range_checkbox)
        self.date_filter = self.locator(date_filter)

        # Email locators
        self.send_email_btn = self.locator(send_email_btn)
        self.email_templates_dropdown = self.locator(email_templates_dropdown)
        self.send_emails_confirm_btn = self.locator(send_emails_confirm_btn)
        self.email_sent_modal = self.locator(email_sent_modal)
        self.email_sent_close_icon = self.locator(email_sent_close_icon)

        # Cancel order locators
        self.risk_queue_cancel_order_btn = self.locator(risk_queue_cancel_order_btn)
        self.cancel_orders_modal_header = self.locator(cancel_orders_modal_header)
        self.cancellation_reason_dropdown = self.locator(cancellation_reason_dropdown)
        self.cancel_orders_modal_cancel_btn = self.locator(cancel_orders_modal_cancel_btn)
        self.cancel_orders_modal = self.locator(cancel_orders_modal)
        self.cancel_success_message = self.locator(cancel_success_message)
        self.cancel_modal_close_icon = self.locator(cancel_modal_close_icon)

        # Order details locators
        self.order_id_hyperlink = self.locator(order_id_hyperlink)
        self.global_search_field = self.locator(global_search_field)
        self.global_search_icon = self.locator(global_search_icon)
        self.canceled_by_badge = self.locator(canceled_by_badge)
        self.cancellation_reason = self.locator(cancellation_reason)

    def navigate_to_risk_queue(self):
        """Navigate to the Risk Queue page"""
        self.click(self.menu_btn)
        self.click(self.risk_queue_menu_option)
        self.expect_to_be_visible(self.results_table)

    def select_items_per_page(self, items: str = "10"):
        """Select number of items to display per page"""
        self.click(self.item_list_ddl)
        self.click(self.list_filter_10)

    def navigate_to_next_page(self):
        """Navigate to the next page of results"""
        self.click(self.next_page)
        self.expect_to_be_visible(self.results_table)

    def select_order_and_clear_risk(self):
        """Select first order and clear its risk status"""
        self.click(self.order_checkbox)
        self.click(self.clear_risk_btn)
        self.page.on("dialog", lambda dialog: dialog.accept())

    def filter_by_payment_method(self, payment_method: str):
        """Filter orders by payment method"""
        self.click(self.clear_filter_btn)
        self.expect_to_be_visible(self.results_table)
        self.click(self.payment_method_dropdown)
        payment_option = self.locator((payment_method_option[0].format(payment_method), f"{payment_method} Option"))
        self.click(payment_option)
        self.click(self.apply_filter_btn)

        payment_columns = self.page.locator(all_payment_method_columns[0]).all()
        for column in payment_columns:
            self.expect(column).to_contain_text(payment_method)

    def filter_by_shipping_method(self):
        """Filter orders by shipping method"""
        self.click(self.clear_filter_btn)
        self.expect_to_be_visible(self.results_table)
        self.click(self.shipping_method_dropdown)
        self.click(self.shipping_method_delivery)
        self.click(self.apply_filter_btn)

        order_columns = self.page.locator(all_order_id_columns[0]).all()
        for column in order_columns:
            self.expect(column).to_contain_text("Express Delivery")

    def filter_by_amount_range(self, minimum: str = None, maximum: str = None):
        """Filter orders by amount range"""
        self.click(self.clear_filter_btn)
        self.expect_to_be_visible(self.results_table)

        if minimum:
            self.click(self.minimum_total_dropdown)
            min_option = self.locator((payment_method_option[0].format(minimum), f"Minimum {minimum} Option"))
            self.click(min_option)

        if maximum:
            self.click(self.maximum_total_dropdown)
            max_option = self.locator((payment_method_option[0].format(maximum), f"Maximum {maximum} Option"))
            self.click(max_option)

        self.click(self.apply_filter_btn)

    def apply_multiple_filters(self):
        """Apply multiple filters at once"""
        self.click(self.clear_filter_btn)
        self.expect_to_be_visible(self.results_table)
        self.click(self.virtual_items_checkbox)
        self.click(self.date_range_checkbox)
        self.click(self.payment_method_dropdown)
        self.click(self.locator((payment_method_option[0].format("Credit"), "Credit Option")))
        self.click(self.maximum_total_dropdown)
        self.click(self.locator((payment_method_option[0].format("5000"), "5000 Maximum Option")))
        self.click(self.apply_filter_btn)

    def filter_by_daily_deals(self):
        """Filter orders by daily deals"""
        self.click(self.clear_filter_btn)
        self.expect_to_be_visible(self.daily_deals_checkbox)
        self.click(self.daily_deals_checkbox)
        self.click(self.apply_filter_btn)
        self.expect_to_be_visible(self.results_table)

    def filter_by_date_range(self, date_range: str):
        """Filter orders by date range"""
        self.click(self.clear_filter_btn)
        self.click(self.date_filter)
        self.fill(self.date_filter, date_range)
        self.click(self.apply_filter_btn)

    def select_first_order(self) -> str:
        """Select the first order and return its ID"""
        order_id = self.get_text(self.order_id_hyperlink)
        self.click(self.order_checkbox)
        return order_id

    def select_email_template_and_send(self):
        """Select an email template and send email"""
        self.click(self.send_email_btn)
        self.click(self.email_templates_dropdown)

        template_index = random.randint(1, 14)
        template_types = [
            "Identification required: Credit card",
            "Identification and card details required",
            "Identification required: Payfast & Ozow",
            "Identification not accepted",
            "Identification not received: Payfast & Ozow",
            "Identification not received: Credit card",
            "Credit card refund failed",
            "EFT refund failed",
            "Refund delayed",
            "Short paid",
            "Deposit Match",
            "Duplicate Payment",
            "Voucher Payment",
            "Generic",
        ]

        template_option = self.locator((email_template_option[0].format(template_types[template_index - 1]), f"{template_types[template_index-1]} Template"))
        self.click(template_option)
        self.click(self.send_emails_confirm_btn)

    def verify_email_sent(self):
        """Verify email was sent successfully"""
        self.wait_for_seconds(2)
        self.expect_to_be_visible(self.email_sent_modal)
        self.click(self.email_sent_close_icon)

    def cancel_selected_order(self):
        """Cancel the selected order"""
        self.scroll_into_view(self.risk_queue_cancel_order_btn)
        self.click(self.risk_queue_cancel_order_btn)
        self.wait_for_seconds(2)

        self.expect_to_be_visible(self.cancel_orders_modal_header)
        modal_text = self.get_text(self.cancel_orders_modal_header)
        assert "Please confirm" in modal_text

        self.click(self.cancellation_reason_dropdown)

        reason_index = random.randint(1, 5)
        reason_types = ["Customer request", "Supplier out of stock", "Fraud", "Damaged", "Incorrect Packaging"]

        reason_option = self.locator((cancellation_reason_option[0].format(reason_types[reason_index - 1]), f"{reason_types[reason_index-1]} Reason"))
        self.click(reason_option)
        selected_reason = self.get_text(self.cancellation_reason_dropdown)

        self.click(self.cancel_orders_modal_cancel_btn)
        self.expect_to_be_visible(self.cancel_orders_modal)
        self.wait_for_seconds(3)

        success_text = self.get_text(self.cancel_success_message)
        assert "Successfully processed 1 item(s)" in success_text
        self.click(self.cancel_modal_close_icon)
        return selected_reason

    def verify_canceled_order_status(self, order_id: str, selected_reason: str):
        """Verify the canceled order status"""
        self.fill(self.global_search_field, order_id)
        self.click(self.global_search_icon)
        self.scroll_into_view(self.canceled_by_badge)

        canceled_by_text = self.get_text(self.canceled_by_badge)
        assert "Canceled by Test en-gcs" in canceled_by_text

        order_reason = self.get_text(self.cancellation_reason)
        assert selected_reason in order_reason
        assert "Test en-gcs" in order_reason
