from base.page_base import PageBase


class OrderListPO(PageBase):
    """Page Object for Order List page."""

    # region General UI Elements

    @property
    def order_list_table(self):
        selector = "//table[@class='ui small celled compact table']//tbody//tr"
        return self.locator(selector, "Order list table")

    @property
    def btn_menu(self):
        selector = "//i[@class='content large icon' and @aria-hidden='true']"
        return self.locator(selector, "Menu button")

    @property
    def order_list_menu_option(self):
        selector = "//*[contains(text(),'Order List')]"
        return self.locator(selector, "Order list menu option")

    # endregion

    # region Filter Buttons

    @property
    def order_list_apply_filter_button(self):
        selector = "//button[contains(text(), 'Apply Filter')]"
        return self.locator(selector, "Apply filter button")

    @property
    def clear_filter_button(self):
        selector = "//button[contains(text(), 'Clear Filter')]"
        return self.locator(selector, "Clear filter button")

    @property
    def clear_auth_status_icon(self):
        selector = "//i[@class='dropdown icon clear' and @aria-hidden='true']"
        return self.locator(selector, "Clear auth status icon")

    # endregion

    # region Date Filters

    @property
    def clear_date_range_today(self):
        selector = "//div[@class='ui checked checkbox']//label[text()='Today']"
        return self.locator(selector, "Clear date range today")

    @property
    def past_10_days(self):
        selector = "//label[text()='Past 10 Days']"
        return self.locator(selector, "Past 10 days")

    @property
    def daily_deals_checkbox(self):
        selector = "//label[text()='Daily Deals']"
        return self.locator(selector, "Daily deals checkbox")

    # endregion

    # region Status Filters

    @property
    def auth_status_dropdown(self):
        selector = "//div[@name='authStatus']"
        return self.locator(selector, "Auth status dropdown")

    @property
    def auth_status_new(self):
        selector = "//span[contains(text(), 'New')]"
        return self.locator(selector, "Auth status: New")

    @property
    def auth_status_auth(self):
        selector = "//span[text()='Auth']"
        return self.locator(selector, "Auth status: Auth")

    @property
    def all_auth_status_columns(self):
        selector = "//td[position() = (count(//th[text()='Auth Status']/preceding-sibling::th) + 1)]"
        return self.locator(selector, "All auth status columns")

    # endregion

    # region Payment Method Filters

    @property
    def payment_method_dropdown(self):
        selector = "//div[@name='paymentMethod']"
        return self.locator(selector, "Payment method dropdown")

    @property
    def payment_method_credit_card(self):
        selector = "//span[text()='Credit Card']"
        return self.locator(selector, "Payment method: Credit Card")

    @property
    def payment_method_credit(self):
        selector = "//span[text()='Credit']"
        return self.locator(selector, "Payment method: Credit")

    @property
    def payment_method_payfast(self):
        selector = "//span[text()='PayFast']"
        return self.locator(selector, "Payment method: PayFast")

    @property
    def payment_method_deposit(self):
        selector = "//span[text()='Deposit']"
        return self.locator(selector, "Payment method: Deposit")

    @property
    def all_payment_method_columns(self):
        selector = "//td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 1)]"
        return self.locator(selector, "All payment method columns")

    # endregion

    # region Shipping Method Filters

    @property
    def shipping_method_dropdown(self):
        selector = "//div[@name='shippingMethod']"
        return self.locator(selector, "Shipping method dropdown")

    @property
    def shipping_method_collect(self):
        selector = "//span[text()='Collect']"
        return self.locator(selector, "Shipping method: Collect")

    @property
    def shipping_method_courier(self):
        selector = "//span[text()='Courier']"
        return self.locator(selector, "Shipping method: Courier")

    # endregion

    # region Order Total Filters

    @property
    def minimum_order_total_dropdown(self):
        selector = "//div[@name='minimumTotal']"
        return self.locator(selector, "Minimum order total dropdown")

    @property
    def minimum_order_total_r500(self):
        selector = "//div[@name='minimumTotal']//span[text()='R 500']"
        return self.locator(selector, "Minimum order total: R500")

    @property
    def minimum_order_total_r0(self):
        selector = "//div[@name='minimumTotal']//span[text()='R 0']"
        return self.locator(selector, "Minimum order total: R0")

    @property
    def maximum_order_total_dropdown(self):
        selector = "//div[@name='maximumTotal']"
        return self.locator(selector, "Maximum order total dropdown")

    @property
    def maximum_order_total_r500(self):
        selector = "//div[@name='maximumTotal']//span[text()='R 500']"
        return self.locator(selector, "Maximum order total: R500")

    @property
    def all_order_total_columns(self):
        selector = "//td[position() = (count(//th[text()='Order Total']/preceding-sibling::th) + 1)]"
        return self.locator(selector, "All order total columns")

    # endregion

    # region New Order Elements

    @property
    def first_row_new_order_checkbox(self):
        selector = "//tr[td[9]/div[contains(text(), 'New Order')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
        return self.locator(selector, "First new order checkbox")

    @property
    def second_row_new_order_checkbox(self):
        selector = "//tr[td[9]/div[contains(text(), 'New Order')]][2]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
        return self.locator(selector, "Second new order checkbox")

    @property
    def third_row_new_order_checkbox(self):
        selector = "//tr[td[9]/div[contains(text(), 'New Order')]][3]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
        return self.locator(selector, "Third new order checkbox")

    @property
    def order_id_column(self):
        selector = "//tr[td[9]/div[contains(text(), 'New Order')]][1]//a[contains(@href, '/order/')]"
        return self.locator(selector, "First order ID")

    @property
    def order_id_column2(self):
        selector = "//tr[td[9]/div[contains(text(), 'New Order')]][2]//a[contains(@href, '/order/')]"
        return self.locator(selector, "Second order ID")

    @property
    def order_id_column3(self):
        selector = "//tr[td[9]/div[contains(text(), 'New Order')]][3]//a[contains(@href, '/order/')]"
        return self.locator(selector, "Third order ID")

    @property
    def all_order_id_columns(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
        return self.locator(selector, "All order ID columns")

    # endregion

    # region Cancelled Order Elements

    @property
    def first_row_canceled_checkbox(self):
        selector = "//tr[td[9]/div[contains(text(), 'Canceled')]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]"
        return self.locator(selector, "First canceled order checkbox")

    @property
    def order_id_column_canceled(self):
        selector = "//tr[td[9]/div[contains(text(), 'Canceled')]][1]//a[contains(@href, '/order/')]"
        return self.locator(selector, "Canceled order ID")

    @property
    def canceled_by_badge(self):
        selector = "//div[contains(text(), 'Canceled by')]"
        return self.locator(selector, "Canceled by badge")

    @property
    def order_item_cancellation_reason(self):
        selector = "//div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]"
        return self.locator(selector, "Order item cancellation reason")

    # endregion

    # region Authorize Order Elements
    @property
    def authorise_order_button(self):
        selector = "//button[contains(text(), 'Authorise Order(s)')]"
        return self.locator(selector, "Authorise order button")

    @property
    def authorise_orders_modal(self):
        selector = "//div[contains(@class, 'ui large modal transition visible active')]"
        return self.locator(selector, "Authorise orders modal")

    @property
    def authorise_orders_modal_close_icon(self):
        selector = "//*[@class= 'close icon']"
        return self.locator(selector, "Authorise modal close icon")

    @property
    def authed_by_badge(self):
        selector = "//div[contains(text(), 'Auth by')]"
        return self.locator(selector, "Authed by badge")

    # endregion

    # region Cancel Order Elements

    @property
    def cancel_order_button(self):
        selector = "//button[contains(text(), 'Cancel Order(s)')]"
        return self.locator(selector, "Cancel order button")

    @property
    def cancel_orders_modal(self):
        selector = "//div[contains(@class, 'ui large modal transition visible active')]"
        return self.locator(selector, "Cancel orders modal")

    @property
    def cancel_orders_modal_header(self):
        selector = "//div[contains(text(),'Please confirm')]"
        return self.locator(selector, "Cancel orders modal header")

    @property
    def cancel_orders_modal_close_icon(self):
        selector = "//*[@class= 'close icon']"
        return self.locator(selector, "Cancel modal close icon")

    @property
    def cancel_orders_button(self):
        selector = "//button[contains(text(), 'Cancel Orders')]"
        return self.locator(selector, "Cancel orders button")

    # endregion

    # region Cancellation Reasons

    @property
    def cancellation_reason_dropdown(self):
        selector = "//div[@name='cancelReason']"
        return self.locator(selector, "Cancellation reason dropdown")

    @property
    def reason_customer_request(self):
        selector = "//span[contains(text(), 'Customer request')]"
        return self.locator(selector, "Reason: Customer request")

    @property
    def reason_supplier_out_of_stock(self):
        selector = "//span[contains(text(), 'Supplier out of stock')]"
        return self.locator(selector, "Reason: Supplier out of stock")

    @property
    def reason_fraud(self):
        selector = "//span[contains(text(), 'Fraud')]"
        return self.locator(selector, "Reason: Fraud")

    @property
    def reason_damaged(self):
        selector = "//span[contains(text(), 'Damaged')]"
        return self.locator(selector, "Reason: Damaged")

    @property
    def reason_incorrect_packaging(self):
        selector = "//span[contains(text(), 'Incorrect Packaging')]"
        return self.locator(selector, "Reason: Incorrect Packaging")

    # endregion

    # region Search Elements

    @property
    def global_search_field(self):
        selector = "//*[@name='searchText' and @type='text']"
        return self.locator(selector, "Global search field")

    @property
    def global_search_icon(self):
        selector = "//*[@class='search icon']"
        return self.locator(selector, "Global search icon")

    # endregion
