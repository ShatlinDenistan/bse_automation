from base.page_base import PageBase

# Module-level constants for all locators
APPLY_SEARCH_FILTER = "//button[contains(text(), 'Filter')]"
ALL_ORDER_PAID_COLUMNS = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 7)]"
ALL_ORDER_STATUS_COLUMNS = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]"
CLEAR_FILTER = "//button[contains(text(), 'Clear Filter')]"
NOT_PAID_BTN = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[5]/button'
CLOSE_ICON = '//i[@aria-hidden="true" and @class="close icon"]'
EXPIRE_BTN = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[3]/button'
MENU_BTN = '//i[@aria-hidden="true" and @class="content large icon"]'
ORDER_ID_CHECKBOX = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div'
PAID_STATUS_DROPDOWN = '//*[@id="root"]/div[3]/div/div/div/form/div/div/div[5]/div/div'
PAID_BTN = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[4]/button'
PAID_STATUS_OPTION = "//span[text()='Paid']"
NOT_PAID_STATUS_OPTION = "//span[text()='Not Paid']"
RESULTS_TABLE = '//*[@class="ui small celled compact table"]'
REDEEMED_STATUS_DROPDOWN = '//*[@id="root"]/div[3]/div/div/div/form/div/div/div[4]/div/div/div[1]'
REDEEMED_STATUS_AVAILABLE = "//span[text()='Available']"
VERIFICATION_MESSAGE = "//div[contains(text(),'Successfully processed 1 item(s)')]"
VOUCHERS_MENU_OPTION = "//body/div[@id='root']/div[1]/a[2]"
REDEEMED_STATUS_CANCELLED = "//span[text()='Cancelled']"
ACTIVE_BTN = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[2]/button'
ACTIVE_VOUCHER_BTN = "//html/body/div[2]/div/div[2]/div/div[2]"
VERIFY_ACTIVATED_VOUCHER = "//div[contains(text(),'Successfully processed 1 item(s)')]"
VOUCHER_CODE = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[6]/a'
FILTER_BY_FIELD = "//div[@name='searchCriteria']"
FILTER_BY_VOUCHER_CODE = "//span[contains(text(), 'Voucher Code')]"
SEARCH_TERM_FIELD = "//*[@name='searchTerm']"
VOUCHER_STATUS = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr/td[10]/div'
PAID_STATUS = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr/td[8]/div'
VOUCHER_CATEGORY_DROPDOWN = '//*[@id="root"]/div[3]/div/div/div/form/div/div/div[3]/div'
VOUCHER_CATEGORY_CV = "//span[contains(text(), 'Corporate Voucher')]"
VOUCHER_CATEGORY_LIST = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 4)]"
REDEEMED_STATUS_LIST = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]"
VOUCHER_ORDER_ID = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
SEARCH_CRITERIA_OPTION_ORDER_ID = "//span[contains(text(), 'Order ID')]"
VOUCHER_CODE_ID = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 5)]"
REDEEMED_STATUS_REDEEMED = "//span[text()='Redeemed']"
FILTER_BY_CUSTOMER_ID = "//span[contains(text(), 'Customer ID')]"
OPEN_CUSTOMER_INFO = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[4]/a'
OPEN_USED_BY_CUSTOMER_INFO = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[12]/a'
FILTER_BY_USED_BY_CUSTOMER_ID = "//span[contains(text(), 'Used By Customer ID')]"
CUSTOMER_INFO_ID = '//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/span'
EMAIL_BTN = '//*[@class="mail icon"]'
EMAIL_SENT_MODAL = "/html/body/div[2]/div"
EMAIL_SENT_MODAL_CLOSE_ICON = "//body/div[2]/div[1]/i[1]"
DATE_FILTER = "//input[@name='dateRange']"
APPLY_FILTER_BTN = "//button[contains(text(), 'Filter')]"
RESULTS_TABLE = '//*[@class="ui small celled compact table"]'


