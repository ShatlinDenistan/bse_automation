import random
from pos.risk_queue_po import RiskQueuePO


class RiskQueuePage(RiskQueuePO):
    """Risk Queue page implementation."""

    def __init__(self, page):
        """Initialize Risk Queue page with all elements."""
        super().__init__(page)
        self.order_id_text = None
        self.selected_reason = None

    def navigate_to_risk_queue(self):
        """Navigate to the Risk Queue page."""
        self.click(self.menu_btn)
        self.click(self.risk_queue_menu_option)
        self.wait_till_element_visible(self.results_table)

    def click_show_items_dropdown_and_select_10_items(self):
        """Select 10 items from the show items dropdown."""
        self.click(self.item_list_dropdown)
        self.click(self.list_filter_10)

    def navigate_to_next_page(self):
        """Navigate to the next page in the results."""
        self.click(self.next_page)
        self.wait_till_element_visible(self.results_table)

    def select_an_order_to_clear_risk(self):
        """Select an order and clear its risk status."""
        self.click(self.order_checkbox)
        self.click(self.clear_risk_btn)

    def handle_alerts(self):
        """Handle browser alerts by accepting them."""
        self.page.on("dialog", lambda dialog: dialog.accept())

    def filter_using_payment_method(self):
        """Apply filters based on payment method."""
        self.click(self.clear_filter_btn)
        self.wait_till_element_visible(self.results_table)
        self.click(self.payment_method_dropdown)

        # Randomly select payment method
        random_number = random.randint(1, 2)
        if random_number == 1:
            self.click(self.payment_method_credit)
        else:
            self.click(self.payment_method_payfast)

        selected_payment_method = self.get_text(self.payment_method_dropdown)
        self.click(self.apply_filter_btn)

        # Verify all payment methods match the selected one
        payment_method_elements = self.page.locator(self.all_payment_method_columns.selector).all()
        for element in payment_method_elements:
            assert selected_payment_method in element.inner_text(), f"Payment method mismatch: Expected {selected_payment_method}"

    def filter_using_shipping_method(self):
        """Apply filters based on shipping method."""
        self.click(self.clear_filter_btn)
        self.wait_till_element_visible(self.results_table)
        self.click(self.shipping_method_dropdown)
        self.click(self.shipping_method_delivery)
        self.click(self.apply_filter_btn)

        # Verify shipping method is Express Delivery
        shipping_method_elements = self.all_order_id_columns.count()
        for i in range(shipping_method_elements):
            shipping_method_element = self.all_order_id_columns.nth(i)
            shipping_method_text = shipping_method_element.inner_text()
            assert "Express Delivery" in shipping_method_text, f"Shipping method mismatch: Expected 'Express Delivery' but got {shipping_method_text}"

    def filter_using_minimum_amount(self):
        """Filter orders using minimum amount filter."""
        self.click(self.clear_filter_btn)
        self.wait_till_element_visible(self.results_table)
        self.click(self.minimum_order_total_dropdown)
        self.click(self.minimum_order_total_r500)
        self.click(self.apply_filter_btn)

        # Verify all orders have total > 500
        rows = self.page.locator("//table[@class='ui small celled compact table']//tbody//tr").all()
        for row in rows:
            order_total_cell = row.locator("td").nth(9)
            order_total_text = order_total_cell.inner_text()
            numeric_value = float(order_total_text.replace("R", "").replace(",", ""))
            assert numeric_value > 500, f"Order total {numeric_value} is not greater than R500"

    def filter_using_maximum_amount(self):
        """Filter orders using maximum amount filter."""
        self.click(self.clear_filter_btn)
        self.wait_till_element_visible(self.results_table)
        self.click(self.minimum_order_total_dropdown)
        self.click(self.minimum_order_total_r0)
        self.click(self.maximum_order_total_dropdown)
        self.click(self.maximum_order_total_r5000)
        self.click(self.apply_filter_btn)

        # Verify all orders have total < 5000
        rows = self.page.locator("//table[@class='ui small celled compact table']//tbody//tr").all()
        for row in rows:
            order_total_cell = row.locator("td").nth(9)
            order_total_text = order_total_cell.inner_text()
            numeric_value = float(order_total_text.replace("R", "").replace(",", ""))
            assert numeric_value < 5000, f"Order total {numeric_value} is not less than R5000"

    def filter_using_multiple_filters(self):
        """Apply multiple filters at once."""
        self.click(self.clear_filter_btn)
        self.wait_till_element_visible(self.results_table)
        self.click(self.virtual_items_checkbox)
        self.click(self.date_range_checkbox)
        self.click(self.payment_method_dropdown)
        self.click(self.payment_method_credit)
        self.click(self.maximum_order_total_dropdown)
        self.click(self.maximum_order_total_r5000)
        self.click(self.apply_filter_btn)

        # Verify orders have total < 5000
        rows = self.page.locator("//table[@class='ui small celled compact table']//tbody//tr").all()
        for row in rows:
            order_total_cell = row.locator("td").nth(9)
            order_total_text = order_total_cell.inner_text()
            numeric_value = float(order_total_text.replace("R", "").replace(",", ""))
            assert numeric_value < 5000, f"Order total {numeric_value} is not less than R5000"

        # Verify payment method is Credit
        payment_method_elements = self.page.locator(self.all_payment_method_columns.selector).all()
        for element in payment_method_elements:
            assert "Credit" in element.inner_text(), "Payment method is not Credit"

    def filter_using_daily_deal(self):
        """Apply filter for daily deal orders."""
        self.click(self.clear_filter_btn)
        self.wait_till_element_visible(self.checkbox_daily_deals)
        self.click(self.checkbox_daily_deals)
        self.click(self.apply_filter_btn)
        self.wait_till_element_visible(self.results_table)

    def filter_using_date_range(self):
        """Apply filter for a specific date range."""
        self.click(self.clear_filter_btn)
        self.click(self.date_range_filter)
        self.fill(self.date_range_filter, "01-05-2024 - 31-05-2024")
        self.click(self.apply_filter_btn)

        # Verify dates are in May 2024
        rows = self.page.locator("//tbody/tr").all()
        for row in rows:
            date_cell = row.locator("td").nth(3)
            date_text = date_cell.inner_text()
            assert "May-2024" in date_text, f"Date {date_text} is not in May 2024"

    def select_first_order_on_grid(self):
        """Select the first order on the grid."""
        self.order_id_text = self.get_text(self.order_id_hyperlink)
        self.click(self.order_checkbox)

    def select_email_template_and_send_email(self):
        """Select an email template and send the email."""
        self.click(self.btn_send_email_table)
        self.click(self.ddl_email_templates)

        # Randomly select an email template
        random_number = random.randint(1, 14)
        self.click(self.email_template_options[random_number])
        self.click(self.btn_send_email)

    def verify_email_sent_success_message(self):
        """Verify the email sent success message."""
        self.wait_till_element_visible(self.email_sent_modal)
        email_sent_text = self.get_text(self.email_sent_modal)
        assert "Successfully processed" in email_sent_text, "Email success message not found"
        self.click(self.email_sent_modal_close_icon)

    def cancel_single_order(self):
        """Cancel a single order."""
        self.scroll_to_element(self.risk_queue_cancel_order_button)
        self.click(self.risk_queue_cancel_order_button)
        self.page.wait_for_timeout(2000)

        self.wait_till_element_visible(self.cancel_orders_modal_header)
        cancel_orders_header_text = self.get_text(self.cancel_orders_modal_header)
        assert "Please confirm if you would like to cancel selected orders." in cancel_orders_header_text, "Cancel orders header text mismatch"

        self.click(self.cancellation_reason_dropdown)

        # Randomly select a cancellation reason
        random_number = random.randint(1, 5)
        self.click(self.cancellation_reason_options[random_number])

        self.selected_reason = self.get_text(self.cancellation_reason_dropdown)
        self.click(self.cancel_orders_modal_cancel_button)

        self.wait_till_element_visible(self.cancel_orders_modal)
        cancel_orders_modal_text = self.get_text(self.cancel_orders_modal)
        assert "Cancelling Orders" in cancel_orders_modal_text, "Cancelling orders text not found"

        self.page.wait_for_timeout(3000)
        cancel_orders_success_message_text = self.get_text(self.cancel_order_modal_success_message)
        assert "Successfully processed 1 item(s)" in cancel_orders_success_message_text, "Success message not found"

        self.click(self.cancel_orders_modal_close_icon)

    def verify_canceled_order_status(self):
        """Verify the status of a canceled order."""
        self.fill(self.fin_portal_global_search_field, self.order_id_text)
        self.click(self.fin_portal_global_search_icon)
        self.scroll_to_element(self.canceled_by_order_page_badge)

        canceled_by_text = self.get_text(self.canceled_by_order_page_badge)
        assert "Canceled by Test en-gcs" in canceled_by_text, "Canceled by text mismatch"

        order_item_reason_text = self.get_text(self.order_item_cancellation_reason)
        assert self.selected_reason in order_item_reason_text, "Order cancellation reason mismatch"
        assert "Test en-gcs" in order_item_reason_text, "Cancellation by user mismatch"
