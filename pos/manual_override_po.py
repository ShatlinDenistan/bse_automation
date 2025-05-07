from base.page_base import PageBase


class ManualOverridePO(PageBase):
    """Page Object class for Manual Override screen"""

    # region Header
    @property
    def manual_override_header(self):
        selector = "//h1[contains(text(),'Manual Override')]"
        return self.locator(selector, "Manual Override Header")

    # endregion

    # region Input Fields
    @property
    def order_number_input(self):
        selector = "//input[@id='orderNumber']"
        return self.locator(selector, "Order Number Input")

    @property
    def notes_textarea(self):
        selector = "//textarea[@id='notesField']"
        return self.locator(selector, "Notes Textarea")

    # endregion

    # region Dropdowns
    @property
    def order_type_dropdown(self):
        selector = "//select[@id='orderTypeSelect']"
        return self.locator(selector, "Order Type Dropdown")

    @property
    def order_status_dropdown(self):
        selector = "//select[@id='orderStatusSelect']"
        return self.locator(selector, "Order Status Dropdown")

    # endregion

    # region Buttons
    @property
    def search_button(self):
        selector = "//button[@id='searchBtn']"
        return self.locator(selector, "Search Button")

    @property
    def apply_button(self):
        selector = "//button[@id='applyBtn']"
        return self.locator(selector, "Apply Button")

    @property
    def cancel_button(self):
        selector = "//button[@id='cancelBtn']"
        return self.locator(selector, "Cancel Button")

    # endregion

    # region Confirmation Modal
    @property
    def confirm_modal(self):
        selector = "//div[@class='modal-content']"
        return self.locator(selector, "Confirmation Modal")

    @property
    def confirm_ok_button(self):
        selector = "//button[@id='confirmYesBtn']"
        return self.locator(selector, "Confirm OK Button")

    @property
    def confirm_cancel_button(self):
        selector = "//button[@id='confirmNoBtn']"
        return self.locator(selector, "Confirm Cancel Button")

    # endregion

    # region Order Table
    @property
    def order_table(self):
        selector = "//table[@id='orderTable']"
        return self.locator(selector, "Order Table")

    @property
    def order_rows(self):
        selector = "//table[@id='orderTable']/tbody/tr"
        return self.locator(selector, "Order Rows")

    # endregion
