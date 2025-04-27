from base.page_base import PageBase


class RiskQueuePO(PageBase):
    """Page Object for the Risk Queue page."""

    # region General Elements

    @property
    def all_order_id_columns(self):
        selector = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
        return self.locator(selector, "All order ID columns")

    @property
    def results_table(self):
        selector = '//*[@class="ui small celled compact table"]'
        return self.locator(selector, "Results table")

    # endregion

    # region Navigation Elements

    @property
    def menu_btn(self):
        selector = '//i[@aria-hidden="true" and @class="content large icon"]'
        return self.locator(selector, "Menu button")

    @property
    def risk_queue_menu_option(self):
        selector = '//body/div[@id="root"]/div[1]/a[4]'
        return self.locator(selector, "Risk Queue menu option")

    # endregion

    # region Pagination Elements

    @property
    def item_list_dropdown(self):
        selector = "//div[@class='content' and contains(text(), 'Show')]/following-sibling::div"
        return self.locator(selector, "Item list dropdown")

    @property
    def list_filter_10(self):
        selector = "//span[text()='10']"
        return self.locator(selector, "10 items filter")

    @property
    def next_page(self):
        selector = '//body/div[@id="root"]/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[2]/a[2]'
        return self.locator(selector, "Next page button")

    # endregion

    # region Risk Management Elements

    @property
    def order_checkbox(self):
        selector = '//body/div[@id="root"]/div[3]/div/div/table/tbody/tr[1]/td[1]/div'
        return self.locator(selector, "Order checkbox")

    @property
    def clear_risk_btn(self):
        selector = '//body/div[@id="root"]/div[3]/div/div/table/tfoot/tr/th/div/div[1]'
        return self.locator(selector, "Clear risk button")

    # endregion

    # region Filter Elements

    @property
    def clear_filter_btn(self):
        selector = "//button[contains(text(), 'Clear Filter')]"
        return self.locator(selector, "Clear filter button")

    @property
    def apply_filter_btn(self):
        selector = "//button[contains(text(), 'Filter')]"
        return self.locator(selector, "Apply filter button")

    @property
    def checkbox_daily_deals(self):
        selector = '//*[@id="root"]/div[3]/div/div/form/div/div/div[1]/div/div/div[1]/div'
        return self.locator(selector, "Daily deals checkbox")

    @property
    def virtual_items_checkbox(self):
        selector = '//*[@id="root"]/div[3]/div/div/form/div/div/div[1]/div/div/div[2]/div'
        return self.locator(selector, "Virtual items checkbox")

    @property
    def date_range_checkbox(self):
        selector = '//*[@id="root"]/div[3]/div/div/form/div/div/div[2]/div/div[3]/div'
        return self.locator(selector, "Date range checkbox")

    @property
    def date_range_filter(self):
        selector = '//*[@id="root"]/div[3]/div/div/form/div/div/div[2]/div/div[4]/div'
        return self.locator(selector, "Date range filter")

    # endregion

    # region Payment Method Filter

    @property
    def payment_method_dropdown(self):
        selector = "//div[@name='paymentMethod']"
        return self.locator(selector, "Payment method dropdown")

    @property
    def payment_method_credit(self):
        selector = "//span[text()='Credit']"
        return self.locator(selector, "Credit payment method")

    @property
    def payment_method_payfast(self):
        selector = "//span[text()='PayFast']"
        return self.locator(selector, "PayFast payment method")

    @property
    def payment_method_deposit(self):
        selector = "//span[text()='Deposit']"
        return self.locator(selector, "Deposit payment method")

    @property
    def all_payment_method_columns(self):
        selector = "//td[position() = (count(//th[text()='Payment Method']/preceding-sibling::th) + 7)]"
        return self.locator(selector, "All payment method columns")

    # endregion

    # region Shipping Method Filter

    @property
    def shipping_method_dropdown(self):
        selector = "//div[@name='shippingMethod']"
        return self.locator(selector, "Shipping method dropdown")

    @property
    def shipping_method_delivery(self):
        selector = "//span[text()='Courier']"
        return self.locator(selector, "Delivery shipping method")

    # endregion

    # region Order Total Filter

    @property
    def minimum_order_total_dropdown(self):
        selector = "//div[@name='minimumTotal']"
        return self.locator(selector, "Minimum order total dropdown")

    @property
    def minimum_order_total_r500(self):
        selector = "//div[@name='minimumTotal']//span[text()='500']"
        return self.locator(selector, "R500 minimum order total")

    @property
    def minimum_order_total_r0(self):
        selector = "//div[@name='minimumTotal']//span[text()='0']"
        return self.locator(selector, "R0 minimum order total")

    @property
    def maximum_order_total_dropdown(self):
        selector = "//div[@name='maximumTotal']"
        return self.locator(selector, "Maximum order total dropdown")

    @property
    def maximum_order_total_r5000(self):
        selector = "//div[@name='maximumTotal']//span[text()='5000']"
        return self.locator(selector, "R5000 maximum order total")

    # endregion

    # region Email Elements

    @property
    def btn_send_email_table(self):
        selector = "//table/tfoot/tr/th/div/div[3]/button"
        return self.locator(selector, "Send email table button")

    @property
    def ddl_email_templates(self):
        selector = "//body/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]"
        return self.locator(selector, "Email templates dropdown")

    @property
    def btn_send_email(self):
        selector = "//button[contains(text(),'Send Emails')]"
        return self.locator(selector, "Send email button")

    @property
    def email_sent_modal(self):
        selector = "/html/body/div[2]/div"
        return self.locator(selector, "Email sent modal")

    @property
    def email_sent_modal_close_icon(self):
        selector = "//i[@class='close icon']"
        return self.locator(selector, "Email sent modal close icon")

    # endregion

    # region Email Template Options

    @property
    def email_template_identification_cc(self):
        selector = "//span[contains(text(),'Identification required: Credit card')]"
        return self.locator(selector, "Email template: Identification required (Credit card)")

    @property
    def email_template_identification_and_card(self):
        selector = "//span[contains(text(),'Identification and card details required')]"
        return self.locator(selector, "Email template: Identification and card details required")

    @property
    def email_template_identification_payfast(self):
        selector = "//span[contains(text(),'Identification required: Payfast & Ozow')]"
        return self.locator(selector, "Email template: Identification required (Payfast & Ozow)")

    @property
    def email_template_identification_not_accepted(self):
        selector = "//span[contains(text(),'Identification not accepted')]"
        return self.locator(selector, "Email template: Identification not accepted")

    @property
    def email_template_identification_not_received_payfast(self):
        selector = "//span[contains(text(),'Identification not received: Payfast & Ozow')]"
        return self.locator(selector, "Email template: Identification not received (Payfast & Ozow)")

    @property
    def email_template_identification_not_received_cc(self):
        selector = "//span[contains(text(),'Identification not received: Credit card')]"
        return self.locator(selector, "Email template: Identification not received (Credit card)")

    @property
    def email_template_cc_refund_failed(self):
        selector = "//span[contains(text(),'Credit card refund failed')]"
        return self.locator(selector, "Email template: Credit card refund failed")

    @property
    def email_template_eft_refund_failed(self):
        selector = "//span[contains(text(),'EFT refund failed')]"
        return self.locator(selector, "Email template: EFT refund failed")

    @property
    def email_template_refund_delayed(self):
        selector = "//span[contains(text(),'Refund delayed')]"
        return self.locator(selector, "Email template: Refund delayed")

    @property
    def email_template_short_paid(self):
        selector = "//span[contains(text(),'Short paid')]"
        return self.locator(selector, "Email template: Short paid")

    @property
    def email_template_deposit_match(self):
        selector = "//span[contains(text(),'Deposit Match')]"
        return self.locator(selector, "Email template: Deposit Match")

    @property
    def email_template_duplicate_payment(self):
        selector = "//span[contains(text(),'Duplicate Payment')]"
        return self.locator(selector, "Email template: Duplicate Payment")

    @property
    def email_template_voucher_payment(self):
        selector = "//span[contains(text(),'Voucher Payment')]"
        return self.locator(selector, "Email template: Voucher Payment")

    @property
    def email_template_generic(self):
        selector = "//span[contains(text(),'Generic')]"
        return self.locator(selector, "Email template: Generic")

    # endregion

    # region Cancel Order Elements

    @property
    def risk_queue_cancel_order_button(self):
        selector = "//button[contains(text(), 'Cancel Order(s)')]"
        return self.locator(selector, "Cancel order button")

    @property
    def cancel_orders_modal_header(self):
        selector = "//div[contains(text(),'Please confirm')]"
        return self.locator(selector, "Cancel orders modal header")

    @property
    def cancellation_reason_dropdown(self):
        selector = "//div[@name='cancelReason']"
        return self.locator(selector, "Cancellation reason dropdown")

    @property
    def cancel_orders_modal_cancel_button(self):
        selector = "//button[contains(text(), 'Cancel Orders')]"
        return self.locator(selector, "Cancel orders button")

    @property
    def cancel_orders_modal(self):
        selector = "//div[contains(@class, 'ui large modal transition visible active')]"
        return self.locator(selector, "Cancel orders modal")

    @property
    def cancel_order_modal_success_message(self):
        selector = "//div[contains(@class, 'ui success message')]/div/div"
        return self.locator(selector, "Cancel order success message")

    @property
    def cancel_orders_modal_close_icon(self):
        selector = "//*[@class= 'close icon']"
        return self.locator(selector, "Cancel orders modal close icon")

    # endregion

    # region Cancellation Reason Options

    @property
    def cancellation_reason_customer_request(self):
        selector = "//span[contains(text(), 'Customer request')]"
        return self.locator(selector, "Cancellation reason: Customer request")

    @property
    def cancellation_reason_supplier_out_of_stock(self):
        selector = "//span[contains(text(), 'Supplier out of stock')]"
        return self.locator(selector, "Cancellation reason: Supplier out of stock")

    @property
    def cancellation_reason_fraud(self):
        selector = "//span[contains(text(), 'Fraud')]"
        return self.locator(selector, "Cancellation reason: Fraud")

    @property
    def cancellation_reason_damaged(self):
        selector = "//span[contains(text(), 'Damaged')]"
        return self.locator(selector, "Cancellation reason: Damaged")

    @property
    def cancellation_reason_incorrect_packaging(self):
        selector = "//span[contains(text(), 'Incorrect Packaging')]"
        return self.locator(selector, "Cancellation reason: Incorrect Packaging")

    # endregion

    # region Order Identification Elements

    @property
    def order_id_hyperlink(self):
        selector = '//*[@id="root"]/div[3]/div/div/table/tbody/tr[1]/td[2]/a'
        return self.locator(selector, "Order ID hyperlink")

    @property
    def fin_portal_global_search_field(self):
        selector = "//*[@name='searchText' and @type='text']"
        return self.locator(selector, "Global search field")

    @property
    def fin_portal_global_search_icon(self):
        selector = "//*[@class='search icon']"
        return self.locator(selector, "Global search icon")

    @property
    def canceled_by_order_page_badge(self):
        selector = "//div[contains(text(), 'Canceled by')]"
        return self.locator(selector, "Canceled by badge")

    @property
    def order_item_cancellation_reason(self):
        selector = "//div[span/p[contains(@style, 'color: rgb(65, 131, 196);')]]"
        return self.locator(selector, "Order item cancellation reason")

    # endregion
