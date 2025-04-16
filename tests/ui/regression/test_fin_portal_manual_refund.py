import pytest
from base.test_base import TestBase


class TestFinPortalManualRefund(TestBase):
    """Test suite for Fin-Portal Manual Refunds functionality."""

    @pytest.mark.qaba_478
    def test_manual_refund_processing_credit_card_paygate(self):
        """
        Test manual refund processing for Credit Card payments via PayGate.

        Steps:
        1. Get orders from database with PayGate SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Submit refund request
        7. Verify refund log details
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${paygate_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Click refund button and submit refund request
        date_time = self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for the order again to verify refund
        self.search_page.search_for_order(self.database.order_ids[0])

        # Verify refund log details
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_477
    def test_manual_refund_processing_instant_eft_payfast(self):
        """
        Test manual refund processing for Instant EFT via PayFast.

        Steps:
        1. Get orders from database with PayFast SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Submit refund request
        7. Verify refund log details
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${payfast_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Click refund button and submit refund request
        date_time = self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for the order again to verify refund
        self.search_page.search_for_order(self.database.order_ids[0])

        # Verify refund log details
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("PayFast")

    @pytest.mark.qaba_466
    def test_manual_refund_processing_cash_on_delivery(self):
        """
        Test that manual refund cannot be processed for Cash on Delivery payments.

        Steps:
        1. Get orders from database with Cash on Delivery SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Verify that the order is not eligible for manual refund
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${cash_on_del_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Verify that order is not eligible for manual refund
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(self.database.order_ids[0])

    @pytest.mark.qaba_462
    def test_manual_refund_processing_discovery_miles(self):
        """
        Test manual refund processing for Discovery Miles payments.

        Steps:
        1. Get orders from database with Discovery Miles SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Submit refund request
        7. Verify refund log details
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${discovery_miles_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Click refund button and submit refund request
        date_time = self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for the order again to verify refund
        self.search_page.search_for_order(self.database.order_ids[0])

        # Verify refund log details
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Discovery Miles")

    @pytest.mark.qaba_461
    def test_manual_refund_processing_ebucks(self):
        """
        Test manual refund processing for eBucks payments.

        Steps:
        1. Get orders from database with eBucks SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Submit refund request
        7. Verify refund log details
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${ebucks_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Click refund button and submit refund request
        date_time = self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Search for the order again to verify refund
        self.search_page.search_for_order(self.database.order_ids[0])

        # Verify refund log details
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("eBucks")

    @pytest.mark.qaba_456
    def test_manual_refund_processing_staggered_credit_card_refunds(self):
        """
        Test manual refund processing for staggered Credit Card refunds.

        Steps:
        1. Create new TAL orders with Credit Card
        2. Cancel first order item
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Submit refund request
        7. Cancel second order item
        8. Search for the order again
        9. Verify refund log details
        """
        # Create new TAL orders and cancel first order item
        self.database.create_new_tal_orders("${2420369}", "Credit Card")
        self.database.cancel_order_item(self.database.id_order_item1[0])

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Click refund button and submit refund request
        date_time = self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        # Cancel second order item
        self.database.cancel_order_item(self.database.id_order_item2[0])

        # Search for the order again
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion and verify refund log details
        self.customer_credit_page.expand_customer_credit_accordion()
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_455
    def test_manual_refund_processing_payflex(self):
        """
        Test manual refund processing for Payflex payments.

        Steps:
        1. Get orders from database with Payflex SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Verify that refund is not available
        7. Search for the order again
        8. Verify refund log details
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${payflex_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Verify that refund is not available
        self.manual_refund_page.verify_that_refund_not_available(self.database.order_ids[0])

        # Search for the order again
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion and verify refund log details
        self.customer_credit_page.expand_customer_credit_accordion()
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Payflex")

    @pytest.mark.qaba_465
    def test_manual_refund_processing_takealot_credit(self):
        """
        Test that manual refund cannot be processed for Takealot Credit payments.

        Steps:
        1. Get orders from database with Takealot Credit SQL
        2. Cancel a paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items and click refund
        6. Verify that the order is not eligible for manual refund
        """
        # Get orders from database and cancel a paid order
        self.database.get_orders_from_database("${tal_credit_sql}")
        self.database.cancel_paid_order()

        # Search for the order
        self.search_page.search_for_order(self.database.order_ids[0])

        # Expand customer credit accordion
        self.customer_credit_page.expand_customer_credit_accordion()

        # Expand order items and click refund
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        # Verify that order is not eligible for manual refund
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(self.database.order_ids[0])
