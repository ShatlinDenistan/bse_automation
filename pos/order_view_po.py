from base.page_base import PageBase

# Module-level constants for all locators
ADD_NOTES_BTN = "//button[@class='ui mini primary right floated button']"
CONFIRM_ADD_BTN = "//button[@class='ui blue right floated button']"
NOTE_DD = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/span"
NOTES_TXT_FIELD = "//textarea[@name='customerNote']"
NOTE_CONFIRM_MESSAGE = "//*[@id='noty_layout__topRight']"
BLACKLIST_CUST_BTN = "//button[contains(text(),'Blacklist Customer')]"
FRAUD_REASON_LIST = "//div[contains(text(),'Fraud Reason')]"
FRAUD_REASON_SELECTION = "//span[contains(text(),'Returns abuse')]"
FIN_NOTE = "//input[@name='finNote']"
CONFIRM_BLACKLIST = "//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]"
CONFIRM_WHITELIST = "//button[@class='ui blue right floated button'][contains(text(),'Confirm')]"
WHITELIST_CUST_BTN = "//button[contains(text(),'Whitelist Customer')]"
CANCEL_ALL_ITEM_BTN = "//button[contains(text(),'Cancel All Items')]"
CANCELLATION_REASON = "//*[@name='reasonTypeID']"
CUSTOMER_REQUEST_CANCEL_REASON = "//span[contains(text(),'Customer request')]"
CONFIRM_CANCELLING_BTN = "//button[contains(text(),'Confirm Cancelling')]"
CLOSE_CANCEL_MODAL = "//*[@class='close icon']"
ORDER_STATUS = "//div[@class='ten wide column label-container']/span/div[1]"
EMAIL_CUSTOMER = "//button[contains(text(),'Email Customer')]"
EMAIL_TEMPLATE_SELECTION = "//span[contains(text(),'Identification not accepted')]"
EMAIL_TEMPLATE_DDL = "//*[@name='emailTemplate']"
CUSTOMER_ID = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]"
MARK_AS_RISKY_BTN = "//button[contains(text(),'Mark as risky')]"
MARK_AS_RISKY_REASON = "//input[@name='reason']"
ADD_REASON_BTN = "//button[contains(text(),'Add Reason')]"
FLAGGED_AS_RISK = "//div[@class='ui red basic label']"
ORDER_ELLIPSIS_MENU = "//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']"
AUDIT_LOG_MENU_OPTION = "//*[contains(text(),'Audit log')]"
AUDIT_LOG_ACTION_TYPE = "//*[@class='ui striped basic very compact table']/tbody/tr/td[3]"
AUTHORISE_NOW_BTN = "//button[contains(text(),'Authorise Now')]"
AUTHORISE_NOW_MODAL_MESSAGE = "//div[@class='ui success message']/div/div"
AUTHORISE_NOW_MODAL_CLOSE_ICON = "//i[@class='close icon']"
ORDER_FULLFILMENT_ACCORDION = "//*[contains(text(),'Order Fulfillment')]"
ORDER_TRACKING_HEADING = "//h5[@class='ui header']"
ORDER_TRACKING_USER_INFO = "//div[@class='ui info message']/div[1]"
EVENT_LOG_RESULTS = "//*[@class='ui red celled padded table']"
ORDER_EVENTS_MENU = "//*[contains(text(),'Order events')]"
FIRST_PAYMENT_METHOD_BADGE = "//div[@class='ui blue basic label']"
SECOND_PAYMENT_METHOD_BADGE = "//div[@class='ui orange basic label']"
ORDER_NOTES_ACCORDION = "//div[@class='ten wide column']//span[text()='Notes']"
ORDER_NOTES_BTN = "//button[@class='ui mini icon primary right floated button']"
ORDER_NOTES_TEXT_FIELD = "//textarea[@name='orderNote']"
ADD_NOTES_CONFIRM_BTN = "//button[@class='ui primary button']"
CUSTOMER_NOTES_ACCORDION = "//div[@class='six wide column']//span[text()='Notes']"
ADD_CUSTOMER_NOTES_BTN = "//button[@class='ui mini primary right floated button']"
CUSTOMER_NOTES_TEXT_FIELD = "//textarea[@name='customerNote']"
ADD_CUSTOMER_NOTES_CONFIRM_BTN = "//button[@class='ui blue right floated button']"
FIN_NOTES_ACCORDION = "//div[@class='six wide column']//span[text()='Notes']"
ADD_FIN_NOTES_BTN = "//button[@class='ui mini primary right floated button']"
FIN_NOTES_TEXT_FIELD = "//textarea[@name='customerNote']"
ADD_FIN_NOTES_CONFIRM_BTN = "//button[@class='ui blue right floated button']"
NOTE_ADDED_MESSAGE = "//*[@id='noty_layout__topRight']"
CANCEL_SELECTED_ITEM_BTN = "//button[contains(text(),'Cancel Selected Items')]"
SELECT_ITEM_CHECKBOX = "//div[@class='ui fitted checkbox']"
CANCELLATION_RESULTS = "//*[@class='ui celled striped table']/tbody/tr/td[2]"
PAYMENT_LEDGER_ACCORDION = "//div[@class='ten wide column']//*[text()='Payment Ledger']"
PAYMENT_LEDGER_FIRST_PROVIDER = "//*[@class='ui celled fixed structured table']/tbody/tr/td[@rowspan='2']"
PAYMENT_LEDGER_SECOND_PROVIDER = "//*[@class='ui celled fixed structured table']/tbody/tr/td[@rowspan='3']"
PAYMENT_LEDGER_PAID_TOTAL_AMOUNT = "//tfoot/tr[@class='center aligned']/th[2]"
BOOKMARK_ICON = "//*[@class='grey bookmark outline link icon']"
BOOKMARK_NOTES = "//textarea[@placeholder='Notes...']"
BOOKMARK_COUNTER = "//*[@class='ui teal mini circular floating label label-on-corner']"
BOOKMARKS_PAGE = "//*[@class='grey bookmark outline large icon']"
CLOSE_MODAL = "//*[@class='close icon']"
CONFIRMATION_MSG = "//*[@class='ui message']"
DONE_BUTTON = "//button[@class='ui primary right floated button']"
REMOVE_BOOKMARKS_CHECKBOX = "//*[@class='ui fitted checkbox']"
REMOVE_BTN = "//button[@class='ui mini icon negative right floated button']"
PROGRESS_BAR = "//*[@class='ui green progress']"
ORDER_FINANCIALS_ACCORDION = "//div[@class='ten wide column']//*[text()='Order Financials']"
TOTAL_ORDER_ITEMS_AMOUNT = "//tbody/tr/td[text()='Total Order Items']/following-sibling::*[1]/div"
SHIPPING_AMOUNT = "//tbody/tr/td[text()='Shipping']/following-sibling::*[1]/div"
SUB_TOTAL_AMOUNT = "//tbody/tr/td[text()='Sub-Total']/following-sibling::*[1]/div"
DISCOUNT_AMOUNT = "//tbody/tr/td[text()='Discount']/following-sibling::*[1]/div"
ORDER_TOTAL_AMOUNT = "//tbody/tr/td[text()='Order Total']/following-sibling::*[1]/div"
TOTAL_PAID_AMOUNT = "//tbody/tr/td[text()='Total Paid']/following-sibling::*[1]/div"
LOGS_TABLE = "//*[@class='ui striped basic very compact table']"
CUST_ACC_NUMBER = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]"
ADDRESS_GOOGLE_ICON = "//*[@class='google icon']"
ORDER_ID = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]"
ORDER_DATE = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[3]/div[1]"
AUTH_STATUS = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[1]"
AUTH_DATE = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[3]"
WAYBILL_MENU_OPTION = "//*[contains(text(),'Waybill log')]"
ORDER_COMMENTS = "//*[@class='ui mini comments']"
CLOSE_ICON = "//*[@class='close icon']"
CUST_INFO_POPUP = "//*[@class='ui bottom center basic popup transition visible']"
CUST_STATUS = "//*[@class='ui green mini basic label']"
CUST_NAME_POPUP = "//table[@class='ui small unstackable very basic very compact table']//td[text()='Slindile Mncwango']"
CUST_DATE_REGISTERED = "//table[@class='ui small unstackable very basic very compact table']//td[text()='16-Oct-2018 @ 10:41']"
CUST_BLACKLIST_STATUS = "//div[@class='ui green basic label'][contains(text(),'Not Blacklisted')]"
CS_CLOSE_ICON = "/html/body/div[2]/div/i"
CS_SEARCH_TXT = "//*[@id='app']/div/div[1]/div[1]/div/input[1]"
CS_SEARCH_BTN = "//*[@id='app']/div/div[1]/div[1]/div/button"
RRN = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[7]/div[2]/a"
EDIT_ORDER_ITEM_MENU = "//*[@class='blue write square large icon']"
UPDATE_STATUS_MENU_OPTION = "//*[contains(text(),'Update to shipped')]"
UPDATE_TO_SHIPPED_BUTTON = "//button[@class='ui blue button'][contains(text(),'Update to shipped')]"
SHIPPED_TAG = "//div[@class='ui green tiny label'][contains(text(),'Shipped')]"
RETURN_CANCELED_TAG = "//div[@class='ui red tiny label'][contains(text(),'Return Canceled')]"
PAYMENT_LEDGER_PAYMENT_PROVIDER = "//*[@class='ui celled fixed structured table']/tbody/tr[1]/td[1]"
EMAIL_LOGS_ACCORDION = "//div[@class='ten wide column']//*[text()='Email Logs']"
VIEW_EMAIL_BTN = "//*[@class='blue mail outline icon']"
EMAIL_VIEW = "//*[@class='ui scrolling modal transition visible active']"
ORDER_ITEM_STATUS = "//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[1]"
ORDER_ITEM_CANCELED_BY = "//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[3]/div/p[3]"
ORDER_ITEMS_SHOW_ITEMS = "//div[@class='ui compact item dropdown']"
ORDER_ITEMS_PAGINATION_PAGE_TWO = "//*[@aria-label='Pagination Navigation']/a[3]"
COUPON_HISTORY_ACCORDION = "//*[text()='Coupon History']"
COUPON_CODE = "//div[text()='UAFORHER']"
SIGNED_BY = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/p"
INSTRUCTION_DROPPED_DATETIME = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div"
SHIPPED_FROM_WAREHOUSE_DATETIME = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div"
DELIVERED_TO_CUSTOMER_DATETIME = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div"
WAYBILL_NO = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]"
COURIER = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]"
PARCEL_BLOCK = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/a/div"
PARCEL = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/span/a"
ORDER_ITEM = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a"
DELIVERED_TAG = "//div[@class='ui green tiny label'][contains(text(),'Delivered')]"
TRACK_BTN = "//button[@class='ui blue small button']"
ESTIMATED_COLLECTION_DATE = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/h5"
WAYBILL_ESTIMATE_COLLECTION_DATE = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]"
COLLECTION_ESTIMATE = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/div/span"
REFUND_HISTORY_ACCORDION = "//*[text()='Refund History']"
REFUNDED_AMOUNT = "//td[contains(text(),'RFN-pg3x-45rz')]/following-sibling::td[1]/div[2]/div"
REFUNDED_PAYMENT_METHOD = "//td[contains(text(),'RFN-pg3x-45rz')]/following::td[3]"
STREET_ADDRESS = "//div[@class='column'][contains(text(),'6 Birkenhead Road')]"
SUBURB_ADDRESS = "//div[@class='column'][contains(text(),'Umbilo')]"
CITY_ADDRESS = "//div[@class='column'][contains(text(),'Berea')]"
PROVINCE_ADDRESS = "//div[@class='column'][contains(text(),'KwaZulu-Natal')]"
CODE_ADDRESS = "//div[@class='column'][contains(text(),'4075')]"
COPY_ADDRESS_BTN = "//button[@class='ui blue mini right floated button']"
ADDRESS_COPIED_BTN = "//button[@class='ui green mini right floated button']"
RESIDENTIAL_TXT = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div[1]"
SEARCH_GOOGLE_ICON = "//div[@class='header customer-card-header']//i[@class='google icon']"
SHIPPING_METHOD = "(//table[@class='ui small unstackable basic very compact table']//td[text()='Courier'])[1]"
SHIPPING_PLAN = "(//table[@class='ui small unstackable basic very compact table']//td[text()='Standard'])[1]"
SHIPPING_COURIER = "(//table[@class='ui small unstackable basic very compact table']//td[text()='MDX133806010 - Takealot Delivery Team'])[1]"
SHIPPING_PROMISED_DATE = "(//table[@class='ui small unstackable basic very compact table']//td[text()='28 Aug 2024'])[1]"
SHIPPING_DELIVERED_DATE = "(//table[@class='ui small unstackable basic very compact table']//td[text()='30 Aug 2024'])[1]"
INSTRUCTION_DROPPED_DATE1 = "(//div[text()='27 May 2024 @ 17:46'])[1]"
INSTRUCTION_DROPPED_DATE2 = "(//div[text()='27 May 2024 @ 0:34'])"
SHIPPED_FROM_WAREHOUSE_DATE1 = "(//div[text()='28 May 2024 @ 1:31'])"
SHIPPED_FROM_WAREHOUSE_DATE2 = "(//div[text()='27 May 2024 @ 17:46'])[2]"
DELIVERED_DATE1 = "(//div[text()='30 May 2024 @ 11:40'])"
DELIVERED_DATE2 = "(//div[text()='29 May 2024 @ 10:58'])"
ORDER_TRACKING_HEADING1 = "(//*[text()='Delivered Thu, 30 May 2024'])"
ORDER_TRACKING_HEADING2 = "(//*[text()='Delivered Wed, 29 May 2024'])"
SIGNED_BY1 = "(//*[text()='Signed by: Slindile Mncwango (Customer)'])"
SIGNED_BY2 = "(//*[text()='Signed by Slindile Mncwango'])"
WAYBILL_NUMBER1 = "(//*[text()='MDX127668689'])"
WAYBILL_NUMBER2 = "(//*[text()='MDX127583371'])"
WAYBILL_NUMBER_LINK = "(//*[text()='MDX133806010'])"
MR_DEXPRESS_COPYRIGHT = "//*[@class='popup ui-dialog-content ui-widget-content']"
ORDER_TRACKING_FIRST_CONSIGNMENT = "//div[@class='ui segment instruction-container'][1]"
FIRST_CONSIGMENT_DELIVERED_DATE = "//div[@class='ui segment instruction-container'][1]/div[1]/div/h5"
FIRST_CONSIGMENT_SIGNED_BY = "//div[@class='ui segment instruction-container'][1]/div[1]/div/p"
FIRST_CONSIGMENT_WAYBILL_NUMBER = "//div[@class='ui segment instruction-container'][1]/div[2]/div/div[1]/span/a"
CANCELLED_ITEMS = "(//*[text()='Cancelled Item(s)'])"
CANCELLED_TAG = "//div[@class='ui red tiny label'][contains(text(),'Canceled')]"
PART_DELIVERED_DATE = "(//*[text()='Delivered Mon, 19 Sep 2022'])"
IP_ADDRESS_ICON = "//*[@class='question circle outline icon link']"
IP_ADDRESS = "//input[@name='ipAddress']"
IP_ADDRESS_MODEL = "//*[@class='ui tiny modal transition visible active']"
FIRST_CONSIGMENT_TRACK_BTN = "//div[@class='ui segment instruction-container'][1]/div[1]/button"
TRACKING_WAYBILL_NUMBER = "//strong[text()='Waybill No: ']/following-sibling::*[1]"
TRACKING_FIRST_PARCEL_INFO = "//div[@class='ui fluid vertical tabular menu']/a[1]"
TRACKING_FIRST_PARCEL_NUMBER = "//div[@class='ui fluid vertical tabular menu']/a[1]/div/div/strong"
TRACKING_FIRST_PARCEL_ITEM = "//div[@class='stretched twelve wide computer sixteen wide mobile twelve wide tablet column']//*[@class='content']/span"
ORDER_ITEMS_ACCORDION = "//div[@class='accordion ui']"
COLLECTION_ESTIMATE_DATE = "//div[@class='ui segment instruction-container']//h5"
COLLECTION_NOT_YET_READY_MESSAGE = "//div[@class='ui segment instruction-container']//div/span"
DELIVERY_ESTIMATE_DATE = "//div[@class='ui segment instruction-container']//h5"
DELIVERY_NOT_YET_READY_MESSAGE = "//div[@class='ui segment instruction-container']//div/span"
SEND_EMAIL_BTN = "//button[@class='ui right floated primary button']"
EDIT_CUSTOMER_BTN = "//button[@class='ui mini primary right floated button']//i[@class='edit icon']"
CUST_NAME = "//input[@name='name']"
CUST_SURNAME = "//input[@name='surname']"
BUSINESS_NAME = "//input[@name='businessName']"
VAT_NUMBER = "//input[@name='vatNumber']"
ACC_STATUS_DDL = "//div[@name='accountStatus']"
ACC_STATUS = "//span[text()='Active']"
STAFF_ACCOUNT_CHECK = "//label[text()=' Staff']"
BLOCK_VOU_CHECK = "//label[text()=' Voucher Block']"
CONFIRM_BTN = "//button[@class='ui primary button right floated']"
POP_UP = "//*[@id='noty_layout__topRight']"


