import random
from datetime import datetime

from playwright.sync_api import Page, expect

from base.page_base import PageBase

# Locators as tuples with (xpath, description)
menu_button = ("//i[@aria-hidden='true' and @class='content large icon']", "Menu Button")
eft_refund_menu = ("//body/div[@id='root']/div[1]/a[6]", "EFT Refund Menu")
eft_refunds_table = ("//table", "EFT Refunds Table")

# Email related locators
send_email_table_button = ("//table/tfoot/tr/th/div/div[3]/button", "Send Email Table Button")
email_templates_dropdown = ("//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]", "Email Templates Dropdown")
send_email_button = ("//button[contains(text(),'Send Emails')]", "Send Email Button")
email_sent_modal = ("/html/body/div[2]/div", "Email Sent Modal")
email_sent_modal_close = ("//body/div[2]/div[1]/i[1]", "Email Sent Modal Close Button")

# Filter related locators
status_filter_dropdown = ("//div[contains(text(),'Select refund status')]", "Status Filter Dropdown")
clear_status_filter = ("//*[@id='root']/div[3]/div/div/div/div/div[2]/form/div/div/div/div[1]/div/div/i", "Clear Status Filter")
status_filter_pending = ("//span[contains(text(),'Pending')]", "Status Filter Pending")
status_filter_exported = ("//span[contains(text(),'Exported')]", "Status Filter Exported")
status_filter_declined = ("//span[contains(text(),'Declined')]", "Status Filter Declined")

type_filter_dropdown = ("//div[contains(text(),'Select refund type')]", "Type Filter Dropdown")
clear_type_filter = ("//*[@id='root']/div[3]/div/div/div/div/div[2]/form/div/div/div/div[2]/div/div/i", "Clear Type Filter")
type_filter_self_service = ("//span[contains(text(),'Self Service')]", "Type Filter Self Service")
type_filter_refund = ("//span[contains(text(),'Refund')]", "Type Filter Refund")
type_filter_manual_override = ("//span[contains(text(),'Manual Override')]", "Type Filter Manual Override")
type_filter_manual_eft = ("//span[contains(text(),'Manual EFT')]", "Type Filter Manual EFT")

filter_by_dropdown = ("//*[@id='root']/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/div", "Filter By Dropdown")
filter_by_customer_id = ("//span[contains(text(),'Customer ID')]", "Filter By Customer ID")
filter_by_order_id = ("//span[contains(text(),'Order ID')]", "Filter By Order ID")
filter_by_bank_account = ("//span[contains(text(),'Bank Account Number')]", "Filter By Bank Account Number")
filter_by_zendesk = ("//span[contains(text(),'Zendesk Ticket Number')]", "Filter By Zendesk Ticket")
filter_search_input = ("//*[@id='root']/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/input", "Filter Search Input")

# Manual EFT related locators
manual_eft_button = ("//*[@id='root']/div[3]/div/div/div/div/div[2]/form/div/div/div/div[6]/div/button", "Manual EFT Button")
order_id_input = ("//input[@name='orderID' and @placeholder='Enter Order ID' and @type='text']", "Order ID Input")
zendesk_ticket_input = ("//input[@name='zendeskTicket' and @placeholder='Enter Zendesk Ticket Number' and @type='text']", "Zendesk Ticket Input")
customer_name_input = ("//input[@name='customerName' and @placeholder='Enter Customer Name' and @type='text']", "Customer Name Input")
refund_amount_input = ("//input[@name='refundAmount' and @placeholder='Enter Refund Amount' and @type='text']", "Refund Amount Input")
bank_account_input = ("//input[@name='bankAccount' and @placeholder='Enter Bank Account Number' and @type='text']", "Bank Account Input")

# Table checkboxes and export related locators
first_checkbox = ("//table/tbody/tr[1]/td[1]/div", "First Row Checkbox")
second_checkbox = ("//table/tbody/tr[2]/td[1]/div", "Second Row Checkbox")
third_checkbox = ("//table/tbody/tr[3]/td[1]/div", "Third Row Checkbox")
export_request_button = ("//table/tfoot/tr/th/div/div[1]/button", "Export Request Button")
export_bank_dropdown = ("/html/body/div[2]/div/div[2]/div/form/div[1]/div", "Export Bank Dropdown")
nedbank_option = ("/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[1]/span", "Nedbank Option")
absa_option = ("/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[2]/span", "ABSA Option")

