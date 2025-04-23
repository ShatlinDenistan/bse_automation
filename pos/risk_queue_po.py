from base.page_base import PageBase

# Module-level constants for selectors
ALL_ORDER_ID_COLUMNS = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
APPLY_FILTER_BTN = "//button[contains(text(), 'Filter')]"
CHECKBOX_DAILY_DEALS = '//*[@id="root"]/div[3]/div/div/form/div/div/div[1]/div/div/div[1]/div'
CLEAR_FILTER_BTN = "//button[contains(text(), 'Clear Filter')]"
CLEAR_RISK_BTN = '//body/div[@id="root"]/div[3]/div/div/table/tfoot/tr/th/div/div[1]'
DATE_RANGE_CHECKBOX = '//*[@id="root"]/div[3]/div/div/form/div/div/div[2]/div/div[3]/div'
DATE_RANGE_FILTER = '//*[@id="root"]/div[3]/div/div/form/div/div/div[2]/div/div[4]/div'
MENU_BTN = '//i[@aria-hidden="true" and @class="content large icon"]'
MINIMUM_ORDER_TOTAL_DROPDOWN = "//div[@name='minimumTotal']"
MINIMUM_ORDER_TOTAL_R500 = "//div[@name='minimumTotal']//span[text()='500']"
MINIMUM_ORDER_TOTAL_R0 = "//div[@name='minimumTotal']//span[text()='0']"
MAXIMUM_ORDER_TOTAL_DROPDOWN = "//div[@name='maximumTotal']"
MAXIMUM_ORDER_TOTAL_R5000 = "//div[@name='maximumTotal']//span[text()='5000']"
NEXT_PAGE = '//body/div[@id="root"]/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[2]/a[2]'
ORDER_CHECKBOX = '//body/div[@id="root"]/div[3]/div/div/table/tbody/tr[1]/td[1]/div'
RESULTS_TABLE = '//*[@class="ui small celled compact table"]'
RISK_QUEUE_MENU_OPTION = '//body/div[@id="root"]/div[1]/a[4]'
PAYMENT_METHOD_CREDIT = "//span[text()='Credit']"
PAYMENT_METHOD_DEPOSIT = "//span[text()='Deposit']"
PAYMENT_METHOD_DROPDOWN = "//div[@name='paymentMethod']"
PAYMENT_METHOD_PAYFAST = "//span[text()='PayFast']"
ALL_PAYMENT_METHOD_COLUMNS = "//td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 7)]"
SHIPPING_METHOD_DROPDOWN = "//div[@name='shippingMethod']"
SHIPPING_METHOD_DELIVERY = "//span[text()='Courier']"
VIRTUAL_ITEMS_CHECKBOX = '//*[@id="root"]/div[3]/div/div/form/div/div/div[1]/div/div/div[2]/div'
ITEM_LIST_DDL = "//div[@class='content' and contains(text(), 'Show')]/following-sibling::div"
LIST_FILTER_10 = "//span[text()='10']"

BTN_SEND_EMAIL_TABLE = "//table/tfoot/tr/th/div/div[3]/button"
DDL_EMAIL_TEMPLATES = "//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]"
BTN_SEND_EMAIL = "//button[contains(text(),'Send Emails')]"
EMAIL_SENT_MODAL = "/html/body/div[2]/div"
EMAIL_SENT_MODAL_CLOSE_ICON = "//i[@class='close icon']"

# Email template options
OPTION_TEMPLATES = {
    1: "//span[contains(text(),'Identification required: Credit card')]",
    2: "//span[contains(text(),'Identification and card details required')]",
    3: "//span[contains(text(),'Identification required: Payfast & Ozow')]",
    4: "//span[contains(text(),'Identification not accepted')]",
    5: "//span[contains(text(),'Identification not received: Payfast & Ozow')]",
    6: "//span[contains(text(),'Identification not received: Credit card')]",
    7: "//span[contains(text(),'Credit card refund failed')]",
    8: "//span[contains(text(),'EFT refund failed')]",
    9: "//span[contains(text(),'Refund delayed')]",
    10: "//span[contains(text(),'Short paid')]",
    11: "//span[contains(text(),'Deposit Match')]",
    12: "//span[contains(text(),'Duplicate Payment')]",
    13: "//span[contains(text(),'Voucher Payment')]",
    14: "//span[contains(text(),'Generic')]",
}