class OrderViewPO(PageBase):
    """Page Object for Order View page."""

    def __init__(self, page):
        super().__init__(page)
        # Initialize elements using self.locator
        self.add_notes_btn = self.locator(ADD_NOTES_BTN, "Add Notes button")
        self.confirm_add_btn = self.locator(CONFIRM_ADD_BTN, "Confirm Add button")
        self.note_dd = self.locator(NOTE_DD, "Notes dropdown")
        self.notes_txt_field = self.locator(NOTES_TXT_FIELD, "Notes text field")
        self.note_confirm_message = self.locator(NOTE_CONFIRM_MESSAGE, "Note confirmation message")
        self.blacklist_cust_btn = self.locator(BLACKLIST_CUST_BTN, "Blacklist Customer button")
        self.fraud_reason_list = self.locator(FRAUD_REASON_LIST, "Fraud Reason list")
        self.fraud_reason_selection = self.locator(FRAUD_REASON_SELECTION, "Fraud Reason selection")
        self.fin_note = self.locator(FIN_NOTE, "Financial Note field")
        self.confirm_blacklist = self.locator(CONFIRM_BLACKLIST, "Confirm Blacklist button")
        self.confirm_whitelist = self.locator(CONFIRM_WHITELIST, "Confirm Whitelist button")
        self.whitelist_cust_btn = self.locator(WHITELIST_CUST_BTN, "Whitelist Customer button")
        self.cancel_all_item_btn = self.locator(CANCEL_ALL_ITEM_BTN, "Cancel All Items button")
        self.cancellation_reason = self.locator(CANCELLATION_REASON, "Cancellation reason dropdown")
        self.customer_request_cancel_reason = self.locator(CUSTOMER_REQUEST_CANCEL_REASON, "Customer request cancellation reason")
        self.confirm_cancelling_btn = self.locator(CONFIRM_CANCELLING_BTN, "Confirm Cancelling button")
        self.close_cancel_modal = self.locator(CLOSE_CANCEL_MODAL, "Close cancel modal icon")
        self.order_status = self.locator(ORDER_STATUS, "Order status")
        self.email_customer = self.locator(EMAIL_CUSTOMER, "Email Customer button")
        self.email_template_selection = self.locator(EMAIL_TEMPLATE_SELECTION, "Email template selection")
        self.email_template_ddl = self.locator(EMAIL_TEMPLATE_DDL, "Email template dropdown")
        self.customer_id = self.locator(CUSTOMER_ID, "Customer ID")
        self.mark_as_risky_btn = self.locator(MARK_AS_RISKY_BTN, "Mark as risky button")
        self.mark_as_risky_reason = self.locator(MARK_AS_RISKY_REASON, "Mark as risky reason field")
        self.add_reason_btn = self.locator(ADD_REASON_BTN, "Add Reason button")
        self.flagged_as_risk = self.locator(FLAGGED_AS_RISK, "Flagged as risk label")
        self.order_ellipsis_menu = self.locator(ORDER_ELLIPSIS_MENU, "Order ellipsis menu")
        self.audit_log_menu_option = self.locator(AUDIT_LOG_MENU_OPTION, "Audit log menu option")
        self.audit_log_action_type = self.locator(AUDIT_LOG_ACTION_TYPE, "Audit log action type")
        self.authorise_now_btn = self.locator(AUTHORISE_NOW_BTN, "Authorise Now button")
        self.authorise_now_modal_message = self.locator(AUTHORISE_NOW_MODAL_MESSAGE, "Authorise Now modal message")
        self.authorise_now_modal_close_icon = self.locator(AUTHORISE_NOW_MODAL_CLOSE_ICON, "Authorise Now modal close icon")
        self.order_fullfilment_accordion = self.locator(ORDER_FULLFILMENT_ACCORDION, "Order Fulfillment accordion")
        self.order_tracking_heading = self.locator(ORDER_TRACKING_HEADING, "Order tracking heading")
        self.order_tracking_user_info = self.locator(ORDER_TRACKING_USER_INFO, "Order tracking user info")
        self.event_log_results = self.locator(EVENT_LOG_RESULTS, "Event log results")
        self.order_events_menu = self.locator(ORDER_EVENTS_MENU, "Order events menu")
        self.first_payment_method_badge = self.locator(FIRST_PAYMENT_METHOD_BADGE, "First payment method badge")
        self.second_payment_method_badge = self.locator(SECOND_PAYMENT_METHOD_BADGE, "Second payment method badge")
        self.order_notes_accordion = self.locator(ORDER_NOTES_ACCORDION, "Order Notes accordion")
        self.order_notes_btn = self.locator(ORDER_NOTES_BTN, "Order Notes button")
        self.order_notes_text_field = self.locator(ORDER_NOTES_TEXT_FIELD, "Order Notes text field")
        self.add_notes_confirm_btn = self.locator(ADD_NOTES_CONFIRM_BTN, "Add Notes confirm button")
        self.customer_notes_accordion = self.locator(CUSTOMER_NOTES_ACCORDION, "Customer Notes accordion")
        self.add_customer_notes_btn = self.locator(ADD_CUSTOMER_NOTES_BTN, "Add Customer Notes button")
        self.customer_notes_text_field = self.locator(CUSTOMER_NOTES_TEXT_FIELD, "Customer Notes text field")
        self.add_customer_notes_confirm_btn = self.locator(ADD_CUSTOMER_NOTES_CONFIRM_BTN, "Add Customer Notes confirm button")
        self.fin_notes_accordion = self.locator(FIN_NOTES_ACCORDION, "Financial Notes accordion")
        self.add_fin_notes_btn = self.locator(ADD_FIN_NOTES_BTN, "Add Financial Notes button")
        self.fin_notes_text_field = self.locator(FIN_NOTES_TEXT_FIELD, "Financial Notes text field")
        self.add_fin_notes_confirm_btn = self.locator(ADD_FIN_NOTES_CONFIRM_BTN, "Add Financial Notes confirm button")
        self.note_added_message = self.locator(NOTE_ADDED_MESSAGE, "Note added message")
        self.cancel_selected_item_btn = self.locator(CANCEL_SELECTED_ITEM_BTN, "Cancel Selected Items button")
        self.select_item_checkbox = self.locator(SELECT_ITEM_CHECKBOX, "Select item checkbox")
        self.cancellation_results = self.locator(CANCELLATION_RESULTS, "Cancellation results")
        self.payment_ledger_accordion = self.locator(PAYMENT_LEDGER_ACCORDION, "Payment Ledger accordion")
        self.payment_ledger_first_provider = self.locator(PAYMENT_LEDGER_FIRST_PROVIDER, "Payment Ledger first provider")
        self.payment_ledger_second_provider = self.locator(PAYMENT_LEDGER_SECOND_PROVIDER, "Payment Ledger second provider")
        self.payment_ledger_paid_total_amount = self.locator(PAYMENT_LEDGER_PAID_TOTAL_AMOUNT, "Payment Ledger paid total amount")
        self.bookmark_icon = self.locator(BOOKMARK_ICON, "Bookmark icon")
        self.bookmark_notes = self.locator(BOOKMARK_NOTES, "Bookmark notes")
        self.bookmark_counter = self.locator(BOOKMARK_COUNTER, "Bookmark counter")
        self.bookmarks_page = self.locator(BOOKMARKS_PAGE, "Bookmarks page")
        self.close_modal = self.locator(CLOSE_MODAL, "Close modal")
        self.confirmation_msg = self.locator(CONFIRMATION_MSG, "Confirmation message")
        self.done_button = self.locator(DONE_BUTTON, "Done button")
        self.remove_bookmarks_checkbox = self.locator(REMOVE_BOOKMARKS_CHECKBOX, "Remove bookmarks checkbox")
        self.remove_btn = self.locator(REMOVE_BTN, "Remove button")
        self.progress_bar = self.locator(PROGRESS_BAR, "Progress bar")
        self.order_financials_accordion = self.locator(ORDER_FINANCIALS_ACCORDION, "Order Financials accordion")
        self.total_order_items_amount = self.locator(TOTAL_ORDER_ITEMS_AMOUNT, "Total order items amount")
        self.shipping_amount = self.locator(SHIPPING_AMOUNT, "Shipping amount")
        self.sub_total_amount = self.locator(SUB_TOTAL_AMOUNT, "Sub-total amount")
        self.discount_amount = self.locator(DISCOUNT_AMOUNT, "Discount amount")
        self.order_total_amount = self.locator(ORDER_TOTAL_AMOUNT, "Order total amount")
        self.total_paid_amount = self.locator(TOTAL_PAID_AMOUNT, "Total paid amount")
        self.logs_table = self.locator(LOGS_TABLE, "Logs table")
        self.cust_acc_number = self.locator(CUST_ACC_NUMBER, "Customer account number")
        self.address_google_icon = self.locator(ADDRESS_GOOGLE_ICON, "Address Google icon")
        self.order_id = self.locator(ORDER_ID, "Order ID")
        self.order_date = self.locator(ORDER_DATE, "Order date")
        self.auth_status = self.locator(AUTH_STATUS, "Auth status")
        self.auth_date = self.locator(AUTH_DATE, "Auth date")
        self.waybill_menu_option = self.locator(WAYBILL_MENU_OPTION, "Waybill menu option")
        self.order_comments = self.locator(ORDER_COMMENTS, "Order comments")
        self.close_icon = self.locator(CLOSE_ICON, "Close icon")
        self.cust_info_popup = self.locator(CUST_INFO_POPUP, "Customer info popup")
        self.cust_status = self.locator(CUST_STATUS, "Customer status")
        self.cust_name_popup = self.locator(CUST_NAME_POPUP, "Customer name in popup")
        self.cust_date_registered = self.locator(CUST_DATE_REGISTERED, "Customer date registered")
        self.cust_blacklist_status = self.locator(CUST_BLACKLIST_STATUS, "Customer blacklist status")
        self.cs_close_icon = self.locator(CS_CLOSE_ICON, "CS close icon")
        self.cs_search_txt = self.locator(CS_SEARCH_TXT, "CS search text")
        self.cs_search_btn = self.locator(CS_SEARCH_BTN, "CS search button")
        self.rrn = self.locator(RRN, "RRN")
        self.edit_order_item_menu = self.locator(EDIT_ORDER_ITEM_MENU, "Edit order item menu")
        self.update_status_menu_option = self.locator(UPDATE_STATUS_MENU_OPTION, "Update status menu option")
        self.update_to_shipped_button = self.locator(UPDATE_TO_SHIPPED_BUTTON, "Update to shipped button")
        self.shipped_tag = self.locator(SHIPPED_TAG, "Shipped tag")
        self.return_canceled_tag = self.locator(RETURN_CANCELED_TAG, "Return canceled tag")
        self.payment_ledger_payment_provider = self.locator(PAYMENT_LEDGER_PAYMENT_PROVIDER, "Payment Ledger payment provider")
        self.email_logs_accordion = self.locator(EMAIL_LOGS_ACCORDION, "Email Logs accordion")
        self.view_email_btn = self.locator(VIEW_EMAIL_BTN, "View email button")
        self.email_view = self.locator(EMAIL_VIEW, "Email view")
        self.order_item_status = self.locator(ORDER_ITEM_STATUS, "Order item status")
        self.order_item_canceled_by = self.locator(ORDER_ITEM_CANCELED_BY, "Order item canceled by")
        self.order_items_show_items = self.locator(ORDER_ITEMS_SHOW_ITEMS, "Order items show items")
        self.order_items_pagination_page_two = self.locator(ORDER_ITEMS_PAGINATION_PAGE_TWO, "Order items pagination page two")
        self.coupon_history_accordion = self.locator(COUPON_HISTORY_ACCORDION, "Coupon History accordion")
        self.coupon_code = self.locator(COUPON_CODE, "Coupon code")
        self.signed_by = self.locator(SIGNED_BY, "Signed by")
        self.instruction_dropped_datetime = self.locator(INSTRUCTION_DROPPED_DATETIME, "Instruction dropped datetime")
        self.shipped_from_warehouse_datetime = self.locator(SHIPPED_FROM_WAREHOUSE_DATETIME, "Shipped from warehouse datetime")
        self.delivered_to_customer_datetime = self.locator(DELIVERED_TO_CUSTOMER_DATETIME, "Delivered to customer datetime")
        self.waybill_no = self.locator(WAYBILL_NO, "Waybill number")
        self.courier = self.locator(COURIER, "Courier")
        self.parcel_block = self.locator(PARCEL_BLOCK, "Parcel block")
        self.parcel = self.locator(PARCEL, "Parcel")
        self.order_item = self.locator(ORDER_ITEM, "Order item")
        self.delivered_tag = self.locator(DELIVERED_TAG, "Delivered tag")
        self.track_btn = self.locator(TRACK_BTN, "Track button")
        self.estimated_collection_date = self.locator(ESTIMATED_COLLECTION_DATE, "Estimated collection date")
        self.waybill_estimate_collection_date = self.locator(WAYBILL_ESTIMATE_COLLECTION_DATE, "Waybill estimate collection date")
        self.collection_estimate = self.locator(COLLECTION_ESTIMATE, "Collection estimate")
        self.refund_history_accordion = self.locator(REFUND_HISTORY_ACCORDION, "Refund History accordion")
        self.refunded_amount = self.locator(REFUNDED_AMOUNT, "Refunded amount")
        self.refunded_payment_method = self.locator(REFUNDED_PAYMENT_METHOD, "Refunded payment method")
        self.street_address = self.locator(STREET_ADDRESS, "Street address")
        self.suburb_address = self.locator(SUBURB_ADDRESS, "Suburb address")
        self.city_address = self.locator(CITY_ADDRESS, "City address")
        self.province_address = self.locator(PROVINCE_ADDRESS, "Province address")
        self.code_address = self.locator(CODE_ADDRESS, "Code address")
        self.copy_address_btn = self.locator(COPY_ADDRESS_BTN, "Copy address button")
        self.address_copied_btn = self.locator(ADDRESS_COPIED_BTN, "Address copied button")
        self.residential_txt = self.locator(RESIDENTIAL_TXT, "Residential text")
        self.search_google_icon = self.locator(SEARCH_GOOGLE_ICON, "Search Google icon")
        self.shipping_method = self.locator(SHIPPING_METHOD, "Shipping method")
        self.shipping_plan = self.locator(SHIPPING_PLAN, "Shipping plan")
        self.shipping_courier = self.locator(SHIPPING_COURIER, "Shipping courier")
        self.shipping_promised_date = self.locator(SHIPPING_PROMISED_DATE, "Shipping promised date")
        self.shipping_delivered_date = self.locator(SHIPPING_DELIVERED_DATE, "Shipping delivered date")
        self.instruction_dropped_date1 = self.locator(INSTRUCTION_DROPPED_DATE1, "Instruction dropped date 1")
        self.instruction_dropped_date2 = self.locator(INSTRUCTION_DROPPED_DATE2, "Instruction dropped date 2")
        self.shipped_from_warehouse_date1 = self.locator(SHIPPED_FROM_WAREHOUSE_DATE1, "Shipped from warehouse date 1")
        self.shipped_from_warehouse_date2 = self.locator(SHIPPED_FROM_WAREHOUSE_DATE2, "Shipped from warehouse date 2")
        self.delivered_date1 = self.locator(DELIVERED_DATE1, "Delivered date 1")
        self.delivered_date2 = self.locator(DELIVERED_DATE2, "Delivered date 2")
        self.order_tracking_heading1 = self.locator(ORDER_TRACKING_HEADING1, "Order tracking heading 1")
        self.order_tracking_heading2 = self.locator(ORDER_TRACKING_HEADING2, "Order tracking heading 2")
        self.signed_by1 = self.locator(SIGNED_BY1, "Signed by 1")
        self.signed_by2 = self.locator(SIGNED_BY2, "Signed by 2")
        self.waybill_number1 = self.locator(WAYBILL_NUMBER1, "Waybill number 1")
        self.waybill_number2 = self.locator(WAYBILL_NUMBER2, "Waybill number 2")
        self.waybill_number_link = self.locator(WAYBILL_NUMBER_LINK, "Waybill number link")
        self.mr_dexpress_copyright = self.locator(MR_DEXPRESS_COPYRIGHT, "MR Dexpress copyright")
        self.order_tracking_first_consignment = self.locator(ORDER_TRACKING_FIRST_CONSIGNMENT, "Order tracking first consignment")
        self.first_consigment_delivered_date = self.locator(FIRST_CONSIGMENT_DELIVERED_DATE, "First consignment delivered date")
        self.first_consigment_signed_by = self.locator(FIRST_CONSIGMENT_SIGNED_BY, "First consignment signed by")
        self.first_consigment_waybill_number = self.locator(FIRST_CONSIGMENT_WAYBILL_NUMBER, "First consignment waybill number")
        self.cancelled_items = self.locator(CANCELLED_ITEMS, "Cancelled items")
        self.cancelled_tag = self.locator(CANCELLED_TAG, "Cancelled tag")
        self.part_delivered_date = self.locator(PART_DELIVERED_DATE, "Part delivered date")
        self.ip_address_icon = self.locator(IP_ADDRESS_ICON, "IP address icon")
        self.ip_address = self.locator(IP_ADDRESS, "IP address")
        self.ip_address_model = self.locator(IP_ADDRESS_MODEL, "IP address model")
        self.first_consigment_track_btn = self.locator(FIRST_CONSIGMENT_TRACK_BTN, "First consignment track button")
        self.tracking_waybill_number = self.locator(TRACKING_WAYBILL_NUMBER, "Tracking waybill number")
        self.tracking_first_parcel_info = self.locator(TRACKING_FIRST_PARCEL_INFO, "Tracking first parcel info")
        self.tracking_first_parcel_number = self.locator(TRACKING_FIRST_PARCEL_NUMBER, "Tracking first parcel number")
        self.tracking_first_parcel_item = self.locator(TRACKING_FIRST_PARCEL_ITEM, "Tracking first parcel item")
        self.order_items_accordion = self.locator(ORDER_ITEMS_ACCORDION, "Order items accordion")
        self.collection_estimate_date = self.locator(COLLECTION_ESTIMATE_DATE, "Collection estimate date")
        self.collection_not_yet_ready_message = self.locator(COLLECTION_NOT_YET_READY_MESSAGE, "Collection not yet ready message")
        self.delivery_estimate_date = self.locator(DELIVERY_ESTIMATE_DATE, "Delivery estimate date")
        self.delivery_not_yet_ready_message = self.locator(DELIVERY_NOT_YET_READY_MESSAGE, "Delivery not yet ready message")
        self.send_email_btn = self.locator(SEND_EMAIL_BTN, "Send email button")
        self.edit_customer_btn = self.locator(EDIT_CUSTOMER_BTN, "Edit customer button")
        self.cust_name = self.locator(CUST_NAME, "Customer name")
        self.cust_surname = self.locator(CUST_SURNAME, "Customer surname")
        self.business_name = self.locator(BUSINESS_NAME, "Business name")
        self.vat_number = self.locator(VAT_NUMBER, "VAT number")
        self.acc_status_ddl = self.locator(ACC_STATUS_DDL, "Account status dropdown")
        self.acc_status = self.locator(ACC_STATUS, "Account status")
        self.staff_account_check = self.locator(STAFF_ACCOUNT_CHECK, "Staff account check")
        self.block_vou_check = self.locator(BLOCK_VOU_CHECK, "Block voucher check")
        self.confirm_btn = self.locator(CONFIRM_BTN, "Confirm button")
        self.pop_up = self.locator(POP_UP, "Popup")
