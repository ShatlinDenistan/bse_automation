from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
addresses_accordion = ("//span[contains(text(),'Addresses')]", "Addresses Accordion")
address_google_icon = ("//*[@class='map small icon']", "Address Google Icon")
allocate_credit_btn = ("//button[contains(text(),'Allocate credit')]", "Allocate Credit Button")
credit_history_table = ("//*[@class='ui small celled compact table']", "Credit History Table")
available_credit = ("//*[@class='ui green small circular horizontal label']", "Available Credit")
customer_credit_accordion = ("//span[contains(text(),'Customer Credit')]", "Customer Credit Accordion")
email_google_icon = ("//*[@class='google icon']", "Email Google Icon")
email_logs_accordion = ("//span[contains(text(),'Email Logs')]", "Email Logs Accordion")
email_cards = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[12]/div/div[1]", "Email Cards")
fin_notes_dropdown = ("//span[contains(text(),'Fin Notes')]", "Fin Notes Dropdown")
fin_notes_edit_btn = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/button", "Fin Notes Edit Button")
notes_dropdown = ("//span[contains(text(),'Notes')]", "Notes Dropdown")
notes_edit_btn = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/button", "Notes Edit Button")
name_google_icon = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/i", "Name Google Icon")
modified_date = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]", "Modified Date")
refund_history_accordion = ("//span[contains(text(),'Refund History')]", "Refund History Accordion")
refund_history_table = ("//*[@class='ui small celled structured compact table']", "Refund History Table")
returns_history_accordion = ("//span[contains(text(),'Returns History')]", "Returns History Accordion")
returns_table = ("//*[@class='ui small celled table']", "Returns Table")
registered_date = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]", "Registered Date")
verified_cellphone_icon = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div", "Verified Cellphone Icon")
zendesk_ticket_accordion = ("//span[contains(text(),'Zendesk Tickets')]", "Zendesk Ticket Accordion")
fraud_reason_ddl = ("//div[contains(text(),'Fraud Reason')]", "Fraud Reason Dropdown")
fraud_reason_id = ("//span[contains(text(),'Returns abuse')]", "Fraud Reason Returns Abuse")
fin_notes = ("//input[@name='finNote']", "Fin Notes Input")
submit_blacklist_customer = ("//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]", "Submit Blacklist Customer Button")
popup = ("//*[@id='noty_layout__topRight']", "Popup Message")
blacklist_btn = ("//button[contains(text(),'Blacklist Customer')]", "Blacklist Customer Button")
credit_amount_txt = ("//input[@name='amount']", "Credit Amount Input")
credit_reason_ddl = ("//div[@name='reason']", "Credit Reason Dropdown")
credit_reason = ("//*[contains(text(),'B2B bulk orders')]", "Credit Reason B2B Bulk Orders")
admin_notes = ("//textarea[@name='adminNote']", "Admin Notes Textarea")
add_credit_btn = ("//button[@class='ui blue button']", "Add Credit Button")
ok_btn = ("//button[@class='ui primary button']", "OK Button")
edit_customer_btn = ("//button[contains(text(),'Customer Info')]", "Edit Customer Button")
cust_name = ("//input[@name='customerFirstName']", "Customer First Name Input")
cust_surname = ("//input[@name='customerSurname']", "Customer Surname Input")
business_name = ("//input[@name='businessName']", "Business Name Input")
vat_number = ("//input[@name='vatNumber']", "VAT Number Input")
acc_status_ddl = ("//div[@name='accountStatus']", "Account Status Dropdown")
acc_status = ("//span[text()='suspended']", "Account Status Suspended")
fraud_reason_list = ("//div[@name='fraudReasonID']", "Fraud Reason List Dropdown")
fraud_reason = ("//span[text()='Coupon abuse']", "Fraud Reason Coupon Abuse")
staff_account_check = ("//label[text()='Staff Account']", "Staff Account Checkbox")
block_vou_check = ("//label[text()='Block Vouchers']", "Block Vouchers Checkbox")
confirm_btn = ("//button[contains(text(),'Confirm')]", "Confirm Button")
email_customer_btn = ("//button[contains(text(),'Email Customer')]", "Email Customer Button")
ddl_email_templates = ("//div[@name='emailTemplate']", "Email Templates Dropdown")
email_modal_customer_id = ("//input[@name='customerId']", "Email Modal Customer ID Input")
email_modal_order_id = ("//input[@name='orderId']", "Email Modal Order ID Input")
email_modal_subject = ("//input[@name='emailSubject']", "Email Modal Subject Input")
email_modal_body = ("//textarea[@name='emailBody']", "Email Modal Body Textarea")
send_email_btn = ("//button[contains(text(),'Send Email')]", "Send Email Button")
latest_email_sent = ("//*[@class='ui fluid card email-card']/div/div/span/a/span[1]", "Latest Email Sent")
address_cards = ("//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/div", "Address Cards")
notes_accordion = ("//span[contains(text(),'Notes')]", "Notes Accordion")
note_btn = ("//button[contains(text(),'Note')]", "Note Button")
add_notes_text_field = ("//textarea[@name='customerNote']", "Add Notes Text Field")
add_note_btn = ("//button[contains(text(),'Add Note')]", "Add Note Button")
note_added_message = ("//*[@class='noty_body']", "Note Added Message")
audit_logs_icon = ("//*[@class='list alternate outline icon link']", "Audit Logs Icon")
audit_log_results = ("//*[@class='ui striped basic very compact table']", "Audit Log Results")
sales_history_accordion = ("//span[contains(text(),'Sales History')]", "Sales History Accordion")
sales_history_table = ("//*[@class='ui small celled striped compact table']", "Sales History Table")
order_id = ("//*[@id='root']/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[1]/a", "Order ID Link")
order_id_pg2 = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]", "Order ID Page 2")
product_title_pg1 = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a", "Product Title Page 1")
product_title_pg2 = ("//*[@id='root']/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[6]", "Product Title Page 2")
show_10_items_ddl = ("//div[contains(text(),'Show 10 Items')]", "Show 10 Items Dropdown")
show_30_items_ddl = ("//div[contains(text(),'Show 30 Items')]", "Show 30 Items Dropdown")
show_30_order_items = ("//span[contains(text(),'30')]", "Show 30 Order Items")
show_10_order_items = ("//span[contains(text(),'10')]", "Show 10 Order Items")
order_items_accordion = ("//span[contains(text(),'Order Items')]", "Order Items Accordion")
order_link = ("//*[@id='root']/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[5]/a", "Order Link")
next_page = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[12]/div/div[2]/a[4]", "Next Page Button")
prev_page = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[6]/div/div[2]/a[1]", "Previous Page Button")
refund_type_column = ("//*[@id='root']/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[9]", "Refund Type Column")
upload_id = ("//button[contains(text(),'Upload')]", "Upload Button")
upload_field = ("//input[@type='file']", "Upload Field")
documents_accordion = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[13]", "Documents Accordion")
remove_id = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[14]/div/div/div/div[2]/ol/a[2]", "Remove ID")
confirm_upload = ("//*[@class='ui primary button']", "Confirm Upload")


