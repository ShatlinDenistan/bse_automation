from base.page_base import PageBase

# Selector constants
MANUAL_OVERRIDE_HEADER = "//h1[contains(text(),'Manual Override')]"
ORDER_NUMBER_INPUT = "//input[@id='orderNumber']"
SEARCH_BUTTON = "//button[@id='searchBtn']"
ORDER_TYPE_DROPDOWN = "//select[@id='orderTypeSelect']"
ORDER_STATUS_DROPDOWN = "//select[@id='orderStatusSelect']"
APPLY_BUTTON = "//button[@id='applyBtn']"
CANCEL_BUTTON = "//button[@id='cancelBtn']"
CONFIRM_MODAL = "//div[@class='modal-content']"
CONFIRM_OK_BUTTON = "//button[@id='confirmYesBtn']"
CONFIRM_CANCEL_BUTTON = "//button[@id='confirmNoBtn']"
ORDER_TABLE = "//table[@id='orderTable']"
ORDER_ROWS = "//table[@id='orderTable']/tbody/tr"
NOTES_TEXTAREA = "//textarea[@id='notesField']"


class ManualOverridePO(PageBase):
    """Page Object class for Manual Override screen"""

    def __init__(self, page):
        super().__init__(page)

        # Initialize locators
        self.manual_override_header = self.locator(MANUAL_OVERRIDE_HEADER, "Manual Override Header")
        self.order_number_input = self.locator(ORDER_NUMBER_INPUT, "Order Number Input")
        self.search_button = self.locator(SEARCH_BUTTON, "Search Button")
        self.order_type_dropdown = self.locator(ORDER_TYPE_DROPDOWN, "Order Type Dropdown")
        self.order_status_dropdown = self.locator(ORDER_STATUS_DROPDOWN, "Order Status Dropdown")
        self.apply_button = self.locator(APPLY_BUTTON, "Apply Button")
        self.cancel_button = self.locator(CANCEL_BUTTON, "Cancel Button")
        self.confirm_modal = self.locator(CONFIRM_MODAL, "Confirmation Modal")
        self.confirm_ok_button = self.locator(CONFIRM_OK_BUTTON, "Confirm OK Button")
        self.confirm_cancel_button = self.locator(CONFIRM_CANCEL_BUTTON, "Confirm Cancel Button")
        self.order_table = self.locator(ORDER_TABLE, "Order Table")
        self.order_rows = self.locator(ORDER_ROWS, "Order Rows")
        self.notes_textarea = self.locator(NOTES_TEXTAREA, "Notes Textarea")
