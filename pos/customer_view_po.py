from base.page_base import PageBase


# Module-level constants for all locators
ADDRESSES_ACCORDION = "//span[contains(text(),'Addresses')]"
ADDRESS_GOOGLE_ICON = "//*[@class='map small icon']"
ALLOCATE_CREDIT_BTN = "//button[contains(text(),'Allocate credit')]"
CREDIT_HISTORY_TABLE = "//*[@class='ui small celled compact table']"
AVAILABLE_CREDIT = "//*[@class='ui green small circular horizontal label']"
CUSTOMER_CREDIT_ACCORDION = "//span[contains(text(),'Customer Credit')]"
CUSTOMER_FULLNAME = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/text()[2]"
EMAIL_GOOGLE_ICON = "//*[@class='google icon']"
EMAIL_LOGS_ACCORDION = "//span[contains(text(),'Email Logs')]"
EMAIL_CARDS = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[12]/div/div[1]"
FIN_NOTES_DROPDOWN = "//span[contains(text(),'Fin Notes')]"
FIN_NOTES_EDIT_BTN = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/button"
NOTES_DROPDOWN = "//span[contains(text(),'Notes')]"
NOTES_EDIT_BTN = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/button"
NAME_GOOGLE_ICON = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/i"
MODIFIED_DATE = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]"
REFUND_HISTORY_ACCORDION = "//span[contains(text(),'Refund History')]"
REFUND_HISTORY_TABLE = "//*[@class='ui small celled structured compact table']"
RETURNS_HISTORY_ACCORDION = "//span[contains(text(),'Returns History')]"
RETURNS_TABLE = "//*[@class='ui small celled table']"
REGISTERED_DATE = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]"
VERIFIED_CELLPHONE_ICON = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div"
ZENDESK_TICKET_ACCORDION = "//span[contains(text(),'Zendesk Tickets')]"
FRAUD_REASON_DDL = "//div[contains(text(),'Fraud Reason')]"
FRAUD_REASON_ID = "//span[contains(text(),'Returns abuse')]"
FIN_NOTES = "//input[@name='finNote']"
SUBMIT_BLACKLIST_CUSTOMER = "//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]"
POPUP = "//*[@id='noty_layout__topRight']"
BLACKLIST_BTN = "//button[contains(text(),'Blacklist Customer')]"
CREDIT_AMOUNT_TXT = "//input[@name='amount']"
CREDIT_REASON_DDL = "//div[@name='reason']"
CREDIT_REASON = "//*[contains(text(),'B2B bulk orders')]"
ADMIN_NOTES = "//textarea[@name='adminNote']"
ADD_CREDIT_BTN = "//button[@class='ui blue button']"
OK_BTN = "//button[@class='ui primary button']"
EDIT_CUSTOMER_BTN = "//button[contains(text(),'Customer Info')]"
CUST_NAME = "//input[@name='customerFirstName']"
CUST_SURNAME = "//input[@name='customerSurname']"
BUSINESS_NAME = "//input[@name='businessName']"
VAT_NUMBER = "//input[@name='vatNumber']"
ACC_STATUS_DDL = "//div[@name='accountStatus']"
ACC_STATUS = "//span[text()='suspended']"
FRAUD_REASON_LIST = "//div[@name='fraudReasonID']"
FRAUD_REASON = "//span[text()='Coupon abuse']"
STAFF_ACCOUNT_CHECK = "//label[text()='Staff Account']"
BLOCK_VOU_CHECK = "//label[text()='Block Vouchers']"
CONFIRM_BTN = "//button[contains(text(),'Confirm')]"
EMAIL_CUSTOMER_BTN = "//button[contains(text(),'Email Customer')]"
DDL_EMAIL_TEMPLATES_DROPDOWN = "//div[@name='emailTemplate']"
EMAIL_MODAL_CUSTOMER_ID = "//input[@name='customerId']"
EMAIL_MODAL_ORDER_ID = "//input[@name='orderId']"
EMAIL_MODAL_SUBJECT = "//input[@name='emailSubject']"
EMAIL_MODAL_BODY = "//textarea[@name='emailBody']"
SEND_EMAIL_BTN = "//button[contains(text(),'Send Email')]"
LASTEST_EMAIL_SENT = "//*[@class='ui fluid card email-card']/div/div/span/a/span[1]"
ADDRESS_CARDS = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/div"
NOTES_ACCORDION = "//span[contains(text(),'Notes')]"
NOTE_BTN = "//button[contains(text(),'Note')]"
ADD_NOTES_TEXT_FIELD = "//textarea[@name='customerNote']"
ADD_NOTE_BTN = "//button[contains(text(),'Add Note')]"
NOTE_ADDED_MESSAGE = "//*[@class='noty_body']"
AUDIT_LOGS_ICON = "//*[@class='list alternate outline icon link']"
AUDIT_LOG_RESULTS = "//*[@class='ui striped basic very compact table']"
SALES_HISTORY_ACCORDION = "//span[contains(text(),'Sales History')]"
SALES_HISTORY_TABLE = "//*[@class='ui small celled striped compact table']"
ORDER_ID = "//*[@id='root']/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[1]/a"
ORDER_ID_PG2 = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]"
PRODUCT_TITLE_PG1 = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a"
PRODUCT_TITLE_PG2 = "//*[@id='root']/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[6]"
SHOW_10_ITEMS_DDL = "//div[contains(text(),'Show 10 Items')]"
SHOW_30_ITEMS_DDL = "//div[contains(text(),'Show 30 Items')]"
SHOW_30_ORDER_ITEMS = "//span[contains(text(),'30')]"
SHOW_10_ORDER_ITEMS = "//span[contains(text(),'10')]"
ORDER_ITEMS_ACCORDION = "//span[contains(text(),'Order Items')]"
ORDER_LINK = "//*[@id='root']/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[5]/a"
NEXT_PAGE = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[12]/div/div[2]/a[4]"
PREV_PAGE = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[6]/div/div[2]/a[1]"
REFUND_TYPE_COLUMN = "//*[@id='root']/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[9]"
UPLOAD_ID = "//button[contains(text(),'Upload')]"
UPLOAD_FIELD = "//input[@type='file']"
DOCUMENTS_ACCORDION = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[13]"
REMOVE_ID = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[14]/div/div/div/div[2]/ol/a[2]"
CONFIRM_UPLOAD = "//*[@class='ui primary button']"


