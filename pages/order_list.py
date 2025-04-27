import random

from pos.order_list_po import OrderListPO


class OrderListPage(OrderListPO):
    """Order List page with all functionality."""

    def navigate_to_order_list_page(self):
        """Navigate to Order List page from main menu."""
        self.click(self.btn_menu)
        self.click(self.order_list_menu_option)

    def clear_today_filter(self):
        """Clear today's date filter."""
        self.click(self.clear_date_range_today)
        self.click(self.order_list_apply_filter_button)

    def apply_filter(self):
        """Click apply filter button."""
        self.click(self.order_list_apply_filter_button)

    def clear_filters(self):
        """Clear all filters."""
        self.click(self.clear_filter_button)
        self.wait_till_element_visible(self.order_list_table)

    def authorise_single_order(self):
        """Authorise a single order from the list."""
        self.click(self.past_10_days)
        self.apply_filter()

        self.wait_till_element_visible(self.first_row_new_order_checkbox)
        self.wait_for_element_enabled(self.first_row_new_order_checkbox)
        self.click(self.first_row_new_order_checkbox)
        order_id = self.get_text(self.order_id_column)

        self.scroll_to_element(self.authorise_order_button)
        self.click(self.authorise_order_button)
        self.wait_for_seconds(5)

        self.wait_till_element_visible(self.authorise_orders_modal)
        modal_text = self.get_text(self.authorise_orders_modal)

        assert "Authorizing Orders" in modal_text, "Modal doesn't show authorizing orders"
        self.wait_for_seconds(3)
        assert "Successfully processed 1 item(s)" in modal_text, "Not showing success message"
        assert f"Successfully processed item: {order_id}" in modal_text, "Order ID not found in success message"

        self.click(self.authorise_orders_modal_close_icon)

        self.fill(self.global_search_field, order_id)
        self.click(self.global_search_icon)

        self.scroll_to_element(self.authed_by_badge)
        auth_by_text = self.get_text(self.authed_by_badge)

        assert "Auth by Test en-gcs" in auth_by_text, "Auth details not showing correctly"

        return order_id

    def authorise_multiple_orders(self):
        """Authorise multiple orders from the list."""
        self.click(self.past_10_days)
        self.apply_filter()

        self.wait_till_element_visible(self.first_row_new_order_checkbox)
        self.wait_for_element_enabled(self.first_row_new_order_checkbox)

        self.click(self.first_row_new_order_checkbox)
        self.click(self.second_row_new_order_checkbox)
        self.click(self.third_row_new_order_checkbox)

        order_id_1 = self.get_text(self.order_id_column)
        order_id_2 = self.get_text(self.order_id_column2)
        order_id_3 = self.get_text(self.order_id_column3)

        self.scroll_to_element(self.authorise_order_button)
        self.click(self.authorise_order_button)
        self.wait_for_seconds(5)

        self.wait_till_element_visible(self.authorise_orders_modal)
        modal_text = self.get_text(self.authorise_orders_modal)

        assert "Authorizing Orders" in modal_text, "Modal doesn't show authorizing orders"
        self.wait_for_seconds(12)
        assert "Successfully processed 3 item(s)" in modal_text, "Not showing success for 3 items"
        assert f"Successfully processed item: {order_id_1}" in modal_text, "Order ID 1 not found in success"
        assert f"Successfully processed item: {order_id_2}" in modal_text, "Order ID 2 not found in success"
        assert f"Successfully processed item: {order_id_3}" in modal_text, "Order ID 3 not found in success"

        self.click(self.authorise_orders_modal_close_icon)

        # Verify all three orders
        order_ids = [order_id_1, order_id_2, order_id_3]
        for order_id in order_ids:
            self.fill(self.global_search_field, order_id)
            self.click(self.global_search_icon)
            self.wait_for_seconds(5)

            self.scroll_to_element(self.authed_by_badge)
            auth_by_text = self.get_text(self.authed_by_badge)
            assert "Auth by Test en-gcs" in auth_by_text, f"Auth details not showing for order {order_id}"

            if order_id != order_ids[-1]:  # Don't reload on last iteration
                self.reload_page()
                self.wait_for_seconds(5)
                self.clear(self.global_search_field)

        return order_ids

    def cancel_single_order(self):
        """Cancel a single order from the list."""
        self.wait_till_element_visible(self.first_row_new_order_checkbox)
        self.wait_for_element_enabled(self.first_row_new_order_checkbox)
        self.click(self.first_row_new_order_checkbox)
        order_id = self.get_text(self.order_id_column)

        self.scroll_to_element(self.cancel_order_button)
        self.click(self.cancel_order_button)
        self.wait_for_seconds(2)

        self.wait_till_element_visible(self.cancel_orders_modal_header)
        header_text = self.get_text(self.cancel_orders_modal_header)
        assert "Please confirm" in header_text, "Confirmation header not showing"

        self.click(self.cancellation_reason_dropdown)

        # Choose a random reason
        random_number = random.randint(1, 5)
        if random_number == 1:
            self.click(self.reason_customer_request)
        elif random_number == 2:
            self.click(self.reason_supplier_out_of_stock)
        elif random_number == 3:
            self.click(self.reason_fraud)
        elif random_number == 4:
            self.click(self.reason_damaged)
        elif random_number == 5:
            self.click(self.reason_incorrect_packaging)

        selected_reason = self.get_text(self.cancellation_reason_dropdown)

        self.click(self.cancel_orders_button)

        self.wait_till_element_visible(self.cancel_orders_modal)
        modal_text = self.get_text(self.cancel_orders_modal)

        assert "Cancelling Orders" in modal_text, "Modal doesn't show cancelling orders"
        assert "Successfully processed 1 item(s)" in modal_text, "Not showing success message"
        assert f"Successfully processed item: {order_id}" in modal_text, "Order ID not found in success"

        self.click(self.cancel_orders_modal_close_icon)

        self.fill(self.global_search_field, order_id)
        self.click(self.global_search_icon)

        self.scroll_to_element(self.canceled_by_badge)
        canceled_by_text = self.get_text(self.canceled_by_badge)

        assert "Canceled by Test en-gcs" in canceled_by_text, "Cancel details not showing"

        order_item_reason = self.get_text(self.order_item_cancellation_reason)
        assert selected_reason in order_item_reason, "Selected reason not showing"
        assert "Test en-gcs" in order_item_reason, "User not showing in reason"

        return order_id, selected_reason

    def cancel_multiple_orders(self):
        """Cancel multiple orders from the list."""
        self.click(self.past_10_days)
        self.apply_filter()

        self.wait_till_element_visible(self.first_row_new_order_checkbox)
        self.wait_for_element_enabled(self.first_row_new_order_checkbox)

        self.click(self.first_row_new_order_checkbox)
        self.click(self.second_row_new_order_checkbox)
        self.click(self.third_row_new_order_checkbox)

        order_id_1 = self.get_text(self.order_id_column)
        order_id_2 = self.get_text(self.order_id_column2)
        order_id_3 = self.get_text(self.order_id_column3)

        self.scroll_to_element(self.cancel_order_button)
        self.click(self.cancel_order_button)
        self.wait_for_seconds(5)

        self.click(self.cancellation_reason_dropdown)
        self.click(self.reason_customer_request)
        selected_reason = "Customer request"

        self.click(self.cancel_orders_button)
        self.wait_for_seconds(5)

        self.wait_till_element_visible(self.cancel_orders_modal)
        modal_text = self.get_text(self.cancel_orders_modal)

        assert "Cancelling Orders" in modal_text, "Modal doesn't show cancelling orders"
        self.wait_for_seconds(12)
        assert "Successfully processed 3 item(s)" in modal_text, "Not showing success for 3 items"
        assert f"Successfully processed item: {order_id_1}" in modal_text, "Order ID 1 not found in success"
        assert f"Successfully processed item: {order_id_2}" in modal_text, "Order ID 2 not found in success"
        assert f"Successfully processed item: {order_id_3}" in modal_text, "Order ID 3 not found in success"

        self.wait_for_seconds(5)
        self.click(self.cancel_orders_modal_close_icon)

        # Verify all three orders
        order_ids = [order_id_1, order_id_2, order_id_3]
        for order_id in order_ids:
            self.fill(self.global_search_field, order_id)
            self.click(self.global_search_icon)
            self.wait_for_seconds(5)

            self.scroll_to_element(self.canceled_by_badge)
            canceled_by_text = self.get_text(self.canceled_by_badge)
            assert "Canceled by Test en-gcs" in canceled_by_text, f"Cancel details not showing for order {order_id}"

            if order_id == order_ids[-1]:
                # Check reason on the last order
                order_item_reason = self.get_text(self.order_item_cancellation_reason)
                assert selected_reason in order_item_reason, "Selected reason not showing"
                assert "Test en-gcs" in order_item_reason, "User not showing in reason"
            elif order_id != order_ids[-1]:  # Don't reload on last iteration
                self.reload_page()
                self.wait_for_seconds(5)

        return order_ids, selected_reason

    def cancel_already_cancelled_order(self):
        """Try to cancel an already cancelled order."""
        self.wait_till_element_visible(self.first_row_canceled_checkbox)
        self.wait_for_element_enabled(self.first_row_canceled_checkbox)
        self.click(self.first_row_canceled_checkbox)
        order_id = self.get_text(self.order_id_column_canceled)

        self.scroll_to_element(self.cancel_order_button)
        self.click(self.cancel_order_button)
        self.wait_for_seconds(2)

        self.click(self.cancellation_reason_dropdown)
        self.click(self.reason_customer_request)
        self.click(self.cancel_orders_button)

        self.wait_for_seconds(5)
        self.wait_till_element_visible(self.cancel_orders_modal)
        modal_text = self.get_text(self.cancel_orders_modal)

        assert "Cancelling Orders" in modal_text, "Modal doesn't show cancelling orders"
        assert "Failed to process 1 item(s)" in modal_text, "Not showing failure message"
        assert f"Failed to process item: {order_id} , Unable to process service request" in modal_text, "Error details not found"

        return order_id

    def filter_by_daily_deal(self):
        """Filter orders by daily deals."""
        self.click(self.clear_filter_button)
        self.wait_for_seconds(2)
        self.wait_till_element_visible(self.daily_deals_checkbox)
        self.click(self.daily_deals_checkbox)
        self.click(self.order_list_apply_filter_button)

        # Verify all orders are daily deals
        element_count = self.all_order_id_columns.count()
        for i in range(element_count):
            element = self.all_order_id_columns.nth(i)
            element_text = self.get_text(element)
            assert "Daily Deal" in element_text, "Found order that isn't a daily deal"

        return element_count

    def filter_by_auth_status(self):
        """Filter orders by authorization status."""
        self.click(self.clear_filter_button)
        self.wait_for_seconds(2)
        self.wait_till_element_visible(self.order_list_table)
        self.click(self.auth_status_dropdown)

        # Choose a random status
        random_number = random.randint(1, 2)
        if random_number == 1:
            self.click(self.auth_status_new)
            selected_status = "New"
        else:
            self.click(self.auth_status_auth)
            selected_status = "Auth"

        self.click(self.order_list_apply_filter_button)

        # Verify all orders have the selected status
        element_count = self.all_auth_status_columns.count()
        for i in range(element_count):
            element = self.all_auth_status_columns.nth(i)
            element_text = self.get_text(element)
            assert selected_status in element_text, f"Found order with status other than {selected_status}"

        return selected_status, element_count

    def filter_by_payment_method(self):
        """Filter orders by payment method."""
        self.click(self.clear_filter_button)
        self.wait_till_element_visible(self.order_list_table)
        self.click(self.payment_method_dropdown)

        # Choose a random payment method
        random_number = random.randint(1, 2)
        if random_number == 1:
            self.click(self.payment_method_credit_card)
            selected_method = "Credit Card"
        else:
            self.click(self.payment_method_payfast)
            selected_method = "PayFast"

        self.click(self.order_list_apply_filter_button)

        # Verify all orders have the selected payment method
        element_count = self.all_payment_method_columns.count()
        for i in range(element_count):
            element = self.all_payment_method_columns.nth(i)
            element_text = self.get_text(element)
            assert selected_method in element_text, f"Found order with payment method other than {selected_method}"

        return selected_method, element_count

    def filter_by_shipping_method(self):
        """Filter orders by shipping method (collect)."""
        self.click(self.clear_filter_button)
        self.wait_till_element_visible(self.order_list_table)
        self.click(self.shipping_method_dropdown)

        self.click(self.shipping_method_collect)

        self.click(self.order_list_apply_filter_button)

        # Verify all orders are collection orders
        element_count = self.all_order_id_columns.count()
        for i in range(element_count):
            element = self.all_order_id_columns.nth(i)
            element_text = self.get_text(element)
            assert "Collection" in element_text, "Found order that isn't a collection order"

        return element_count

    def filter_by_minimum_order_total(self):
        """Filter orders by minimum order total."""
        self.click(self.clear_filter_button)
        self.wait_till_element_visible(self.order_list_table)

        self.click(self.minimum_order_total_dropdown)
        self.click(self.minimum_order_total_r500)

        self.click(self.order_list_apply_filter_button)

        # Get the row count and verify each amount is above R500
        element_count = self.order_list_table.count()

        for i in range(element_count):
            # Using 1-based indexing for the XPath because the locator is built that way
            row_index = i + 1
            order_total = self.get_text(f"//table[@class='ui small celled compact table']//tbody//tr[{row_index}]//td[7]")
            numeric_value = float(order_total.replace("R", "").replace(",", ""))
            assert numeric_value > 500, f"Found order total less than R500: {numeric_value}"

        return element_count

    def filter_by_maximum_order_total(self):
        """Filter orders by maximum order total."""
        self.click(self.clear_filter_button)
        self.wait_till_element_visible(self.order_list_table)

        self.click(self.minimum_order_total_dropdown)
        self.click(self.minimum_order_total_r0)

        self.click(self.maximum_order_total_dropdown)
        self.click(self.maximum_order_total_r500)

        self.click(self.order_list_apply_filter_button)

        # Get the row count and verify each amount is below R500
        element_count = self.order_list_table.count()

        for i in range(element_count):
            # Using 1-based indexing for the XPath because the locator is built that way
            row_index = i + 1
            order_total = self.get_text(f"//table[@class='ui small celled compact table']//tbody//tr[{row_index}]//td[7]")
            numeric_value = float(order_total.replace("R", "").replace(",", ""))
            assert numeric_value < 500, f"Found order total greater than R500: {numeric_value}"

        return element_count

    def filter_by_multiple_filters(self):
        """Apply multiple filters at once."""
        self.click(self.clear_filter_button)
        self.wait_till_element_visible(self.order_list_table)

        self.click(self.auth_status_dropdown)
        self.click(self.auth_status_new)

        self.click(self.payment_method_dropdown)
        self.click(self.payment_method_credit_card)

        self.click(self.shipping_method_dropdown)
        self.click(self.shipping_method_collect)

        self.click(self.order_list_apply_filter_button)

        # Verify auth status
        auth_status_count = self.all_auth_status_columns.count()
        for i in range(auth_status_count):
            element = self.all_auth_status_columns.nth(i)
            element_text = self.get_text(element)
            assert "New" in element_text, "Found order with Auth status other than New"

        # Verify payment method
        payment_method_count = self.all_payment_method_columns.count()
        for i in range(payment_method_count):
            element = self.all_payment_method_columns.nth(i)
            element_text = self.get_text(element)
            assert "Credit Card" in element_text, "Found order with Payment method other than Credit Card"

        # Verify shipping method
        shipping_method_count = self.all_order_id_columns.count()
        for i in range(shipping_method_count):
            element = self.all_order_id_columns.nth(i)
            element_text = self.get_text(element)
            assert "Collection" in element_text, "Found order that isn't a Collection order"

        return auth_status_count
