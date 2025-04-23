import pytest
from base.test_base import TestBase


class TestFinPortalCustomerView(TestBase):
    """Tests for Customer View functionality in Fin Portal"""

    @pytest.mark.QABSE_260
    def test_verify_customer_details(self):
        """Verify that the customer details are displayed on the customer view page"""

        self.step("Search for customer")
        # Note: Search for customer functionality would need to be implemented
        # Assuming there's a search method that already exists
        self.top_nav.search_for_customer("1")

        self.step("Verify customer details")
        self.customer_view_page.verify_customer_details()

    @pytest.mark.QABSE_260
    def test_verify_notes_section(self):
        """Verify that the customer notes are displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify notes section")
        self.customer_view_page.verify_notes_section_with_edit_option()

    @pytest.mark.QABSE_260
    def test_verify_fin_note_section(self):
        """Verify that the Fin Notes are displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify Fin Note section")
        self.customer_view_page.verify_fin_notes_section_with_edit_option()

    @pytest.mark.QABSE_260
    def test_verify_customer_credit(self):
        """Verify that the Customer Credit Accordion is displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify customer credit")
        self.customer_view_page.verify_customer_credit()

    @pytest.mark.QABSE_260
    def test_verify_customer_address(self):
        """Verify that the Customer Address is displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify customer address")
        self.customer_view_page.verify_customer_address()

    @pytest.mark.QABSE_260
    def test_verify_email_logs(self):
        """Verify that the Email Logs are displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify email logs")
        self.customer_view_page.verify_email_logs()

    @pytest.mark.QABSE_260
    def test_verify_returns_history(self):
        """Verify that the Returns History Accordion is displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify customer returns history")
        self.customer_view_page.verify_customer_returns_history()

    @pytest.mark.QABSE_260
    def test_verify_zendesk_tickets(self):
        """Verify that the Zendesk Tickets are displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify zendesk tickets")
        self.customer_view_page.verify_zendesk_tickets()

    @pytest.mark.QABSE_260
    def test_verify_registered_and_modified_dates(self):
        """Verify that the Registered and Last Modified Dates are displayed on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify registered and modified dates")
        self.customer_view_page.verify_registered_and_last_modified_dates()

    @pytest.mark.QABSE_260
    def test_blacklist_a_customer(self):
        """Verify that a user can Blacklist a TAL customer on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("34345")

        self.step("Blacklist customer")
        self.customer_view_page.blacklist_a_customer()

    @pytest.mark.QABSE_260
    def test_add_credit(self):
        """Verify that a user can add credit to a customer on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("34345")

        self.step("Add credit")
        self.customer_view_page.add_credit()

    @pytest.mark.QABSE_211
    def test_edit_customer(self):
        """Verify that a user can edit customer information on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("34345")

        self.step("Edit customer")
        self.customer_view_page.edit_customer()

    @pytest.mark.QABSE_251
    @pytest.mark.QABSE_223
    def test_email_customer(self):
        """Verify that a user can send a generic email on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("112")

        self.step("Send generic email")
        subject_text = self.customer_view_page.send_generic_email()

        self.step("View email logs")
        self.customer_view_page.view_email_logs_for_latest_email_sent(subject_text)

    @pytest.mark.QABSE_250
    def test_add_note(self):
        """Verify that a user can add a note on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("555")

        self.step("Add admin note")
        self.customer_view_page.add_admin_note()

    @pytest.mark.QABSE_941
    def test_view_audit_logs(self):
        """Verify that a user can view the audit logs on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("555")

        self.step("View audit logs")
        self.customer_view_page.view_audit_logs()

    @pytest.mark.QABSE_222
    def test_view_sales_history(self):
        """Verify that a user can view the sales history on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1")

        self.step("Verify order link")
        order_page = self.customer_view_page.verify_order_link()

        self.step("Verify product title")
        self.customer_view_page.verify_product_title(order_page)

    @pytest.mark.QABSE_86
    def test_view_refund_history(self):
        """Verify that a user can view the refunds history on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("14046903")

        self.step("Verify refund history")
        self.customer_view_page.verify_refund_history()

        self.step("Click paging button")
        self.customer_view_page.click_paging_button()

        self.step("Click items per page")
        self.customer_view_page.click_items_per_page()

    @pytest.mark.QABA_85
    def test_view_ssr_history(self):
        """Verify that a user can view self service refund history on the customer view page"""

        self.step("Search for customer")
        self.top_nav.search_for_customer("1322249")

        self.step("Verify SSR history")
        self.customer_view_page.verify_ssr_history()

    @pytest.mark.QABA_247
    def test_upload_and_remove_id_document(self):
        """Verify that a user can Upload & Remove ID document on the customer view page"""

        self.step("Get orders from database")
        # This would need to be implemented or adapted to match the existing functionality
        # Using a sample approach assuming utils.database_utils has a method for this
        order_ids = self.utils.get_orders_from_database("paygate_sql")

        self.step("Search for order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Upload and remove ID document")
        customer_id_doc_path = self.config.get_doc_path("Customer_ID.jpeg")
        self.customer_view_page.upload_valid_id_doc(customer_id_doc_path)
        self.customer_view_page.remove_id_doc()
