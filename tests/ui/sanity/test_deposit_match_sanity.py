"""
Deposit Match Sanity Test Suite.
Tests for the Deposit Match functionality in Fin-Portal.
"""

import pytest
from base.test_base import TestBase


@pytest.mark.ui
@pytest.mark.sanity
class TestDepositMatchSanity(TestBase):
    """Test class for Deposit Match sanity functionality"""

    @pytest.mark.QABA_514
    def test_show_items_and_pagination(self):
        """
        View all the records in a large deposit csv file via Show Items and Pagination

        Steps:
        1. Navigate to Deposit Match
        2. Upload valid deposit match file
        3. Click the refresh button
        4. Click show items dropdown and select 30 items
        5. Navigate to second page
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload valid Deposit Match file")
        deposit_match_file = "/data/GENERIC MORE THAN 15 RECORDS.csv"
        self.deposit_match_page.upload_valid_deposit_match_file(deposit_match_file)

        self.step("Click the refresh button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Click Show Items dropdown and select 30 items")
        self.deposit_match_page.click_show_items_dropdown_and_select_30_items()

        self.step("Navigate to second page")
        self.deposit_match_page.navigate_to_second_page()

    @pytest.mark.QABA_511
    def test_batch_authorise_order(self):
        """
        Manually Auth a new order from the Batch screen

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with new status orders
        3. Click the refresh button
        4. Select new order and authorise
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with new status orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click the refresh button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Select new order and authorise")
        self.deposit_match_page.select_new_order_and_authorise()

    @pytest.mark.QABA_509
    def test_batch_cancel_order(self):
        """
        Cancel a new order from the Batch screen

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with new status orders
        3. Click the refresh button
        4. Select authorised order and cancel
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with new status orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click the refresh button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Select authorised order and cancel")
        self.deposit_match_page.select_authorised_order_and_cancel()

    @pytest.mark.QABA_513
    def test_batch_manually_match_and_credit_order(self):
        """
        Manually Match a deposit/payment to a canceled order and credit the order in the Batch screen.

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with authorised orders
        3. Select authorised order and cancel
        4. Click the match button and type in the order ID
        5. Click the match button and close modal
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorised orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Select authorised order and cancel")
        self.deposit_match_page.select_authorised_order_and_cancel()

        self.step("Click the match button and type in the order ID")
        self.deposit_match_page.click_the_match_button_and_type_in_the_order_id("12345")

        self.step("Click the match button and close modal")
        self.deposit_match_page.click_the_match_button_and_close_modal()

    @pytest.mark.QABA_512
    def test_batch_manually_match_and_auth_order(self):
        """
        Manually Match a deposit/payment to a new order and Authorise it in the Batch screen.

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with authorised orders
        3. Click the match button and type in the order ID
        4. Click the match button and close modal
        5. Select authorised order and authorise
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorised orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click the match button and type in the order ID")
        self.deposit_match_page.click_the_match_button_and_type_in_the_order_id("12345")

        self.step("Click the match button and close modal")
        self.deposit_match_page.click_the_match_button_and_close_modal()

        self.step("Select authorised order and authorise")
        self.deposit_match_page.select_authorised_order_and_authorise()
