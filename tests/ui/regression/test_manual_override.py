import pytest
from base.test_base import TestBase


@pytest.mark.ui
class TestManualOverride(TestBase):
    """Test class for Manual Override functionality in Fin-Portal"""

    @pytest.mark.regression
    @pytest.mark.QABA_482
    def test_manual_override_credit_card(self):
        """
        Test manual override with Credit Card payment method

        Steps:
        1. Get orders from database with Credit Card payment
        2. Cancel the paid order
        3. Search for the cancelled order
        4. Expand the customer credit accordion
        5. Expand order items and click refund
        6. Complete manual override with Credit Card details
        7. Verify override details
        """
        self.step("Get orders from database with Credit Card payment")
        self.database.get_orders_from_database(self.database.paygate_sql)

        self.step("Cancel the paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for the cancelled order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Expand the customer credit accordion")
        self.customer_credit_page.expand_customer_credit_accordion()

        self.step("Expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Complete manual override with Credit Card details")
        self.manual_override_page.complete_override_form("Credit Card", self.database.order_total[0], "Test Override")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_override()
        self.order_view_page.view_refunds_logs()

        self.step("Verify override details")
        self.manual_override_page.verify_override_details("Paygate")

    @pytest.mark.regression
    @pytest.mark.QABA_488
    def test_manual_override_instant_eft_payfast(self):
        """
        Test manual override with PayFast payment method

        Steps:
        1. Get orders from database with PayFast payment
        2. Cancel the paid order
        3. Search for the cancelled order
        4. Expand the customer credit accordion
        5. Expand order items and click refund
        6. Complete manual override with PayFast details
        7. Verify override details
        """
        self.step("Get orders from database with PayFast payment")
        self.database.get_orders_from_database(self.database.payfast_sql)

        self.step("Cancel the paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for the cancelled order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Expand the customer credit accordion")
        self.customer_credit_page.expand_customer_credit_accordion()

        self.step("Expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Complete manual override with PayFast details")
        self.manual_override_page.complete_override_form("PayFast", self.database.order_total[0], "Test Override")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_override()
        self.order_view_page.view_refunds_logs()

        self.step("Verify override details")
        self.manual_override_page.verify_override_details("PayFast")

    @pytest.mark.regression
    @pytest.mark.QABA_484
    def test_manual_override_masterpass(self):
        """
        Test manual override with Masterpass payment converted to EFT

        Steps:
        1. Get orders from database with Masterpass payment
        2. Cancel the paid order
        3. Search for the cancelled order
        4. Expand the customer credit accordion
        5. Expand order items and click refund
        6. Complete manual override with EFT details
        7. Verify override details
        """
        self.step("Get orders from database with Masterpass payment")
        self.database.get_orders_from_database(self.database.masterpass_sql)

        self.step("Cancel the paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for the cancelled order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Expand the customer credit accordion")
        self.customer_credit_page.expand_customer_credit_accordion()

        self.step("Expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Complete manual override with EFT details")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify override details")
        self.manual_override_page.verify_manual_override_details("EFT")

    @pytest.mark.regression
    @pytest.mark.QABA_484
    def test_manual_override_eft_credit_card_original(self):
        """
        Test manual override with Credit Card payment converted to EFT

        Steps:
        1. Get orders from database with Credit Card payment
        2. Cancel the paid order
        3. Search for the cancelled order
        4. Expand the customer credit accordion
        5. Expand order items and click refund
        6. Complete manual override with EFT details
        7. Verify override details
        """
        self.step("Get orders from database with Credit Card payment")
        self.database.get_orders_from_database(self.database.paygate_sql)

        self.step("Cancel the paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for the cancelled order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Expand the customer credit accordion")
        self.customer_credit_page.expand_customer_credit_accordion()

        self.step("Expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Complete manual override with EFT details")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify override details")
        self.manual_override_page.verify_manual_override_details("EFT")

    @pytest.mark.regression
    @pytest.mark.QABA_486
    def test_manual_override_eft_discovery_miles(self):
        """
        Test manual override with Discovery Miles payment converted to EFT

        Steps:
        1. Get orders from database with Discovery Miles payment
        2. Cancel the paid order
        3. Search for the cancelled order
        4. Expand the customer credit accordion
        5. Expand order items and click refund
        6. Complete manual override with Discovery Miles details
        7. Verify override details
        """
        self.step("Get orders from database with Discovery Miles payment")
        self.database.get_orders_from_database(self.database.discovery_miles_sql)

        self.step("Cancel the paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for the cancelled order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Expand the customer credit accordion")
        self.customer_credit_page.expand_customer_credit_accordion()

        self.step("Expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Complete manual override with Discovery Miles details")
        self.manual_override_page.complete_override_form("Discovery Miles", self.database.order_total[0], "Test Override")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_override()
        self.order_view_page.view_refunds_logs()

        self.step("Verify override details")
        self.manual_override_page.verify_override_details("Discovery Miles")

    @pytest.mark.regression
    @pytest.mark.QABA_483
    def test_manual_override_refund_amount_exceeds_settlement(self):
        """
        Test manual override with refund amount exceeding settlement amount

        Steps:
        1. Get orders from database with Credit Card payment
        2. Cancel the paid order
        3. Search for the cancelled order
        4. Expand the customer credit accordion
        5. Expand order items and click refund
        6. Complete manual override with amount exceeding total
        7. Verify failed override admin note
        """
        self.step("Get orders from database with Credit Card payment")
        self.database.get_orders_from_database(self.database.paygate_sql)

        self.step("Cancel the paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for the cancelled order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Expand the customer credit accordion")
        self.customer_credit_page.expand_customer_credit_accordion()

        self.step("Expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Complete manual override with amount exceeding total")
        self.manual_override_page.complete_override_form_with_amount_exceeding_total("Credit Card", self.database.order_total[0])

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_override()
        self.order_view_page.view_refunds_logs()

        self.step("Verify failed override admin note")
        self.manual_override_page.verify_failed_override_admin_note()
