from base.page_base import PageBase

# Search
BATCH_DOWNLOAD = "//tbody/tr[1]/td[10]/div[1]/button[1]/i[1]"
APPLY_FILTER = "//button[contains(text(),'Apply Filter')]"
CLEAR_FILTER = "//button[contains(text(),'Clear Filter')]"
DATE_FILTER = "//input[@name='dateRange']"
BATCH_DATE = "//td[contains(text(),'12-May-2023')]"
PAYMENT_METHOD_LST = "//tbody/tr[1]/td[5]"
PAYMENT_METHOD_DDL = "//div[contains(text(),'Select payment method')]"
PAYFAST_LST = "//span[contains(text(),'PayFast')]"
CUSTOMER_NAME_LBL = "//th[contains(text(),'Customer Name')]"
PAGE_TWO_NAV = "//body/div[@id='root']/div[3]/div[1]/div[1]/table[1]/tfoot[1]/tr[1]/th[1]/div[1]/div[6]/div[2]/a[2]"
ITEM_LIST_DDL = "//div[contains(text(),'Show 15 Items')]"
LIST_FILTER_30 = "//span[contains(text(),'30')]"
LIST_FILTER_10 = "//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[1]"
REFRESH_BUTTON = "//body/div[@id='root']/div[3]/div[1]/div[1]/div[4]/button[1]"
ERROR_MESSAGE = "//*[contains(text(),'Error')]"
CRITERIA_DROPDOWN = "//div[contains(text(),'Criteria')]"
DEPOSIT_MATCH_SEARCH = "//input[@name='searchTerm']"
ORDER_ID_DM = "//span[contains(text(),'Order ID')]"
STATEMENT_AMOUNT_DM = "//span[contains(text(),'Statement Amount')]"
CUSTOMER_ID_DM = "//span[contains(text(),'Customer ID')]"
CUSTOMER_NAME_DM = "//span[contains(text(),'Customer Name')]"
BATCH_ID = "//span[contains(text(),'Batch ID')]"
ORDER_NO_TEXT = "//tbody/tr[1]/td[2]/a[1]"
CUST_NAME_TEXT = "//tbody/tr[1]/td[3]/a[1]"
STATEM_AMOUNT_TEXT = "//tbody/tr[1]/td[6]"
CUSTOMER_NAME_LINK = "//tbody/tr[1]/td[3]/a[1]"
CHK_ORDER = "//*[@id='root']/div[3]/div/div/table/tbody/tr[2]/td[1]/div"
CHK_NEW_ORDER = "//*[@id='root']/div[3]/div/div/table/tbody/tr/td[1]/div"
CANCEL_REASON_DROPDOWN = "//div[@name='cancelReason']"
CANCEL_REASON = "//span[contains(text(),'Supplier out of stock')]"
BTN_CANCEL_ORDER = "//button[contains(text(),'Cancel Order')]"
BTN_CONFIRM_CANCEL_ORDER = "//button[contains(text(),'Cancel Orders')]"
BTN_AUTHORISE_ORDER = "//button[contains(text(),'Authorise Order')]"
VERIFY_AUTHORISE_ORDER = "//div[contains(text(),'Successfully processed 1 item(s)')]"
TXT_CRITERIA_SEARCH = "//input[@name='searchTerm' and @type='text']"
BATCH_ID_VALUE = "//tbody/tr[1]/td[2]/a[1]"
MATCH_STATUS = "//div[@name='matchStatus' and @role='listbox']"
CLOSE_FILTER_BUTTON = "//i[@aria-hidden='true' and @class='dropdown icon clear']"
CLOSE_ICON = "//i[@aria-hidden='true' and @class='close icon']"
REMOVE_ORDER = "//button[contains(text(),'Remove Order')]"
ORDER_NUMBER_CHECKBOX = "//tbody/tr[1]/td[1]"
ORDER_NUMBER_TEXT = "//tbody/tr[1]/td[2]"
BTN_UNCLAIMED_PAYMENT = "//button[contains(text(),'Unclaimed Payment')]"
UNCLAIMED_PAYMENTS_TAB = "//a[contains(text(),'Unclaimed Payments ')]"
ORDER_NOT_FOUND = "//span[contains(text(),'Order Not Found')]"
AMOUNT_DIFFER = "//span[contains(text(),'Amount Differ')]"
AUTO_MATCH = "//span[contains(text(),'Auto Match')]"
BTN_UPLOAD_CSV = "//button[contains(text(),'Upload CSV')]"
SELECT_STATEMENT_TYPE = "//div[@name='statementType' and @role='listbox']"
BTN_MATCH = "//tbody/tr[1]/td[10]/div[1]/button[1]"
TXT_MATCH_ORDER_ID = "//input[@name='order_id' and  @type='number']"
BTN_MATCH_SUBMIT = "//button[@class='ui blue button' and @type='submit']"


