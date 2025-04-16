import pytest
from base.test_base import TestBase


@pytest.mark.ui
class TestManualAuthSanity(TestBase):
    """Test class for Manual Authorization functionality in Fin-Portal"""

    @pytest.mark.sanity
    @pytest.mark.qaba_499
    def test_manual_auth_ebucks_and_credit_card(self):
        """
        Test manual authorization for eBucks and Credit Card payment method

        Steps:
        1. Get orders from database with eBucks and Credit Card payment
        2. Search for the retrieved order
        3. Click on payments ledger accordion
        4. Get refund amount for eBucks
        5. Process the payment authorization
        6. Expand order items and initiate refund
        7. Complete manual override with eBucks details
        8. Confirm override and view logs
        9. Verify override details
        """
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.new_order_ebucks_cc_sql)

        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Click payments ledger accordion")
        self.manual_auth_page.click_payments_ledger_accordion()

        self.step("Get refund amount for eBucks")
        refund_amount = self.manual_auth_page.get_refund_amount_for_ebucks()

        self.step("Click authorize now button and close notification")
        self.manual_auth_page.click_authorize_now_button_and_close_notification()

        self.step("On order view page expand the order items accordion and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Click manual auth override button and complete the override form")
        self.manual_auth_page.click_manual_auth_override_button_and_complete_form("eBucks")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("eBucks")

    @pytest.mark.sanity
    @pytest.mark.qaba_496
    def test_manual_auth_credit_card_and_ebucks_part_pay_unauth_order(self):
        """
        Test manual authorization for Credit Card and eBucks Part Pay with unauthorized order

        Steps:
        1. Get orders from database with eBucks and Credit Card payment
        2. Search for the retrieved order
        3. Click on payments ledger accordion
        4. Process the payment authorization
        5. Expand order items and initiate refund
        6. Complete manual override with EFT details
        7. Capture EFT banking details
        8. Confirm override and view logs
        9. Verify override details
        """
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.new_order_ebucks_cc_sql)

        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids[0])

        self.step("Click payments ledger accordion")
        self.manual_auth_page.click_payments_ledger_accordion()

        self.step("Click authorize now button and close notification")
        self.manual_auth_page.click_authorize_now_button_and_close_notification()

        self.step("On order view page expand the order items accordion and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete the form with EFT details")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("EFT")
