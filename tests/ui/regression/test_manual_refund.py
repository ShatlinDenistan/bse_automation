"""
Manual Refund Test Suite.
Tests for the Manual Refund functionality in Fin-Portal.
"""

import pytest
from base.test_base import TestBase


class TestManualRefund(TestBase):
    """Test class for Manual Refund functionality"""

    @pytest.mark.regression
    @pytest.mark.QABA_478
    def test_paygate_credit_card_refund(self):
        """
        Test manual refunds processing for Credit Card (Paygate) payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.paygate_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Submit refund request
        self.step("Click the refund button and submit refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for order again
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Verify refund details
        self.step("Click the view refund log button and verify details")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.regression
    @pytest.mark.QABA_477
    def test_payfast_instant_eft_refund(self):
        """
        Test manual refunds processing for Instant EFT PayFast payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.payfast_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Submit refund request
        self.step("Click the refund button and submit refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for order again
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Verify refund details
        self.step("Click the view refund log button and verify details")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("PayFast")

    @pytest.mark.regression
    @pytest.mark.QABA_466
    def test_cash_on_delivery_refund(self):
        """
        Test manual refunds processing for Cash On Delivery payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.cash_on_del_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Verify that order is not eligible for manual refund
        self.step("Verify that order is not eligible for manual refund")
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(self.database.order_ids)

    @pytest.mark.regression
    @pytest.mark.QABA_462
    def test_discovery_miles_refund(self):
        """
        Test manual refunds processing for Discovery Miles payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.discovery_miles_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Submit refund request
        self.step("Click the refund button and submit refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for order again
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Verify refund details
        self.step("Click the view refund log button and verify details")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Discovery Miles")

    @pytest.mark.regression
    @pytest.mark.QABA_461
    def test_ebucks_refund(self):
        """
        Test manual refunds processing for eBucks payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.ebucks_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Submit refund request
        self.step("Click the refund button and submit refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for order again
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Verify refund details
        self.step("Click the view refund log button and verify details")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("eBucks")

    @pytest.mark.regression
    @pytest.mark.QABA_456
    def test_staggered_credit_card_refunds(self):
        """
        Test manual refunds processing for staggered credit card refunds.
        """
        # Create new TAL orders
        self.step("Create new TAL orders")
        self.database.create_new_tal_orders("2420369", "Credit Card")

        # Cancel first order item
        self.step("Cancel order item")
        self.cancel_order.cancel_order_item(self.database.id_order_item1[0])

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Submit refund request
        self.step("Click the refund button and submit refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Cancel second order item
        self.step("Cancel second order item")
        self.cancel_order.cancel_order_item(self.database.id_order_item2[0])

        # Search for order again
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Verify refund details
        self.step("Click the view refund log button and verify details")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.regression
    @pytest.mark.QABA_455
    def test_payflex_refund(self):
        """
        Test manual refunds processing for Payflex payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.payflex_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Verify that refund is not available
        self.step("Verify that refund is not available")
        self.manual_refund_page.verify_that_refund_not_available(self.database.order_ids)

        # Search for order again
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Verify refund details
        self.step("Click the view refund log button and verify details")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Payflex")

    @pytest.mark.regression
    @pytest.mark.QABA_465
    def test_takealot_credit_refund(self):
        """
        Test manual refunds processing for Takealot Credit payment method.
        """
        # Get orders from database
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.tal_credit_sql)

        # Cancel paid order
        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        # Search for order
        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        # Expand customer credit accordion
        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        # Navigate to refund page and click refund
        self.step("Expand the order items accordion and click refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(self.database.order_ids)

        # Verify that order is not eligible for manual refund
        self.step("Verify that order is not eligible for manual refund")
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(self.database.order_ids)
