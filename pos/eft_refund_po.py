from base.page_base import PageBase


class EftRefundPO(PageBase):
    """Page Object class for EFT Refund functionality."""

    # region Menu Buttons

    @property
    def btn_menu(self):
        selector = "//body/div[@id='root']/div[2]/a[1]/i[1]"
        return self.locator(selector, "Menu button")

    @property
    def btn_eft_refund_menu(self):
        selector = "//body/div[@id='root']/div[1]/a[6]"
        return self.locator(selector, "EFT Refund menu button")

    # region Tables

    @property
    def eft_refunds_table(self):
        selector = "//table"
        return self.locator(selector, "EFT Refunds table")

    # region Email Section

    @property
    def btn_send_email_table(self):
        selector = "//table/tfoot/tr/th/div/div[3]/button"
        return self.locator(selector, "Send email button")

    @property
    def ddl_email_templates(self):
        selector = "//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]"
        return self.locator(selector, "Email templates dropdown")

    @property
    def btn_send_email(self):
        selector = "//button[contains(text(),'Send Emails')]"
        return self.locator(selector, "Send emails button")

    @property
    def email_sent_modal(self):
        selector = "/html/body/div[2]/div"
        return self.locator(selector, "Email sent modal")

    @property
    def email_sent_modal_close_icon(self):
        selector = "//body/div[2]/div[1]/i[1]"
        return self.locator(selector, "Email sent modal close button")

    # region Manual EFT Section

    @property
    def btn_manual_eft(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[6]/div/button'
        return self.locator(selector, "Manual EFT button")

    @property
    def txt_order_id(self):
        selector = '//input[@name="orderID" and @placeholder="Enter Order ID" and @type="text"]'
        return self.locator(selector, "Order ID input")

    @property
    def txt_zendesk_ticket(self):
        selector = '//input[@name="zendeskTicket" and @placeholder="Enter Zendesk Ticket Number" and @type="text"]'
        return self.locator(selector, "Zendesk Ticket input")

    @property
    def txt_customer_name(self):
        selector = '//input[@name="customerName" and @placeholder="Enter Customer Name" and @type="text"]'
        return self.locator(selector, "Customer Name input")

    @property
    def txt_refund_amount_manual_eft(self):
        selector = '//input[@name="refundAmount" and @placeholder="Enter Refund Amount" and @type="text"]'
        return self.locator(selector, "Refund Amount input")

    @property
    def txt_bank_account_manual_eft(self):
        selector = '//input[@name="bankAccount" and @placeholder="Enter Bank Account Number" and @type="text"]'
        return self.locator(selector, "Bank Account input")

    @property
    def ddl_bank_name_manual_eft(self):
        selector = "//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[6]/div[2]/div[1]/div[1]"
        return self.locator(selector, "Bank Name dropdown")

    @property
    def ddl_bank_name_manual_eft_fnb_namibia(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div/div[6]/div[2]/div/div/div[2]"
        return self.locator(selector, "FNB Namibia bank option")

    @property
    def ddl_branch_name_manual_eft(self):
        selector = '//div[@name="branchCode"]'
        return self.locator(selector, "Branch Name dropdown")

    @property
    def ddl_branch_name_manual_eft_all_namibia(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div/div[7]/div[2]/div/div/div[2]/div"
        return self.locator(selector, "All Namibia branch option")

    @property
    def btn_submit_manual_eft(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div/div[8]/div/div/div[1]/button"
        return self.locator(selector, "Submit Manual EFT button")

    @property
    def confirmation_header_manual_eft(self):
        selector = "//div[contains(text(),'Credit Deduction')]"
        return self.locator(selector, "Confirmation Header")

    @property
    def confirmation_text_manual_eft(self):
        selector = '//div[contains(text(),"Don\'t forget to remove credit.")]'
        return self.locator(selector, "Confirmation Text")

    @property
    def btn_okay_manual_eft(self):
        selector = "//button[contains(text(),'Okay')]"
        return self.locator(selector, "Okay button")

    @property
    def success_manual_eft(self):
        selector = "//div[contains(text(),'EFT Refund Created Successfully.')]"
        return self.locator(selector, "Success message")

    # region Filter elements

    @property
    def ddl_status_filter(self):
        selector = "//div[contains(text(),'Select refund status')]"
        return self.locator(selector, "Status filter dropdown")

    @property
    def ddl_clear_status_filter(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[1]/div/div/i'
        return self.locator(selector, "Clear status filter button")

    @property
    def ddl_status_filter_pending(self):
        selector = "//span[contains(text(),'Pending')]"
        return self.locator(selector, "Pending status option")

    @property
    def ddl_status_filter_exported(self):
        selector = "//span[contains(text(),'Exported')]"
        return self.locator(selector, "Exported status option")

    @property
    def ddl_status_filter_declined(self):
        selector = "//span[contains(text(),'Declined')]"
        return self.locator(selector, "Declined status option")

    @property
    def btn_apply_filter(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[5]/div[1]/button'
        return self.locator(selector, "Apply filter button")

    @property
    def btn_clear_filter(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[5]/div[2]/button'
        return self.locator(selector, "Clear filter button")

    @property
    def ddl_type_filter(self):
        selector = "//div[contains(text(),'Select refund type')]"
        return self.locator(selector, "Type filter dropdown")

    @property
    def ddl_clear_type_filter(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[2]/div/div/i'
        return self.locator(selector, "Clear type filter button")

    @property
    def ddl_type_filter_self_service(self):
        selector = "//span[contains(text(),'Self Service')]"
        return self.locator(selector, "Self Service type option")

    @property
    def ddl_type_filter_refund(self):
        selector = "//span[contains(text(),'Refund')]"
        return self.locator(selector, "Refund type option")

    @property
    def ddl_type_filter_manual_override(self):
        selector = "//span[contains(text(),'Manual Override')]"
        return self.locator(selector, "Manual Override type option")

    @property
    def ddl_type_filter_manual_eft(self):
        selector = "//span[contains(text(),'Manual EFT')]"
        return self.locator(selector, "Manual EFT type option")

    # region Search filters

    @property
    def ddl_filter_by(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/div'
        return self.locator(selector, "Filter by dropdown")

    @property
    def ddl_filter_by_customer_id(self):
        selector = "//span[contains(text(),'Customer ID')]"
        return self.locator(selector, "Customer ID filter option")

    @property
    def customer_name(self):
        selector = "//table/tbody/tr/td[8]/a"
        return self.locator(selector, "Customer name link")

    @property
    def filter_by_search(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/input'
        return self.locator(selector, "Filter search field")

    @property
    def customer_info(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/span'
        return self.locator(selector, "Customer info")

    @property
    def ddl_filter_by_order_id(self):
        selector = "//span[contains(text(),'Order ID')]"
        return self.locator(selector, "Order ID filter option")

    @property
    def order_id_eft_refunds_table2(self):
        selector = "//table/tbody/tr/td[6]"
        return self.locator(selector, "Order ID in table")

    @property
    def order_id_eft_refunds_table1(self):
        selector = "//table/tbody/tr[15]/td[6]"
        return self.locator(selector, "Order ID in table (row 15)")

    @property
    def ddl_filter_by_bank_account_number(self):
        selector = "//span[contains(text(),'Bank Account Number')]"
        return self.locator(selector, "Bank Account Number filter option")

    @property
    def bank_acc_eft_refunds_table(self):
        selector = "//table/tbody/tr/td[10]"
        return self.locator(selector, "Bank account in table")

    @property
    def ddl_filter_by_zendesk_ticket_number(self):
        selector = "//span[contains(text(),'Zendesk Ticket Number')]"
        return self.locator(selector, "Zendesk ticket filter option")

    @property
    def zendesk_ticket_eft_refunds_table(self):
        selector = "//table/tbody/tr/td[7]"
        return self.locator(selector, "Zendesk ticket in table")

    # region Pagination and display options

    @property
    def ddl_show_250_items(self):
        selector = "//table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[6]"
        return self.locator(selector, "Show 250 items option")

    @property
    def chk_date_range_today(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[3]/div/div[1]/div[1]/div/label'
        return self.locator(selector, "Today date range checkbox")

    @property
    def ddl_date_range(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[3]/div/div[2]/div/div/input'
        return self.locator(selector, "Date range field")

    @property
    def fld_date_created(self):
        selector = "//table/tbody/tr[1]/td[4]"
        return self.locator(selector, "Date created field")

    @property
    def ddl_show_items(self):
        selector = "//div[contains(text(),'Show 15 Items')]"
        return self.locator(selector, "Show items dropdown")

    @property
    def ddl_show_30_items(self):
        selector = "//table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[3]"
        return self.locator(selector, "Show 30 items option")

    @property
    def last_page(self):
        selector = "//table/tfoot/tr/th/div/div[5]/div[2]/a[7]"
        return self.locator(selector, "Last page button")

    @property
    def orderid_link_text(self):
        selector = "//tbody/tr[1]/td[6]/a[1]"
        return self.locator(selector, "Order ID link")

    # region Table row elements

    @property
    def eft_refunds_table_first_checkbox(self):
        selector = "//table/tbody/tr[1]/td[1]/div"
        return self.locator(selector, "First checkbox in table")

    @property
    def eft_refunds_table_second_checkbox(self):
        selector = "//table/tbody/tr[2]/td[1]/div"
        return self.locator(selector, "Second checkbox in table")

    @property
    def eft_refunds_table_third_checkbox(self):
        selector = "//table/tbody/tr[3]/td[1]/div"
        return self.locator(selector, "Third checkbox in table")

    @property
    def eft_refunds_table_first_order(self):
        selector = "//table/tbody/tr[1]/td[6]/a"
        return self.locator(selector, "First order in table")

    @property
    def eft_refunds_table_second_order(self):
        selector = "//table/tbody/tr[2]/td[6]/a"
        return self.locator(selector, "Second order in table")

    @property
    def eft_refunds_table_third_order(self):
        selector = "//table/tbody/tr[3]/td[6]/a"
        return self.locator(selector, "Third order in table")

    # region Export request elements

    @property
    def btn_export_request(self):
        selector = "//table/tfoot/tr/th/div/div[1]/button"
        return self.locator(selector, "Export request button")

    @property
    def export_modal(self):
        selector = "/html/body/div[2]/div/div[1]"
        return self.locator(selector, "Export modal")

    @property
    def error_modal(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div"
        return self.locator(selector, "Error modal")

    @property
    def ddl_export_bank(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div[1]/div"
        return self.locator(selector, "Export bank dropdown")

    @property
    def ddl_nedbank(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[1]/span"
        return self.locator(selector, "Nedbank option")

    @property
    def ddl_absa(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[2]/span"
        return self.locator(selector, "Absa option")

    @property
    def btn_export(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div[2]/button[2]"
        return self.locator(selector, "Export button")

    @property
    def export_status(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]"
        return self.locator(selector, "Export status")

    @property
    def btn_export_close_icon(self):
        selector = "/html/body/div[2]/div/i"
        return self.locator(selector, "Export close button")

    # region Decline request elements

    @property
    def btn_decline_eft_requests(self):
        selector = "//table/tfoot/tr/th/div/div[2]/button"
        return self.locator(selector, "Decline EFT requests button")

    @property
    def decline_modal(self):
        selector = "/html/body/div[2]/div"
        return self.locator(selector, "Decline modal")

    @property
    def btn_confirm_decline(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div[2]/button[1]"
        return self.locator(selector, "Confirm decline button")

    @property
    def fld_decline_cancellation_reason(self):
        selector = "/html/body/div[2]/div/div[2]/div/form/div[1]/div/input"
        return self.locator(selector, "Decline cancellation reason field")

    @property
    def decline_confirm_modal(self):
        selector = "/html/body/div[2]/div/div[1]"
        return self.locator(selector, "Decline confirm modal")

    @property
    def decline_confirm_modal_success(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div"
        return self.locator(selector, "Decline confirm success message")

    @property
    def close_decline_confirm(self):
        selector = "/html/body/div[2]/div/i"
        return self.locator(selector, "Close decline confirm button")

    @property
    def decline_text(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/p/span[1]/text()[3]"
        return self.locator(selector, "Decline text")

    # region File download elements

    @property
    def exported_file_download_icon(self):
        selector = "//table/tbody/tr/td[12]/a/i"
        return self.locator(selector, "Exported file download icon")

    @property
    def eft_refunds_table_first_file_text(self):
        selector = "//table/tbody/tr/td[12]/a"
        return self.locator(selector, "First file text in table")

    # region Email template options

    @property
    def option1_identification_required_credit_card(self):
        selector = "//span[contains(text(),'Identification required: Credit card')]"
        return self.locator(selector, "Identification required: Credit card option")

    @property
    def option2_identification_and_card_details_required(self):
        selector = "//span[contains(text(),'Identification and card details required')]"
        return self.locator(selector, "Identification and card details required option")

    @property
    def option3_identification_required_payfast_ozow(self):
        selector = "//span[contains(text(),'Identification required: Payfast & Ozow')]"
        return self.locator(selector, "Identification required: Payfast & Ozow option")

    @property
    def option4_identification_not_accepted(self):
        selector = "//span[contains(text(),'Identification not accepted')]"
        return self.locator(selector, "Identification not accepted option")

    @property
    def option5_identification_not_received_payfast_ozow(self):
        selector = "//span[contains(text(),'Identification not received: Payfast & Ozow')]"
        return self.locator(selector, "Identification not received: Payfast & Ozow option")

    @property
    def option6_identification_not_received_credit_card(self):
        selector = "//span[contains(text(),'Identification not received: Credit card')]"
        return self.locator(selector, "Identification not received: Credit card option")

    @property
    def option7_credit_card_refund_failed(self):
        selector = "//span[contains(text(),'Credit card refund failed')]"
        return self.locator(selector, "Credit card refund failed option")

    @property
    def option8_eft_refund_failed(self):
        selector = "//span[contains(text(),'EFT refund failed')]"
        return self.locator(selector, "EFT refund failed option")

    @property
    def option9_refund_delayed(self):
        selector = "//span[contains(text(),'Refund delayed')]"
        return self.locator(selector, "Refund delayed option")

    @property
    def option10_short_paid(self):
        selector = "//span[contains(text(),'Short paid')]"
        return self.locator(selector, "Short paid option")

    @property
    def option11_deposit_match(self):
        selector = "//span[contains(text(),'Deposit Match')]"
        return self.locator(selector, "Deposit Match option")

    @property
    def option12_duplicate_payment(self):
        selector = "//span[contains(text(),'Duplicate Payment')]"
        return self.locator(selector, "Duplicate Payment option")

    @property
    def option13_voucher_payment(self):
        selector = "//span[contains(text(),'Voucher Payment')]"
        return self.locator(selector, "Voucher Payment option")

    @property
    def option14_generic(self):
        selector = "//span[contains(text(),'Generic')]"
        return self.locator(selector, "Generic option")
