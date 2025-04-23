from base.page_base import PageBase

# Module-level constants
OPTION1_XPATH = "//span[contains(text(),'Identification required: Credit card')]"
OPTION2_XPATH = "//span[contains(text(),'Identification and card details required')]"
OPTION3_XPATH = "//span[contains(text(),'Identification required: Payfast & Ozow')]"
OPTION4_XPATH = "//span[contains(text(),'Identification not accepted')]"
OPTION5_XPATH = "//span[contains(text(),'Identification not received: Payfast & Ozow')]"
OPTION6_XPATH = "//span[contains(text(),'Identification not received: Credit card')]"
OPTION7_XPATH = "//span[contains(text(),'Credit card refund failed')]"
OPTION8_XPATH = "//span[contains(text(),'EFT refund failed')]"
OPTION9_XPATH = "//span[contains(text(),'Refund delayed')]"
OPTION10_XPATH = "//span[contains(text(),'Short paid')]"
OPTION11_XPATH = "//span[contains(text(),'Deposit Match')]"
OPTION12_XPATH = "//span[contains(text(),'Duplicate Payment')]"
OPTION13_XPATH = "//span[contains(text(),'Voucher Payment')]"
OPTION14_XPATH = "//span[contains(text(),'Generic')]"

BTN_MENU = "//body/div[@id='root']/div[2]/a[1]/i[1]"
BTN_EFT_REFUND_MENU = "//body/div[@id='root']/div[1]/a[6]"
EFT_REFUNDS_TABLE = "//table"
BTN_SEND_EMAIL_TABLE = "//table/tfoot/tr/th/div/div[3]/button"
DDL_EMAIL_TEMPLATES = "//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]"
BTN_SEND_EMAIL = "//button[contains(text(),'Send Emails')]"
EMAIL_SENT_MODAL = "/html/body/div[2]/div"
EMAIL_SENT_MODAL_CLOSE_ICON = "//body/div[2]/div[1]/i[1]"

BTN_MANUAL_EFT = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[6]/div/button'
TXT_ORDER_ID = '//input[@name="orderID" and @placeholder="Enter Order ID" and @type="text"]'
TXT_ZENDESK_TICKET = '//input[@name="zendeskTicket" and @placeholder="Enter Zendesk Ticket Number" and @type="text"]'
TXT_CUSTOMER_NAME = '//input[@name="customerName" and @placeholder="Enter Customer Name" and @type="text"]'
TXT_REFUND_AMOUNT_MANUAL_EFT = '//input[@name="refundAmount" and @placeholder="Enter Refund Amount" and @type="text"]'
TXT_BANK_ACCOUNT_MANUAL_EFT = '//input[@name="bankAccount" and @placeholder="Enter Bank Account Number" and @type="text"]'
DDL_BANK_NAME_MANUAL_EFT = "//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[6]/div[2]/div[1]/div[1]"
DDL_BRANCH_NAME_MANUAL_EFT = '//div[@name="branchCode"]'
BTN_SUBMIT_MANUAL_EFT = "/html/body/div[2]/div/div[2]/div/form/div/div[8]/div/div/div[1]/button"
DDL_BANK_NAME_MANUAL_EFT_FNB_NAMIBIA = "/html/body/div[2]/div/div[2]/div/form/div/div[6]/div[2]/div/div/div[2]"
DDL_BRANCH_NAME_MANUAL_EFT_ALL_NAMIBIA = "/html/body/div[2]/div/div[2]/div/form/div/div[7]/div[2]/div/div/div[2]/div"
CONFIRMATION_HEADER_MANUAL_EFT = "//div[contains(text(),'Credit Deduction')]"
CONFIRMATION_TEXT_MANUAL_EFT = '//div[contains(text(),"Don\'t forget to remove credit.")]'
BTN_OKAY_MANUAL_EFT = "//button[contains(text(),'Okay')]"
SUCCESS_MANUAL_EFT = "//div[contains(text(),'EFT Refund Created Successfully.')]"

