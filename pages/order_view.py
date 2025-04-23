from pos.order_view_po import OrderViewPO
import time


class OrderViewPage(OrderViewPO):
    """Order View page with all functionality."""

    def add_admin_notes(self):
        """Add admin notes to a customer."""
        self.wait_for_element_visible(self.note_dd)
        self.click(self.note_dd)
        self.click(self.add_notes_btn)
        self.fill_text(self.notes_txt_field, "Automation Admin Note")
        self.click(self.confirm_add_btn)

        self.wait_for_element_visible(self.note_confirm_message)
        note_message_text = self.get_text(self.note_confirm_message)
        note_message_text = note_message_text.replace("Request failed with status code 403\n×\n", "")

        assert "Note successfully added to Customer: " in note_message_text, "Note was not added successfully"

        return note_message_text

    def update_to_blacklist(self):
        """Blacklist a customer."""
        self.wait_for_element_visible(self.blacklist_cust_btn)
        self.click(self.blacklist_cust_btn)
        self.click(self.fraud_reason_list)
        self.click(self.fraud_reason_selection)

        self.fill_text(self.fin_note, "Automation Testing")
        self.click(self.confirm_blacklist)

        # Handle alert
        self.accept_alert()

        self.wait(3)
        self.wait_for_element_visible(self.note_confirm_message)
        message = self.get_text(self.note_confirm_message)
        message = message.replace("Request failed with status code 403\n×\n", "")

        assert "Successfully blacklisted the customer" in message, "Customer was not blacklisted successfully"

        return message

    def update_to_whitelist(self):
        """Whitelist a customer."""
        self.wait_for_element_visible(self.whitelist_cust_btn)
        self.click(self.whitelist_cust_btn)
        self.click(self.confirm_whitelist)

        # Handle alert
        self.accept_alert()

        self.wait(6)
        self.wait_for_element_visible(self.note_confirm_message)
        message = self.get_text(self.note_confirm_message)
        message = message.replace("Request failed with status code 403\n×\n", "")

        assert "Successfully Whitelisted Customer:" in message, "Customer was not whitelisted successfully"

        return message

    def cancel_all_order_items(self):
        """Cancel all items in an order."""
        self.wait_for_element_visible(self.cancel_all_item_btn)
        self.click(self.cancel_all_item_btn)
        self.click(self.cancellation_reason)

        self.scroll_to_element(self.customer_request_cancel_reason)
        self.click(self.customer_request_cancel_reason)
        self.click(self.confirm_cancelling_btn)
        self.click(self.close_cancel_modal)

        order_status_text = self.get_text(self.order_status)
        assert "Canceled by" in order_status_text, "Order was not canceled successfully"

        return order_status_text

    def send_an_email(self):
        """Send an email to the customer."""
        cust_id = self.get_text(self.customer_id)

        self.click(self.email_customer)
        self.click(self.email_template_ddl)
        self.click(self.email_template_selection)

        self.scroll_to_element(self.send_email_btn)
        self.click(self.send_email_btn)

        self.wait_for_element_visible(self.note_confirm_message)
        message = self.get_text(self.note_confirm_message)
        message = message.replace("\n×\nRequest failed with status code 404\n×", "")

        assert f"(Identification Not Accepted) email sent to customer {cust_id}" in message, "Email was not sent successfully"

        return message

    def mark_order_as_risky(self):
        """Mark an order as risky."""
        self.wait_for_element_visible(self.mark_as_risky_btn)
        self.click(self.mark_as_risky_btn)

        self.fill_text(self.mark_as_risky_reason, "Automation Test Risky Reason")
        self.click(self.add_reason_btn)

        flagged_as_risk_text = self.get_text(self.flagged_as_risk)
        assert "Flagged as risky" in flagged_as_risk_text, "Order was not marked as risky"

        return flagged_as_risk_text

    def verify_audit_log_entry(self, action_type):
        """Verify an entry in the audit log."""
        self.wait_for_element_visible(self.order_ellipsis_menu)
        self.click(self.order_ellipsis_menu)
        self.click(self.audit_log_menu_option)

        self.wait_for_element_visible(self.audit_log_action_type)
        action_type_text = self.get_text(self.audit_log_action_type)

        assert action_type in action_type_text, f"Audit log does not contain entry for {action_type}"

        return action_type_text

    def manually_authorize_an_order(self):
        """Manually authorize an order."""
        self.wait_for_element_visible(self.authorise_now_btn)
        self.click(self.authorise_now_btn)

        self.wait_for_element_visible(self.authorise_now_modal_message)
        success_message = self.get_text(self.authorise_now_modal_message)

        assert "Successfully processed 1 item(s)" in success_message, "Order was not authorized successfully"

        self.click(self.authorise_now_modal_close_icon)

        return success_message

    def verify_tracking_information_for_cancelled_order(self, heading):
        """Verify tracking information for a cancelled order."""
        self.wait_for_element_visible(self.order_fullfilment_accordion)
        self.click(self.order_fullfilment_accordion)

        order_tracking_heading_text = self.get_text(self.order_tracking_heading)
        assert heading in order_tracking_heading_text, f"Tracking heading does not contain '{heading}'"

        return order_tracking_heading_text

    def verify_order_tracking_heading(self, heading):
        """Verify the order tracking heading."""
        self.wait_for_element_visible(self.order_fullfilment_accordion)
        self.click(self.order_fullfilment_accordion)

        order_tracking_heading_text = self.get_text(self.order_tracking_heading)
        assert heading in order_tracking_heading_text, f"Tracking heading does not contain '{heading}'"

        return order_tracking_heading_text

    def verify_order_tracking_for_digital_products_only_order(self):
        """Verify tracking information for digital products only order."""
        self.wait_for_element_visible(self.order_fullfilment_accordion)
        self.click(self.order_fullfilment_accordion)

        order_tracking_user_info_text = self.get_text(self.order_tracking_user_info)
        assert "Digital Product(s)" in order_tracking_user_info_text, "Order tracking does not indicate digital products"

        return order_tracking_user_info_text

    def edit_customer_details(self):
        """Edit customer details."""
        self.click(self.edit_customer_btn)

        self.fill_text(self.cust_name, "Mike")
        self.fill_text(self.cust_surname, "Jackson")
        self.fill_text(self.business_name, "Automation Test PTY LTD")
        self.fill_text(self.vat_number, "9876543211")

        self.click(self.acc_status_ddl)
        self.click(self.acc_status)

        self.click(self.fraud_reason_list)
        self.click(self.fraud_reason_selection)

        self.click(self.staff_account_check)
        self.click(self.block_vou_check)
        self.click(self.confirm_btn)

        self.wait_for_element_visible(self.pop_up)
        message = self.get_text(self.pop_up)

        assert "Customer status data updated successfully" in message, "Customer details were not updated successfully"

        return message

    def view_order_events(self):
        """View order events."""
        self.click(self.order_ellipsis_menu)
        self.click(self.order_events_menu)

        self.wait_for_element_visible(self.event_log_results)

        return True

    def verify_part_payment_methods_badges(self):
        """Verify part payment methods badges."""
        self.wait_for_element_visible(self.first_payment_method_badge)

        first_payment_method_text = self.get_text(self.first_payment_method_badge)
        second_payment_method_text = self.get_text(self.second_payment_method_badge)

        assert "Credit Card" in first_payment_method_text, "First payment method badge is not Credit Card"
        assert "eBucks" in second_payment_method_text, "Second payment method badge is not eBucks"

        return first_payment_method_text, second_payment_method_text

    def add_order_notes(self):
        """Add notes to an order."""
        self.wait_for_element_visible(self.order_notes_accordion)
        self.click(self.order_notes_btn)

        self.fill_text(self.order_notes_text_field, "Automation Test: Order Note")
        self.click(self.add_notes_confirm_btn)

        self.wait_for_element_visible(self.note_added_message)
        add_note_message_text = self.get_text(self.note_added_message)

        assert "Note successfully added to Order" in add_note_message_text, "Order note was not added successfully"

        return add_note_message_text

    def add_fin_notes(self):
        """Add financial notes."""
        self.wait(10)
        self.wait_for_element_visible(self.fin_notes_accordion)
        self.click(self.add_fin_notes_btn)

        self.fill_text(self.fin_notes_text_field, "Automation Test: Fin Note")
        self.click(self.add_fin_notes_confirm_btn)

        self.wait_for_element_visible(self.note_added_message)
        add_note_message_text = self.get_text(self.note_added_message)

        assert "Note successfully added to Customer" in add_note_message_text, "Financial note was not added successfully"

        return add_note_message_text

    def add_customer_notes(self):
        """Add customer notes."""
        self.wait(10)
        self.wait_for_element_visible(self.customer_notes_accordion)
        self.click(self.customer_notes_accordion)
        self.click(self.add_customer_notes_btn)

        self.fill_text(self.customer_notes_text_field, "Automation Test: Customer Note")
        self.click(self.add_customer_notes_confirm_btn)

        self.wait_for_element_visible(self.note_added_message)
        add_note_message_text = self.get_text(self.note_added_message)

        assert "Note successfully added to Customer" in add_note_message_text, "Customer note was not added successfully"

        return add_note_message_text

    def cancel_an_order_item(self):
        """Cancel a specific order item."""
        self.click(self.select_item_checkbox)
        self.click(self.cancel_selected_item_btn)

        self.click(self.cancellation_reason)
        self.scroll_to_element(self.customer_request_cancel_reason)
        self.click(self.customer_request_cancel_reason)
        self.click(self.confirm_cancelling_btn)

        self.wait_for_element_visible(self.cancellation_results)
        message = self.get_text(self.cancellation_results)

        assert "Orderitem has successfully been cancelled" in message, "Order item was not cancelled successfully"

        return message

    def view_payment_ledger(self):
        """View payment ledger information."""
        self.wait_for_element_visible(self.payment_ledger_accordion)
        self.click(self.payment_ledger_accordion)

        first_payment_provider_text = self.get_text(self.payment_ledger_first_provider)
        second_payment_provider_text = self.get_text(self.payment_ledger_second_provider)

        assert "eBucks" in first_payment_provider_text, "First payment provider is not eBucks"
        assert "PayU" in second_payment_provider_text, "Second payment provider is not PayU"

        amount_paid_text = self.get_text(self.payment_ledger_paid_total_amount)
        assert "1,699.00" in amount_paid_text, "Amount paid is not 1,699.00"

        return first_payment_provider_text, second_payment_provider_text, amount_paid_text

    def bookmark_an_order(self):
        """Bookmark an order."""
        self.wait_for_element_visible(self.bookmark_icon)
        self.click(self.bookmark_icon)

        self.fill_text(self.bookmark_notes, "Testing")
        self.click(self.done_button)

        self.wait(3)
        counter = self.get_text(self.bookmark_counter)
        assert counter == "1", "Bookmark counter is not 1"

        return counter

    def remove_bookmarks(self):
        """Remove bookmarks."""
        self.click(self.bookmarks_page)
        self.click(self.remove_bookmarks_checkbox)
        self.click(self.remove_btn)

        self.wait_for_element_visible(self.progress_bar)
        self.click(self.close_modal)

        msg = self.get_text(self.confirmation_msg)
        assert msg == "No bookmarks to show here", "Bookmarks were not removed successfully"

        return msg

    def verify_order_financials(self, order_total, order_shipping, order_discount):
        """Verify order financial information."""
        self.wait_for_element_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)

        # Verify Order Items Amount
        order_item_amount_text = self.get_text(self.total_order_items_amount)
        order_item_amount = float(order_item_amount_text.replace("R ", ""))
        assert order_item_amount == order_total, f"Order item amount is {order_item_amount}, expected {order_total}"

        # Verify Shipping Amount
        shipping_amount_text = self.get_text(self.shipping_amount)
        shipping_amount = float(shipping_amount_text.replace("R ", ""))
        assert shipping_amount == order_shipping, f"Shipping amount is {shipping_amount}, expected {order_shipping}"

        # Verify Sub-Total Amount
        sub_total_amount_text = self.get_text(self.sub_total_amount)
        sub_total_amount = float(sub_total_amount_text.replace("R ", ""))
        sub_total_calculation = order_total + order_shipping
        assert sub_total_amount == sub_total_calculation, f"Sub-total amount is {sub_total_amount}, expected {sub_total_calculation}"

        # Verify Discount Amount
        discount_amount_text = self.get_text(self.discount_amount)
        discount_amount_text = discount_amount_text.replace("?", "").replace("R ", "").replace("-", "")
        discount_amount = float(discount_amount_text)
        assert discount_amount == order_discount, f"Discount amount is {discount_amount}, expected {order_discount}"

        return order_item_amount, shipping_amount, sub_total_amount, discount_amount

    def view_order_audit_logs(self):
        """View order audit logs."""
        self.wait_for_element_visible(self.order_ellipsis_menu)
        self.click(self.order_ellipsis_menu)
        self.click(self.audit_log_menu_option)

        self.wait_for_element_visible(self.logs_table)

        return True

    def view_address(self):
        """View address on Google Maps."""
        self.wait_for_element_visible(self.cust_acc_number)
        self.hover(self.cust_acc_number)

        self.wait_for_element_visible(self.address_google_icon)
        self.click(self.address_google_icon)

        self.wait(2)

        # Handle new window - return to original window instead of switching

        return True

    def verify_order_details(self, search_order_id):
        """Verify order details."""
        # Verify Order ID
        order_id_text = self.get_text(self.order_id)
        assert order_id_text == search_order_id, f"Order ID is {order_id_text}, expected {search_order_id}"

        # Verify auth status
        status_check = self.get_text(self.auth_status)
        assert "Auth" in status_check, "Auth status is not Auth"

        # Payment method
        payment_method_tag = self.get_text(self.first_payment_method_badge)
        assert "Credit Card Token" in payment_method_tag, "Payment method is not Credit Card Token"

        # Auth date
        auth_date_tag = self.get_text(self.auth_date)
        assert "25-Jan-2024 @ 9:31" in auth_date_tag, "Auth date is incorrect"

        self.click(self.order_fullfilment_accordion)

        # Order Fulfillment
        order_tracking_user_info_text = self.get_text(self.order_tracking_user_info)
        assert "Digital Product(s)" in order_tracking_user_info_text, "Order is not for digital products"

        self.click(self.order_fullfilment_accordion)

        # Order Notes
        self.scroll_to_element(self.order_notes_accordion)
        self.wait_for_element_visible(self.order_comments)

        # Cust Info
        self.hover(self.cust_acc_number)
        self.wait_for_element_visible(self.cust_info_popup)

        cust_status_check = self.get_text(self.cust_status)
        assert "active" in cust_status_check, "Customer status is not active"

        # Order Financials
        self.click(self.order_financials_accordion)

        # Verify Total Paid Amount
        order_total_paid_text = self.get_text(self.total_paid_amount)
        assert "R 100.00" in order_total_paid_text, "Total paid amount is not R 100.00"

        return order_id_text, status_check, payment_method_tag, auth_date_tag, order_tracking_user_info_text, cust_status_check, order_total_paid_text

    def get_rrn_details(self):
        """Get RRN (Retrieval Reference Number) details."""
        self.wait_for_element_visible(self.rrn)
        self.click(self.rrn)

        self.wait(2)

        # Handle new window - return RRN number instead of switching
        rrn_text = self.get_text(self.rrn)

        return rrn_text

    def update_order_item_to_shipped(self):
        """Update order item status to shipped."""
        self.wait_for_element_visible(self.edit_order_item_menu)

        item_status = self.get_text(self.return_canceled_tag)
        assert "Return Canceled" in item_status, "Item status is not Return Canceled"

        self.click(self.edit_order_item_menu)
        self.click(self.update_status_menu_option)
        self.click(self.update_to_shipped_button)

        self.wait(4)

        item_status_after = self.get_text(self.shipped_tag)
        assert "Shipped" in item_status_after, "Item was not updated to Shipped"

        return item_status, item_status_after

    def verify_payment_ledger_logs(self):
        """Verify payment ledger logs."""
        self.wait_for_element_visible(self.payment_ledger_accordion)
        self.click(self.payment_ledger_accordion)

        payment_provider_text = self.get_text(self.payment_ledger_payment_provider)
        assert "Payflex" in payment_provider_text, "Payment provider is not Payflex"

        return payment_provider_text

    def view_email_logs(self):
        """View email logs."""
        self.scroll_to_element(self.email_logs_accordion)
        self.click(self.email_logs_accordion)
        self.click(self.view_email_btn)

        self.wait_for_element_visible(self.email_view)

        return True

    def view_order_items_information(self):
        """View order items information."""
        self.wait_for_element_visible(self.order_items_accordion)

        order_item_status_text = self.get_text(self.order_item_status)
        assert order_item_status_text == "Canceled", f"Order item status is {order_item_status_text}, expected Canceled"

        order_item_canceled_by_text = self.get_text(self.order_item_canceled_by)
        assert order_item_canceled_by_text == "auto_cancel", f"Order item was not canceled by auto_cancel"

        return order_item_status_text, order_item_canceled_by_text

    def verify_show_items_and_pagination(self):
        """Verify show items dropdown and pagination."""
        self.wait_for_element_visible(self.order_items_show_items)
        self.click(self.order_items_show_items)

        # Simulate arrow keys press
        self.press_key("ArrowUp")
        self.press_key("ArrowUp")
        self.press_key("Enter")

        self.wait(1)
        self.click(self.order_items_pagination_page_two)

        return True

    def view_coupon_history(self):
        """View coupon history."""
        self.wait_for_element_visible(self.coupon_history_accordion)
        self.scroll_to_element(self.coupon_history_accordion)
        self.click(self.coupon_history_accordion)

        is_coupon_visible = self.is_element_visible(self.coupon_code)

        return is_coupon_visible

    def verify_delivery_tracking_information(self, heading):
        """Verify delivery tracking information."""
        item_status = self.get_text(self.delivered_tag)
        assert "Delivered" in item_status, "Item status is not Delivered"

        self.click(self.order_fullfilment_accordion)
        self.scroll_to_element(self.instruction_dropped_datetime)

        self.wait_for_element_visible(self.order_tracking_heading)
        order_tracking_heading_text = self.get_text(self.order_tracking_heading)
        assert heading in order_tracking_heading_text, f"Tracking heading does not contain '{heading}'"

        signed_by_text = self.get_text(self.signed_by)
        assert "Signed by: Nqobani (Customer)" in signed_by_text, "Signed by information is incorrect"

        instruction_datetime_text = self.get_text(self.instruction_dropped_datetime)
        assert "25 Aug 2024 @ 22:01" in instruction_datetime_text, "Instruction dropped datetime is incorrect"

        shipped_datetime_text = self.get_text(self.shipped_from_warehouse_datetime)
        assert "26 Aug 2024 @ 11:27" in shipped_datetime_text, "Shipped from warehouse datetime is incorrect"

        delivered_to_datetime_text = self.get_text(self.delivered_to_customer_datetime)
        assert "30 Aug 2024 @ 9:34" in delivered_to_datetime_text, "Delivered to customer datetime is incorrect"

        item_status = self.get_text(self.delivered_tag)
        assert "Delivered" in item_status, "Item status is not Delivered"

        self.click(self.order_fullfilment_accordion)

        return order_tracking_heading_text, signed_by_text, instruction_datetime_text, shipped_datetime_text, delivered_to_datetime_text, item_status

    def verify_waybill_tracking(self):
        """Verify waybill tracking information."""
        order_item_text = self.get_text(self.order_item)
        self.click(self.track_btn)

        self.wait_for_element_visible(self.waybill_no)
        waybill_no_text = self.get_text(self.waybill_no)
        assert "Waybill No: MDX133806010" in waybill_no_text, "Waybill number is incorrect"

        courier_text = self.get_text(self.courier)
        assert "Courier: Takealot Delivery Team" in courier_text, "Courier information is incorrect"

        self.click(self.parcel_block)

        parcel_order_item_text = self.get_text(self.parcel)
        assert order_item_text == parcel_order_item_text, "Parcel order item text does not match order item text"
        assert "Menggao - Baby Play Mat - Activity Gym & Ball Pit - Toys for Babies" in parcel_order_item_text, "Parcel item description is incorrect"

        return order_item_text, waybill_no_text, courier_text, parcel_order_item_text

    def not_ready_for_collection(self):
        """Verify order not ready for collection message."""
        self.click(self.order_fullfilment_accordion)

        self.wait_for_element_visible(self.order_tracking_heading)
        is_ready_text = self.get_text(self.signed_by)
        assert "Note: We'll send you an SMS or email once your order is ready for collection" in is_ready_text, "Not ready for collection message is missing"

        estimate_collection_date_text = self.get_text(self.estimated_collection_date)
        assert "Estimated Collection from Wed, 4 Dec 2024" in estimate_collection_date_text, "Estimated collection date is incorrect"

        self.click(self.track_btn)

        waybill_collection_text = self.get_text(self.waybill_estimate_collection_date)
        assert "NOT YET READY" in waybill_collection_text, "Waybill collection status is not 'NOT YET READY'"

        return is_ready_text, estimate_collection_date_text, waybill_collection_text

    def verify_refund_history_information(self):
        """Verify refund history information."""
        self.wait_for_element_visible(self.refund_history_accordion)
        self.click(self.refund_history_accordion)

        self.scroll_to_element(self.refund_history_accordion)
        refunded_amount_text = self.get_text(self.refunded_amount)
        assert "R 649.00" in refunded_amount_text, "Refunded amount is incorrect"

        refunded_payment_method_text = self.get_text(self.refunded_payment_method)
        assert "Credit card" in refunded_payment_method_text, "Refunded payment method is incorrect"

        return refunded_amount_text, refunded_payment_method_text

    def verify_delivery_address(self):
        """Verify delivery address information."""
        self.click(self.order_fullfilment_accordion)

        street_text = self.get_text(self.street_address)
        assert "6 Birkenhead Road" in street_text, "Street address is incorrect"

        suburb_text = self.get_text(self.suburb_address)
        assert "Umbilo" in suburb_text, "Suburb is incorrect"

        city_text = self.get_text(self.city_address)
        assert "Berea" in city_text, "City is incorrect"

        province_text = self.get_text(self.province_address)
        assert "KwaZulu-Natal" in province_text, "Province is incorrect"

        code_text = self.get_text(self.code_address)
        assert "4075" in code_text, "Postal code is incorrect"

        self.click(self.copy_address_btn)

        address_copied_text = self.get_text(self.address_copied_btn)
        assert "Address copied!" in address_copied_text, "Address was not copied"

        residential_text = self.get_text(self.residential_txt)
        assert "residential" in residential_text, "Address type is not residential"

        self.click(self.order_fullfilment_accordion)

        return street_text, suburb_text, city_text, province_text, code_text, address_copied_text, residential_text

    def verify_the_google_search(self):
        """Verify Google search functionality."""
        self.wait_for_element_visible(self.search_google_icon)
        self.click(self.search_google_icon)

        self.wait(2)

        # Handle new window - return True instead of switching

        return True

    def verify_order_total_on_canceled_order(self):
        """Verify order total on a canceled order."""
        self.wait_for_element_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)

        order_total_amount_text = self.get_text(self.order_total_amount)
        order_total_amount_text = order_total_amount_text.replace("R ", "")

        assert "439.0" in order_total_amount_text, "Order total amount is incorrect"

        return order_total_amount_text

    def verify_order_total_on_return_item(self):
        """Verify order total on a return item."""
        self.wait_for_element_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)

        order_total_amount_text = self.get_text(self.order_total_amount)
        order_total_amount_text = order_total_amount_text.replace("R ", "")

        assert "2,550.00" in order_total_amount_text, "Order total amount is incorrect"

        return order_total_amount_text

    def verify_shipping_information(self):
        """Verify shipping information."""
        self.click(self.order_fullfilment_accordion)

        method_text = self.get_text(self.shipping_method)
        assert "Courier" in method_text, "Shipping method is incorrect"

        plan_text = self.get_text(self.shipping_plan)
        assert "Standard" in plan_text, "Shipping plan is incorrect"

        courier_text = self.get_text(self.shipping_courier)
        assert "MDX133806010 - Takealot Delivery Team" in courier_text, "Shipping courier is incorrect"

        promised_date_text = self.get_text(self.shipping_promised_date)
        assert "28 Aug 2024" in promised_date_text, "Promised delivery date is incorrect"

        delivered_date_text = self.get_text(self.shipping_delivered_date)
        assert "30 Aug 2024" in delivered_date_text, "Actual delivery date is incorrect"

        return method_text, plan_text, courier_text, promised_date_text, delivered_date_text

    def verify_multiple_waybill_tracking(self):
        """Verify tracking for multiple waybills."""
        self.click(self.order_fullfilment_accordion)
        self.scroll_to_element(self.instruction_dropped_date1)

        self.wait_for_element_visible(self.order_tracking_heading1)
        order_tracking_heading1_txt = self.get_text(self.order_tracking_heading1)
        assert "Delivered Thu, 30 May 2024" in order_tracking_heading1_txt, "First tracking heading is incorrect"

        signed_by_txt = self.get_text(self.signed_by1)
        assert "Signed by: Slindile Mncwango (Customer)" in signed_by_txt, "First signed by information is incorrect"

        waybill_no_txt = self.get_text(self.waybill_number1)
        assert "MDX127668689" in waybill_no_txt, "First waybill number is incorrect"

        instruction_datetime_txt = self.get_text(self.instruction_dropped_date1)
        assert "27 May 2024 @ 17:46" in instruction_datetime_txt, "First instruction datetime is incorrect"

        shipped_datetime_txt = self.get_text(self.shipped_from_warehouse_date1)
        assert "28 May 2024 @ 1:31" in shipped_datetime_txt, "First shipped datetime is incorrect"

        delivered_to_datetime_txt = self.get_text(self.delivered_date1)
        assert "30 May 2024 @ 11:40" in delivered_to_datetime_txt, "First delivery datetime is incorrect"

        self.scroll_to_element(self.instruction_dropped_date2)

        signed_by_txt2 = self.get_text(self.signed_by2)
        assert "Signed by Slindile Mncwango" in signed_by_txt2, "Second signed by information is incorrect"

        waybill_no_txt2 = self.get_text(self.waybill_number2)
        assert "MDX127583371" in waybill_no_txt2, "Second waybill number is incorrect"

        instruction_datetime_txt2 = self.get_text(self.instruction_dropped_date2)
        assert "27 May 2024 @ 0:34" in instruction_datetime_txt2, "Second instruction datetime is incorrect"

        shipped_datetime_txt2 = self.get_text(self.shipped_from_warehouse_date2)
        assert "27 May 2024 @ 17:46" in shipped_datetime_txt2, "Second shipped datetime is incorrect"

        delivered_to_datetime_txt2 = self.get_text(self.delivered_date2)
        assert "29 May 2024 @ 10:58" in delivered_to_datetime_txt2, "Second delivery datetime is incorrect"

        return (
            order_tracking_heading1_txt,
            signed_by_txt,
            waybill_no_txt,
            instruction_datetime_txt,
            shipped_datetime_txt,
            delivered_to_datetime_txt,
            signed_by_txt2,
            waybill_no_txt2,
            instruction_datetime_txt2,
            shipped_datetime_txt2,
            delivered_to_datetime_txt2,
        )

    def verify_waybill_link(self):
        """Verify waybill link functionality."""
        self.click(self.order_fullfilment_accordion)
        self.scroll_to_element(self.waybill_number_link)
        self.click(self.waybill_number_link)

        self.wait(2)

        # Handle new window - return waybill number instead of switching
        waybill_number = self.get_text(self.waybill_number_link)

        return waybill_number

    def verify_order_tracking_for_delivered_physical_products(self):
        """Verify tracking for delivered physical products."""
        self.click(self.order_fullfilment_accordion)

        self.scroll_to_element(self.order_tracking_first_consignment)
        self.wait_for_element_visible(self.first_consigment_delivered_date)

        delivered_datetime_txt = self.get_text(self.first_consigment_delivered_date)
        assert "Delivered Wed, 15 Dec 2021" in delivered_datetime_txt, "Consignment delivery date is incorrect"

        signed_by_txt = self.get_text(self.first_consigment_signed_by)
        assert "Signed by: Trimira Chetty (Customer)" in signed_by_txt, "Consignment signed by information is incorrect"

        waybill_no_txt = self.get_text(self.first_consigment_waybill_number)
        assert "MDX69461955" in waybill_no_txt, "Consignment waybill number is incorrect"

        return delivered_datetime_txt, signed_by_txt, waybill_no_txt

    def verify_partial_order_delivery(self):
        """Verify partial order delivery information."""
        item_status_delivered = self.get_text(self.delivered_tag)
        assert "Delivered" in item_status_delivered, "First item status is not Delivered"

        item_status_cancelled = self.get_text(self.cancelled_tag)
        assert "Canceled" in item_status_cancelled, "Second item status is not Canceled"

        self.click(self.order_fullfilment_accordion)
        self.scroll_to_element(self.signed_by1)

        order_tracking_heading_txt = self.get_text(self.part_delivered_date)
        assert "Delivered Mon, 19 Sep 2022" in order_tracking_heading_txt, "Partial delivery date is incorrect"

        signed_by_txt = self.get_text(self.signed_by1)
        assert "Signed by: Slindile Mncwango (Customer)" in signed_by_txt, "Signed by information is incorrect"

        self.scroll_to_element(self.cancelled_items)

        cancelled_items_txt = self.get_text(self.cancelled_items)
        assert "Cancelled Item(s)" in cancelled_items_txt, "Cancelled items section is missing"

        return item_status_delivered, item_status_cancelled, order_tracking_heading_txt, signed_by_txt, cancelled_items_txt

    def verify_ip_address(self):
        """Verify IP address information."""
        self.click(self.ip_address_icon)
        self.wait_for_element_visible(self.ip_address_model)

        ip_address_txt = self.get_value(self.ip_address)
        assert "41.115.115.60" in ip_address_txt, "IP address is incorrect"

        return ip_address_txt

    def hover_over_customer_id(self):
        """Hover over customer ID to show customer information."""
        self.wait_for_element_visible(self.cust_acc_number)
        self.hover(self.cust_acc_number)

        self.wait_for_element_visible(self.cust_info_popup)

        return True

    def verify_customer_info(self):
        """Verify customer information in popup."""
        cust_name_popup_txt = self.get_text(self.cust_name_popup)
        assert "Slindile Mncwango" in cust_name_popup_txt, "Customer name is incorrect"

        cust_date_registered_txt = self.get_text(self.cust_date_registered)
        assert "16-Oct-2018 @ 10:41" in cust_date_registered_txt, "Customer registration date is incorrect"

        cust_blacklist_status_check = self.get_text(self.cust_blacklist_status)
        assert "Not Blacklisted" in cust_blacklist_status_check, "Customer blacklist status is incorrect"

        return cust_name_popup_txt, cust_date_registered_txt, cust_blacklist_status_check

    def verify_order_shipping_info(self):
        """Verify order shipping tracking information."""
        self.click(self.order_fullfilment_accordion)
        self.scroll_to_element(self.order_tracking_first_consignment)

        self.wait_for_element_visible(self.first_consigment_track_btn)
        self.click(self.first_consigment_track_btn)

        self.wait(2)

        tracking_waybill_number_txt = self.get_text(self.tracking_waybill_number)
        assert "MDX144323298" in tracking_waybill_number_txt, "Tracking waybill number is incorrect"

        self.click(self.tracking_first_parcel_info)

        tracking_first_parcel_number_txt = self.get_text(self.tracking_first_parcel_number)
        assert "Parcel - S057933520" in tracking_first_parcel_number_txt, "Parcel number is incorrect"

        tracking_first_parcel_item_txt = self.get_text(self.tracking_first_parcel_item)
        assert "1 × Flaming Thai Sauces - 4 Asian Flavour Mixed Pack" in tracking_first_parcel_item_txt, "Parcel item description is incorrect"

        return tracking_waybill_number_txt, tracking_first_parcel_number_txt, tracking_first_parcel_item_txt

    def verify_collection_not_yet_ready(self):
        """Verify collection not yet ready message."""
        self.wait_for_element_visible(self.order_fullfilment_accordion)
        self.click(self.order_fullfilment_accordion)

        collection_estimate_date_text = self.get_text(self.collection_estimate_date)
        assert "Estimated Collection from" in collection_estimate_date_text, "Collection estimate date is incorrect"

        collection_not_yet_ready_message_text = self.get_text(self.collection_not_yet_ready_message)
        assert "NOT YET READY" in collection_not_yet_ready_message_text, "Collection not yet ready message is incorrect"

        return collection_estimate_date_text, collection_not_yet_ready_message_text

    def verify_delivery_not_yet_shipped(self):
        """Verify delivery not yet shipped message."""
        self.wait_for_element_visible(self.order_fullfilment_accordion)
        self.click(self.order_fullfilment_accordion)

        delivery_estimate_date_text = self.get_text(self.delivery_estimate_date)
        assert "Delivery by ------" in delivery_estimate_date_text, "Delivery estimate date is incorrect"

        delivery_not_yet_ready_message_text = self.get_text(self.delivery_not_yet_ready_message)
        assert "NOT YET SHIPPED" in delivery_not_yet_ready_message_text, "Delivery not yet shipped message is incorrect"

        return delivery_estimate_date_text, delivery_not_yet_ready_message_text