# Cancel order elements
RISK_QUEUE_CANCEL_ORDER_BUTTON = "//button[contains(text(), 'Cancel Order(s)')]"
CANCEL_ORDERS_MODAL_HEADER = "//div[contains(text(),'Please confirm')]"
CANCELLATION_REASON_DROPDOWN = "//div[@name='cancelReason']"
CANCELLATION_REASON_OPTIONS = {
    1: "//span[contains(text(), 'Customer request')]",
    2: "//span[contains(text(), 'Supplier out of stock')]",
    3: "//span[contains(text(), 'Fraud')]",
    4: "//span[contains(text(), 'Damaged')]",
    5: "//span[contains(text(), 'Incorrect Packaging')]",
}
CANCEL_ORDERS_MODAL_CANCEL_BUTTON = "//button[contains(text(), 'Cancel Orders')]"
CANCEL_ORDERS_MODAL = "//div[contains(@class, 'ui large modal transition visible active')]"
CANCEL_ORDER_MODAL_SUCCESS_MESSAGE = "//div[contains(@class, 'ui success message')]/div/div"
CANCEL_ORDERS_MODAL_CLOSE_ICON = "//*[@class= 'close icon']"
ORDER_ID_HYPERLINK = '//*[@id="root"]/div[3]/div/div/table/tbody/tr[1]/td[2]/a'
FIN_PORTAL_GLOBAL_SEARCH_FIELD = "//*[@name='searchText' and @type='text']"
FIN_PORTAL_GLOBAL_SEARCH_ICON = "//*[@class='search icon']"
CANCELED_BY_ORDER_PAGE_BADGE = "//div[contains(text(), 'Canceled by')]"
ORDER_ITEM_CANCELLATION_REASON = "//div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]"


