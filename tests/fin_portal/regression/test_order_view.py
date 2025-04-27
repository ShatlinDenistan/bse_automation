import pytest
from base.test_base import TestBase


class TestOrderView(TestBase):
    """Test cases for Order View functionality."""

    @pytest.mark.regression
    @pytest.mark.qabse_242
    def test_add_admin_notes(self):
        """Verify that a user can add a note on the order view page."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("126388782")

        self.step("Add admin notes")
        note_message = self.order_view_page.add_admin_notes()
        assert "Note successfully added to Customer:" in note_message

    @pytest.mark.regression
    @pytest.mark.qabse_235
    def test_blacklist_and_whitelist_customer(self):
        """Verify that a user can update the blacklist status on the order view page."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("126388782")

        self.step("Update customer to blacklist")
        blacklist_message = self.order_view_page.update_to_blacklist()
        assert "Successfully blacklisted the customer" in blacklist_message

        self.step("Update customer to whitelist")
        whitelist_message = self.order_view_page.update_to_whitelist()
        assert "Successfully Whitelisted Customer:" in whitelist_message

    @pytest.mark.regression
    @pytest.mark.qabse_131
    def test_cancel_order(self):
        """Verify that a user can cancel an order."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("new_order_with_no_discount_amount.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Cancel all order items")
        order_status = self.order_view_page.cancel_all_order_items()
        assert "Canceled by" in order_status

    @pytest.mark.regression
    @pytest.mark.qabse_234
    def test_send_email(self):
        """Verify that a user can send an email to the customer on the order view page."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("new_order_with_no_discount_amount.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Send email to customer")
        email_message = self.order_view_page.send_an_email()
        assert "(Identification Not Accepted) email sent to customer" in email_message

    @pytest.mark.regression
    @pytest.mark.qabse_231
    def test_mark_order_as_risky(self):
        """Verify that a user can mark an order as risky on the order view page."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("non_risky_order.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Mark order as risky")
        risk_text = self.order_view_page.mark_order_as_risky()
        assert "Flagged as risky" in risk_text

        self.step("Verify audit log entry")
        audit_text = self.order_view_page.verify_audit_log_entry("mark_order_as_risky")
        assert "mark_order_as_risky" in audit_text

    @pytest.mark.regression
    @pytest.mark.qabse_132
    def test_authorize_order(self):
        """Verify that a user can manually authorize an order."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("new_order_with_no_discount__and_shipping_amount.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Manually authorize order")
        success_message = self.order_view_page.manually_authorize_an_order()
        assert "Successfully processed 1 item(s)" in success_message

        self.step("Verify audit log entry")
        audit_text = self.order_view_page.verify_audit_log_entry("authorise_order")
        assert "authorise_order" in audit_text

    @pytest.mark.regression
    @pytest.mark.qabse_853
    def test_no_tracking_for_digital_items_order(self):
        """Verify that there is no tracking information for a digital items only order."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("145423528")

        self.step("Verify order tracking for digital products")
        tracking_info = self.order_view_page.verify_order_tracking_for_digital_products_only_order()
        assert "Digital Product(s)" in tracking_info

    @pytest.mark.regression
    @pytest.mark.qabse_857
    def test_no_tracking_for_cancelled_order(self):
        """Verify that there is no tracking information for a cancelled order."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("new_order_with_no_discount_amount.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Cancel all order items")
        self.order_view_page.cancel_all_order_items()

        self.step("Verify order tracking heading")
        heading = self.order_view_page.verify_order_tracking_heading("Cancelled Item(s)")
        assert "Cancelled Item(s)" in heading

    @pytest.mark.regression
    @pytest.mark.qabse_210
    def test_edit_customer_details(self):
        """Verify that a user can edit customer information on the order view page."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("162699008")

        self.step("Edit customer details")
        update_message = self.order_view_page.edit_customer_details()
        assert "Customer status data updated successfully" in update_message

    @pytest.mark.regression
    @pytest.mark.qabse_134
    def test_view_order_events(self):
        """Verify that the order events can be viewed on the order view page."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("paygate_sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("View order events")
        result = self.order_view_page.view_order_events()
        assert result is True

    @pytest.mark.regression
    @pytest.mark.qabse_825
    def test_multiple_payment_methods_badges(self):
        """Verify that we display all payment method badges for a part paid order."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("part_payment_order.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Verify part payment methods badges")
        badges = self.order_view_page.verify_part_payment_methods_badges()
        assert len(badges) > 1

    @pytest.mark.regression
    @pytest.mark.qabse_233
    def test_add_notes(self):
        """Verify that a user can add order, customer and fin notes on the order view page."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("new_order_with_no_discount_amount.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Add order notes")
        order_note = self.order_view_page.add_order_notes()
        assert "Note successfully added to Order" in order_note

        self.step("Add customer notes")
        customer_note = self.order_view_page.add_customer_notes()
        assert "Note successfully added to Customer" in customer_note

        self.step("Add fin notes")
        fin_note = self.order_view_page.add_fin_notes()
        assert "Note successfully added to Customer" in fin_note

    @pytest.mark.regression
    @pytest.mark.qabse_228
    def test_cancel_order_item(self):
        """Verify that a user can cancel an order item."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("order_with_more_order_items.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Cancel an order item")
        cancel_message = self.order_view_page.cancel_an_order_item()
        assert "Orderitem has successfully been cancelled" in cancel_message

    @pytest.mark.regression
    @pytest.mark.qabse_244
    def test_view_payment_ledger(self):
        """Verify that a user can view Payment Ledger information."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("162110009")

        self.step("View payment ledger")
        ledger_info = self.order_view_page.view_payment_ledger()
        assert ledger_info is not None

    @pytest.mark.regression
    @pytest.mark.qabse_135
    def test_bookmarks_page(self):
        """Verify that a user can bookmark an order and remove bookmarks."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("126388782")

        self.step("Bookmark an order")
        bookmark_count = self.order_view_page.bookmark_an_order()
        assert bookmark_count != "0"

        self.step("Remove bookmarks")
        message = self.order_view_page.remove_bookmarks()
        assert "No bookmarks to show here" in message

    @pytest.mark.regression
    @pytest.mark.qabse_96
    def test_order_financials_breakdown(self):
        """Verify that a user can view order financials information."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Verify order financials")
        financials = self.order_view_page.verify_order_financials()
        assert financials is not None

    @pytest.mark.regression
    @pytest.mark.qabse_239
    def test_view_order_audit_logs(self):
        """Verify that a user can view the order audit logs on the order view page."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("145480196")

        self.step("View order audit logs")
        logs = self.order_view_page.view_order_audit_logs()
        assert logs is not None

    @pytest.mark.regression
    @pytest.mark.qabse_245
    def test_view_address(self):
        """Verify that a user can view the address on Google maps."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("145480196")

        self.step("View address")
        result = self.order_view_page.view_address()
        assert result is True

    @pytest.mark.regression
    @pytest.mark.qabse_246
    def test_view_order(self):
        """Verify the order information is displayed on the order view page."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("145423528")

        self.step("Verify order details")
        details = self.order_view_page.verify_order_details("145423528")
        assert details is not None

    @pytest.mark.regression
    @pytest.mark.qabse_227
    def test_view_rrn(self):
        """Verify that the user can view the RRN details."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("163732899")

        self.step("Get RRN details")
        rrn = self.order_view_page.get_rrn_details()
        assert rrn is not None

        self.step("Login to CS-Admin and verify RRN details")
        # This step might need special handling or mocking as it involves switching applications
        rrn_details = self.cs_admin.verify_rrn_details("RRN-T6QRV-9K4W")
        assert rrn_details is not None

    @pytest.mark.regression
    @pytest.mark.qabse_230
    def test_update_order_item_status(self):
        """Verify that the user can edit an order item status."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("order_with_returned_canceled_order_item.sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Update order item to shipped")
        status = self.order_view_page.update_order_item_to_shipped()
        assert "Shipped" in status

    @pytest.mark.regression
    @pytest.mark.qabse_97
    def test_view_payment_ledger_logs(self):
        """Verify that a user can view payment ledger logs."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("payflex_sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("Verify payment ledger logs")
        logs = self.order_view_page.verify_payment_ledger_logs()
        assert "Payflex" in logs

    @pytest.mark.regression
    @pytest.mark.qabse_238
    def test_view_email_logs(self):
        """Verify that a user can view email logs."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("163732899")

        self.step("Send an email and view email logs")
        self.order_view_page.send_an_email()
        logs = self.order_view_page.view_email_logs()
        assert logs is not None

    @pytest.mark.regression
    @pytest.mark.qabse_99
    def test_view_order_items_status(self):
        """Verify that a user can view order item information."""
        self.step("Get orders from database")
        order_id = self.order_data.get_orders("auto_canceled_orders_sql")[0]

        self.step("Navigate to the order view page")
        self.top_nav.search_for_order(order_id)

        self.step("View order items information")
        status, canceled_by = self.order_view_page.view_order_items_information()
        assert status == "Canceled"
        assert canceled_by == "auto_cancel"

    @pytest.mark.regression
    @pytest.mark.qabse_99
    def test_verify_order_items_pagination(self):
        """Verify order items accordion pagination."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("165251543")

        self.step("Verify show items and pagination")
        result = self.order_view_page.verify_show_items_and_pagination()
        assert result is True

    @pytest.mark.regression
    @pytest.mark.qabse_24
    def test_view_coupon_history(self):
        """Verify that a user can view coupon history on the order page."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("148935094")

        self.step("View coupon history")
        is_coupon_visible = self.order_view_page.view_coupon_history()
        assert is_coupon_visible is True

    @pytest.mark.regression
    @pytest.mark.qabse_874
    def test_verify_order_tracking_information(self):
        """Verify that the delivery order is delivered and all waybill tracking information displays."""
        self.step("Navigate to the order view page")
        self.top_nav.search_for_order("159445954")

        self.step("Verify delivery tracking information")
        tracking_info = self.order_view_page.verify_delivery_tracking_information("Delivered Fri, 30 Aug 2024")
        assert "Delivered" in tracking_info

        self.step("Verify waybill tracking")
        waybill_info = self.order_view_page.verify_waybill_tracking()
        assert waybill_info is not None

    @pytest.mark.regression
    @pytest.mark.qabse_873
    def test_verify_order_not_yet_ready_collected(self):
        """Verify order that is not yet ready for collection."""
        self.step("Navigate to OrderList Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter by collect shipping method and daily deals")
        self.order_list_page.filter_by_collect_shipping_method_and_daily_deals()

        self.step("Verify collection not yet ready")
        status = self.order_list_page.verify_collection_not_yet_ready()
        assert "NOT YET READY" in status

    @pytest.mark.regression
    @pytest.mark.qabse_873
    def test_verify_order_not_yet_ready_for_delivery(self):
        """Verify order that is not yet ready for delivery."""
        self.step("Navigate to OrderList Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter by courier shipping method and daily deals")
        self.order_list_page.filter_by_courier_shipping_method_and_daily_deals()

        self.step("Verify delivery not yet shipped")
        status = self.order_list_page.verify_delivery_not_yet_shipped()
        assert "NOT YET SHIPPED" in status