class DepositMatchPO(PageBase):
    def __init__(self, page):
        super().__init__(page)
        # Search
        self.batch_download = self.locator(BATCH_DOWNLOAD, "Batch download button")
        self.apply_filter = self.locator(APPLY_FILTER, "Apply filter button")
        self.clear_filter = self.locator(CLEAR_FILTER, "Clear filter button")
        self.date_filter = self.locator(DATE_FILTER, "Date filter input")
        self.batch_date = self.locator(BATCH_DATE, "Batch date")
        self.payment_method_lst = self.locator(PAYMENT_METHOD_LST, "Payment method list")
        self.payment_method_ddl = self.locator(PAYMENT_METHOD_DDL, "Payment method dropdown")
        self.payfast_lst = self.locator(PAYFAST_LST, "PayFast option")
        self.customer_name_lbl = self.locator(CUSTOMER_NAME_LBL, "Customer Name label")
        self.page_two_nav = self.locator(PAGE_TWO_NAV, "Page two navigation")
        self.item_list_ddl = self.locator(ITEM_LIST_DDL, "Items list dropdown")
        self.list_filter_30 = self.locator(LIST_FILTER_30, "30 items filter")
        self.list_filter_10 = self.locator(LIST_FILTER_10, "10 items filter")
        self.refresh_button = self.locator(REFRESH_BUTTON, "Refresh button")
        self.error_message = self.locator(ERROR_MESSAGE, "Error message")
        self.criteria_dropdown = self.locator(CRITERIA_DROPDOWN, "Criteria dropdown")
        self.deposit_match_search = self.locator(DEPOSIT_MATCH_SEARCH, "Deposit match search")
        self.order_id_dm = self.locator(ORDER_ID_DM, "Order ID option")
        self.statement_amount_dm = self.locator(STATEMENT_AMOUNT_DM, "Statement Amount option")
        self.customer_id_dm = self.locator(CUSTOMER_ID_DM, "Customer ID option")
        self.customer_name_dm = self.locator(CUSTOMER_NAME_DM, "Customer Name option")
        self.batch_id = self.locator(BATCH_ID, "Batch ID option")
        self.order_no_text = self.locator(ORDER_NO_TEXT, "Order number text")
        self.cust_name_text = self.locator(CUST_NAME_TEXT, "Customer name text")
        self.statem_amount_text = self.locator(STATEM_AMOUNT_TEXT, "Statement amount text")
        self.customer_name_link = self.locator(CUSTOMER_NAME_LINK, "Customer name link")
        self.chk_order = self.locator(CHK_ORDER, "Order checkbox")
        self.chk_new_order = self.locator(CHK_NEW_ORDER, "New order checkbox")
        self.cancel_reason_dropdown = self.locator(CANCEL_REASON_DROPDOWN, "Cancel reason dropdown")
        self.cancel_reason = self.locator(CANCEL_REASON, "Cancel reason option")
        self.btn_cancel_order = self.locator(BTN_CANCEL_ORDER, "Cancel order button")
        self.btn_confirm_cancel_order = self.locator(BTN_CONFIRM_CANCEL_ORDER, "Confirm cancel order button")
        self.btn_authorise_order = self.locator(BTN_AUTHORISE_ORDER, "Authorise order button")
        self.verify_authorise_order = self.locator(VERIFY_AUTHORISE_ORDER, "Authorise order verification")
        self.txt_criteria_search = self.locator(TXT_CRITERIA_SEARCH, "Criteria search input")
        self.batch_id_value = self.locator(BATCH_ID_VALUE, "Batch ID value")
        self.match_status = self.locator(MATCH_STATUS, "Match status dropdown")
        self.close_filter_button = self.locator(CLOSE_FILTER_BUTTON, "Close filter button")
        self.close_icon = self.locator(CLOSE_ICON, "Close icon")
        self.remove_order = self.locator(REMOVE_ORDER, "Remove order button")
        self.order_number_checkbox = self.locator(ORDER_NUMBER_CHECKBOX, "Order number checkbox")
        self.order_number_text = self.locator(ORDER_NUMBER_TEXT, "Order number text")
        self.btn_unclaimed_payment = self.locator(BTN_UNCLAIMED_PAYMENT, "Unclaimed payment button")
        self.unclaimed_payments_tab = self.locator(UNCLAIMED_PAYMENTS_TAB, "Unclaimed payments tab")
        self.order_not_found = self.locator(ORDER_NOT_FOUND, "Order not found option")
        self.amount_differ = self.locator(AMOUNT_DIFFER, "Amount differ option")
        self.auto_match = self.locator(AUTO_MATCH, "Auto match option")
        self.btn_upload_csv = self.locator(BTN_UPLOAD_CSV, "Upload CSV button")
        self.select_statement_type = self.locator(SELECT_STATEMENT_TYPE, "Select statement type dropdown")
        self.btn_match = self.locator(BTN_MATCH, "Match button")
        self.txt_match_order_id = self.locator(TXT_MATCH_ORDER_ID, "Match order ID input")
        self.btn_match_submit = self.locator(BTN_MATCH_SUBMIT, "Match submit button")
