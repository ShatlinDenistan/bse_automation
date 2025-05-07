import pytest
from base.test_base import TestBase


class TestDepositMatch(TestBase):

    @pytest.mark.QABA_522
    def test_incorrect_upload_file_format_do_not_process(self):
        """Verify that the file does not meeting the Deposit Match file format requirements."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload invalid Deposit Match file")
        self.deposit_match_page.upload_invalid_deposit_match_file(self.test_data_files.deposit_match_file)

        self.step("Verify CSV error occurred")
        self.deposit_match_page.verify_csv_error_occurred()

    @pytest.mark.QABA_522
    def test_deposit_match_download_batch_file(self):
        """Verify that the file does not meeting the Deposit Match file format requirements."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload a valid Deposit Match file")
        self.deposit_match_page.upload_valid_deposit_match_file(self.test_data_files.deposit_match_file)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Go to Deposit Match page")
        self.deposit_match_page.go_to_deposit_match_page()

        self.step("Download batch file")
        self.deposit_match_page.download_batch_file()

    @pytest.mark.QABA_523
    def test_deposit_match_all_batches_filters(self):
        """Only view filtered data on the All Batched screen."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select PayFast from payment method dropdown and apply filter")
        self.deposit_match_page.click_the_select_payment_method_dropdown_and_select_payfast_and_apply_filter()

        self.step("Verify batches are filtered by payment method")
        self.deposit_match_page.verify_that_batches_are_filtered_by_payment_method()

        self.step("Clear the filter")
        self.deposit_match_page.click_the_clear_filter_button()

        self.step("Select date range and apply filter")
        self.deposit_match_page.click_the_select_date_range_field_and_select_date_from_the_previous_week()

    @pytest.mark.QABA_516
    def test_deposit_match_batch_search(self):
        """Search for orders based on specific search criteria on the Batch screen."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Click on existing batch")
        self.deposit_match_page.click_on_existing_batch()

        self.step("Click criteria dropdown and select Order ID")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_orderid()

        self.step("Enter order ID on searchbox and apply filter")
        _, customer_name, amount = self.deposit_match_page.enter_order_id_on_searchbox_and_apply_filer()

        self.step("Click criteria dropdown and select Statement Amount")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_statement_amount()

        self.step("Enter statement amount on searchbox and apply filter")
        self.deposit_match_page.enter_statement_amount_on_searchbox_and_apply_filer(amount)

        self.step("Click criteria dropdown and select Customer ID")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_customer_id()

        self.step("Enter Customer ID on searchbox and apply filter")
        self.deposit_match_page.enter_customer_id_on_searchbox_and_apply_filer()

        self.step("Click criteria dropdown and select Customer Name")
        self.deposit_match_page.click_the_criteria_dropdown_list_and_select_customer_name()

        self.step("Enter Customer name on searchbox and apply filter")
        self.deposit_match_page.enter_customer_name_on_searchbox_and_apply_filer(customer_name)

    @pytest.mark.QABA_515
    def test_deposit_match_batch_filtering(self):
        """Only view filtered data on the Batch screen."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click match status dropdown and select Auto Match")
        self.deposit_match_page.click_match_status_dropdown_and_select_auto_match()

        self.step("Click match status dropdown and select Amount Differ")
        self.deposit_match_page.click_match_status_dropdown_and_select_amount_differ()

        self.step("Click match status dropdown and select Order Not Found")
        self.deposit_match_page.click_match_status_dropdown_and_select_order_not_found()

    @pytest.mark.QABA_524
    def test_deposit_match_unclaimed_payments_filters(self):
        """Search for orders based on specific search criteria on the Batch screen."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Click the Unclaimed Payment tab")
        self.deposit_match_page.click_the_unclaimed_payment_tab()

        self.step("Click criteria dropdown and select Customer Name")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_customer_name()

        self.step("Enter customer name and apply filter")
        self.deposit_match_page.enter_customer_name_and_apply_filter()

        self.step("Click criteria dropdown and select Order ID")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_order_id()

        self.step("Enter order ID and apply filter")
        self.deposit_match_page.enter_order_id_and_apply_filter()

        self.step("Click criteria dropdown and select Statement Amount")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_statement_amount()

        self.step("Enter statement amount and apply filter")
        self.deposit_match_page.enter_statement_amount_and_apply_filter()

        self.step("Click criteria dropdown and select Batch ID")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_batch_id()

        self.step("Enter batch ID and apply filter")
        self.deposit_match_page.enter_batch_id_and_apply_filter()

    @pytest.mark.QABA_510
    def test_deposit_match_batch_unclaimed_payment(self):
        """Move deposits to the Unclaimed Payments page from the Batch screen for further investigation."""

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

        self.step("Click criteria dropdown and select Order ID")
        self.deposit_match_page.click_criteria_dropdown_list_and_select_order_id()

        self.step("Enter unclaimed payment order ID and apply filter")
        self.deposit_match_page.enter_unclaimed_payment_order_id_and_apply_filter(unclaimed_order_id)

    @pytest.mark.QABA_507
    def test_deposit_match_batch_remove_order(self):
        """As a user, I want to remove an order from the batch."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload valid Deposit Match file")
        self.deposit_match_page.upload_valid_deposit_match_file(self.test_data_files.deposit_match_file)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Click match status dropdown and select Order Not Found")
        self.deposit_match_page.click_match_status_dropdown_and_select_order_not_found()

        self.step("Click checkbox next to first order in the batch")
        self.deposit_match_page.click_checkbox_next_to_first_order_in_the_batch()

        self.step("Click the Remove Order button")
        self.deposit_match_page.click_the_remove_order_button()

    @pytest.mark.QABA_529
    def test_deposit_match_upload_file_staggered_uploads(self):
        """Upload multiple files one after the other and ensure that they are processed without any issues."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Upload valid Deposit Match file")
        batch_id1 = self.deposit_match_page.upload_valid_deposit_match_file(self.test_data_files.deposit_match_file)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Navigate to All Batches")
        self.deposit_match_page.navigate_to_all_batches(batch_id1)

        self.step("Upload another valid Deposit Match file")
        batch_id2 = self.deposit_match_page.upload_valid_deposit_match_file(self.test_data_files.deposit_match_file)

        self.step("Click the Refresh Button")
        self.deposit_match_page.click_the_refresh_button()

        self.step("Navigate to All Batches")
        self.deposit_match_page.navigate_to_all_batches(batch_id2)

    @pytest.mark.QABA_507
    def test_deposit_match_batch_send_email(self):
        """Send a "Deposit Update" email to multiple customers from the Batch screen."""

        self.step("Navigate to Deposit Match")
        self.deposit_match_page.navigate_to_deposit_match()

        self.step("Select batch with authorized orders")
        self.deposit_match_page.select_batch_with_authorised_orders()

        self.step("Click checkbox next to first order in the batch")
        self.deposit_match_page.click_checkbox_next_to_first_order_in_the_batch()

        self.step("Click Send Email button and send email")
        self.deposit_match_page.click_send_email_button_and_send_email()