DDL_STATUS_FILTER = "//div[contains(text(),'Select refund status')]"
DDL_CLEAR_STATUS_FILTER = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[1]/div/div/i'
DDL_STATUS_FILTER_PENDING = "//span[contains(text(),'Pending')]"
DDL_STATUS_FILTER_EXPORTED = "//span[contains(text(),'Exported')]"
DDL_STATUS_FILTER_DECLINED = "//span[contains(text(),'Declined')]"

BTN_APPLY_FILTER = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[5]/div[1]/button'
BTN_CLEAR_FILTER = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[5]/div[2]/button'

DDL_TYPE_FILTER = "//div[contains(text(),'Select refund type')]"
DDL_CLEAR_TYPE_FILTER = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[2]/div/div/i'
DDL_TYPE_FILTER_SELF_SERVICE = "//span[contains(text(),'Self Service')]"
DDL_TYPE_FILTER_REFUND = "//span[contains(text(),'Refund')]"
DDL_TYPE_FILTER_MANUAL_OVERRIDE = "//span[contains(text(),'Manual Override')]"
DDL_TYPE_FILTER_MANUAL_EFT = "//span[contains(text(),'Manual EFT')]"

DDL_FILTER_BY = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/div'
DDL_FILTER_BY_CUSTOMER_ID = "//span[contains(text(),'Customer ID')]"
CUSTOMER_NAME = "//table/tbody/tr/td[8]/a"
FILTER_BY_SEARCH = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[4]/div/div/input'
CUSTOMER_INFO = '//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/span'
DDL_FILTER_BY_ORDER_ID = "//span[contains(text(),'Order ID')]"
ORDER_ID_EFT_REFUNDS_TABLE2 = "//table/tbody/tr/td[6]"
ORDER_ID_EFT_REFUNDS_TABLE1 = "//table/tbody/tr[15]/td[6]"
DDL_FILTER_BY_BANK_ACCOUNT_NUMBER = "//span[contains(text(),'Bank Account Number')]"
BANK_ACC_EFT_REFUNDS_TABLE = "//table/tbody/tr/td[10]"
DDL_FILTER_BY_ZENDESK_TICKET_NUMBER = "//span[contains(text(),'Zendesk Ticket Number')]"
ZENDESK_TICKET_EFT_REFUNDS_TABLE = "//table/tbody/tr/td[7]"
DDL_SHOW_250_ITEMS = "//table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[6]"

CHK_DATE_RANGE_TODAY = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[3]/div/div[1]/div[1]/div/label'
DDL_DATE_RANGE = '//*[@id="root"]/div[3]/div/div/div/div/div[2]/form/div/div/div/div[3]/div/div[2]/div/div/input'
FLD_DATE_CREATED = "//table/tbody/tr[1]/td[4]"
DDL_SHOW_ITEMS = "//div[contains(text(),'Show 15 Items')]"
DDL_SHOW_30_ITEMS = "//table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[3]"
LAST_PAGE = "//table/tfoot/tr/th/div/div[5]/div[2]/a[7]"

ORDERID_LINK_TEXT = "//tbody/tr[1]/td[6]/a[1]"

EFT_REFUNDS_TABLE_FIRST_CHECKBOX = "//table/tbody/tr[1]/td[1]/div"
EFT_REFUNDS_TABLE_SECOND_CHECKBOX = "//table/tbody/tr[2]/td[1]/div"
EFT_REFUNDS_TABLE_THIRD_CHECKBOX = "//table/tbody/tr[3]/td[1]/div"
EFT_REFUNDS_TABLE_FIRST_ORDER = "//table/tbody/tr[1]/td[6]/a"
EFT_REFUNDS_TABLE_SECOND_ORDER = "//table/tbody/tr[2]/td[6]/a"
EFT_REFUNDS_TABLE_THIRD_ORDER = "//table/tbody/tr[3]/td[6]/a"

BTN_EXPORT_REQUEST = "//table/tfoot/tr/th/div/div[1]/button"
EXPORT_MODAL = "/html/body/div[2]/div/div[1]"
ERROR_MODAL = "/html/body/div[2]/div/div[2]/div/div/div"
DDL_EXPORT_BANK = "/html/body/div[2]/div/div[2]/div/form/div[1]/div"
DDL_NEDBANK = "/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[1]/span"
DDL_ABSA = "/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[2]/span"
BTN_EXPORT = "/html/body/div[2]/div/div[2]/div/form/div[2]/button[2]"
EXPORT_STATUS = "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr/td[1]"
BTN_EXPORT_CLOSE_ICON = "/html/body/div[2]/div/i"