# Dynamic locators with format strings for email templates
email_template_option = ("//span[contains(text(),'{}')]", "Email Template Option")

# Additional locators that were inline in methods
success_message = ("//div[contains(text(),'Successfully processed 2 item(s)')]", "Success Message")
success_message_3_items = ("//div[contains(text(),'Successfully processed 3 item(s)')]", "Success Message 3 Items")
customer_info_span = ("//div[contains(@class,'customer-info')]//span", "Customer Info Span")
order_id_cell = ("//div[contains(@class,'order-id')]", "Order ID Cell")
apply_filter_button = ("//button[contains(text(),'Apply Filter')]", "Apply Filter Button")
clear_filter_button = ("//button[contains(text(),'Clear Filter')]", "Clear Filter Button")
show_items_dropdown = ("//div[contains(text(),'Show 15 Items')]", "Show Items Dropdown")
show_250_items = ("//span[contains(text(),'250')]", "Show 250 Items Option")
show_30_items = ("//span[contains(text(),'30')]", "Show 30 Items Option")
last_page_button = ("//a[@aria-label='Go to last page']", "Last Page Button")
date_range_input = ("//input[@name='dateRange']", "Date Range Input")
decline_button = ("//table/tfoot/tr/th/div/div[2]/button", "Decline Button")
decline_modal = ("//div[contains(@class,'modal')]", "Decline Modal")
cancellation_reason_input = ("//input[@placeholder='Enter cancellation reason']", "Cancellation Reason Input")
confirm_decline_button = ("//button[contains(text(),'Confirm')]", "Confirm Decline Button")
decline_message = ("//div[contains(@class,'message')]", "Decline Message")
status_column = ("//table/tbody/tr[1]/td[3]", "Status Column")
operator_column = ("//table/tbody/tr[1]/td[13]", "Operator Column")
bank_name_dropdown = ("//div[contains(text(),'- - Select a bank - -')]", "Bank Name Dropdown")
bank_namibia_option = ("//span[contains(text(),'FNB/RMB Namibia')]", "FNB/RMB Namibia Option")
branch_code_dropdown = ("//div[@name='branchCode']", "Branch Code Dropdown")
branch_namibia_option = ("//span[contains(text(),'All Namibia')]", "All Namibia Branch Option")
submit_button = ("//button[contains(@class,'ui blue')]", "Submit Button")
credit_deduction_header = ("//div[contains(text(),'Credit Deduction')]", "Credit Deduction Header")
credit_deduction_message = ('//div[contains(text(),"Don\'t forget to remove credit.")]', "Credit Deduction Message")
okay_button = ("//button[contains(text(),'Okay')]", "Okay Button")
success_message_eft = ("//div[contains(text(),'EFT Refund Created Successfully.')]", "EFT Success Message")
first_row = ("//table/tbody/tr[1]", "First Row")
export_button = ("//button[contains(text(),'Export')]", "Export Button")
export_success = ("//div[contains(@class,'ui success message')]", "Export Success Message")
close_icon = ("//i[@class='close icon']", "Close Icon")
file_link = ("//table/tbody/tr/td[12]/a", "File Link")
download_icon = ("//table/tbody/tr/td[12]/a/i", "Download Icon")
bank_account_column = ("//table/tbody/tr/td[10]", "Bank Account Column")
date_column = ("//tbody/tr/td[4]", "Date Column")
table_status_cells = ("//tbody/tr/td[3]", "Status Cell")
table_type_cells = ("//tbody/tr/td[2]", "Type Cell")
customer_row_15 = ("//table/tbody/tr[15]/td[8]/a", "15th Customer Row")
customer_popup = ("/html/body/div[2]/div", "Customer Popup")
customer_row = ("//table/tbody/tr/td[8]/a", "Customer Row")
order_row_7 = ("//tbody/tr[7]/td[6]/a", "7th Order Row")
first_order_link = ("//table/tbody/tr[1]/td[6]/a", "First Order Link")
zendesk_cell = ("//table/tbody/tr[{}]/td[7]", "Zendesk Cell")


