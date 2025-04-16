import pytest
from base.test_base import TestBase


@pytest.mark.ui
class TestManualAuth(TestBase):
    """Test class for Manual Authorization functionality in Fin-Portal"""

    @pytest.mark.regression
    @pytest.mark.QABA_495
    def test_manual_auth_mobicred(self):
        """
        Test manual authorization for Mobicred payment method

        Steps:
        1. Get orders from database with Mobicred payment
        2. Search for the retrieved order
        3. Process the payment authorization
        4. Add credit to the customer account
        5. Expand order items and initiate refund
        6. Complete manual override with EFT details
        7. Verify override details
        """
        self.step("Get orders from database")
        self.database.get_orders_from_database(self.database.new_order_mobicred_sql)

        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Click payments ledger accordion")
        self.manual_auth_page.click_payments_ledger_accordion()

        self.step("Click authorize now button and close notification")
        self.manual_auth_page.click_authorize_now_button_and_close_notification()

        self.step("Expand the customer credit accordion and add credit")
        self.customer_credit_page.expand_customer_credit_accordion()
        self.manual_auth_page.click_credit_button_and_add_credit_amount(self.database.order_total)

        self.step("On order view page expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete the form with EFT details")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("EFT")

    @pytest.mark.regression
    @pytest.mark.QABA_494
    def test_manual_auth_sbux_order_not_canceled(self):
        """
        Test manual authorization for sBux payment method with order not canceled

        Steps:
        1. Create a new order that's not paid with sBux payment method
        2. Search for the created order
        3. Process the payment authorization
        4. Add credit to the customer account
        5. Expand order items and initiate refund
        6. Complete manual override with EFT details
        7. Verify override details
        """
        self.step("Create new TAL orders not paid")
        self.database.create_new_tal_orders_not_paid(13866233, "sBux")

        self.step("Search for order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Click payments ledger accordion")
        self.manual_auth_page.click_payments_ledger_accordion()

        self.step("Click authorize now button and close notification")
        self.manual_auth_page.click_authorize_now_button_and_close_notification()

        self.step("Expand the customer credit accordion and add credit")
        self.customer_credit_page.expand_customer_credit_accordion()
        self.manual_auth_page.click_credit_button_and_add_credit_amount(self.database.order_total)

        self.step("On order view page expand order items and click refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete the form with EFT details")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("EFT")
