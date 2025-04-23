from base.page_base import PageBase
import random

# Module-level constants for all locators
ORDER_LIST_TABLE = "//table[@class='ui small celled compact table']//tbody//tr"
BTN_MENU = "//i[@class='content large icon' and @aria-hidden='true']"
ORDER_LIST_TABLE_ROW = "//table[@class='ui small celled compact table']//tr"
ORDER_LIST_MENU_OPTION = "//*[contains(text(),'Order List')]"
CLEAR_AUTH_STATUS_ICON = "//i[@class='dropdown icon clear' and @aria-hidden='true']"
CLEAR_DATE_RANGE_TODAY = "//div[@class='ui checked checkbox']//label[text()='Today']"
ORDER_LIST_APPLY_FILTER_BUTTON = "//button[contains(text(), 'Apply Filter')]"
PAST_10_DAYS = "//label[text()='Past 10 Days']"
FIRST_ROW_WITH_ORDER_STATUS_NEW_ORDER_CHECKBOX = "//tr[td[9]/div[contains(text(), 'New Order')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
SECOND_ROW_WITH_ORDER_STATUS_NEW_ORDER_CHECKBOX = "//tr[td[9]/div[contains(text(), 'New Order')]][2]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
THIRD_ROW_WITH_ORDER_STATUS_NEW_ORDER_CHECKBOX = "//tr[td[9]/div[contains(text(), 'New Order')]][3]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
ORDER_ID_COLUMN = "//tr[td[9]/div[contains(text(), 'New Order')]][1]//a[contains(@href, '/order/')]"
ORDER_ID_COLUMN2 = "//tr[td[9]/div[contains(text(), 'New Order')]][2]//a[contains(@href, '/order/')]"
ORDER_ID_COLUMN3 = "//tr[td[9]/div[contains(text(), 'New Order')]][3]//a[contains(@href, '/order/')]"
ORDER_LIST_AUTHORISE_ORDER_BUTTON = "//button[contains(text(), 'Authorise Order(s)')]"
AUTHORISE_ORDERS_MODAL = "//div[contains(@class, 'ui large modal transition visible active')]"
AUTHORISE_ORDERS_MODAL_CLOSE_ICON = "//*[@class= 'close icon']"
FIN_PORTAL_GLOBAL_SEARCH_FIELD = "//*[@name='searchText' and @type='text']"
FIN_PORTAL_GLOBAL_SEARCH_ICON = "//*[@class='search icon']"
AUTHED_BY_ORDER_PAGE_BADGE = "//div[contains(text(), 'Auth by')]"
ORDER_LIST_CANCEL_ORDER_BUTTON = "//button[contains(text(), 'Cancel Order(s)')]"
CANCEL_ORDERS_MODAL_HEADER = "//div[contains(text(),'Please confirm')]"
CANCELLATION_REASON_DROPDOWN = "//div[@name='cancelReason']"
CANCELLATION_REASON_CUSTOMER_REQUEST = "//span[contains(text(), 'Customer request')]"
CANCELLATION_REASON_SUPPLIER_OUT_OF_STOCK = "//span[contains(text(), 'Supplier out of stock')]"
CANCELLATION_REASON_FRAUD = "//span[contains(text(), 'Fraud')]"
CANCELLATION_REASON_DAMAGED = "//span[contains(text(), 'Damaged')]"
CANCELLATION_REASON_INCORRECT_PACKAGING = "//span[contains(text(), 'Incorrect Packaging')]"
CANCEL_ORDERS_MODAL_CANCEL_BUTTON = "//button[contains(text(), 'Cancel Orders')]"
CANCEL_ORDERS_MODAL = "//div[contains(@class, 'ui large modal transition visible active')]"
CANCEL_ORDERS_MODAL_CLOSE_ICON = "//*[@class= 'close icon']"
CANCELED_BY_ORDER_PAGE_BADGE = "//div[contains(text(), 'Canceled by')]"
ORDER_ITEM_CANCELLATION_REASON = "//div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]"
FIRST_ROW_WITH_ORDER_STATUS_CANCELLED_CHECKBOX = "//tr[td[9]/div[contains(text(), 'Canceled')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
ORDER_ID_COLUMN_CANCELED = "//tr[td[9]/div[contains(text(), 'Canceled')]][1]//a[contains(@href, '/order/')]"
ORDER_LIST_CLEAR_FILTER_BUTTON = "//button[contains(text(), 'Clear Filter')]"
DAILY_DEALS_CHECKBOX = "//label[text()='Daily Deals']"
ALL_ORDER_ID_COLUMNS = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
AUTH_STATUS_DROPDOWN = "//div[@name='authStatus']"
AUTH_STATUS_NEW = "//span[contains(text(), 'New')]"
AUTH_STATUS_AUTH = "//span[text()='Auth']"
ALL_AUTH_STATUS_COLUMNS = "//td[position() = (count(//th[text()='Auth Status']/preceding-sibling::th) + 1)]"
PAYMENT_METHOD_DROPDOWN = "//div[@name='paymentMethod']"
PAYMENT_METHOD_CREDIT_CARD = "//span[text()='Credit Card']"
PAYMENT_METHOD_CREDIT = "//span[text()='Credit']"
PAYMENT_METHOD_PAYFAST = "//span[text()='PayFast']"
PAYMENT_METHOD_DEPOSIT = "//span[text()='Deposit']"
ALL_PAYMENT_METHOD_COLUMNS = "//td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 1)]"
SHIPPING_METHOD_DROPDOWN = "//div[@name='shippingMethod']"
SHIPPING_METHOD_COLLECT = "//span[text()='Collect']"
SHIPPING_METHOD_COURIER = "//span[text()='Courier']"
MINIMUM_ORDER_TOTAL_DROPDOWN = "//div[@name='minimumTotal']"
MINIMUM_ORDER_TOTAL_R500 = "//div[@name='minimumTotal']//span[text()='R 500']"
MINIMUM_ORDER_TOTAL_R0 = "//div[@name='minimumTotal']//span[text()='R 0']"
MAXIMUM_ORDER_TOTAL_DROPDOWN = "//div[@name='maximumTotal']"
MAXIMUM_ORDER_TOTAL_R500 = "//div[@name='maximumTotal']//span[text()='R 500']"
ALL_ORDER_TOTAL_COLUMNS = "//td[position() = (count(//th[text()='Order Total']/preceding-sibling::th) + 1)]"


