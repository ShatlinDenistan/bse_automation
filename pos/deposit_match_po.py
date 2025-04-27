from base.page_base import PageBase


class DepositMatchPO(PageBase):

    # region Search section

    @property
    def batch_download(self):
        selector = "//tbody/tr[1]/td[10]/div[1]/button[1]/i[1]"
        return self.locator(selector, "Batch download button")

    @property
    def apply_filter(self):
        selector = "//button[contains(text(),'Apply Filter')]"
        return self.locator(selector, "Apply filter button")

    @property
    def clear_filter(self):
        selector = "//button[contains(text(),'Clear Filter')]"
        return self.locator(selector, "Clear filter button")

    @property
    def date_filter(self):
        selector = "//input[@name='dateRange']"
        return self.locator(selector, "Date filter input")

    @property
    def batch_date(self):
        selector = "//td[contains(text(),'12-May-2023')]"
        return self.locator(selector, "Batch date")

    @property
    def refresh_button(self):
        selector = "//body/div[@id='root']/div[3]/div[1]/div[1]/div[4]/button[1]"
        return self.locator(selector, "Refresh button")

    @property
    def deposit_match_search(self):
        selector = "//input[@name='searchTerm']"
        return self.locator(selector, "Deposit match search")

    @property
    def txt_criteria_search(self):
        selector = "//input[@name='searchTerm' and @type='text']"
        return self.locator(selector, "Criteria search input")

    # region Payment Method section

    @property
    def payment_method_lst(self):
        selector = "//tbody/tr[1]/td[5]"
        return self.locator(selector, "Payment method list")

    @property
    def payment_method_ddl(self):
        selector = "//div[contains(text(),'Select payment method')]"
        return self.locator(selector, "Payment method dropdown")

    @property
    def payfast_lst(self):
        selector = "//span[contains(text(),'PayFast')]"
        return self.locator(selector, "PayFast option")

    @property
    def payment_method_dropdown(self):
        selector = "//div[@name='paymentMethod' and @aria-disabled='false' and @aria-expanded='false']"
        return self.locator(selector, "Payment method dropdown")

    @property
    def payment_method_option(self):
        selector = "//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]"
        return self.locator(selector, "Payment method option")

    # region Navigation section

    @property
    def page_two_nav(self):
        selector = "//body/div[@id='root']/div[3]/div[1]/div[1]/table[1]/tfoot[1]/tr[1]/th[1]/div[1]/div[6]/div[2]/a[2]"
        return self.locator(selector, "Page two navigation")

    @property
    def item_list_ddl(self):
        selector = "//div[contains(text(),'Show 15 Items')]"
        return self.locator(selector, "Items list dropdown")

    @property
    def list_filter_30(self):
        selector = "//span[contains(text(),'30')]"
        return self.locator(selector, "30 items filter")

    @property
    def list_filter_10(self):
        selector = "//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[1]"
        return self.locator(selector, "10 items filter")

    @property
    def content_icon(self):
        selector = "//i[@aria-hidden='true' and @class='content large icon']"
        return self.locator(selector, "Content icon")

    @property
    def deposit_match_link(self):
        selector = "//body/div[@id='root']/div[1]/a[3]"
        return self.locator(selector, "Deposit match link")

    @property
    def all_batches_link(self):
        selector = "//a[contains(text(),'All Batches')]"
        return self.locator(selector, "All Batches link")

    @property
    def unclaimed_payments_tab(self):
        selector = "//a[contains(text(),'Unclaimed Payments ')]"
        return self.locator(selector, "Unclaimed payments tab")

    # region Search criteria section

    @property
    def criteria_dropdown(self):
        selector = "//div[contains(text(),'Criteria')]"
        return self.locator(selector, "Criteria dropdown")

    @property
    def order_id_dm(self):
        selector = "//span[contains(text(),'Order ID')]"
        return self.locator(selector, "Order ID option")

    @property
    def statement_amount_dm(self):
        selector = "//span[contains(text(),'Statement Amount')]"
        return self.locator(selector, "Statement amount option")

    @property
    def customer_id_dm(self):
        selector = "//span[contains(text(),'Customer ID')]"
        return self.locator(selector, "Customer ID option")

    @property
    def customer_name_dm(self):
        selector = "//span[contains(text(),'Customer Name')]"
        return self.locator(selector, "Customer Name option")

    @property
    def batch_id(self):
        selector = "//span[contains(text(),'Batch ID')]"
        return self.locator(selector, "Batch ID option")

    # region Error and Status section

    @property
    def error_message(self):
        selector = "//*[contains(text(),'Error')]"
        return self.locator(selector, "Error message")

    @property
    def match_status(self):
        selector = "//div[@name='matchStatus' and @role='listbox']"
        return self.locator(selector, "Match status dropdown")

    @property
    def close_filter_button(self):
        selector = "//i[@aria-hidden='true' and @class='dropdown icon clear']"
        return self.locator(selector, "Close filter button")

    @property
    def close_icon(self):
        selector = "//i[@aria-hidden='true' and @class='close icon']"
        return self.locator(selector, "Close icon")

    # region Order Details section

    @property
    def customer_name_lbl(self):
        selector = "//th[contains(text(),'Customer Name')]"
        return self.locator(selector, "Customer Name label")

    @property
    def order_no_text(self):
        selector = "//tbody/tr[1]/td[2]/a[1]"
        return self.locator(selector, "Order number text")

    @property
    def cust_name_text(self):
        selector = "//tbody/tr[1]/td[3]/a[1]"
        return self.locator(selector, "Customer name text")

    @property
    def statem_amount_text(self):
        selector = "//tbody/tr[1]/td[6]"
        return self.locator(selector, "Statement amount text")

    @property
    def customer_name_link(self):
        selector = "//tbody/tr[1]/td[3]/a[1]"
        return self.locator(selector, "Customer name link")

    @property
    def chk_order(self):
        selector = "//*[@id='root']/div[3]/div/div/table/tbody/tr[2]/td[1]/div"
        return self.locator(selector, "Order checkbox")

    @property
    def chk_new_order(self):
        selector = "//*[@id='root']/div[3]/div/div/table/tbody/tr/td[1]/div"
        return self.locator(selector, "New order checkbox")

    @property
    def batch_id_value(self):
        selector = "//tbody/tr[1]/td[2]/a[1]"
        return self.locator(selector, "Batch ID value")

    @property
    def order_number_checkbox(self):
        selector = "//tbody/tr[1]/td[1]"
        return self.locator(selector, "Order number checkbox")

    @property
    def order_number_text(self):
        selector = "//tbody/tr[1]/td[2]"
        return self.locator(selector, "Order number text")

    # region Match status options

    @property
    def order_not_found(self):
        selector = "//span[contains(text(),'Order Not Found')]"
        return self.locator(selector, "Order not found option")

    @property
    def amount_differ(self):
        selector = "//span[contains(text(),'Amount Differ')]"
        return self.locator(selector, "Amount differ option")

    @property
    def auto_match(self):
        selector = "//span[contains(text(),'Auto Match')]"
        return self.locator(selector, "Auto match option")

    # region Cancel/Order actions section

    @property
    def cancel_reason_dropdown(self):
        selector = "//div[@name='cancelReason']"
        return self.locator(selector, "Cancel reason dropdown")

    @property
    def cancel_reason(self):
        selector = "//span[contains(text(),'Supplier out of stock')]"
        return self.locator(selector, "Cancel reason option")

    @property
    def btn_cancel_order(self):
        selector = "//button[contains(text(),'Cancel Order')]"
        return self.locator(selector, "Cancel order button")

    @property
    def btn_confirm_cancel_order(self):
        selector = "//button[contains(text(),'Cancel Orders')]"
        return self.locator(selector, "Confirm cancel order button")

    @property
    def btn_authorise_order(self):
        selector = "//button[contains(text(),'Authorise Order')]"
        return self.locator(selector, "Authorise order button")

    @property
    def verify_authorise_order(self):
        selector = "//div[contains(text(),'Successfully processed 1 item(s)')]"
        return self.locator(selector, "Authorise order verification")

    @property
    def remove_order(self):
        selector = "//button[contains(text(),'Remove Order')]"
        return self.locator(selector, "Remove order button")

    @property
    def btn_unclaimed_payment(self):
        selector = "//button[contains(text(),'Unclaimed Payment')]"
        return self.locator(selector, "Unclaimed payment button")

    # region Upload and match section

    @property
    def btn_upload_csv(self):
        selector = "//button[contains(text(),'Upload CSV')]"
        return self.locator(selector, "Upload CSV button")

    @property
    def select_statement_type(self):
        selector = "//div[@name='statementType' and @role='listbox']"
        return self.locator(selector, "Select statement type dropdown")

    @property
    def btn_match(self):
        selector = "//tbody/tr[1]/td[10]/div[1]/button[1]"
        return self.locator(selector, "Match button")

    @property
    def txt_match_order_id(self):
        selector = "//input[@name='order_id' and  @type='number']"
        return self.locator(selector, "Match order ID input")

    @property
    def btn_match_submit(self):
        selector = "//button[@class='ui blue button' and @type='submit']"
        return self.locator(selector, "Match submit button")

    @property
    def batches_heading(self):
        selector = "//h1[contains(text(),'Batches')]"
        return self.locator(selector, "Batches heading")

    @property
    def generic_option(self):
        selector = "//span[contains(text(),'Generic')]"
        return self.locator(selector, "Generic option")

    @property
    def file_input(self):
        selector = "//input[@type='file']"
        return self.locator(selector, "File input")

    @property
    def upload_button(self):
        selector = "//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]"
        return self.locator(selector, "Upload button")

    @property
    def batch_id_active_section(self):
        selector = "//a[@class='active section']"
        return self.locator(selector, "Batch ID active section")

    @property
    def batch_id_header(self):
        selector = "//th[contains(text(),'Batch Id')]"
        return self.locator(selector, "Batch ID header")

    @property
    def send_email_button(self):
        selector = "//button[contains(text(),'Send Email')]"
        return self.locator(selector, "Send Email button")