BTN_DECLINE_EFT_REQUESTS = "//table/tfoot/tr/th/div/div[2]/button"
DECLINE_MODAL = "/html/body/div[2]/div"
BTN_CONFIRM_DECLINE = "/html/body/div[2]/div/div[2]/div/form/div[2]/button[1]"
FLD_DECLINE_CANCELLATION_REASON = "/html/body/div[2]/div/div[2]/div/form/div[1]/div/input"
DECLINE_CONFIRM_MODAL = "/html/body/div[2]/div/div[1]"
DECLINE_CONFIRM_MODAL_SUCCESS = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div"
CLOSE_DECLINE_CONFIRM = "/html/body/div[2]/div/i"
DECLINE_TEXT = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/p/span[1]/text()[3]"

EXPORTED_FILE_DOWNLOAD_ICON = "//table/tbody/tr/td[12]/a/i"
EFT_REFUNDS_TABLE_FIRST_FILE_TEXT = "//table/tbody/tr/td[12]/a"


class EftRefundPO(PageBase):
    """Page Object class for EFT Refund functionality."""

    def __init__(self, page):
        """Initialize the EFT Refund PO."""
        super().__init__(page)

        # Initialize elements using self.locator() with descriptive names
        self.btn_menu = self.locator(BTN_MENU, "Menu button")
        self.btn_eft_refund_menu = self.locator(BTN_EFT_REFUND_MENU, "EFT Refund menu button")
        self.eft_refunds_table = self.locator(EFT_REFUNDS_TABLE, "EFT Refunds table")
        self.btn_send_email_table = self.locator(BTN_SEND_EMAIL_TABLE, "Send email button")
        self.ddl_email_templates = self.locator(DDL_EMAIL_TEMPLATES, "Email templates dropdown")
        self.btn_send_email = self.locator(BTN_SEND_EMAIL, "Send emails button")
        self.email_sent_modal = self.locator(EMAIL_SENT_MODAL, "Email sent modal")
        self.email_sent_modal_close_icon = self.locator(EMAIL_SENT_MODAL_CLOSE_ICON, "Email sent modal close button")

        # Manual EFT elements
        self.btn_manual_eft = self.locator(BTN_MANUAL_EFT, "Manual EFT button")
        self.txt_order_id = self.locator(TXT_ORDER_ID, "Order ID text field")
        self.txt_zendesk_ticket = self.locator(TXT_ZENDESK_TICKET, "Zendesk ticket text field")
        self.txt_customer_name = self.locator(TXT_CUSTOMER_NAME, "Customer name text field")
        self.txt_refund_amount_manual_eft = self.locator(TXT_REFUND_AMOUNT_MANUAL_EFT, "Refund amount text field")
        self.txt_bank_account_manual_eft = self.locator(TXT_BANK_ACCOUNT_MANUAL_EFT, "Bank account text field")
        self.ddl_bank_name_manual_eft = self.locator(DDL_BANK_NAME_MANUAL_EFT, "Bank name dropdown")
        self.ddl_branch_name_manual_eft = self.locator(DDL_BRANCH_NAME_MANUAL_EFT, "Branch name dropdown")
        self.btn_submit_manual_eft = self.locator(BTN_SUBMIT_MANUAL_EFT, "Submit manual EFT button")
        self.ddl_bank_name_manual_eft_fnb_namibia = self.locator(DDL_BANK_NAME_MANUAL_EFT_FNB_NAMIBIA, "FNB Namibia option")
        self.ddl_branch_name_manual_eft_all_namibia = self.locator(DDL_BRANCH_NAME_MANUAL_EFT_ALL_NAMIBIA, "All Namibia branch option")
        self.confirmation_header_manual_eft = self.locator(CONFIRMATION_HEADER_MANUAL_EFT, "Credit deduction confirmation header")
        self.confirmation_text_manual_eft = self.locator(CONFIRMATION_TEXT_MANUAL_EFT, "Credit deduction confirmation text")
        self.btn_okay_manual_eft = self.locator(BTN_OKAY_MANUAL_EFT, "Okay button")
        self.success_manual_eft = self.locator(SUCCESS_MANUAL_EFT, "Success message")

        # Filter elements
        self.ddl_status_filter = self.locator(DDL_STATUS_FILTER, "Status filter dropdown")
        self.ddl_clear_status_filter = self.locator(DDL_CLEAR_STATUS_FILTER, "Clear status filter button")
        self.ddl_status_filter_pending = self.locator(DDL_STATUS_FILTER_PENDING, "Pending status option")
        self.ddl_status_filter_exported = self.locator(DDL_STATUS_FILTER_EXPORTED, "Exported status option")
        self.ddl_status_filter_declined = self.locator(DDL_STATUS_FILTER_DECLINED, "Declined status option")

        self.btn_apply_filter = self.locator(BTN_APPLY_FILTER, "Apply filter button")
        self.btn_clear_filter = self.locator(BTN_CLEAR_FILTER, "Clear filter button")

        self.ddl_type_filter = self.locator(DDL_TYPE_FILTER, "Type filter dropdown")
        self.ddl_clear_type_filter = self.locator(DDL_CLEAR_TYPE_FILTER, "Clear type filter button")
        self.ddl_type_filter_self_service = self.locator(DDL_TYPE_FILTER_SELF_SERVICE, "Self Service type option")
        self.ddl_type_filter_refund = self.locator(DDL_TYPE_FILTER_REFUND, "Refund type option")
        self.ddl_type_filter_manual_override = self.locator(DDL_TYPE_FILTER_MANUAL_OVERRIDE, "Manual Override type option")
        self.ddl_type_filter_manual_eft = self.locator(DDL_TYPE_FILTER_MANUAL_EFT, "Manual EFT type option")

        self.ddl_filter_by = self.locator(DDL_FILTER_BY, "Filter by dropdown")
        self.ddl_filter_by_customer_id = self.locator(DDL_FILTER_BY_CUSTOMER_ID, "Customer ID filter option")
        self.customer_name = self.locator(CUSTOMER_NAME, "Customer name link")
        self.filter_by_search = self.locator(FILTER_BY_SEARCH, "Filter search field")
        self.customer_info = self.locator(CUSTOMER_INFO, "Customer info")
        self.ddl_filter_by_order_id = self.locator(DDL_FILTER_BY_ORDER_ID, "Order ID filter option")
        self.order_id_eft_refunds_table2 = self.locator(ORDER_ID_EFT_REFUNDS_TABLE2, "Order ID in table")
        self.order_id_eft_refunds_table1 = self.locator(ORDER_ID_EFT_REFUNDS_TABLE1, "Order ID in table (row 15)")
        self.ddl_filter_by_bank_account_number = self.locator(DDL_FILTER_BY_BANK_ACCOUNT_NUMBER, "Bank Account Number filter option")
        self.bank_acc_eft_refunds_table = self.locator(BANK_ACC_EFT_REFUNDS_TABLE, "Bank account in table")
        self.ddl_filter_by_zendesk_ticket_number = self.locator(DDL_FILTER_BY_ZENDESK_TICKET_NUMBER, "Zendesk ticket filter option")
        self.zendesk_ticket_eft_refunds_table = self.locator(ZENDESK_TICKET_EFT_REFUNDS_TABLE, "Zendesk ticket in table")
        self.ddl_show_250_items = self.locator(DDL_SHOW_250_ITEMS, "Show 250 items option")

        self.chk_date_range_today = self.locator(CHK_DATE_RANGE_TODAY, "Today date range checkbox")
        self.ddl_date_range = self.locator(DDL_DATE_RANGE, "Date range field")
        self.fld_date_created = self.locator(FLD_DATE_CREATED, "Date created field")
        self.ddl_show_items = self.locator(DDL_SHOW_ITEMS, "Show items dropdown")
        self.ddl_show_30_items = self.locator(DDL_SHOW_30_ITEMS, "Show 30 items option")
        self.last_page = self.locator(LAST_PAGE, "Last page button")

        self.orderid_link_text = self.locator(ORDERID_LINK_TEXT, "Order ID link")

        # Table row elements
        self.eft_refunds_table_first_checkbox = self.locator(EFT_REFUNDS_TABLE_FIRST_CHECKBOX, "First checkbox in table")
        self.eft_refunds_table_second_checkbox = self.locator(EFT_REFUNDS_TABLE_SECOND_CHECKBOX, "Second checkbox in table")
        self.eft_refunds_table_third_checkbox = self.locator(EFT_REFUNDS_TABLE_THIRD_CHECKBOX, "Third checkbox in table")
        self.eft_refunds_table_first_order = self.locator(EFT_REFUNDS_TABLE_FIRST_ORDER, "First order in table")
        self.eft_refunds_table_second_order = self.locator(EFT_REFUNDS_TABLE_SECOND_ORDER, "Second order in table")
        self.eft_refunds_table_third_order = self.locator(EFT_REFUNDS_TABLE_THIRD_ORDER, "Third order in table")

        # Export request elements
        self.btn_export_request = self.locator(BTN_EXPORT_REQUEST, "Export request button")
        self.export_modal = self.locator(EXPORT_MODAL, "Export modal")
        self.error_modal = self.locator(ERROR_MODAL, "Error modal")
        self.ddl_export_bank = self.locator(DDL_EXPORT_BANK, "Export bank dropdown")
        self.ddl_nedbank = self.locator(DDL_NEDBANK, "Nedbank option")
        self.ddl_absa = self.locator(DDL_ABSA, "Absa option")
        self.btn_export = self.locator(BTN_EXPORT, "Export button")
        self.export_status = self.locator(EXPORT_STATUS, "Export status")
        self.btn_export_close_icon = self.locator(BTN_EXPORT_CLOSE_ICON, "Export close button")

        # Decline request elements
        self.btn_decline_eft_requests = self.locator(BTN_DECLINE_EFT_REQUESTS, "Decline EFT requests button")
        self.decline_modal = self.locator(DECLINE_MODAL, "Decline modal")
        self.btn_confirm_decline = self.locator(BTN_CONFIRM_DECLINE, "Confirm decline button")
        self.fld_decline_cancellation_reason = self.locator(FLD_DECLINE_CANCELLATION_REASON, "Decline cancellation reason field")
        self.decline_confirm_modal = self.locator(DECLINE_CONFIRM_MODAL, "Decline confirm modal")
        self.decline_confirm_modal_success = self.locator(DECLINE_CONFIRM_MODAL_SUCCESS, "Decline confirm success message")
        self.close_decline_confirm = self.locator(CLOSE_DECLINE_CONFIRM, "Close decline confirm button")

        # File download elements
        self.exported_file_download_icon = self.locator(EXPORTED_FILE_DOWNLOAD_ICON, "Exported file download icon")
        self.eft_refunds_table_first_file_text = self.locator(EFT_REFUNDS_TABLE_FIRST_FILE_TEXT, "First file text in table")

        # Email template options
        self.option_templates = {
            1: self.locator(OPTION1_XPATH, "Identification required: Credit card option"),
            2: self.locator(OPTION2_XPATH, "Identification and card details required option"),
            3: self.locator(OPTION3_XPATH, "Identification required: Payfast & Ozow option"),
            4: self.locator(OPTION4_XPATH, "Identification not accepted option"),
            5: self.locator(OPTION5_XPATH, "Identification not received: Payfast & Ozow option"),
            6: self.locator(OPTION6_XPATH, "Identification not received: Credit card option"),
            7: self.locator(OPTION7_XPATH, "Credit card refund failed option"),
            8: self.locator(OPTION8_XPATH, "EFT refund failed option"),
            9: self.locator(OPTION9_XPATH, "Refund delayed option"),
            10: self.locator(OPTION10_XPATH, "Short paid option"),
            11: self.locator(OPTION11_XPATH, "Deposit Match option"),
            12: self.locator(OPTION12_XPATH, "Duplicate Payment option"),
            13: self.locator(OPTION13_XPATH, "Voucher Payment option"),
            14: self.locator(OPTION14_XPATH, "Generic option"),
        }
