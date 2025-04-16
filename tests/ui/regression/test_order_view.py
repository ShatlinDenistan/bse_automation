"""
Tests for Order View functionality in the Financial Portal.
This file contains tests converted from Robot Framework tests in Fin-Portal_Order_View.robot.
"""

import pytest
from base.test_base import TestBase


class TestOrderView(TestBase):
    """Test class for Order View functionality in the Financial Portal."""

    @pytest.mark.QABSE_242
    def test_add_note(self):
        """Verify that a user can add a note on the order view page."""
        self.search_page.search_for_order("126388782")
        self.order_view_page.add_admin_notes()

    @pytest.mark.QABSE_235
    def test_blacklist_and_whitelist_customer(self):
        """Verify that a user can update the blacklist status on the order view page."""
        self.search_page.search_for_order("126388782")
        self.order_view_page.update_to_blacklist()
        self.order_view_page.update_to_whitelist()

    @pytest.mark.QABSE_131
    def test_cancel_order(self):
        """Verify that a user can cancel an order."""
        self.database.get_orders_from_database(self.database.new_order_with_no_discount_amount_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.cancel_all_order_items()

    @pytest.mark.QABSE_234
    def test_send_email(self):
        """Verify that a user can send an email to the customer on the order view page."""
        self.database.get_orders_from_database(self.database.new_order_with_no_discount_amount_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.send_an_email()

    @pytest.mark.QABSE_231
    def test_mark_order_as_risky(self):
        """Verify that a user can mark an order as risky on the order view page."""
        self.database.get_orders_from_database(self.database.non_risky_order_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.mark_order_as_risky()
        self.order_view_page.verify_audit_log_entry("mark_order_as_risky")

    @pytest.mark.QABSE_132
    def test_authorize_order(self):
        """Verify that a user can manually authorize an order."""
        self.database.get_orders_from_database(self.database.new_order_with_no_discount_and_shipping_amount_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.manually_authorize_order()
        self.order_view_page.verify_audit_log_entry("authorise_order")

    @pytest.mark.QABSE_853
    def test_no_order_tracking_for_digital_items(self):
        """Verify that there is no tracking information for a digital items only order."""
        self.search_page.search_for_order("145423528")
        self.order_view_page.verify_order_tracking_for_digital_products()

    @pytest.mark.QABSE_857
    def test_no_order_tracking_for_cancelled_order(self):
        """Verify that there is no tracking information for a cancelled order."""
        self.database.get_orders_from_database(self.database.new_order_with_no_discount_amount_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.cancel_all_order_items()
        self.order_view_page.verify_order_tracking_heading("Cancelled Item(s)")

    @pytest.mark.QABSE_210
    def test_edit_customer_details(self):
        """Verify that a user can edit customer information on the order view page."""
        self.search_page.search_for_order("162699008")
        self.order_view_page.edit_customer_details()

    @pytest.mark.QABSE_134
    def test_view_order_events(self):
        """Verify that the order events can be viewed on the order view page."""
        self.database.get_orders_from_database(self.database.paygate_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.view_order_events()

    @pytest.mark.QABSE_825
    def test_multiple_payment_methods_badges(self):
        """Verify that we display all payment method badges for a part paid order."""
        self.database.get_orders_from_database(self.database.part_payment_order_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.verify_part_payment_methods_badges()

    @pytest.mark.QABSE_233
    def test_add_notes(self):
        """Verify that a user can add order, customer and fin notes on the order view page."""
        self.database.get_orders_from_database(self.database.new_order_with_no_discount_amount_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.add_order_notes()
        self.order_view_page.add_customer_notes()
        self.order_view_page.add_fin_notes()

    @pytest.mark.QABSE_228
    def test_cancel_order_item(self):
        """Verify that a user can cancel an order item."""
        self.database.get_orders_from_database(self.database.order_with_more_order_items_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.cancel_an_order_item()

    @pytest.mark.QABSE_244
    def test_view_payment_ledger(self):
        """Verify that a user can view Payment Ledger information."""
        self.search_page.search_for_order("162110009")
        self.order_view_page.view_payment_ledger()

    @pytest.mark.QABSE_135
    def test_bookmarks_page(self):
        """Verify that a user can bookmark an order and remove bookmarks."""
        self.search_page.search_for_order("126388782")
        self.order_view_page.bookmark_an_order()
        self.order_view_page.remove_bookmarks()

    @pytest.mark.QABSE_96
    def test_order_financials_breakdown(self):
        """Verify that a user can view order financials information."""
        self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.verify_order_financials()

    @pytest.mark.QABSE_239
    def test_view_order_audit_logs(self):
        """Verify that a user can view the order audit logs on the order view page."""
        self.search_page.search_for_order("145480196")
        self.order_view_page.view_order_audit_logs()

    @pytest.mark.QABSE_245
    def test_view_address(self):
        """Verify that a user can view the address on Google maps."""
        self.search_page.search_for_order("145480196")
        self.order_view_page.view_address()

    @pytest.mark.QABSE_246
    def test_view_order(self):
        """Verify the order information is displayed on the order view page."""
        self.search_page.search_for_order("145423528")
        self.order_view_page.verify_order_details("145423528")

    @pytest.mark.QABSE_227
    def test_view_rrn(self):
        """Verify that the user can view the RRN details."""
        self.search_page.search_for_order("163732899")
        pages = self.order_view_page.get_rrn_details()
        self.top_nav.login_cs_admin()
        self.search_page.search_for_rrn("RRN-T6QRV-9K4W")

    @pytest.mark.QABSE_230
    def test_update_order_item_status(self):
        """Verify that the user can edit an order item status."""
        self.database.get_orders_from_database(self.database.order_with_returned_canceled_order_item_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.update_order_item_to_shipped()

    @pytest.mark.QABSE_97
    def test_view_payment_ledger_logs(self):
        """Verify that a user can view payment ledger."""
        self.database.get_orders_from_database(self.database.payflex_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.verify_payment_ledger_logs()

    @pytest.mark.QABSE_238
    def test_view_email_logs(self):
        """Verify that a user can view email logs."""
        self.search_page.search_for_order("163732899")
        self.order_view_page.send_an_email()
        self.order_view_page.view_email_logs()

    @pytest.mark.QABSE_99
    def test_view_order_items_status(self):
        """Verify that a user can view order item information."""
        self.database.get_orders_from_database(self.database.auto_canceled_orders_sql)
        self.search_page.search_for_order(self.database.order_ids)
        self.order_view_page.view_order_items_information()

    @pytest.mark.QABSE_99
    def test_verify_order_items_pagination(self):
        """Verify order items accordion pagination."""
        self.search_page.search_for_order("165251543")
        self.order_view_page.verify_show_items_and_pagination()

    @pytest.mark.QABSE_24
    def test_view_coupon_history(self):
        """Verify that a user can view coupon history on the order page."""
        self.search_page.search_for_order("148935094")
        self.order_view_page.view_coupon_history()

    @pytest.mark.QABSE_874
    def test_verify_order_tracking_information(self):
        """Verify that the delivery order is delivered and all waybill tracking information displays."""
        self.search_page.search_for_order("159445954")
        self.order_view_page.verify_delivery_tracking_information("Delivered Fri, 30 Aug 2024")
        self.order_view_page.verify_waybill_tracking()

    @pytest.mark.QABSE_873
    def test_verify_order_not_ready_for_collection(self):
        """Verify that the order is not ready for collection and no waybill tracking information displays."""
        self.search_page.search_for_order("166825424")
        self.order_view_page.verify_collection_not_yet_ready()

    @pytest.mark.QABSE_957
    def test_verify_refund_history_information(self):
        """Verify refund history information."""
        self.search_page.search_for_order("154899984")
        self.order_view_page.verify_refund_history_information()

    @pytest.mark.QABSE_98
    def test_verify_delivery_address(self):
        """Verify the order delivery address."""
        self.search_page.search_for_order("163732899")
        self.order_view_page.verify_delivery_address()

    @pytest.mark.QABSE_237
    def test_verify_customer_google_search(self):
        """Verify the google search of the customer."""
        self.search_page.search_for_order("163732899")
        self.order_view_page.verify_the_google_search()

    @pytest.mark.QABSE_237
    def test_verify_canceled_order(self):
        """Verify the order total on canceled orders."""
        self.search_page.search_for_order("148158095")
        self.order_view_page.verify_order_total_on_canceled_order()

    @pytest.mark.QABSE_782
    def test_verify_return_order_total_calculation(self):
        """Verify Return Order Total Calculation."""
        self.search_page.search_for_order("160199453")
        self.order_view_page.verify_order_total_on_return_item()

    @pytest.mark.QABSE_241
    def test_verify_delivery_information(self):
        """Verify that the user is able to view the delivery information."""
        self.search_page.search_for_order("159445954")
        self.order_view_page.verify_delivery_tracking_information("Delivered Fri, 30 Aug 2024")
        self.order_view_page.verify_delivery_address()
        self.order_view_page.verify_shipping_information()

    @pytest.mark.QABSE_875
    def test_verify_multiple_waybill_information(self):
        """Verify that the delivery order with multiple waybills is delivered and all waybill tracking information displays."""
        self.search_page.search_for_order("153301924")
        self.order_view_page.verify_multiple_waybill_tracking()

    @pytest.mark.QABSE_855
    def test_verify_waybill_link(self):
        """Verify that when the user clicks the waybill number link, the user is redirected to the mrdexpress page."""
        self.search_page.search_for_order("159445954")
        self.order_view_page.verify_waybill_link()

    @pytest.mark.QABSE_854
    def test_verify_order_tracking_for_physical_products(self):
        """Verify tracking information displays for physical products that have been delivered."""
        self.search_page.search_for_order("98278540")
        self.order_view_page.verify_order_tracking_for_delivered_physical_products()

    @pytest.mark.QABSE_682
    def test_verify_order_information_for_part_delivered_order(self):
        """Verify that the delivery order includes delivery details for the part of the order that has already been delivered."""
        self.search_page.search_for_order("112799490")
        self.order_view_page.verify_partial_order_delivery()

    @pytest.mark.QABSE_243
    def test_verify_ip_address(self):
        """Verify that a user is able to check the IP Address."""
        self.search_page.search_for_order("112799490")
        self.order_view_page.verify_ip_address()

    @pytest.mark.QABSE_221
    def test_quick_customer_view(self):
        """Verify that hovering over the CustomerID displays a small popup with basic customer information."""
        self.search_page.search_for_order("112799490")
        self.order_view_page.hover_over_customer_id()
        self.order_view_page.verify_customer_info()

    @pytest.mark.QABSE_852
    def test_verify_order_shipping_information(self):
        """Verify order shipping information on the waybill tracking modal."""
        self.search_page.search_for_order("169820566")
        self.order_view_page.verify_order_shipping_info()

    @pytest.mark.QABSE_871
    def test_verify_order_not_yet_ready_collected(self):
        """Verify order that is not yet ready for collection."""
        self.order_list_page.navigate_to_order_list_page()
        self.order_list_page.filter_by_collect_shipping_method_and_daily_deals()
        self.order_view_page.verify_collection_not_yet_ready()

    @pytest.mark.QABSE_873
    def test_verify_order_not_yet_ready_for_delivery(self):
        """Verify order that is not yet ready for delivery."""
        self.order_list_page.navigate_to_order_list_page()
        self.order_list_page.filter_by_courier_shipping_method_and_daily_deals()
        self.order_view_page.verify_delivery_not_yet_shipped()
