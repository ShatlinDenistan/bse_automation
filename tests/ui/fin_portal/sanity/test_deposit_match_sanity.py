import pytest
from base.test_base import TestBase


class TestDepositMatchSanity(TestBase):

    @pytest.mark.QABA_514
    def test_deposit_match_batch_show_items_and_pagination(self):
        """View all the records in a large deposit csv file via Show Items and Pagination."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload a valid Deposit Match file with 30+ records")
        self.deposit_match_page.upload_valid_deposit_match_file(self.config.DEPOSIT_MATCH_FILE_30)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Click show items dropdown and select 30 items")
        self.deposit_match_page.click_show_items_dropdown_and_select_30_items()

        self.step("Navigate to the second page")
        self.deposit_match_page.navigate_to_second_page()

    @pytest.mark.QABA_511
    def test_deposit_match_batch_authorise_order(self):
        """Manually Auth a new order from the Batch screen."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with new status orders")
        batch_id = self.deposit_match_page.select_batch_with_new_status_orders(self.config.NEW_ORDER_EBUCKS_CC_SQL, self.order_ids)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Select new order and authorize it")
        self.deposit_match_page.select_new_order_and_authorise()

    @pytest.mark.QABA_509
    def test_deposit_match_batch_cancel_order(self):
        """Cancel a new order from the Batch screen."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with new status orders")
        batch_id = self.deposit_match_page.select_batch_with_new_status_orders(self.config.NEW_ORDER_EBUCKS_CC_SQL, self.order_ids)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Select authorized order and cancel it")
        self.deposit_match_page.select_authorised_order_and_cancel()

    @pytest.mark.QABA_513
    def test_deposit_match_batch_manually_match_and_credit_order(self):
        """Manually Match a deposit/payment to a canceled order and credit the order in the Batch screen."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Select authorized order and cancel it")
        self.deposit_match_page.select_authorised_order_and_cancel()

        self.step("Click the Match button and type in the order ID")
        order_id = "12345"  # This would typically come from test data or config
        self.deposit_match_page.click_the_match_button_and_type_in_the_order_id(order_id)

        self.step("Click the Match button and close modal")
        self.deposit_match_page.click_the_match_button_and_close_modal()

    @pytest.mark.QABA_512
    def test_deposit_match_batch_manually_match_and_auth_order(self):
        """Manually Match a deposit/payment to a new order and Authorise it in the Batch screen."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click the Match button and type in the order ID")
        order_id = "12345"  # This would typically come from test data or config
        self.deposit_match_page.click_the_match_button_and_type_in_the_order_id(order_id)

        self.step("Click the Match button and close modal")
        self.deposit_match_page.click_the_match_button_and_close_modal()

        self.step("Select authorized order and authorize it")
        self.deposit_match_page.select_authorised_order_and_authorise()
