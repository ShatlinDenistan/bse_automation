from base.page_base import PageBase


class ManualAuthPO(PageBase):
    """Page Object class for Manual Authorization screen"""

    # region Header

    @property
    def manual_auth_header(self):
        selector = "//h1[contains(text(),'Manual Auth')]"
        return self.locator(selector, "Manual Auth Header")

    # endregion

    # region Search Section

    @property
    def search_order_input(self):
        selector = "//input[@id='searchOrderInput']"
        return self.locator(selector, "Search Order Input")

    @property
    def search_button(self):
        selector = "//button[@id='searchOrderBtn']"
        return self.locator(selector, "Search Button")

    # endregion

    # region Order Table Section

    @property
    def order_table(self):
        selector = "//table[@id='orderTable']"
        return self.locator(selector, "Order Table")

    @property
    def order_rows(self):
        selector = "//table[@id='orderTable']/tbody/tr"
        return self.locator(selector, "Order Rows")

    @property
    def order_id_column(self):
        selector = "//table[@id='orderTable']/tbody/tr/td[1]"
        return self.locator(selector, "Order ID Column")

    @property
    def customer_name_column(self):
        selector = "//table[@id='orderTable']/tbody/tr/td[2]"
        return self.locator(selector, "Customer Name Column")

    @property
    def order_date_column(self):
        selector = "//table[@id='orderTable']/tbody/tr/td[3]"
        return self.locator(selector, "Order Date Column")

    @property
    def order_amount_column(self):
        selector = "//table[@id='orderTable']/tbody/tr/td[4]"
        return self.locator(selector, "Order Amount Column")

    # endregion

    # region Action Buttons

    @property
    def authorize_button(self):
        selector = "//button[@id='authorizeBtn']"
        return self.locator(selector, "Authorize Button")

    @property
    def reject_button(self):
        selector = "//button[@id='rejectBtn']"
        return self.locator(selector, "Reject Button")

    @property
    def confirm_auth_button(self):
        selector = "//button[@id='confirmAuthBtn']"
        return self.locator(selector, "Confirm Authorization Button")

    @property
    def cancel_auth_button(self):
        selector = "//button[@id='cancelAuthBtn']"
        return self.locator(selector, "Cancel Authorization Button")

    # endregion

    # region Dropdowns and Textareas

    @property
    def reason_dropdown(self):
        selector = "//select[@id='reasonSelect']"
        return self.locator(selector, "Reason Dropdown")

    @property
    def comments_textarea(self):
        selector = "//textarea[@id='commentsTextarea']"
        return self.locator(selector, "Comments Textarea")

    # endregion

    # region Confirmation Modal

    @property
    def confirmation_modal(self):
        selector = "//div[@class='modal-content']"
        return self.locator(selector, "Confirmation Modal")

    @property
    def modal_ok_button(self):
        selector = "//button[contains(@class,'btn-primary')]"
        return self.locator(selector, "Modal OK Button")

    # endregion
