import random
import string

from pos.customer_view_po import CustomerViewPO


class CustomerViewPage(CustomerViewPO):
    """Page class for Customer View page with business logic methods"""

    def verify_customer_details(self):
        """Verify that customer details are displayed correctly"""
        self.step("Verify customer details")

        self.page.wait_for_selector("text=Brian Delta")
        self.click(self.name_google_icon)
        self.wait_for_seconds(2)

        window_handles = self.page.context.pages
        self.page.bring_to_front()

        self.page.wait_for_selector("text=dev+1@take2.co.za")
        self.click(self.email_google_icon)
        self.wait_for_seconds(2)

        window_handles = self.page.context.pages
        self.page.bring_to_front()

        assert self.verified_cellphone_icon.is_visible(), "Verified cellphone icon is not visible"

    def verify_notes_section_with_edit_option(self):
        """Verify notes section with edit option"""
        self.step("Verify notes section with edit option")

        self.page.wait_for_selector(self.notes_dropdown)
        self.click(self.notes_dropdown)
        assert self.notes_edit_btn.is_visible(), "Notes edit button is not visible"
        self.click(self.notes_edit_btn)

    def verify_fin_notes_section_with_edit_option(self):
        """Verify fin notes section with edit option"""
        self.step("Verify fin notes section with edit option")

        self.page.wait_for_selector(self.fin_notes_dropdown)
        self.click(self.fin_notes_dropdown)
        assert self.fin_notes_edit_btn.is_visible(), "Fin notes edit button is not visible"
        self.click(self.fin_notes_edit_btn)

    def verify_customer_credit(self):
        """Verify customer credit details"""
        self.step("Verify customer credit section")

        self.page.wait_for_selector(self.customer_credit_accordion)
        assert self.available_credit.is_visible(), "Available credit is not visible"
        assert self.allocate_credit_btn.is_visible(), "Allocate credit button is not visible"
        assert self.credit_history_table.is_visible(), "Credit history table is not visible"

    def verify_customer_address(self):
        """Verify customer address details"""
        self.step("Verify customer address")

        self.page.wait_for_selector(self.addresses_accordion)
        self.click(self.addresses_accordion)

        addresses = self.page.query_selector_all(self.address_cards.selector)
        for address in addresses:
            address_google_icon = self.page.locator(self.address_google_icon.selector)
            assert address_google_icon.is_visible(), "Address Google icon is not visible"
            self.click(address_google_icon)
            self.wait_for_seconds(2)

            window_handles = self.page.context.pages
            self.page.bring_to_front()

    def verify_email_logs(self):
        """Verify email logs section"""
        self.step("Verify email logs")

        self.page.wait_for_selector(self.email_logs_accordion)
        self.click(self.email_logs_accordion)
        assert self.email_cards.is_visible(), "Email cards are not visible"

    def verify_customer_returns_history(self):
        """Verify customer returns history"""
        self.step("Verify customer returns history")

        self.page.wait_for_selector(self.customer_credit_accordion)
        self.click(self.customer_credit_accordion)

        self.page.wait_for_selector(self.returns_history_accordion)
        self.click(self.returns_history_accordion)
        assert self.returns_table.is_visible(), "Returns table is not visible"

    def verify_zendesk_tickets(self):
        """Verify zendesk tickets section"""
        self.step("Verify zendesk tickets")

        self.page.wait_for_selector(self.zendesk_ticket_accordion)
        self.click(self.zendesk_ticket_accordion)

    def verify_registered_and_last_modified_dates(self):
        """Verify registered and last modified dates"""
        self.step("Verify registered and last modified dates")

        assert self.registered_date.is_visible(), "Registered date is not visible"
        assert self.modified_date.is_visible(), "Modified date is not visible"

    def blacklist_a_customer(self):
        """Blacklist a customer"""
        self.step("Blacklist a customer")

        self.page.wait_for_selector(self.blacklist_btn)
        self.click(self.blacklist_btn)
        self.click(self.fraud_reason_ddl)
        self.click(self.fraud_reason_id)
        self.fill(self.fin_notes, "Automation Testing")
        self.click(self.submit_blacklist_customer)

        self.page.on("dialog", lambda dialog: dialog.accept())

        self.page.wait_for_selector(self.popup)
        popup_message = self.popup.text_content()
        assert "Successfully blacklisted the customer" in popup_message, "Failed to blacklist customer"

    def add_credit(self):
        """Add credit to customer account"""
        self.step("Add credit to customer")

        self.click(self.allocate_credit_btn)
        self.wait_for_seconds(2)
        self.click(self.credit_reason_ddl)
        self.click(self.credit_reason)

        credit_amount = "".join(random.choices(string.digits, k=3))
        self.fill(self.credit_amount_txt, credit_amount)
        self.fill(self.admin_notes, "Good will")
        self.click(self.add_credit_btn)
        self.click(self.ok_btn)

        self.page.wait_for_selector(self.popup)
        popup_message = self.popup.text_content()
        assert "Successfully credited user" in popup_message, "Failed to add credit"

    def edit_customer(self):
        """Edit customer information"""
        self.step("Edit customer information")

        self.click(self.edit_customer_btn)
        self.fill(self.cust_name, "Mike")
        self.fill(self.cust_surname, "Jackson")
        self.fill(self.business_name, "Automation Test PTY LTD")
        self.fill(self.vat_number, "9876543211")
        self.click(self.acc_status_ddl)
        self.click(self.acc_status)
        self.click(self.fraud_reason_list)
        self.click(self.fraud_reason)
        self.click(self.staff_account_check)
        self.click(self.block_vou_check)
        self.click(self.confirm_btn)

        self.page.wait_for_selector(self.popup)
        popup_message = self.popup.text_content()
        assert "Customer status data updated successfully" in popup_message, "Failed to update customer status"

    def send_generic_email(self):
        """Send a generic email to customer"""
        self.step("Send generic email to customer")

        self.click(self.email_customer_btn)
        self.page.wait_for_selector(self.ddl_email_templates)

        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Tab")
        self.wait_for_seconds(1)
        self.page.keyboard.press("Tab")

        subject_text = "Automation Test Email Subject"
        self.fill(self.email_modal_subject, subject_text)
        self.fill(self.email_modal_body, "Automation Test Email Subject 123 %*$&")

        self.page.evaluate("element => element.scrollIntoView()", self.send_email_btn)
        self.click(self.send_email_btn)
        return subject_text

    def view_email_logs_for_latest_email_sent(self, expected_subject):
        """View email logs for the latest email sent"""
        self.step("View email logs for latest email sent")

        self.page.reload()
        self.page.wait_for_selector(self.email_logs_accordion)
        self.click(self.email_logs_accordion)

        latest_email_subject = self.latest_email_sent.text_content()
        assert latest_email_subject == expected_subject, f"Expected subject '{expected_subject}' but got '{latest_email_subject}'"

    def add_admin_note(self):
        """Add admin note to customer"""
        self.step("Add admin note to customer")

        self.page.wait_for_selector(self.notes_accordion)
        self.click(self.notes_accordion)
        self.click(self.note_btn)
        self.fill(self.add_notes_text_field, "Automation Admin Note")
        self.click(self.add_note_btn)

        self.page.wait_for_selector(self.note_added_message)
        note_message = self.note_added_message.text_content()
        assert "Note successfully added to Customer" in note_message, "Failed to add note"

    def view_audit_logs(self):
        """View audit logs"""
        self.step("View audit logs")

        self.page.wait_for_selector(self.audit_logs_icon)
        self.click(self.audit_logs_icon)
        assert self.audit_log_results.is_visible(), "Audit log results are not visible"

    def verify_order_link(self):
        """Verify order link functionality"""
        self.step("Verify order link")

        self.page.wait_for_selector(self.customer_credit_accordion)
        self.click(self.customer_credit_accordion)
        self.click(self.sales_history_accordion)

        order_id1 = self.order_id.text_content()
        self.click(self.order_id)

        window_handles = self.page.context.pages
        new_page = window_handles[-1]

        order_id2 = new_page.locator(self.order_id_pg2.selector).text_content()
        assert order_id1 == order_id2, f"Order IDs don't match: {order_id1} vs {order_id2}"

        return new_page

    def verify_product_title(self, order_page):
        """Verify product title matches between pages"""
        self.step("Verify product title")

        product_title1 = order_page.locator(self.product_title_pg1.selector).text_content()

        # Switch back to main page
        self.page.bring_to_front()

        product_title2 = self.product_title_pg2.text_content()
        assert product_title1 == product_title2, f"Product titles don't match: {product_title1} vs {product_title2}"

    def verify_refund_history(self):
        """Verify refund history"""
        self.step("Verify refund history")

        self.click(self.customer_credit_accordion)
        self.click(self.refund_history_accordion)
        assert self.refund_history_table.is_visible(), "Refund history table is not visible"
        self.click(self.order_link)

    def click_paging_button(self):
        """Click paging buttons"""
        self.step("Click paging buttons")

        window_handles = self.page.context.pages
        order_page = window_handles[-1]

        order_page.wait_for_selector(self.order_items_accordion.selector)
        order_page.evaluate("element => element.scrollIntoView()", order_page.locator(self.show_10_items_ddl.selector))
        order_page.locator(self.show_10_items_ddl.selector).click()
        order_page.locator(self.show_30_order_items.selector).click()

        order_page.evaluate("element => element.scrollIntoView()", order_page.locator(self.show_30_items_ddl.selector))
        order_page.locator(self.show_30_items_ddl.selector).click()
        order_page.locator(self.show_10_order_items.selector).click()

    def click_items_per_page(self):
        """Click items per page controls"""
        self.step("Click items per page controls")

        window_handles = self.page.context.pages
        order_page = window_handles[-1]

        order_page.evaluate("element => element.scrollIntoView()", order_page.locator(self.show_10_items_ddl.selector))
        order_page.locator(self.next_page.selector).click()
        order_page.locator(self.prev_page.selector).click()

    def verify_ssr_history(self):
        """Verify self-service refund history"""
        self.step("Verify self-service refund history")

        self.click(self.customer_credit_accordion)
        self.click(self.refund_history_accordion)

        self.page.wait_for_selector(self.refund_history_table, timeout=60000)

        refund_types = self.page.locator(self.refund_type_column.selector).all()
        found = False

        for refund in refund_types:
            if refund.text_content() == "SelfService":
                found = True
                break

        assert found, "Self Service Refund not found"

    def upload_valid_id_doc(self, csv_file_path):
        """Upload a valid ID document"""
        self.step("Upload valid ID document")

        self.page.evaluate("element => element.scrollIntoView()", self.documents_accordion)
        self.click(self.documents_accordion)

        with self.page.expect_file_chooser() as fc_info:
            self.click(self.upload_field)
            file_chooser = fc_info.value
            file_chooser.set_files(csv_file_path)

        self.click(self.upload_id)
        self.wait_for_seconds(5)
        assert self.popup.is_visible(), "Upload confirmation popup not visible"

    def remove_id_doc(self):
        """Remove ID document"""
        self.step("Remove ID document")

        self.click(self.remove_id)
        self.click(self.confirm_upload)
