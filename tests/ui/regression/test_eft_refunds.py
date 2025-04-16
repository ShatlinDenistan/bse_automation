"""EFT Refunds test suite."""

import pytest
from base.test_base import TestBase


class TestEFTRefunds(TestBase):
    """Tests for EFT Refunds functionality in the Fin Portal."""

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_564
    def test_order_id_redirects(self):
        """
        Verify that a user can click on an OrderID and be redirected to the appropriate page.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Click on an Order ID and verify new tab opened")
        self.eft_refund_page.click_order_id_and_verify_new_tab()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_564
    def test_customer_id_redirects(self):
        """
        Verify that a user can click on a customer Name and be redirected to the appropriate page.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Click on a Customer Name and verify new tab opened")
        self.eft_refund_page.filter_by_customer_id()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_filter_by_status_and_type(self):
        """
        Verify that a user can filter by status and type on the EFT Refunds page.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Apply status filter")
        self.eft_refund_page.apply_status_filter()

        self.step("Apply type filter")
        self.eft_refund_page.apply_type_filter()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_filter_by_customer_order_bank_account(self):
        """
        Verify that a user can filter by Customer ID, Order ID, and Bank Account Number.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Filter by Customer ID")
        self.eft_refund_page.filter_by_customer_id()

        self.step("Filter by Order ID")
        self.eft_refund_page.filter_by_order_id()

        self.step("Filter by Bank Account Number")
        self.eft_refund_page.filter_by_bank_account_number()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_filter_by_zendesk_ticket(self):
        """
        Verify that a user can filter by Zendesk Ticket Number.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Filter by Zendesk Ticket Number")
        self.eft_refund_page.filter_by_zendesk_ticket()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_554
    def test_date_range_filter_show_items_pagination(self):
        """
        Verify that a user can filter by date range and then show items per page and navigate between EFT Refunds pages.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Apply date range filter, show items filter and pagination")
        self.eft_refund_page.apply_date_range_filter()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_555
    def test_export_single_request(self):
        """
        Verify that a user can successfully export a single EFT Refund Request.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export one request on pending status")
        self.eft_refund_page.export_request()

        self.step("Verify exported row")
        self.eft_refund_page.verify_exported_row()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_555
    def test_export_multiple_requests(self):
        """
        Verify that a user can successfully export multiple EFT Refund Requests at once.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export three requests on pending status")
        self.eft_refund_page.export_multiple_requests()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_555
    def test_export_incorrect_status_request(self):
        """
        Verify that a user cannot successfully export an EFT Refund Request that is already exported.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export request on exported status")
        self.eft_refund_page.export_request_with_incorrect_status()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_562
    def test_manual_eft_refund_request(self):
        """
        Verify that a user can perform a manual EFT and that the modal has all the necessary fields.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Click the Manual EFT button and verify the fields")
        self.eft_refund_page.click_manual_eft_button_and_verify_fields()

        self.step("Populate manual EFT refund request mandatory fields")
        self.eft_refund_page.populate_manual_eft_fields()

        self.step("Verify credit deduction popup")
        self.eft_refund_page.verify_credit_deduction_popup()

        self.step("Verify manual EFT success")
        self.eft_refund_page.verify_manual_eft_success()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_557
    def test_decline_pending_requests(self):
        """
        Verify that a user can successfully decline EFT Refund Requests on Pending Status.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Decline requests on pending status")
        self.eft_refund_page.decline_requests()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_557
    def test_decline_already_processed_requests(self):
        """
        Verify that a user cannot successfully decline an EFT Refund Request that is exported or declined.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Decline requests on exported or declined status")
        self.eft_refund_page.decline_requests(status="exported")

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_556
    def test_export_and_verify_eft_refund_csv_files(self):
        """
        Verify that the Bank csv files that have exported EFT Refund requests have the correct format.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Export request and download Nedbank file")
        nedbank_file = self.eft_refund_page.verify_nedbank_file_export()
        self.step(f"Successfully downloaded Nedbank file: {nedbank_file}")

        self.step("Export request and download Absa file")
        absa_file = self.eft_refund_page.verify_absa_file_export()
        self.step(f"Successfully downloaded Absa file: {absa_file}")

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_558
    def test_send_email_to_multiple_customers(self):
        """
        Verify that a user can send "scripted" emails to multiple customers from the EFT Refunds page.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Select multiple EFT refund requests")
        self.eft_refund_page.select_multiple_eft_refund_requests()

        self.step("Select random template and send email")
        self.eft_refund_page.select_random_template_and_send_email()

        self.step("Verify email success message")
        self.eft_refund_page.verify_email_success_message()

        self.step("Verify checkboxes are unchecked")
        self.eft_refund_page.verify_checkboxes_are_unchecked()

    @pytest.mark.regression
    @pytest.mark.eftrefunds
    @pytest.mark.qaba_558
    def test_send_email_to_manual_eft_request(self):
        """
        Verify that a user cannot send "scripted" emails to Manual EFT Refund Requests.
        """
        self.step("Navigate to EFT Refunds page")
        self.eft_refund_page.navigate_to_eft_refunds_page()

        self.step("Select a manual EFT refund request")
        self.eft_refund_page.select_manual_eft_refund_request()

        self.step("Select random template and send email")
        self.eft_refund_page.select_random_template_and_send_email()

        self.step("Verify email error message")
        self.eft_refund_page.verify_email_error_message()