class CustomerViewPO(PageBase):
    """Page Object for Customer View page"""

    def __init__(self, page):
        super().__init__(page)
        # Initialize locators
        self.addresses_accordion = self.locator(ADDRESSES_ACCORDION, "Addresses Accordion")
        self.address_google_icon = self.locator(ADDRESS_GOOGLE_ICON, "Address Google Icon")
        self.allocate_credit_btn = self.locator(ALLOCATE_CREDIT_BTN, "Allocate Credit Button")
        self.credit_history_table = self.locator(CREDIT_HISTORY_TABLE, "Credit History Table")
        self.available_credit = self.locator(AVAILABLE_CREDIT, "Available Credit")
        self.customer_credit_accordion = self.locator(CUSTOMER_CREDIT_ACCORDION, "Customer Credit Accordion")
        self.customer_fullname = self.locator(CUSTOMER_FULLNAME, "Customer Fullname")
        self.email_google_icon = self.locator(EMAIL_GOOGLE_ICON, "Email Google Icon")
        self.email_logs_accordion = self.locator(EMAIL_LOGS_ACCORDION, "Email Logs Accordion")
        self.email_cards = self.locator(EMAIL_CARDS, "Email Cards")
        self.fin_notes_dropdown = self.locator(FIN_NOTES_DROPDOWN, "Fin Notes Dropdown")
        self.fin_notes_edit_btn = self.locator(FIN_NOTES_EDIT_BTN, "Fin Notes Edit Button")
        self.notes_dropdown = self.locator(NOTES_DROPDOWN, "Notes Dropdown")
        self.notes_edit_btn = self.locator(NOTES_EDIT_BTN, "Notes Edit Button")
        self.name_google_icon = self.locator(NAME_GOOGLE_ICON, "Name Google Icon")
        self.modified_date = self.locator(MODIFIED_DATE, "Modified Date")
        self.refund_history_accordion = self.locator(REFUND_HISTORY_ACCORDION, "Refund History Accordion")
        self.refund_history_table = self.locator(REFUND_HISTORY_TABLE, "Refund History Table")
        self.returns_history_accordion = self.locator(RETURNS_HISTORY_ACCORDION, "Returns History Accordion")
        self.returns_table = self.locator(RETURNS_TABLE, "Returns Table")
        self.registered_date = self.locator(REGISTERED_DATE, "Registered Date")
        self.verified_cellphone_icon = self.locator(VERIFIED_CELLPHONE_ICON, "Verified Cellphone Icon")
        self.zendesk_ticket_accordion = self.locator(ZENDESK_TICKET_ACCORDION, "Zendesk Ticket Accordion")
        self.fraud_reason_ddl = self.locator(FRAUD_REASON_DDL, "Fraud Reason Dropdown")
        self.fraud_reason_id = self.locator(FRAUD_REASON_ID, "Fraud Reason ID")
        self.fin_notes = self.locator(FIN_NOTES, "Fin Notes")
        self.submit_blacklist_customer = self.locator(SUBMIT_BLACKLIST_CUSTOMER, "Submit Blacklist Customer")
        self.popup = self.locator(POPUP, "Popup Message")
        self.blacklist_btn = self.locator(BLACKLIST_BTN, "Blacklist Button")
        self.credit_amount_txt = self.locator(CREDIT_AMOUNT_TXT, "Credit Amount Text")
        self.credit_reason_ddl = self.locator(CREDIT_REASON_DDL, "Credit Reason Dropdown")
        self.credit_reason = self.locator(CREDIT_REASON, "Credit Reason")
        self.admin_notes = self.locator(ADMIN_NOTES, "Admin Notes")
        self.add_credit_btn = self.locator(ADD_CREDIT_BTN, "Add Credit Button")
        self.ok_btn = self.locator(OK_BTN, "OK Button")
        self.edit_customer_btn = self.locator(EDIT_CUSTOMER_BTN, "Edit Customer Button")
        self.cust_name = self.locator(CUST_NAME, "Customer Name")
        self.cust_surname = self.locator(CUST_SURNAME, "Customer Surname")
        self.business_name = self.locator(BUSINESS_NAME, "Business Name")
        self.vat_number = self.locator(VAT_NUMBER, "VAT Number")
        self.acc_status_ddl = self.locator(ACC_STATUS_DDL, "Account Status Dropdown")
        self.acc_status = self.locator(ACC_STATUS, "Account Status")
        self.fraud_reason_list = self.locator(FRAUD_REASON_LIST, "Fraud Reason List")
        self.fraud_reason = self.locator(FRAUD_REASON, "Fraud Reason")
        self.staff_account_check = self.locator(STAFF_ACCOUNT_CHECK, "Staff Account Check")
        self.block_vou_check = self.locator(BLOCK_VOU_CHECK, "Block Vouchers Check")
        self.confirm_btn = self.locator(CONFIRM_BTN, "Confirm Button")
        self.email_customer_btn = self.locator(EMAIL_CUSTOMER_BTN, "Email Customer Button")
        self.ddl_email_templates = self.locator(DDL_EMAIL_TEMPLATES_DROPDOWN, "Email Templates Dropdown")
        self.email_modal_customer_id = self.locator(EMAIL_MODAL_CUSTOMER_ID, "Email Modal Customer ID")
        self.email_modal_order_id = self.locator(EMAIL_MODAL_ORDER_ID, "Email Modal Order ID")
        self.email_modal_subject = self.locator(EMAIL_MODAL_SUBJECT, "Email Modal Subject")
        self.email_modal_body = self.locator(EMAIL_MODAL_BODY, "Email Modal Body")
        self.send_email_btn = self.locator(SEND_EMAIL_BTN, "Send Email Button")
        self.latest_email_sent = self.locator(LASTEST_EMAIL_SENT, "Latest Email Sent")
        self.address_cards = self.locator(ADDRESS_CARDS, "Address Cards")
        self.notes_accordion = self.locator(NOTES_ACCORDION, "Notes Accordion")
        self.note_btn = self.locator(NOTE_BTN, "Note Button")
        self.add_notes_text_field = self.locator(ADD_NOTES_TEXT_FIELD, "Add Notes Text Field")
        self.add_note_btn = self.locator(ADD_NOTE_BTN, "Add Note Button")
        self.note_added_message = self.locator(NOTE_ADDED_MESSAGE, "Note Added Message")
        self.audit_logs_icon = self.locator(AUDIT_LOGS_ICON, "Audit Logs Icon")
        self.audit_log_results = self.locator(AUDIT_LOG_RESULTS, "Audit Log Results")
        self.sales_history_accordion = self.locator(SALES_HISTORY_ACCORDION, "Sales History Accordion")
        self.sales_history_table = self.locator(SALES_HISTORY_TABLE, "Sales History Table")
        self.order_id = self.locator(ORDER_ID, "Order ID")
        self.order_id_pg2 = self.locator(ORDER_ID_PG2, "Order ID Page 2")
        self.product_title_pg1 = self.locator(PRODUCT_TITLE_PG1, "Product Title Page 1")
        self.product_title_pg2 = self.locator(PRODUCT_TITLE_PG2, "Product Title Page 2")
        self.show_10_items_ddl = self.locator(SHOW_10_ITEMS_DDL, "Show 10 Items Dropdown")
        self.show_30_items_ddl = self.locator(SHOW_30_ITEMS_DDL, "Show 30 Items Dropdown")
        self.show_30_order_items = self.locator(SHOW_30_ORDER_ITEMS, "Show 30 Order Items")
        self.show_10_order_items = self.locator(SHOW_10_ORDER_ITEMS, "Show 10 Order Items")
        self.order_items_accordion = self.locator(ORDER_ITEMS_ACCORDION, "Order Items Accordion")
        self.order_link = self.locator(ORDER_LINK, "Order Link")
        self.next_page = self.locator(NEXT_PAGE, "Next Page")
        self.prev_page = self.locator(PREV_PAGE, "Previous Page")
        self.refund_type_column = self.locator(REFUND_TYPE_COLUMN, "Refund Type Column")
        self.upload_id = self.locator(UPLOAD_ID, "Upload ID")
        self.upload_field = self.locator(UPLOAD_FIELD, "Upload Field")
        self.documents_accordion = self.locator(DOCUMENTS_ACCORDION, "Documents Accordion")
        self.remove_id = self.locator(REMOVE_ID, "Remove ID")
        self.confirm_upload = self.locator(CONFIRM_UPLOAD, "Confirm Upload")