class CustomerViewPage(PageBase):
    """Page object for Customer View functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        # Initialize all locators
        self.addresses_accordion = self.locator(addresses_accordion)
        self.address_google_icon = self.locator(address_google_icon)
        self.allocate_credit_btn = self.locator(allocate_credit_btn)
        self.credit_history_table = self.locator(credit_history_table)
        self.available_credit = self.locator(available_credit)
        self.customer_credit_accordion = self.locator(customer_credit_accordion)
        self.email_google_icon = self.locator(email_google_icon)
        self.email_logs_accordion = self.locator(email_logs_accordion)
        self.email_cards = self.locator(email_cards)
        self.fin_notes_dropdown = self.locator(fin_notes_dropdown)
        self.fin_notes_edit_btn = self.locator(fin_notes_edit_btn)
        self.notes_dropdown = self.locator(notes_dropdown)
        self.notes_edit_btn = self.locator(notes_edit_btn)
        self.name_google_icon = self.locator(name_google_icon)
        self.modified_date = self.locator(modified_date)
        self.refund_history_accordion = self.locator(refund_history_accordion)
        self.refund_history_table = self.locator(refund_history_table)
        self.returns_history_accordion = self.locator(returns_history_accordion)
        self.returns_table = self.locator(returns_table)
        self.registered_date = self.locator(registered_date)
        self.verified_cellphone_icon = self.locator(verified_cellphone_icon)
        self.zendesk_ticket_accordion = self.locator(zendesk_ticket_accordion)
        self.fraud_reason_ddl = self.locator(fraud_reason_ddl)
        self.fraud_reason_id = self.locator(fraud_reason_id)
        self.fin_notes = self.locator(fin_notes)
        self.submit_blacklist_customer = self.locator(submit_blacklist_customer)
        self.popup = self.locator(popup)
        self.blacklist_btn = self.locator(blacklist_btn)
        self.credit_amount_txt = self.locator(credit_amount_txt)
        self.credit_reason_ddl = self.locator(credit_reason_ddl)
        self.credit_reason = self.locator(credit_reason)
        self.admin_notes = self.locator(admin_notes)
        self.add_credit_btn = self.locator(add_credit_btn)
        self.ok_btn = self.locator(ok_btn)
        self.edit_customer_btn = self.locator(edit_customer_btn)
        self.cust_name = self.locator(cust_name)
        self.cust_surname = self.locator(cust_surname)
        self.business_name = self.locator(business_name)
        self.vat_number = self.locator(vat_number)
        self.acc_status_ddl = self.locator(acc_status_ddl)
        self.acc_status = self.locator(acc_status)
        self.fraud_reason_list = self.locator(fraud_reason_list)
        self.fraud_reason = self.locator(fraud_reason)
        self.staff_account_check = self.locator(staff_account_check)
        self.block_vou_check = self.locator(block_vou_check)
        self.confirm_btn = self.locator(confirm_btn)
        self.email_customer_btn = self.locator(email_customer_btn)
        self.ddl_email_templates = self.locator(ddl_email_templates)
        self.email_modal_customer_id = self.locator(email_modal_customer_id)
        self.email_modal_order_id = self.locator(email_modal_order_id)
        self.email_modal_subject = self.locator(email_modal_subject)
        self.email_modal_body = self.locator(email_modal_body)
        self.send_email_btn = self.locator(send_email_btn)
        self.latest_email_sent = self.locator(latest_email_sent)
        self.address_cards = self.locator(address_cards)
        self.notes_accordion = self.locator(notes_accordion)
        self.note_btn = self.locator(note_btn)
        self.add_notes_text_field = self.locator(add_notes_text_field)
        self.add_note_btn = self.locator(add_note_btn)
        self.note_added_message = self.locator(note_added_message)
        self.audit_logs_icon = self.locator(audit_logs_icon)
        self.audit_log_results = self.locator(audit_log_results)
        self.sales_history_accordion = self.locator(sales_history_accordion)
        self.sales_history_table = self.locator(sales_history_table)
        self.order_id = self.locator(order_id)
        self.order_id_pg2 = self.locator(order_id_pg2)
        self.product_title_pg1 = self.locator(product_title_pg1)
        self.product_title_pg2 = self.locator(product_title_pg2)
        self.show_10_items_ddl = self.locator(show_10_items_ddl)
        self.show_30_items_ddl = self.locator(show_30_items_ddl)
        self.show_30_order_items = self.locator(show_30_order_items)
        self.show_10_order_items = self.locator(show_10_order_items)
        self.order_items_accordion = self.locator(order_items_accordion)
        self.order_link = self.locator(order_link)
        self.next_page = self.locator(next_page)
        self.prev_page = self.locator(prev_page)
        self.refund_type_column = self.locator(refund_type_column)
        self.upload_id = self.locator(upload_id)
        self.upload_field = self.locator(upload_field)
        self.documents_accordion = self.locator(documents_accordion)
        self.remove_id = self.locator(remove_id)
        self.confirm_upload = self.locator(confirm_upload)

    def verify_customer_details(self):
        """Verify customer details including name and email"""
        self.expect_to_be_visible(self.page.locator("text=Brian Delta"))
        self.click(self.name_google_icon)
        self.wait_for_seconds(2)
        window_handles = self.page.context.pages
        self.page.bring_to_front()
        self.expect_to_be_visible(self.page.locator("text=dev+1@take2.co.za"))
        self.click(self.email_google_icon)
        self.wait_for_seconds(2)
        window_handles = self.page.context.pages
        self.page.bring_to_front()
        self.expect_to_be_visible(self.verified_cellphone_icon)

    def verify_notes_section_with_edit_option(self):
        """Verify notes section with edit option"""
        self.expect_to_be_visible(self.notes_dropdown)
        self.click(self.notes_dropdown)
        self.expect_to_be_visible(self.notes_edit_btn)
        self.click(self.notes_edit_btn)

    def verify_fin_notes_section_with_edit_option(self):
        """Verify fin notes section with edit option"""
        self.expect_to_be_visible(self.fin_notes_dropdown)
        self.click(self.fin_notes_dropdown)
        self.expect_to_be_visible(self.fin_notes_edit_btn)
        self.click(self.fin_notes_edit_btn)

    def verify_customer_credit(self):
        """Verify customer credit section elements"""
        self.expect_to_be_visible(self.customer_credit_accordion)
        self.expect_to_be_visible(self.available_credit)
        self.expect_to_be_visible(self.allocate_credit_btn)
        self.expect_to_be_visible(self.credit_history_table)

    def verify_customer_address(self):
        """Verify customer addresses"""
        self.expect_to_be_visible(self.addresses_accordion)
        self.click(self.addresses_accordion)
        addresses = self.address_cards.all()

        for _ in addresses:
            self.expect_to_be_visible(self.address_google_icon)
            self.click(self.address_google_icon)
            self.wait_for_seconds(2)
            window_handles = self.page.context.pages
            self.page.bring_to_front()

    def verify_email_logs(self):
        """Verify email logs section"""
        self.expect_to_be_visible(self.email_logs_accordion)
        self.click(self.email_logs_accordion)
        self.expect_to_be_visible(self.email_cards)

    def verify_customer_returns_history(self):
        """Verify customer returns history"""
        self.expect_to_be_visible(self.customer_credit_accordion)
        self.click(self.customer_credit_accordion)
        self.expect_to_be_visible(self.returns_history_accordion)
        self.click(self.returns_history_accordion)
        self.expect_to_be_visible(self.returns_table)

    def verify_zendesk_tickets(self):
        """Verify zendesk tickets section"""
        self.expect_to_be_visible(self.zendesk_ticket_accordion)
        self.click(self.zendesk_ticket_accordion)

    def verify_registered_and_last_modified_dates(self):
        """Verify registered and last modified dates"""
        self.expect_to_be_visible(self.registered_date)
        self.expect_to_be_visible(self.modified_date)

    def blacklist_a_customer(self):
        """Blacklist a customer"""
        self.expect_to_be_visible(self.blacklist_btn)
        self.click(self.blacklist_btn)
        self.click(self.fraud_reason_ddl)
        self.click(self.fraud_reason_id)
        self.fill(self.fin_notes, "Automation Testing")
        self.click(self.submit_blacklist_customer)
        # Accept alert
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.expect_to_be_visible(self.popup)
        popup_text = self.text_content(self.popup)
        assert "Successfully blacklisted the customer" in popup_text, f"Expected success message, got: {popup_text}"

    def add_credit(self):
        """Add credit to customer account"""
        self.click(self.allocate_credit_btn)
        self.wait_for_seconds(1)
        self.click(self.credit_reason_ddl)
        self.click(self.credit_reason)
        # Generate random credit amount
        credit_amount = str(self.faker.random_int(min=100, max=999))
        self.fill(self.credit_amount_txt, credit_amount)
        self.fill(self.admin_notes, "Good will")
        self.click(self.add_credit_btn)
        self.click(self.ok_btn)
        self.expect_to_be_visible(self.popup)
        popup_text = self.text_content(self.popup)
        assert "Successfully credited user" in popup_text, f"Expected success message, got: {popup_text}"
        return credit_amount

    def edit_customer(self):
        """Edit customer details"""
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
        self.expect_to_be_visible(self.popup)
        popup_text = self.text_content(self.popup)
        assert "Customer status data updated successfully" in popup_text, f"Expected success message, got: {popup_text}"

    def send_generic_email(self):
        """Send a generic email to the customer"""
        self.click(self.email_customer_btn)
        self.expect_to_be_visible(self.ddl_email_templates)
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Tab")
        self.wait_for_seconds(1)
        self.page.keyboard.press("Tab")
        subject_text = "Automation Test Email Subject"
        self.fill(self.email_modal_subject, subject_text)
        self.fill(self.email_modal_body, "Automation Test Email Subject 123 %*$&")
        self.click(self.send_email_btn)
        return subject_text

    def view_email_logs_for_latest_email_sent(self, subject_text):
        """View email logs for the latest email sent"""
        self.page.reload()
        self.expect_to_be_visible(self.email_logs_accordion)
        self.click(self.email_logs_accordion)
        latest_email_text = self.text_content(self.latest_email_sent)
        assert subject_text == latest_email_text, f"Expected email subject '{subject_text}', got '{latest_email_text}'"

    def add_admin_note(self):
        """Add an admin note to the customer"""
        self.expect_to_be_visible(self.notes_accordion)
        self.click(self.notes_accordion)
        self.click(self.note_btn)
        self.fill(self.add_notes_text_field, "Automation Admin Note")
        self.click(self.add_note_btn)
        self.expect_to_be_visible(self.note_added_message)
        note_message = self.text_content(self.note_added_message)
        assert "Note successfully added to Customer" in note_message, f"Expected success message, got: {note_message}"

    def view_audit_logs(self):
        """View audit logs for the customer"""
        self.expect_to_be_visible(self.audit_logs_icon)
        self.click(self.audit_logs_icon)
        self.expect_to_be_visible(self.audit_log_results)

    def verify_order_link(self):
        """Verify order link functionality"""
        self.expect_to_be_visible(self.customer_credit_accordion)
        self.click(self.customer_credit_accordion)
        self.click(self.sales_history_accordion)
        order_id_text = self.text_content(self.order_id)
        self.click(self.order_id)
        self.wait_for_seconds(2)
        window_handles = self.page.context.pages
        # Switch to new page
        new_page = window_handles[-1]
        order_id_pg2_text = self.text_content(self.order_id_pg2)
        assert order_id_text == order_id_pg2_text, f"Expected order ID '{order_id_text}', got '{order_id_pg2_text}'"
        self.page.bring_to_front()

    def verify_product_title(self):
        """Verify product title matches between pages"""
        product_title1 = self.text_content(self.product_title_pg1)
        window_handles = self.page.context.pages
        self.page.bring_to_front()
        product_title2 = self.text_content(self.product_title_pg2)
        assert product_title1 == product_title2, f"Expected product title '{product_title1}', got '{product_title2}'"

    def verify_refund_history(self):
        """Verify refund history section"""
        self.click(self.customer_credit_accordion)
        self.click(self.refund_history_accordion)
        self.expect_to_be_visible(self.refund_history_table)
        self.click(self.order_link)

    def click_paging_button(self):
        """Click paging buttons in order details"""
        window_handles = self.page.context.pages
        # Switch to new page
        new_page = window_handles[-1]
        self.expect_to_be_visible(self.order_items_accordion)
        self.click(self.show_10_items_ddl)
        self.click(self.show_30_order_items)
        self.click(self.show_30_items_ddl)
        self.click(self.show_10_order_items)
        self.page.bring_to_front()

    def click_items_per_page(self):
        """Click items per page navigation buttons"""
        self.click(self.next_page)
        self.click(self.prev_page)

    def verify_ssr_history(self):
        """Verify self-service refund history"""
        self.click(self.customer_credit_accordion)
        self.click(self.refund_history_accordion)
        self.expect_to_be_visible(self.refund_history_table)

        refund_types = self.refund_type_column.all()
        found_ssr = False

        for refund_type in refund_types:
            text = refund_type.text_content()
            if text == "SelfService":
                found_ssr = True
                break

        assert found_ssr, "Self Service Refund not found"

    def upload_valid_id_doc(self, csv_file):
        """Upload a valid ID document"""
        self.click(self.documents_accordion)
        self.upload_field.set_input_files(csv_file)
        self.click(self.upload_id)
        self.wait_for_seconds(5)
        self.expect_to_be_visible(self.popup)

    def remove_id_doc(self):
        """Remove an ID document"""
        self.click(self.remove_id)
        self.click(self.confirm_upload)
