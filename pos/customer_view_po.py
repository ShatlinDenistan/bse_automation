from base.page_base import PageBase


class CustomerViewPO(PageBase):
    """Page Object for Customer View page"""

    # region Accordion sections
    @property
    def addresses_accordion(self):
        selector = "//span[contains(text(),'Addresses')]"
        return self.locator(selector, "Addresses Accordion")

    @property
    def customer_credit_accordion(self):
        selector = "//span[contains(text(),'Customer Credit')]"
        return self.locator(selector, "Customer Credit Accordion")

    @property
    def email_logs_accordion(self):
        selector = "//span[contains(text(),'Email Logs')]"
        return self.locator(selector, "Email Logs Accordion")

    @property
    def fin_notes_dropdown(self):
        selector = "//span[contains(text(),'Fin Notes')]"
        return self.locator(selector, "Fin Notes Dropdown")

    @property
    def notes_dropdown(self):
        selector = "//span[contains(text(),'Notes')]"
        return self.locator(selector, "Notes Dropdown")

    @property
    def notes_accordion(self):
        selector = "//span[contains(text(),'Notes')]"
        return self.locator(selector, "Notes Accordion")

    @property
    def refund_history_accordion(self):
        selector = "//span[contains(text(),'Refund History')]"
        return self.locator(selector, "Refund History Accordion")

    @property
    def returns_history_accordion(self):
        selector = "//span[contains(text(),'Returns History')]"
        return self.locator(selector, "Returns History Accordion")

    @property
    def zendesk_ticket_accordion(self):
        selector = "//span[contains(text(),'Zendesk Tickets')]"
        return self.locator(selector, "Zendesk Ticket Accordion")

    @property
    def sales_history_accordion(self):
        selector = "//span[contains(text(),'Sales History')]"
        return self.locator(selector, "Sales History Accordion")

    @property
    def order_items_accordion(self):
        selector = "//span[contains(text(),'Order Items')]"
        return self.locator(selector, "Order Items Accordion")

    @property
    def documents_accordion(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[13]"
        return self.locator(selector, "Documents Accordion")

    # endregion

    # region Customer information elements

    @property
    def customer_fullname(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/text()[2]"
        return self.locator(selector, "Customer Fullname")

    @property
    def registered_date(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]"
        return self.locator(selector, "Registered Date")

    @property
    def modified_date(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]"
        return self.locator(selector, "Modified Date")

    @property
    def verified_cellphone_icon(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div"
        return self.locator(selector, "Verified Cellphone Icon")

    @property
    def cust_name(self):
        selector = "//input[@name='customerFirstName']"
        return self.locator(selector, "Customer Name")

    @property
    def cust_surname(self):
        selector = "//input[@name='customerSurname']"
        return self.locator(selector, "Customer Surname")

    @property
    def business_name(self):
        selector = "//input[@name='businessName']"
        return self.locator(selector, "Business Name")

    @property
    def vat_number(self):
        selector = "//input[@name='vatNumber']"
        return self.locator(selector, "VAT Number")

    @property
    def acc_status_ddl(self):
        selector = "//div[@name='accountStatus']"
        return self.locator(selector, "Account Status Dropdown")

    @property
    def acc_status(self):
        selector = "//span[text()='suspended']"
        return self.locator(selector, "Account Status")

    @property
    def staff_account_check(self):
        selector = "//label[text()='Staff Account']"
        return self.locator(selector, "Staff Account Check")

    @property
    def block_vou_check(self):
        selector = "//label[text()='Block Vouchers']"
        return self.locator(selector, "Block Vouchers Check")

    # endregion

    # region Action buttons
    @property
    def allocate_credit_btn(self):
        selector = "//button[contains(text(),'Allocate credit')]"
        return self.locator(selector, "Allocate Credit Button")

    @property
    def fin_notes_edit_btn(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/button"
        return self.locator(selector, "Fin Notes Edit Button")

    @property
    def notes_edit_btn(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/button"
        return self.locator(selector, "Notes Edit Button")

    @property
    def blacklist_btn(self):
        selector = "//button[contains(text(),'Blacklist Customer')]"
        return self.locator(selector, "Blacklist Button")

    @property
    def add_credit_btn(self):
        selector = "//button[@class='ui blue button']"
        return self.locator(selector, "Add Credit Button")

    @property
    def ok_btn(self):
        selector = "//button[@class='ui primary button']"
        return self.locator(selector, "OK Button")

    @property
    def edit_customer_btn(self):
        selector = "//button[contains(text(),'Customer Info')]"
        return self.locator(selector, "Edit Customer Button")

    @property
    def confirm_btn(self):
        selector = "//button[contains(text(),'Confirm')]"
        return self.locator(selector, "Confirm Button")

    @property
    def email_customer_btn(self):
        selector = "//button[contains(text(),'Email Customer')]"
        return self.locator(selector, "Email Customer Button")

    @property
    def send_email_btn(self):
        selector = "//button[contains(text(),'Send Email')]"
        return self.locator(selector, "Send Email Button")

    @property
    def note_btn(self):
        selector = "//button[contains(text(),'Note')]"
        return self.locator(selector, "Note Button")

    @property
    def add_note_btn(self):
        selector = "//button[contains(text(),'Add Note')]"
        return self.locator(selector, "Add Note Button")

    @property
    def upload_id(self):
        selector = "//button[contains(text(),'Upload')]"
        return self.locator(selector, "Upload ID")

    @property
    def confirm_upload(self):
        selector = "//*[@class='ui primary button']"
        return self.locator(selector, "Confirm Upload")

    @property
    def submit_blacklist_customer(self):
        selector = "//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]"
        return self.locator(selector, "Submit Blacklist Customer")

    # endregion

    # region Tables and data displays
    @property
    def credit_history_table(self):
        selector = "//*[@class='ui small celled compact table']"
        return self.locator(selector, "Credit History Table")

    @property
    def available_credit(self):
        selector = "//*[@class='ui green small circular horizontal label']"
        return self.locator(selector, "Available Credit")

    @property
    def refund_history_table(self):
        selector = "//*[@class='ui small celled structured compact table']"
        return self.locator(selector, "Refund History Table")

    @property
    def returns_table(self):
        selector = "//*[@class='ui small celled table']"
        return self.locator(selector, "Returns Table")

    @property
    def email_cards(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[12]/div/div[1]"
        return self.locator(selector, "Email Cards")

    @property
    def address_cards(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[6]/div"
        return self.locator(selector, "Address Cards")

    @property
    def audit_log_results(self):
        selector = "//*[@class='ui striped basic very compact table']"
        return self.locator(selector, "Audit Log Results")

    @property
    def sales_history_table(self):
        selector = "//*[@class='ui small celled striped compact table']"
        return self.locator(selector, "Sales History Table")

    @property
    def refund_type_column(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[9]"
        return self.locator(selector, "Refund Type Column")

    # endregion

    # region Icons and search elements

    @property
    def address_google_icon(self):
        selector = "//*[@class='map small icon']"
        return self.locator(selector, "Address Google Icon")

    @property
    def email_google_icon(self):
        selector = "//*[@class='google icon']"
        return self.locator(selector, "Email Google Icon")

    @property
    def name_google_icon(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/i"
        return self.locator(selector, "Name Google Icon")

    @property
    def audit_logs_icon(self):
        selector = "//*[@class='list alternate outline icon link']"
        return self.locator(selector, "Audit Logs Icon")

    # endregion

    # region Credit management elements

    @property
    def credit_amount_txt(self):
        selector = "//input[@name='amount']"
        return self.locator(selector, "Credit Amount Text")

    @property
    def credit_reason_ddl(self):
        selector = "//div[@name='reason']"
        return self.locator(selector, "Credit Reason Dropdown")

    @property
    def credit_reason(self):
        selector = "//*[contains(text(),'B2B bulk orders')]"
        return self.locator(selector, "Credit Reason")

    @property
    def admin_notes(self):
        selector = "//textarea[@name='adminNote']"
        return self.locator(selector, "Admin Notes")

    # endregion

    # region Fraud/Blacklisting elements

    @property
    def fraud_reason_ddl(self):
        selector = "//div[contains(text(),'Fraud Reason')]"
        return self.locator(selector, "Fraud Reason Dropdown")

    @property
    def fraud_reason_id(self):
        selector = "//span[contains(text(),'Returns abuse')]"
        return self.locator(selector, "Fraud Reason ID")

    @property
    def fin_notes(self):
        selector = "//input[@name='finNote']"
        return self.locator(selector, "Fin Notes")

    @property
    def fraud_reason_list(self):
        selector = "//div[@name='fraudReasonID']"
        return self.locator(selector, "Fraud Reason List")

    @property
    def fraud_reason(self):
        selector = "//span[text()='Coupon abuse']"
        return self.locator(selector, "Fraud Reason")

    # endregion

    # region Email elements

    @property
    def ddl_email_templates(self):
        selector = "//div[@name='emailTemplate']"
        return self.locator(selector, "Email Templates Dropdown")

    @property
    def email_modal_customer_id(self):
        selector = "//input[@name='customerId']"
        return self.locator(selector, "Email Modal Customer ID")

    @property
    def email_modal_order_id(self):
        selector = "//input[@name='orderId']"
        return self.locator(selector, "Email Modal Order ID")

    @property
    def email_modal_subject(self):
        selector = "//input[@name='emailSubject']"
        return self.locator(selector, "Email Modal Subject")

    @property
    def email_modal_body(self):
        selector = "//textarea[@name='emailBody']"
        return self.locator(selector, "Email Modal Body")

    @property
    def latest_email_sent(self):
        selector = "//*[@class='ui fluid card email-card']/div/div/span/a/span[1]"
        return self.locator(selector, "Latest Email Sent")

    # endregion

    # region Notes elements

    @property
    def add_notes_text_field(self):
        selector = "//textarea[@name='customerNote']"
        return self.locator(selector, "Add Notes Text Field")

    @property
    def note_added_message(self):
        selector = "//*[@class='noty_body']"
        return self.locator(selector, "Note Added Message")

    # endregion

    # region Order elements

    @property
    def order_id(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[1]/a"
        return self.locator(selector, "Order ID")

    @property
    def order_id_pg2(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]"
        return self.locator(selector, "Order ID Page 2")

    @property
    def product_title_pg1(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a"
        return self.locator(selector, "Product Title Page 1")

    @property
    def product_title_pg2(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[6]/div/table/tbody/tr[1]/td[6]"
        return self.locator(selector, "Product Title Page 2")

    @property
    def order_link(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div[8]/div/div/table/tbody/tr/td[5]/a"
        return self.locator(selector, "Order Link")

    # endregion

    # region Pagination and display controls

    @property
    def show_10_items_ddl(self):
        selector = "//div[contains(text(),'Show 10 Items')]"
        return self.locator(selector, "Show 10 Items Dropdown")

    @property
    def show_30_items_ddl(self):
        selector = "//div[contains(text(),'Show 30 Items')]"
        return self.locator(selector, "Show 30 Items Dropdown")

    @property
    def show_30_order_items(self):
        selector = "//span[contains(text(),'30')]"
        return self.locator(selector, "Show 30 Order Items")

    @property
    def show_10_order_items(self):
        selector = "//span[contains(text(),'10')]"
        return self.locator(selector, "Show 10 Order Items")

    @property
    def next_page(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[12]/div/div[2]/a[4]"
        return self.locator(selector, "Next Page")

    @property
    def prev_page(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[6]/div/div[2]/a[1]"
        return self.locator(selector, "Previous Page")

    # endregion

    # region Document elements

    @property
    def upload_field(self):
        selector = "//input[@type='file']"
        return self.locator(selector, "Upload Field")

    @property
    def remove_id(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[14]/div/div/div/div[2]/ol/a[2]"
        return self.locator(selector, "Remove ID")

    # endregion

    # region Notifications

    @property
    def popup(self):
        selector = "//*[@id='noty_layout__topRight']"
        return self.locator(selector, "Popup Message")
