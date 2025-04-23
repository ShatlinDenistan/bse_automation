import pytest
from base.test_base import TestBase


class TestEftRefunds(TestBase):
    """Test class for EFT Refunds functionality."""

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_564
    def test_order_id_redirects(self):
        """Verify that a user can click on an OrderID and be redirected to the appropriate page."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Click on an Order ID and verify new tab opened")
        self.eft_refund_page.click_on_order_id_and_verify_new_tab_opened()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_564
    def test_customer_id_redirects(self):
        """Verify that a user can click on a customer Name and be redirected to the appropriate page."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Click on a Customer Name and verify new tab opened")
        self.eft_refund_page.click_on_customer_name_and_verify_new_tab_opened()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_filter_by_status_and_type(self):
        """Verify that a user can filter by status and type on the EFT Refunds page."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Apply Status Filter")
        self.eft_refund_page.apply_status_filter()

        self.step("Apply Type Filter")
        self.eft_refund_page.apply_type_filter()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_filter_by_customer_id_order_id_and_bank_account_number(self):
        """Verify that a user can filter by Customer ID, Order ID, and Bank Account Number."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Filter By Customer ID")
        self.eft_refund_page.filter_by_customer_id()

        self.step("Filter By Order ID")
        self.eft_refund_page.filter_by_order_id()

        self.step("Filter By Bank Account Number")
        self.eft_refund_page.filter_by_bank_account_number()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_filter_by_zendesk_ticket_number(self):
        """Verify that a user can filter by Zendesk Ticket Number."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Filter By Zendesk Ticket Number")
        self.eft_refund_page.filter_by_zendesk_ticket_number()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_date_range_filter_show_items_and_pagination(self):
        """Verify that a user can filter by date range and then show items per page and navigate between EFT Refunds pages."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Apply Date Range Filter And Show Items Filter And Pagination")
        self.eft_refund_page.apply_date_range_filter_and_pagination()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_555
    def test_export_single_request(self):
        """Verify that a user can successfully export a single EFT Refund Request."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export One Request On Pending Status")
        self.eft_refund_page.export_one_request_on_pending_status()

        self.step("Verify Exported Row")
        self.eft_refund_page.verify_exported_row()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_555
    def test_export_multiple_requests(self):
        """Verify that a user can successfully export multiple EFT Refund Requests at once."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export Three Requests On Pending Status")
        self.eft_refund_page.export_three_requests_on_pending_status()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_555
    def test_export_requests_incorrect_status(self):
        """Verify that a user cannot successfully export an EFT Refund Requests that is already exported."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export Request On Exported Status")
        self.eft_refund_page.export_request_on_exported_status()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_562
    def test_manual_eft_refund_request(self):
        """Verify that a user can perform a manual eft and that the modal has all the necessary fields."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Click The Manual EFT Button And Verify The Fields")
        self.eft_refund_page.click_manual_eft_button_and_verify_fields()

        self.step("Populate Manual EFT Refund Request Mandatory Fields")
        self.eft_refund_page.populate_manual_eft_refund_request_mandatory_fields()

        self.step("Verify Credit Deduction Popup")
        self.eft_refund_page.verify_credit_deduction_popup()

        self.step("Verify Manual EFT Success")
        self.eft_refund_page.verify_manual_eft_success()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_557
    def test_decline_requests(self):
        """Verify that a user can successfully decline EFT Refund Requests on Pending Status."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Decline Requests On Pending Status")
        self.eft_refund_page.decline_requests_on_pending_status()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_557
    def test_decline_requests_already_cancelled_declined(self):
        """Verify that a user cannot successfully decline an EFT Refund Requests that is exported or declined."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Decline Requests On Exported or Declined Status")
        self.eft_refund_page.decline_requests_on_exported_or_declined_status()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_556
    def test_export_requests_verify_eft_refund_exported_csv_file(self):
        """Verify that the Bank csv files that has exported EFT Refund requests, have the correct format."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export Request And Download Nedbank File")
        self.eft_refund_page.export_request_and_download_nedbank_file()

        self.step("Export Request And Download Absa File")
        self.eft_refund_page.export_request_and_download_absa_file()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_558
    def test_send_email(self):
        """Verify that a user can send "scripted" emails to multiple customers from the EFT Refunds page."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Select Multiple EFT Refund Requests")
        self.eft_refund_page.select_multiple_eft_refund_requests()

        self.step("Select Random Template And Send Email")
        self.eft_refund_page.select_random_template_and_send_email()

        self.step("Verify Email Success Message")
        self.eft_refund_page.verify_email_success_message()

        self.step("Verify Checkboxes Are Unchecked")
        self.eft_refund_page.verify_checkboxes_are_unchecked()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_558
    def test_send_email_to_manual_eft_request(self):
        """Verify that a user cannot send "scripted" emails to Manual EFT Refund Requests."""

        self.step("Navigate to EFT Refunds Page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Select A Manual EFT Refund Request")
        self.eft_refund_page.select_manual_eft_refund_request()

        self.step("Select Random Template And Send Email")
        self.eft_refund_page.select_random_template_and_send_email()

        self.step("Verify Email Error Message")
        self.eft_refund_page.verify_email_error_message()