class RiskQueuePO(PageBase):
    """Page Object for the Risk Queue page."""

    def __init__(self, page):
        """Initialize Risk Queue Page Object with all locators."""
        super().__init__(page)

        # Main navigation elements
        self.menu_btn = self.locator(MENU_BTN, "Menu button")
        self.risk_queue_menu_option = self.locator(RISK_QUEUE_MENU_OPTION, "Risk Queue menu option")
        self.results_table = self.locator(RESULTS_TABLE, "Results table")

        # Pagination elements
        self.item_list_dropdown = self.locator(ITEM_LIST_DDL, "Item list dropdown")
        self.list_filter_10 = self.locator(LIST_FILTER_10, "10 items filter")
        self.next_page = self.locator(NEXT_PAGE, "Next page button")

        # Risk management elements
        self.order_checkbox = self.locator(ORDER_CHECKBOX, "Order checkbox")
        self.clear_risk_btn = self.locator(CLEAR_RISK_BTN, "Clear risk button")

        # Filter elements
        self.clear_filter_btn = self.locator(CLEAR_FILTER_BTN, "Clear filter button")
        self.apply_filter_btn = self.locator(APPLY_FILTER_BTN, "Apply filter button")

        # Payment method filter
        self.payment_method_dropdown = self.locator(PAYMENT_METHOD_DROPDOWN, "Payment method dropdown")
        self.payment_method_credit = self.locator(PAYMENT_METHOD_CREDIT, "Credit payment method")
        self.payment_method_payfast = self.locator(PAYMENT_METHOD_PAYFAST, "PayFast payment method")
        self.all_payment_method_columns = self.locator(ALL_PAYMENT_METHOD_COLUMNS, "All payment method columns")

        # Shipping method filter
        self.shipping_method_dropdown = self.locator(SHIPPING_METHOD_DROPDOWN, "Shipping method dropdown")
        self.shipping_method_delivery = self.locator(SHIPPING_METHOD_DELIVERY, "Delivery shipping method")

        # Order total filter
        self.minimum_order_total_dropdown = self.locator(MINIMUM_ORDER_TOTAL_DROPDOWN, "Minimum order total dropdown")
        self.minimum_order_total_r500 = self.locator(MINIMUM_ORDER_TOTAL_R500, "R500 minimum order total")
        self.minimum_order_total_r0 = self.locator(MINIMUM_ORDER_TOTAL_R0, "R0 minimum order total")
        self.maximum_order_total_dropdown = self.locator(MAXIMUM_ORDER_TOTAL_DROPDOWN, "Maximum order total dropdown")
        self.maximum_order_total_r5000 = self.locator(MAXIMUM_ORDER_TOTAL_R5000, "R5000 maximum order total")

        # Additional filters
        self.checkbox_daily_deals = self.locator(CHECKBOX_DAILY_DEALS, "Daily deals checkbox")
        self.virtual_items_checkbox = self.locator(VIRTUAL_ITEMS_CHECKBOX, "Virtual items checkbox")
        self.date_range_checkbox = self.locator(DATE_RANGE_CHECKBOX, "Date range checkbox")
        self.date_range_filter = self.locator(DATE_RANGE_FILTER, "Date range filter")

        # Email elements
        self.btn_send_email_table = self.locator(BTN_SEND_EMAIL_TABLE, "Send email table button")
        self.ddl_email_templates = self.locator(DDL_EMAIL_TEMPLATES, "Email templates dropdown")
        self.btn_send_email = self.locator(BTN_SEND_EMAIL, "Send email button")
        self.email_sent_modal = self.locator(EMAIL_SENT_MODAL, "Email sent modal")
        self.email_sent_modal_close_icon = self.locator(EMAIL_SENT_MODAL_CLOSE_ICON, "Email sent modal close icon")

        # Email template options
        self.email_template_options = {}
        for key, value in OPTION_TEMPLATES.items():
            self.email_template_options[key] = self.locator(value, f"Email template option {key}")

        # Cancel order elements
        self.risk_queue_cancel_order_button = self.locator(RISK_QUEUE_CANCEL_ORDER_BUTTON, "Cancel order button")
        self.cancel_orders_modal_header = self.locator(CANCEL_ORDERS_MODAL_HEADER, "Cancel orders modal header")
        self.cancellation_reason_dropdown = self.locator(CANCELLATION_REASON_DROPDOWN, "Cancellation reason dropdown")

        # Cancellation reason options
        self.cancellation_reason_options = {}
        for key, value in CANCELLATION_REASON_OPTIONS.items():
            self.cancellation_reason_options[key] = self.locator(value, f"Cancellation reason option {key}")

        self.cancel_orders_modal_cancel_button = self.locator(CANCEL_ORDERS_MODAL_CANCEL_BUTTON, "Cancel orders button")
        self.cancel_orders_modal = self.locator(CANCEL_ORDERS_MODAL, "Cancel orders modal")
        self.cancel_order_modal_success_message = self.locator(CANCEL_ORDER_MODAL_SUCCESS_MESSAGE, "Cancel order success message")
        self.cancel_orders_modal_close_icon = self.locator(CANCEL_ORDERS_MODAL_CLOSE_ICON, "Cancel orders modal close icon")

        # Order identification elements
        self.order_id_hyperlink = self.locator(ORDER_ID_HYPERLINK, "Order ID hyperlink")
        self.fin_portal_global_search_field = self.locator(FIN_PORTAL_GLOBAL_SEARCH_FIELD, "Global search field")
        self.fin_portal_global_search_icon = self.locator(FIN_PORTAL_GLOBAL_SEARCH_ICON, "Global search icon")
        self.canceled_by_order_page_badge = self.locator(CANCELED_BY_ORDER_PAGE_BADGE, "Canceled by badge")
        self.order_item_cancellation_reason = self.locator(ORDER_ITEM_CANCELLATION_REASON, "Order item cancellation reason")
