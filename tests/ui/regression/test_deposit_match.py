"""
Deposit Match Test Suite.
Tests for the Deposit Match functionality in Fin-Portal.
"""

import pytest
from base.test_base import TestBase


class TestDepositMatch(TestBase):
    """Test class for Deposit Match functionality"""

    @pytest.mark.regression
    @pytest.mark.QABA_522
    def test_incorrect_upload_file_format(self):
        """
        Verify that the file not meeting the Deposit Match file format requirements is not processed

        Steps:
        1. Navigate to Deposit Match
        2. Upload invalid Deposit Match file
        3. Verify CSV error occurred
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload invalid Deposit Match file")
        invalid_file = "/data/GENERIC GLOBAL 1.csv"
        self.deposit_match_page.upload_invalid_deposit_match_file(invalid_file)

        self.step("Verify CSV error occurred")
        self.deposit_match_page.verify_csv_error_occurred()

    @pytest.mark.regression
    @pytest.mark.QABA_522
    def test_download_batch_file(self):
        """
        Verify the functionality to download batch file

        Steps:
        1. Navigate to Deposit Match
        2. Upload valid Deposit Match file
        3. Click the refresh button
        4. Navigate to Deposit Match page
        5. Download batch file
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload valid Deposit Match file")
        valid_file = "/data/GENERIC MORE THAN 15 RECORDS.csv"
        batch_id = self.deposit_match_page.upload_valid_deposit_match_file(valid_file)

        self.step("Click the refresh button")
        batch_id = self.deposit_match_page.click_the_refresh_button()

        self.step("Navigate to Deposit Match page")
        self.deposit_match_page.go_to_deposit_match_page()

        self.step("Download batch file")
        self.deposit_match_page.download_batch_file()

    @pytest.mark.regression
    @pytest.mark.QABA_523
    def test_all_batches_filters(self):
        """
        Verify only filtered data is displayed on the All Batches screen

        Steps:
        1. Navigate to Deposit Match
        2. Filter batches by PayFast payment method
        3. Verify batches are filtered by payment method
        4. Clear filter
        5. Filter by date range from previous week
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Click the select payment method dropdown and select PayFast and apply filter")
        self.deposit_match_page.click_the_select_payment_method_dropdown_and_select_payfast_and_apply_filter()

        self.step("Verify that batches are filtered by payment method")
        self.deposit_match_page.verify_that_batches_are_filtered_by_payment_method()

        self.step("Click the clear filter button")
        self.deposit_match_page.click_the_clear_filter_button()

        self.step("Click the select date range field and select date from the previous week")
        self.deposit_match_page.click_the_select_date_range_field_and_select_date_from_the_previous_week()

    @pytest.mark.regression
    @pytest.mark.QABA_516
    def test_batch_search(self):
        """
        Search for orders based on specific search criteria on the Batch screen

        Steps:
        1. Navigate to Deposit Match
        2. Click on existing batch
        3. Search by Order ID
        4. Search by Statement Amount
        5. Search by Customer ID
        6. Search by Customer Name
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Click on existing batch")
        self.deposit_match_page.click_on_existing_batch()

        self.step("Click the criteria dropdown list and select Order ID")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_order_id()

        self.step("Enter Order Id on searchbox and apply filter")
        order_id, customer_name, amount = self.deposit_match_page.enter_order_id_on_searchbox_and_apply_filter()

        self.step("Click the criteria dropdown list and select Statement Amount")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_statement_amount()

        self.step("Enter Statement Amount on searchbox and apply filter")
        self.deposit_match_page.enter_statement_amount_on_searchbox_and_apply_filter(amount)

        self.step("Click the criteria dropdown list and select Customer Id")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_customer_id()

        self.step("Enter Customer ID on searchbox and apply filter")
        self.deposit_match_page.enter_customer_id_on_searchbox_and_apply_filter()

        self.step("Click the criteria dropdown list and select Customer Name")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_customer_name()

        self.step("Enter Customer Name on searchbox and apply filter")
        self.deposit_match_page.enter_customer_name_on_searchbox_and_apply_filter(customer_name)

    @pytest.mark.regression
    @pytest.mark.QABA_515
    def test_batch_filtering(self):
        """
        Verify that only filtered data is displayed on the Batch screen

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with authorized orders
        3. Filter by Auto Match status
        4. Filter by Amount Differ status
        5. Filter by Order Not Found status
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Filter by Auto Match status")
        self.deposit_match_page.click_match_status_dropdown_and_select_auto_match()

        self.step("Filter by Amount Differ status")
        self.deposit_match_page.click_match_status_dropdown_and_select_amount_differ()

        self.step("Filter by Order Not Found status")
        self.deposit_match_page.click_match_status_dropdown_and_select_order_not_found()

    @pytest.mark.regression
    @pytest.mark.QABA_524
    def test_unclaimed_payments_filters(self):
        """
        Search for orders based on specific search criteria on the Unclaimed Payments screen

        Steps:
        1. Navigate to Deposit Match
        2. Go to Unclaimed Payments tab
        3. Search by Customer Name
        4. Search by Order ID
        5. Search by Statement Amount
        6. Search by Batch ID
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Click the Unclaimed Payment tab")
        self.deposit_match_page.click_the_unclaimed_payment_tab()

        self.step("Search by Customer Name")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_customer_name()
        self.deposit_match_page.enter_customer_name_and_apply_filter()

        self.step("Search by Order ID")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_order_id()
        self.deposit_match_page.enter_order_id_and_apply_filter()

        self.step("Search by Statement Amount")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_statement_amount()
        self.deposit_match_page.enter_statement_amount_and_apply_filter()

        self.step("Search by Batch ID")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_batch_id()
        self.deposit_match_page.enter_batch_id_and_apply_filter()

    @pytest.mark.regression
    @pytest.mark.QABA_510
    def test_batch_unclaimed_payment(self):
        """
        Move deposits to the Unclaimed Payments page from the Batch screen for further investigation

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with authorized orders
        3. Click checkbox for first order
        4. Move to unclaimed payment
        5. Navigate to unclaimed payment page
        6. Search for the moved order
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click checkbox next to first order in the batch")
        unclaimed_order_id = self.deposit_match_page.click_checkbox_next_to_first_order_in_the_batch()

        self.step("Click the Unclaimed Payment button")
        self.deposit_match_page.click_the_unclaimed_payment_button()

        self.step("Navigate to Unclaimed Payment page")
        self.deposit_match_page.navigate_to_unclaimed_payment_page()

        self.step("Search for the unclaimed payment order")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_order_id()
        self.deposit_match_page.enter_unclaimed_payment_order_id_and_apply_filter(unclaimed_order_id)

    @pytest.mark.regression
    @pytest.mark.QABA_507
    def test_batch_remove_order(self):
        """
        Remove an order from the batch

        Steps:
        1. Navigate to Deposit Match
        2. Upload valid deposit match file
        3. Click the refresh button
        4. Filter by Order Not Found status
        5. Click checkbox for first order
        6. Remove the order
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload valid Deposit Match file")
        valid_file = "/data/GENERIC MORE THAN 15 RECORDS.csv"
        batch_id = self.deposit_match_page.upload_valid_deposit_match_file(valid_file)

        self.step("Click the refresh button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Filter by Order Not Found status")
        self.deposit_match_page.click_match_status_dropdown_and_select_order_not_found()

        self.step("Click checkbox next to first order in the batch")
        self.deposit_match_page.click_checkbox_next_to_first_order_in_the_batch()

        self.step("Click the Remove Order button")
        self.deposit_match_page.click_the_remove_order_button()

    @pytest.mark.regression
    @pytest.mark.QABA_529
    def test_staggered_uploads(self):
        """
        Upload multiple files one after the other and ensure they are processed without issues

        Steps:
        1. Navigate to Deposit Match
        2. Upload first valid deposit match file
        3. Click the refresh button
        4. Navigate to All Batches
        5. Upload second valid deposit match file
        6. Click the refresh button
        7. Navigate to All Batches
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload first valid Deposit Match file")
        valid_file = "/data/GENERIC MORE THAN 15 RECORDS.csv"
        batch_id1 = self.deposit_match_page.upload_valid_deposit_match_file(valid_file)

        self.step("Click the refresh button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Navigate to All Batches")
        self.deposit_match_page.navigate_to_all_batches(batch_id1)

        self.step("Upload second valid Deposit Match file")
        batch_id2 = self.deposit_match_page.upload_valid_deposit_match_file(valid_file)

        self.step("Click the refresh button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Navigate to All Batches")
        self.deposit_match_page.navigate_to_all_batches(batch_id2)

    @pytest.mark.regression
    @pytest.mark.QABA_507
    def test_batch_send_email(self):
        """
        Send a "Deposit Update" email to customers from the Batch screen

        Steps:
        1. Navigate to Deposit Match
        2. Select batch with authorized orders
        3. Click checkbox for first order
        4. Send email to customer
        """
        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click checkbox next to first order in the batch")
        self.deposit_match_page.click_checkbox_next_to_first_order_in_the_batch()

        self.step("Send email to customer")
        self.deposit_match_page.click_send_email_button_and_send_email()