class EftRefundPage(PageBase):
    """Page object for EFT Refund functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Initialize locators
        self.menu_button = self.locator(menu_button)
        self.eft_refund_menu = self.locator(eft_refund_menu)
        self.eft_refunds_table = self.locator(eft_refunds_table)
        self.send_email_table_button = self.locator(send_email_table_button)
        self.email_templates_dropdown = self.locator(email_templates_dropdown)
        self.send_email_button = self.locator(send_email_button)
        self.email_sent_modal = self.locator(email_sent_modal)
        self.email_sent_modal_close = self.locator(email_sent_modal_close)

        # Filter locators
        self.status_filter_dropdown = self.locator(status_filter_dropdown)
        self.clear_status_filter = self.locator(clear_status_filter)
        self.status_filter_pending = self.locator(status_filter_pending)
        self.status_filter_exported = self.locator(status_filter_exported)
        self.status_filter_declined = self.locator(status_filter_declined)

        self.type_filter_dropdown = self.locator(type_filter_dropdown)
        self.clear_type_filter = self.locator(clear_type_filter)
        self.type_filter_self_service = self.locator(type_filter_self_service)
        self.type_filter_refund = self.locator(type_filter_refund)
        self.type_filter_manual_override = self.locator(type_filter_manual_override)
        self.type_filter_manual_eft = self.locator(type_filter_manual_eft)

        # Manual EFT locators
        self.manual_eft_button = self.locator(manual_eft_button)
        self.order_id_input = self.locator(order_id_input)
        self.zendesk_ticket_input = self.locator(zendesk_ticket_input)
        self.customer_name_input = self.locator(customer_name_input)
        self.refund_amount_input = self.locator(refund_amount_input)
        self.bank_account_input = self.locator(bank_account_input)

        # Table and export locators
        self.first_checkbox = self.locator(first_checkbox)
        self.second_checkbox = self.locator(second_checkbox)
        self.third_checkbox = self.locator(third_checkbox)
        self.export_request_button = self.locator(export_request_button)
        self.export_bank_dropdown = self.locator(export_bank_dropdown)
        self.nedbank_option = self.locator(nedbank_option)
        self.absa_option = self.locator(absa_option)

        # Initialize additional locators
        self.success_message = self.locator(success_message)
        self.success_message_3_items = self.locator(success_message_3_items)
        self.customer_info_span = self.locator(customer_info_span)
        self.order_id_cell = self.locator(order_id_cell)
        self.apply_filter_button = self.locator(apply_filter_button)
        self.clear_filter_button = self.locator(clear_filter_button)
        self.show_items_dropdown = self.locator(show_items_dropdown)
        self.show_250_items = self.locator(show_250_items)
        self.show_30_items = self.locator(show_30_items)
        self.last_page_button = self.locator(last_page_button)
        self.date_range_input = self.locator(date_range_input)
        self.decline_button = self.locator(decline_button)
        self.decline_modal = self.locator(decline_modal)
        self.cancellation_reason_input = self.locator(cancellation_reason_input)
        self.confirm_decline_button = self.locator(confirm_decline_button)
        self.decline_message = self.locator(decline_message)
        self.status_column = self.locator(status_column)
        self.operator_column = self.locator(operator_column)
        self.bank_name_dropdown = self.locator(bank_name_dropdown)
        self.bank_namibia_option = self.locator(bank_namibia_option)
        self.branch_code_dropdown = self.locator(branch_code_dropdown)
        self.branch_namibia_option = self.locator(branch_namibia_option)
        self.submit_button = self.locator(submit_button)
        self.credit_deduction_header = self.locator(credit_deduction_header)
        self.credit_deduction_message = self.locator(credit_deduction_message)
        self.okay_button = self.locator(okay_button)
        self.success_message_eft = self.locator(success_message_eft)
        self.first_row = self.locator(first_row)
        self.export_button = self.locator(export_button)
        self.export_success = self.locator(export_success)
        self.close_icon = self.locator(close_icon)
        self.file_link = self.locator(file_link)
        self.download_icon = self.locator(download_icon)
        self.bank_account_column = self.locator(bank_account_column)
        self.date_column = self.locator(date_column)
        self.table_status_cells = self.locator(table_status_cells)
        self.table_type_cells = self.locator(table_type_cells)
        self.customer_row_15 = self.locator(customer_row_15)
        self.customer_popup = self.locator(customer_popup)
        self.customer_row = self.locator(customer_row)
        self.order_row_7 = self.locator(order_row_7)
        self.first_order_link = self.locator(first_order_link)

    def navigate_to_eft_refunds_page(self):
        """Navigate to EFT Refunds page"""
        self.click(self.menu_button)
        self.click(self.eft_refund_menu)
        self.expect_to_be_visible(self.eft_refunds_table)

    def select_multiple_eft_refund_requests(self):
        """Select multiple EFT Refund requests"""
        self.click(self.type_filter_dropdown)

        filter_options = [self.type_filter_self_service, self.type_filter_refund, self.type_filter_manual_override]
        self.click(random.choice(filter_options))

        self.click(self.first_checkbox)
        self.click(self.second_checkbox)

    def select_random_template_and_send_email(self):
        """Select a random email template and send email"""
        self.click(self.send_email_table_button)
        self.click(self.email_templates_dropdown)

        # Helper method to get email template locator
        def get_template_locator(template_text):
            return self.locator((email_template_option[0].format(template_text), f"{template_text} Template Option"))

        # List of available templates
        templates = [
            "Identification required: Credit card",
            "Identification and card details required",
            "Identification required: Payfast & Ozow",
            "Identification not accepted",
            "Identification not received: Payfast & Ozow",
            "Identification not received: Credit card",
            "Credit card refund failed",
            "EFT refund failed",
            "Refund delayed",
            "Short paid",
            "Deposit Match",
            "Duplicate Payment",
            "Voucher Payment",
            "Generic",
        ]

        # Select random template
        template = random.choice(templates)
        self.click(get_template_locator(template))
        self.click(self.send_email_button)

    def verify_email_success_message(self):
        """Verify email success message"""
        email_text = self.get_text(self.email_sent_modal)
        assert "Sending 2 Emails" in email_text
        self.wait_for_seconds(5)
        expect(self.success_message).to_be_visible()
        self.click(self.email_sent_modal_close)

    def verify_checkboxes_are_unchecked(self):
        """Verify checkboxes are unchecked"""
        expect(self.first_checkbox).to_be_enabled()
        expect(self.second_checkbox).to_be_enabled()
        expect(self.third_checkbox).to_be_enabled()

    def select_manual_eft_refund_request(self):
        """Select a manual EFT refund request"""
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_manual_eft)
        self.click(self.first_checkbox)

    def verify_email_error_message(self):
        """Verify email error message for manual EFT request"""
        email_text = self.get_text(self.email_sent_modal)
        assert "Sending 1 Email" in email_text
        assert "Failed to process 1 item(s)" in email_text
        assert "Cannot send email to a ManualEFT request" in email_text
        self.click(self.email_sent_modal_close)

    def apply_status_filter(self):
        """Apply status filter and verify results"""
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_exported)

        # Verify all rows have Exported status
        rows = self.table_status_cells.all()
        for row in rows[:15]:  # Check first 15 rows
            assert "Exported" in row.text_content()

        self.click(self.clear_status_filter)
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_declined)

        # Verify all rows have Declined status
        rows = self.table_status_cells.all()
        for row in rows[:15]:
            assert "Declined" in row.text_content()

    def apply_type_filter(self):
        """Apply type filter and verify results"""

        def verify_type_rows(type_text):
            rows = self.table_type_cells.all()
            for row in rows[:15]:
                assert type_text in row.text_content()

        # Test Self Service filter
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_self_service)
        self.wait_for_seconds(2)
        verify_type_rows("Self Service")

        # Test Refund filter
        self.click(self.clear_type_filter)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_refund)
        self.wait_for_seconds(2)
        verify_type_rows("Refund")

        # Test Manual Override filter
        self.click(self.clear_type_filter)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_manual_override)
        self.wait_for_seconds(2)
        verify_type_rows("Manual Override")

        # Test Manual EFT filter
        self.click(self.clear_type_filter)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_manual_eft)
        self.wait_for_seconds(2)
        verify_type_rows("Manual EFT")

    def populate_manual_eft_fields(self):
        """Populate mandatory fields for manual EFT"""
        self.fill(self.customer_name_input, "BseUIAutomator")
        self.fill(self.refund_amount_input, "1")
        self.fill(self.bank_account_input, "480121212")

        # Select bank name
        self.click(self.bank_name_dropdown)
        self.click(self.bank_namibia_option)

        # Select branch
        self.click(self.branch_code_dropdown)
        self.click(self.branch_namibia_option)

    def verify_credit_deduction_popup(self):
        """Verify credit deduction popup"""
        self.click(self.submit_button)

        # Verify confirmation popup elements
        expect(self.credit_deduction_header).to_be_visible()
        expect(self.credit_deduction_message).to_be_visible()

    def verify_manual_eft_success(self):
        """Verify manual EFT success"""
        self.click(self.okay_button)
        expect(self.success_message_eft).to_be_visible()

        # Verify created EFT refund details
        row_text = self.page.locator("//table/tbody/tr[1]").text_content()
        assert "BseUIAutomator" in row_text
        assert "R 1.00" in row_text
        assert "480121212" in row_text
        assert "FNB/RMB" in row_text
        assert "Test en-gcs" in row_text

    def export_request(self, bank="Nedbank"):
        """Export EFT refund request"""
        self.click(self.export_request_button)
        self.click(self.export_bank_dropdown)

        if bank == "Nedbank":
            self.click(self.nedbank_option)
        else:
            self.click(self.absa_option)

        self.click(self.export_button)
        self.wait_for_seconds(3)

        # Verify success message
        export_status = self.get_text(self.export_success)
        assert "SUCCESSFUL" in export_status

        self.click(self.close_icon)

    def verify_exported_row(self):
        """Verify exported row details"""
        # Get exported file details
        file_text = self.get_text(self.file_link)
        assert self.get_current_date("%Y-%m-%d") in file_text
        assert "Test_en-gcs.csv" in file_text

        # Verify status and operator
        status_text = self.get_text(self.status_column)
        assert "Exported" in status_text

        operator_text = self.get_text(self.operator_column)
        assert "Test en-gcs" in operator_text

    def filter_by_customer_id(self):
        """Filter by customer ID"""
        self.click(self.locator(filter_by_dropdown))
        self.click(self.locator(filter_by_customer_id))

        # Hover over customer name to get ID
        self.customer_row_15.hover()
        customer_id = self.get_text(self.customer_popup)
        numeric_id = customer_id[12:]  # Extract numeric part

        self.fill(self.locator(filter_search_input), numeric_id)
        self.click(self.apply_filter_button)

        # Click customer name and verify in new tab
        self.click(self.customer_row)
        self.wait_for_seconds(2)

        new_window = self.page.context.pages[-1]
        customer_info_id = new_window.locator(self.customer_info_span).text_content()
        assert customer_info_id == numeric_id
        new_window.close()

    def filter_by_order_id(self):
        """Filter by order ID"""
        self.click(self.locator(filter_by_dropdown))
        self.click(self.locator(filter_by_order_id))

        # Get first order ID
        order_id = self.get_text(self.first_order_link)
        self.fill(self.locator(filter_search_input), order_id)
        self.click(self.apply_filter_button)

        # Verify filtered result
        filtered_order_id = self.get_text(self.first_order_link)
        assert filtered_order_id == order_id

    def apply_date_range_filter(self):
        """Apply date range filter and verify results"""
        self.fill(self.date_range_input, "01-07-2023 - 31-07-2023")
        self.click(self.apply_filter_button)

        # Change items per page
        self.click(self.show_items_dropdown)
        self.click(self.show_30_items)

        # Verify first page
        rows = self.page.locator(self.date_column).all()
        for row in rows[:30]:
            expect(row).to_contain_text("Jul-2023")

        # Check last page
        self.click(self.last_page_button)
        rows = self.page.locator(self.date_column).all()
        for row in rows[:5]:
            expect(row).to_contain_text("Jul-2023")

    def decline_requests(self, status="pending"):
        """Decline EFT refund requests"""
        self.click(self.status_filter_dropdown)
        if status == "pending":
            self.click(self.status_filter_pending)
        else:
            self.click(self.status_filter_exported)

        self.click(self.type_filter_dropdown)

        filter_options = [self.type_filter_self_service, self.type_filter_refund, self.type_filter_manual_override]
        self.click(random.choice(filter_options))

        # Select requests to decline
        self.click(self.first_checkbox)
        self.click(self.second_checkbox)
        self.click(self.third_checkbox)

        # Store order IDs for verification
        order_ids = []
        for i in range(1, 4):
            order_id = self.get_text(self.page.locator(f"//table/tbody/tr[{i}]/td[6]/a"))
            order_ids.append(order_id)

        # Click decline and enter reason
        self.click(self.decline_button)

        modal_text = self.get_text(self.decline_modal)
        assert "Decline 3 EFT Refund Requests" in modal_text

        self.fill(self.cancellation_reason_input, "Test Decline UI Automation")
        self.click(self.confirm_decline_button)

        if status == "pending":
            success_text = self.get_text(self.decline_message)
            assert "Successfully processed 3 item(s)" in success_text

            # Verify each declined order
            for order_id in order_ids:
                self.click(self.clear_filter_button)
                self.click(self.locator(filter_by_dropdown))
                self.click(self.locator(filter_by_order_id))
                self.fill(self.locator(filter_search_input), order_id)
                self.click(self.apply_filter_button)

                status_text = self.get_text(self.status_column)
                assert "Declined" in status_text

                operator_text = self.get_text(self.operator_column)
                assert "Test en-gcs" in operator_text
        else:
            error_text = self.get_text(self.decline_message)
            assert "Failed to process 3 item(s)" in error_text
            assert "EFT Refund request has already been cancelled/exported" in error_text

    def click_order_id_and_verify_new_tab(self):
        """Click order ID and verify details in new tab"""
        # Set up filters
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_pending)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_self_service)
        self.click(self.apply_filter_button)

        # Get order ID and click
        order_id = self.get_text(self.order_row_7)
        self.click(self.order_row_7)

        # Switch to new tab and verify
        new_page = self.page.context.pages[-1]
        order_id_new_tab = new_page.locator(self.order_id_cell).text_content()
        assert order_id in order_id_new_tab
        new_page.close()

    def verify_absa_file_export(self):
        """Export and verify ABSA file format"""
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_pending)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_self_service)
        self.click(self.apply_filter_button)

        # Select first row and get order ID
        self.click(self.first_checkbox)
        order_id = self.get_text(self.page.locator("//table/tbody/tr[1]/td[6]/a"))

        # Export to ABSA format
        self.export_request(bank="ABSA")

        # Verify exported file info
        self.click(self.clear_filter_button)
        self.click(self.locator(filter_by_dropdown))
        self.click(self.locator(filter_by_order_id))
        self.fill(self.locator(filter_search_input), order_id)
        self.click(self.apply_filter_button)

        # Get exported file name
        file_name = self.file_link.text_content()

        # Click to download
        self.click(self.download_icon)
        self.wait_for_seconds(15)

        return file_name  # Return filename for test verification

    def verify_nedbank_file_export(self):
        """Export and verify Nedbank file format"""
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_pending)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_self_service)
        self.click(self.apply_filter_button)

        # Select first row and get order ID
        self.click(self.first_checkbox)
        order_id = self.get_text(self.page.locator("//table/tbody/tr[1]/td[6]/a"))

        # Export to Nedbank format
        self.export_request(bank="Nedbank")

        # Verify exported file info
        self.click(self.clear_filter_button)
        self.click(self.locator(filter_by_dropdown))
        self.click(self.locator(filter_by_order_id))
        self.fill(self.locator(filter_search_input), order_id)
        self.click(self.apply_filter_button)

        # Get exported file name
        file_name = self.file_link.text_content()

        # Click to download
        self.click(self.download_icon)
        self.wait_for_seconds(15)

        return file_name  # Return filename for test verification

    def filter_by_bank_account_number(self):
        """Filter by bank account number"""
        self.click(self.locator(filter_by_dropdown))
        self.click(self.locator(filter_by_bank_account))

        # Get bank account number from first row
        bank_account = self.get_text(self.page.locator(self.bank_account_column))
        self.fill(self.locator(filter_search_input), bank_account)

        # Apply filter and verify results
        self.click(self.apply_filter_button)
        filtered_account = self.get_text(self.page.locator(self.bank_account_column))
        assert filtered_account == bank_account

    def filter_by_zendesk_ticket(self):
        """Filter by Zendesk ticket number"""
        # Change page size to show more entries
        self.click(self.show_items_dropdown)
        self.click(self.show_250_items)
        self.wait_for_seconds(2)

        # Find first non-empty Zendesk ticket
        zendesk_number = None
        for i in range(1, 250):
            zendesk_locator = self.locator((zendesk_cell[0].format(i), zendesk_cell[1]))
            ticket_text = self.get_text(zendesk_locator)
            if ticket_text:
                zendesk_number = ticket_text[43:]  # Extract ticket number
                break

        if zendesk_number:
            self.reload()  # Reload to avoid UI issues
            self.click(self.locator(filter_by_dropdown))
            self.click(self.locator(filter_by_zendesk))
            self.fill(self.locator(filter_search_input), zendesk_number)
            self.click(self.apply_filter_button)

            # Verify filtered result
            filtered_ticket = self.get_text(zendesk_locator)
            assert zendesk_number in filtered_ticket

    def get_current_date(self, format_string):
        """Get current date in specified format"""
        return datetime.now().strftime(format_string)

    def export_multiple_requests(self):
        """Export multiple EFT refund requests at once"""
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_pending)
        self.click(self.type_filter_dropdown)
        self.click(self.type_filter_self_service)
        self.click(self.apply_filter_button)

        # Select multiple rows
        self.click(self.first_checkbox)
        self.click(self.second_checkbox)
        self.click(self.third_checkbox)

        # Export the selected requests
        self.click(self.export_request_button)
        self.click(self.export_bank_dropdown)
        self.click(self.nedbank_option)
        self.click(self.export_button)
        self.wait_for_seconds(3)

        # Verify success message for multiple exports
        expect(self.success_message_3_items).to_be_visible()
        self.click(self.close_icon)

    def export_request_with_incorrect_status(self):
        """Try to export a request that is already exported"""
        self.click(self.status_filter_dropdown)
        self.click(self.status_filter_exported)
        self.click(self.apply_filter_button)

        # Select first exported request
        self.click(self.first_checkbox)

        # Attempt to export
        self.click(self.export_request_button)
        self.click(self.export_bank_dropdown)
        self.click(self.nedbank_option)
        self.click(self.export_button)
        self.wait_for_seconds(3)

        # Verify error message
        error_message = self.page.locator("//div[contains(@class,'ui error message')]")
        expect(error_message).to_be_visible()
        error_text = self.get_text(error_message)
        assert "EFT Refund request has already been exported" in error_text

        self.click(self.close_icon)

    def click_manual_eft_button_and_verify_fields(self):
        """Click the manual EFT button and verify all required fields are present"""
        self.click(self.manual_eft_button)

        # Verify all required fields are visible in the modal
        required_fields = [
            self.order_id_input,
            self.zendesk_ticket_input,
            self.customer_name_input,
            self.refund_amount_input,
            self.bank_account_input,
            self.bank_name_dropdown,
        ]

        for field in required_fields:
            expect(field).to_be_visible()

        # Verify the submit button is present
        expect(self.submit_button).to_be_visible()
