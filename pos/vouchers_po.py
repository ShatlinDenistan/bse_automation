from base.page_base import PageBase


class VouchersPO(PageBase):
    """Page Object for Vouchers page"""

    # region Navigation Elements

    @property
    def menu_btn(self):
        selector = '//i[@aria-hidden="true" and @class="content large icon"]'
        return self.locator(selector, "Menu button")

    @property
    def vouchers_menu_option(self):
        selector = "//body/div[@id='root']/div[1]/a[2]"
        return self.locator(selector, "Vouchers menu option")

    @property
    def close_icon(self):
        selector = '//i[@aria-hidden="true" and @class="close icon"]'
        return self.locator(selector, "Close icon")

    # endregion

    # region Search and Filter Elements

    @property
    def filter_by_field(self):
        selector = "//div[@name='searchCriteria']"
        return self.locator(selector, "Filter by field")

    @property
    def filter_voucher_code(self):
        selector = "//span[contains(text(), 'Voucher Code')]"
        return self.locator(selector, "Filter by voucher code option")

    @property
    def filter_by_customer_id(self):
        selector = "//span[contains(text(), 'Customer ID')]"
        return self.locator(selector, "Filter by customer ID option")

    @property
    def filter_used_by_customer_id(self):
        selector = "//span[contains(text(), 'Used By Customer ID')]"
        return self.locator(selector, "Filter by used by customer ID option")

    @property
    def search_criteria_option_order_id(self):
        selector = "//span[contains(text(), 'Order ID')]"
        return self.locator(selector, "Search criteria option order ID")

    @property
    def search_term_field(self):
        selector = "//*[@name='searchTerm']"
        return self.locator(selector, "Search term field")

    @property
    def date_filter(self):
        selector = "//input[@name='dateRange']"
        return self.locator(selector, "Date filter")

    @property
    def apply_search_filter(self):
        selector = "//button[contains(text(), 'Filter')]"
        return self.locator(selector, "Apply search filter button")

    @property
    def apply_filter_btn(self):
        selector = "//button[contains(text(), 'Filter')]"
        return self.locator(selector, "Apply filter button")

    @property
    def clear_filter(self):
        selector = "//button[contains(text(), 'Clear Filter')]"
        return self.locator(selector, "Clear filter button")

    # endregion

    # region Status Dropdowns

    @property
    def paid_status_dropdown(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/form/div/div/div[5]/div/div'
        return self.locator(selector, "Paid status dropdown")

    @property
    def paid_status_option(self):
        selector = "//span[text()='Paid']"
        return self.locator(selector, "Paid status option")

    @property
    def not_paid_status_option(self):
        selector = "//span[text()='Not Paid']"
        return self.locator(selector, "Not paid status option")

    @property
    def redeemed_status_dropdown(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/form/div/div/div[4]/div/div/div[1]'
        return self.locator(selector, "Redeemed status dropdown")

    @property
    def redeemed_status_available(self):
        selector = "//span[text()='Available']"
        return self.locator(selector, "Redeemed status available option")

    @property
    def redeemed_status_cancelled(self):
        selector = "//span[text()='Cancelled']"
        return self.locator(selector, "Redeemed status cancelled option")

    @property
    def redeemed_status_redeemed(self):
        selector = "//span[text()='Redeemed']"
        return self.locator(selector, "Redeemed status redeemed option")

    @property
    def voucher_category_dropdown(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/form/div/div/div[3]/div'
        return self.locator(selector, "Voucher category dropdown")

    @property
    def voucher_category_cv(self):
        selector = "//span[contains(text(), 'Corporate Voucher')]"
        return self.locator(selector, "Voucher category CV option")

    # endregion

    # region Action Buttons

    @property
    def paid_btn(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[4]/button'
        return self.locator(selector, "Paid button")

    @property
    def not_paid_btn(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[5]/button'
        return self.locator(selector, "Not paid button")

    @property
    def expire_btn(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[3]/button'
        return self.locator(selector, "Expire button")

    @property
    def active_btn(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tfoot/tr/th/div/div[2]/button'
        return self.locator(selector, "Active button")

    @property
    def active_voucher_btn(self):
        selector = "//html/body/div[2]/div/div[2]/div/div[2]"
        return self.locator(selector, "Active voucher button")

    @property
    def email_btn(self):
        selector = '//*[@class="mail icon"]'
        return self.locator(selector, "Email button")

    # endregion

    # region Table Elements

    @property
    def results_table(self):
        selector = '//*[@class="ui small celled compact table"]'
        return self.locator(selector, "Results table")

    @property
    def order_id_checkbox(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div'
        return self.locator(selector, "Order ID checkbox")

    @property
    def voucher_code(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[6]/a'
        return self.locator(selector, "Voucher code")

    @property
    def voucher_status(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr/td[10]/div'
        return self.locator(selector, "Voucher status")

    @property
    def paid_status(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr/td[8]/div'
        return self.locator(selector, "Paid status")

    # endregion

    # region Column Selectors

    @property
    def all_order_paid_columns(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 7)]"
        return self.locator(selector, "All order paid columns")

    @property
    def all_order_status_columns(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]"
        return self.locator(selector, "All order status columns")

    @property
    def voucher_category_list(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 4)]"
        return self.locator(selector, "Voucher category list")

    @property
    def redeemed_status_list(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]"
        return self.locator(selector, "Redeemed status list")

    @property
    def voucher_order_id(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
        return self.locator(selector, "Voucher order ID")

    @property
    def voucher_code_id(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 5)]"
        return self.locator(selector, "Voucher code ID")

    # endregion

    # region Customer Info Elements

    @property
    def open_customer_info(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[4]/a'
        return self.locator(selector, "Open customer info link")

    @property
    def open_used_by_customer_info(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/table/tbody/tr[1]/td[12]/a'
        return self.locator(selector, "Open used by customer info link")

    @property
    def customer_info_id(self):
        selector = '//*[@id="root"]/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/span'
        return self.locator(selector, "Customer info ID")

    # endregion

    # region Modals and Notifications

    @property
    def email_sent_modal(self):
        selector = "/html/body/div[2]/div"
        return self.locator(selector, "Email sent modal")

    @property
    def email_sent_modal_close_icon(self):
        selector = "//body/div[2]/div[1]/i[1]"
        return self.locator(selector, "Email sent modal close icon")

    @property
    def verification_message(self):
        selector = "//div[contains(text(),'Successfully processed 1 item(s)')]"
        return self.locator(selector, "Verification message")

    @property
    def verify_activated_voucher(self):
        selector = "//div[contains(text(),'Successfully processed 1 item(s)')]"
        return self.locator(selector, "Verify activated voucher message")

    # endregion
