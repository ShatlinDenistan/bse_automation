import pytest
from base.test_base import TestBase


class TestManualRefund(TestBase):
    """Test class for Manual Refund functionality"""

    @pytest.mark.qaba_478
    def test_processing_refund_credit_card_paygate(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Credit Card | PayGate"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${paygate_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Click the refund button and submit refund request")
        refund_date_time = self.manual_refund_page.click_refund_button_and_submit_request()

        self.step("Search for order again")
        self.top_nav.search_for_order(order_id)

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_and_verify_details("Paygate")

    @pytest.mark.qaba_477
    def test_processing_refund_instant_eft_payfast(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Instant EFT PayFast"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${payfast_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Click the refund button and submit refund request")
        refund_date_time = self.manual_refund_page.click_refund_button_and_submit_request()

        self.step("Search for order again")
        self.top_nav.search_for_order(order_id)

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_and_verify_details("PayFast")

    @pytest.mark.qaba_466
    def test_processing_refund_cash_on_delivery(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Cash On Delivery"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${cash_on_del_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Verify that order is NOT eligible for manual refund")
        self.manual_refund_page.verify_order_not_eligible_for_manual_refund(order_id)

    @pytest.mark.qaba_462
    def test_processing_refund_discovery_miles(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Discovery Miles"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${discovery_miles_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Click the refund button and submit refund request")
        refund_date_time = self.manual_refund_page.click_refund_button_and_submit_request()

        self.step("Search for order again")
        self.top_nav.search_for_order(order_id)

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_and_verify_details("Discovery Miles")

    @pytest.mark.qaba_461
    def test_processing_refund_ebucks(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | eBucks"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${ebucks_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Click the refund button and submit refund request")
        refund_date_time = self.manual_refund_page.click_refund_button_and_submit_request()

        self.step("Search for order again")
        self.top_nav.search_for_order(order_id)

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_and_verify_details("eBucks")

    @pytest.mark.qaba_456
    def test_staggered_credit_card_refunds(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Staggered Credit Card Refunds"""

        self.step("Create new TAL orders")
        order_data = self.order_data.create_order("${2420369}", "Credit Card")
        order_id = order_data["order_ids"][0]

        self.step("Cancel order item")
        self.cancel_order_items.cancel_order_item(order_data["id_order_item1"][0])

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Click the refund button and submit refund request")
        refund_date_time = self.manual_refund_page.click_refund_button_and_submit_request()

        self.step("Cancel second order item")
        self.cancel_order_items.cancel_order_item(order_data["id_order_item2"][0])

        self.step("Search for order again")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_and_verify_details("Paygate")

    @pytest.mark.qaba_455
    def test_processing_refund_payflex(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Payflex"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${payflex_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Verify that refund is not available")
        self.manual_refund_page.verify_refund_not_available(order_id)

        self.step("Search for order again")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_and_verify_details("Payflex")

    @pytest.mark.qaba_465
    def test_processing_refund_takealot_credit(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Takealot Credit"""

        self.step("Get orders from database")
        orders = self.order_data.get_orders("${tal_credit_sql}")
        order_id = orders[0]

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order(order_id)

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Navigate to refund page and expand order items")
        self.manual_refund_page.navigate_to_refund_page(order_id)

        self.step("Verify that order is NOT eligible for manual refund")
        self.manual_refund_page.verify_order_not_eligible_for_manual_refund(order_id)