class OrderListPO(PageBase):
    """Page Object for Order List page."""

    def __init__(self, page):
        super().__init__(page)
        # Initialize all elements using self.locator
        self.order_list_table = self.locator(ORDER_LIST_TABLE, "Order list table")
        self.btn_menu = self.locator(BTN_MENU, "Menu button")
        self.order_list_menu_option = self.locator(ORDER_LIST_MENU_OPTION, "Order list menu option")
        self.clear_auth_status_icon = self.locator(CLEAR_AUTH_STATUS_ICON, "Clear auth status icon")
        self.clear_date_range_today = self.locator(CLEAR_DATE_RANGE_TODAY, "Clear date range today")
        self.order_list_apply_filter_button = self.locator(ORDER_LIST_APPLY_FILTER_BUTTON, "Apply filter button")
        self.past_10_days = self.locator(PAST_10_DAYS, "Past 10 days")
        self.first_row_new_order_checkbox = self.locator(FIRST_ROW_WITH_ORDER_STATUS_NEW_ORDER_CHECKBOX, "First new order checkbox")
        self.second_row_new_order_checkbox = self.locator(SECOND_ROW_WITH_ORDER_STATUS_NEW_ORDER_CHECKBOX, "Second new order checkbox")
        self.third_row_new_order_checkbox = self.locator(THIRD_ROW_WITH_ORDER_STATUS_NEW_ORDER_CHECKBOX, "Third new order checkbox")
        self.order_id_column = self.locator(ORDER_ID_COLUMN, "First order ID")
        self.order_id_column2 = self.locator(ORDER_ID_COLUMN2, "Second order ID")
        self.order_id_column3 = self.locator(ORDER_ID_COLUMN3, "Third order ID")
        self.authorise_order_button = self.locator(ORDER_LIST_AUTHORISE_ORDER_BUTTON, "Authorise order button")
        self.authorise_orders_modal = self.locator(AUTHORISE_ORDERS_MODAL, "Authorise orders modal")
        self.authorise_orders_modal_close_icon = self.locator(AUTHORISE_ORDERS_MODAL_CLOSE_ICON, "Authorise modal close icon")
        self.global_search_field = self.locator(FIN_PORTAL_GLOBAL_SEARCH_FIELD, "Global search field")
        self.global_search_icon = self.locator(FIN_PORTAL_GLOBAL_SEARCH_ICON, "Global search icon")
        self.authed_by_badge = self.locator(AUTHED_BY_ORDER_PAGE_BADGE, "Authed by badge")
        self.cancel_order_button = self.locator(ORDER_LIST_CANCEL_ORDER_BUTTON, "Cancel order button")
        self.cancel_orders_modal_header = self.locator(CANCEL_ORDERS_MODAL_HEADER, "Cancel orders modal header")
        self.cancellation_reason_dropdown = self.locator(CANCELLATION_REASON_DROPDOWN, "Cancellation reason dropdown")
        self.reason_customer_request = self.locator(CANCELLATION_REASON_CUSTOMER_REQUEST, "Reason: Customer request")
        self.reason_supplier_out_of_stock = self.locator(CANCELLATION_REASON_SUPPLIER_OUT_OF_STOCK, "Reason: Supplier out of stock")
        self.reason_fraud = self.locator(CANCELLATION_REASON_FRAUD, "Reason: Fraud")
        self.reason_damaged = self.locator(CANCELLATION_REASON_DAMAGED, "Reason: Damaged")
        self.reason_incorrect_packaging = self.locator(CANCELLATION_REASON_INCORRECT_PACKAGING, "Reason: Incorrect Packaging")
        self.cancel_orders_button = self.locator(CANCEL_ORDERS_MODAL_CANCEL_BUTTON, "Cancel orders button")
        self.cancel_orders_modal = self.locator(CANCEL_ORDERS_MODAL, "Cancel orders modal")
        self.cancel_orders_modal_close_icon = self.locator(CANCEL_ORDERS_MODAL_CLOSE_ICON, "Cancel modal close icon")
        self.canceled_by_badge = self.locator(CANCELED_BY_ORDER_PAGE_BADGE, "Canceled by badge")
        self.order_item_cancellation_reason = self.locator(ORDER_ITEM_CANCELLATION_REASON, "Order item cancellation reason")
        self.first_row_canceled_checkbox = self.locator(FIRST_ROW_WITH_ORDER_STATUS_CANCELLED_CHECKBOX, "First canceled order checkbox")
        self.order_id_column_canceled = self.locator(ORDER_ID_COLUMN_CANCELED, "Canceled order ID")
        self.clear_filter_button = self.locator(ORDER_LIST_CLEAR_FILTER_BUTTON, "Clear filter button")
        self.daily_deals_checkbox = self.locator(DAILY_DEALS_CHECKBOX, "Daily deals checkbox")
        self.all_order_id_columns = self.locator(ALL_ORDER_ID_COLUMNS, "All order ID columns")
        self.auth_status_dropdown = self.locator(AUTH_STATUS_DROPDOWN, "Auth status dropdown")
        self.auth_status_new = self.locator(AUTH_STATUS_NEW, "Auth status: New")
        self.auth_status_auth = self.locator(AUTH_STATUS_AUTH, "Auth status: Auth")
        self.all_auth_status_columns = self.locator(ALL_AUTH_STATUS_COLUMNS, "All auth status columns")
        self.payment_method_dropdown = self.locator(PAYMENT_METHOD_DROPDOWN, "Payment method dropdown")
        self.payment_method_credit_card = self.locator(PAYMENT_METHOD_CREDIT_CARD, "Payment method: Credit Card")
        self.payment_method_credit = self.locator(PAYMENT_METHOD_CREDIT, "Payment method: Credit")
        self.payment_method_payfast = self.locator(PAYMENT_METHOD_PAYFAST, "Payment method: PayFast")
        self.payment_method_deposit = self.locator(PAYMENT_METHOD_DEPOSIT, "Payment method: Deposit")
        self.all_payment_method_columns = self.locator(ALL_PAYMENT_METHOD_COLUMNS, "All payment method columns")
        self.shipping_method_dropdown = self.locator(SHIPPING_METHOD_DROPDOWN, "Shipping method dropdown")
        self.shipping_method_collect = self.locator(SHIPPING_METHOD_COLLECT, "Shipping method: Collect")
        self.shipping_method_courier = self.locator(SHIPPING_METHOD_COURIER, "Shipping method: Courier")
        self.minimum_order_total_dropdown = self.locator(MINIMUM_ORDER_TOTAL_DROPDOWN, "Minimum order total dropdown")
        self.minimum_order_total_r500 = self.locator(MINIMUM_ORDER_TOTAL_R500, "Minimum order total: R500")
        self.minimum_order_total_r0 = self.locator(MINIMUM_ORDER_TOTAL_R0, "Minimum order total: R0")
        self.maximum_order_total_dropdown = self.locator(MAXIMUM_ORDER_TOTAL_DROPDOWN, "Maximum order total dropdown")
        self.maximum_order_total_r500 = self.locator(MAXIMUM_ORDER_TOTAL_R500, "Maximum order total: R500")
        self.all_order_total_columns = self.locator(ALL_ORDER_TOTAL_COLUMNS, "All order total columns")