class VouchersPO(PageBase):
    """Page Object for Vouchers page"""

    def __init__(self, page):
        super().__init__(page)

        # Initialize all locators
        self.apply_search_filter = self.locator(APPLY_SEARCH_FILTER, "Apply search filter button")
        self.all_order_paid_columns = self.locator(ALL_ORDER_PAID_COLUMNS, "All order paid columns")
        self.all_order_status_columns = self.locator(ALL_ORDER_STATUS_COLUMNS, "All order status columns")
        self.clear_filter = self.locator(CLEAR_FILTER, "Clear filter button")
        self.not_paid_btn = self.locator(NOT_PAID_BTN, "Not paid button")
        self.close_icon = self.locator(CLOSE_ICON, "Close icon")
        self.expire_btn = self.locator(EXPIRE_BTN, "Expire button")
        self.menu_btn = self.locator(MENU_BTN, "Menu button")
        self.order_id_checkbox = self.locator(ORDER_ID_CHECKBOX, "Order ID checkbox")
        self.paid_status_dropdown = self.locator(PAID_STATUS_DROPDOWN, "Paid status dropdown")
        self.paid_btn = self.locator(PAID_BTN, "Paid button")
        self.paid_status_option = self.locator(PAID_STATUS_OPTION, "Paid status option")
        self.not_paid_status_option = self.locator(NOT_PAID_STATUS_OPTION, "Not paid status option")
        self.results_table = self.locator(RESULTS_TABLE, "Results table")
        self.redeemed_status_dropdown = self.locator(REDEEMED_STATUS_DROPDOWN, "Redeemed status dropdown")
        self.redeemed_status_available = self.locator(REDEEMED_STATUS_AVAILABLE, "Redeemed status available option")
        self.verification_message = self.locator(VERIFICATION_MESSAGE, "Verification message")
        self.vouchers_menu_option = self.locator(VOUCHERS_MENU_OPTION, "Vouchers menu option")
        self.redeemed_status_cancelled = self.locator(REDEEMED_STATUS_CANCELLED, "Redeemed status cancelled option")
        self.active_btn = self.locator(ACTIVE_BTN, "Active button")
        self.active_voucher_btn = self.locator(ACTIVE_VOUCHER_BTN, "Active voucher button")
        self.verify_activated_voucher = self.locator(VERIFY_ACTIVATED_VOUCHER, "Verify activated voucher message")
        self.voucher_code = self.locator(VOUCHER_CODE, "Voucher code")
        self.filter_by_field = self.locator(FILTER_BY_FIELD, "Filter by field")
        self.filter_by_voucher_code = self.locator(FILTER_BY_VOUCHER_CODE, "Filter by voucher code option")
        self.search_term_field = self.locator(SEARCH_TERM_FIELD, "Search term field")
        self.voucher_status = self.locator(VOUCHER_STATUS, "Voucher status")
        self.paid_status = self.locator(PAID_STATUS, "Paid status")
        self.voucher_category_dropdown = self.locator(VOUCHER_CATEGORY_DROPDOWN, "Voucher category dropdown")
        self.voucher_category_cv = self.locator(VOUCHER_CATEGORY_CV, "Voucher category CV option")
        self.voucher_category_list = self.locator(VOUCHER_CATEGORY_LIST, "Voucher category list")
        self.redeemed_status_list = self.locator(REDEEMED_STATUS_LIST, "Redeemed status list")
        self.voucher_order_id = self.locator(VOUCHER_ORDER_ID, "Voucher order ID")
        self.search_criteria_option_order_id = self.locator(SEARCH_CRITERIA_OPTION_ORDER_ID, "Search criteria option order ID")
        self.voucher_code_id = self.locator(VOUCHER_CODE_ID, "Voucher code ID")
        self.redeemed_status_redeemed = self.locator(REDEEMED_STATUS_REDEEMED, "Redeemed status redeemed option")
        self.filter_by_customer_id = self.locator(FILTER_BY_CUSTOMER_ID, "Filter by customer ID option")
        self.open_customer_info = self.locator(OPEN_CUSTOMER_INFO, "Open customer info link")
        self.open_used_by_customer_info = self.locator(OPEN_USED_BY_CUSTOMER_INFO, "Open used by customer info link")
        self.filter_by_used_by_customer_id = self.locator(FILTER_BY_USED_BY_CUSTOMER_ID, "Filter by used by customer ID option")
        self.customer_info_id = self.locator(CUSTOMER_INFO_ID, "Customer info ID")
        self.email_btn = self.locator(EMAIL_BTN, "Email button")
        self.email_sent_modal = self.locator(EMAIL_SENT_MODAL, "Email sent modal")
        self.email_sent_modal_close_icon = self.locator(EMAIL_SENT_MODAL_CLOSE_ICON, "Email sent modal close icon")
        self.date_filter = self.locator(DATE_FILTER, "Date filter")
        self.apply_filter_btn = self.locator(APPLY_FILTER_BTN, "Apply filter button")
