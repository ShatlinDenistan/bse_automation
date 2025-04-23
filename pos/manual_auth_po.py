from base.page_base import PageBase

# Selector constants
MANUAL_AUTH_HEADER = "//h1[contains(text(),'Manual Auth')]"
SEARCH_ORDER_INPUT = "//input[@id='searchOrderInput']"
SEARCH_BUTTON = "//button[@id='searchOrderBtn']"
ORDER_TABLE = "//table[@id='orderTable']"
ORDER_ROWS = "//table[@id='orderTable']/tbody/tr"
ORDER_ID_COLUMN = "//table[@id='orderTable']/tbody/tr/td[1]"
CUSTOMER_NAME_COLUMN = "//table[@id='orderTable']/tbody/tr/td[2]"
ORDER_DATE_COLUMN = "//table[@id='orderTable']/tbody/tr/td[3]"
ORDER_AMOUNT_COLUMN = "//table[@id='orderTable']/tbody/tr/td[4]"
AUTHORIZE_BUTTON = "//button[@id='authorizeBtn']"
REJECT_BUTTON = "//button[@id='rejectBtn']"
REASON_DROPDOWN = "//select[@id='reasonSelect']"
COMMENTS_TEXTAREA = "//textarea[@id='commentsTextarea']"
CONFIRM_AUTH_BUTTON = "//button[@id='confirmAuthBtn']"
CANCEL_AUTH_BUTTON = "//button[@id='cancelAuthBtn']"
CONFIRMATION_MODAL = "//div[@class='modal-content']"
MODAL_OK_BUTTON = "//button[contains(@class,'btn-primary')]"


class ManualAuthPO(PageBase):
    """Page Object class for Manual Authorization screen"""

    def __init__(self, page):
        super().__init__(page)

        # Initialize locators
        self.manual_auth_header = self.locator(MANUAL_AUTH_HEADER, "Manual Auth Header")
        self.search_order_input = self.locator(SEARCH_ORDER_INPUT, "Search Order Input")
        self.search_button = self.locator(SEARCH_BUTTON, "Search Button")
        self.order_table = self.locator(ORDER_TABLE, "Order Table")
        self.order_rows = self.locator(ORDER_ROWS, "Order Rows")
        self.order_id_column = self.locator(ORDER_ID_COLUMN, "Order ID Column")
        self.customer_name_column = self.locator(CUSTOMER_NAME_COLUMN, "Customer Name Column")
        self.order_date_column = self.locator(ORDER_DATE_COLUMN, "Order Date Column")
        self.order_amount_column = self.locator(ORDER_AMOUNT_COLUMN, "Order Amount Column")
        self.authorize_button = self.locator(AUTHORIZE_BUTTON, "Authorize Button")
        self.reject_button = self.locator(REJECT_BUTTON, "Reject Button")
        self.reason_dropdown = self.locator(REASON_DROPDOWN, "Reason Dropdown")
        self.comments_textarea = self.locator(COMMENTS_TEXTAREA, "Comments Textarea")
        self.confirm_auth_button = self.locator(CONFIRM_AUTH_BUTTON, "Confirm Authorization Button")
        self.cancel_auth_button = self.locator(CANCEL_AUTH_BUTTON, "Cancel Authorization Button")
        self.confirmation_modal = self.locator(CONFIRMATION_MODAL, "Confirmation Modal")
        self.modal_ok_button = self.locator(MODAL_OK_BUTTON, "Modal OK Button")
