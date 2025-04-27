from base.page_base import PageBase


class OrderViewPO(PageBase):
    """Page Object for Order View page."""

    # region Order Information Elements

    @property
    def order_id(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]"
        return self.locator(selector, "Order ID")

    @property
    def order_date(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[3]/div[1]"
        return self.locator(selector, "Order date")

    @property
    def order_status(self):
        selector = "//div[@class='ten wide column label-container']/span/div[1]"
        return self.locator(selector, "Order status")

    @property
    def auth_status(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[1]"
        return self.locator(selector, "Auth status")

    @property
    def auth_date(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[3]"
        return self.locator(selector, "Auth date")

    @property
    def flagged_as_risk(self):
        selector = "//div[@class='ui red basic label']"
        return self.locator(selector, "Flagged as risk label")

    # endregion

    # region Customer Information Elements

    @property
    def customer_id(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]"
        return self.locator(selector, "Customer ID")

    @property
    def cust_acc_number(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]"
        return self.locator(selector, "Customer account number")

    @property
    def cust_info_popup(self):
        selector = "//*[@class='ui bottom center basic popup transition visible']"
        return self.locator(selector, "Customer info popup")

    @property
    def cust_status(self):
        selector = "//*[@class='ui green mini basic label']"
        return self.locator(selector, "Customer status")

    @property
    def cust_name_popup(self):
        selector = "//table[@class='ui small unstackable very basic very compact table']//td[text()='Slindile Mncwango']"
        return self.locator(selector, "Customer name in popup")

    @property
    def cust_date_registered(self):
        selector = "//table[@class='ui small unstackable very basic very compact table']//td[text()='16-Oct-2018 @ 10:41']"
        return self.locator(selector, "Customer date registered")

    @property
    def cust_blacklist_status(self):
        selector = "//div[@class='ui green basic label'][contains(text(),'Not Blacklisted')]"
        return self.locator(selector, "Customer blacklist status")

    @property
    def cust_name(self):
        selector = "//input[@name='name']"
        return self.locator(selector, "Customer name")

    @property
    def cust_surname(self):
        selector = "//input[@name='surname']"
        return self.locator(selector, "Customer surname")

    @property
    def business_name(self):
        selector = "//input[@name='businessName']"
        return self.locator(selector, "Business name")

    @property
    def vat_number(self):
        selector = "//input[@name='vatNumber']"
        return self.locator(selector, "VAT number")

    @property
    def acc_status_ddl(self):
        selector = "//div[@name='accountStatus']"
        return self.locator(selector, "Account status dropdown")

    @property
    def acc_status(self):
        selector = "//span[text()='Active']"
        return self.locator(selector, "Account status")

    @property
    def staff_account_check(self):
        selector = "//label[text()=' Staff']"
        return self.locator(selector, "Staff account check")

    @property
    def block_vou_check(self):
        selector = "//label[text()=' Voucher Block']"
        return self.locator(selector, "Block voucher check")

    # endregion

    # region Menu and Action Buttons

    @property
    def order_ellipsis_menu(self):
        selector = "//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']"
        return self.locator(selector, "Order ellipsis menu")

    @property
    def audit_log_menu_option(self):
        selector = "//*[contains(text(),'Audit log')]"
        return self.locator(selector, "Audit log menu option")

    @property
    def waybill_menu_option(self):
        selector = "//*[contains(text(),'Waybill log')]"
        return self.locator(selector, "Waybill menu option")

    @property
    def order_events_menu(self):
        selector = "//*[contains(text(),'Order events')]"
        return self.locator(selector, "Order events menu")

    @property
    def authorise_now_btn(self):
        selector = "//button[contains(text(),'Authorise Now')]"
        return self.locator(selector, "Authorise Now button")

    @property
    def cancel_all_item_btn(self):
        selector = "//button[contains(text(),'Cancel All Items')]"
        return self.locator(selector, "Cancel All Items button")

    @property
    def cancel_selected_item_btn(self):
        selector = "//button[contains(text(),'Cancel Selected Items')]"
        return self.locator(selector, "Cancel Selected Items button")

    @property
    def email_customer(self):
        selector = "//button[contains(text(),'Email Customer')]"
        return self.locator(selector, "Email Customer button")

    @property
    def mark_as_risky_btn(self):
        selector = "//button[contains(text(),'Mark as risky')]"
        return self.locator(selector, "Mark as risky button")

    @property
    def blacklist_cust_btn(self):
        selector = "//button[contains(text(),'Blacklist Customer')]"
        return self.locator(selector, "Blacklist Customer button")

    @property
    def whitelist_cust_btn(self):
        selector = "//button[contains(text(),'Whitelist Customer')]"
        return self.locator(selector, "Whitelist Customer button")

    @property
    def track_btn(self):
        selector = "//button[@class='ui blue small button']"
        return self.locator(selector, "Track button")

    @property
    def first_consigment_track_btn(self):
        selector = "//div[@class='ui segment instruction-container'][1]/div[1]/button"
        return self.locator(selector, "First consignment track button")

    @property
    def send_email_btn(self):
        selector = "//button[@class='ui right floated primary button']"
        return self.locator(selector, "Send email button")

    @property
    def edit_customer_btn(self):
        selector = "//button[@class='ui mini primary right floated button']//i[@class='edit icon']"
        return self.locator(selector, "Edit customer button")

    # endregion

    # region Accordion Sections

    @property
    def order_fullfilment_accordion(self):
        selector = "//*[contains(text(),'Order Fulfillment')]"
        return self.locator(selector, "Order Fulfillment accordion")

    @property
    def order_financials_accordion(self):
        selector = "//div[@class='ten wide column']//*[text()='Order Financials']"
        return self.locator(selector, "Order Financials accordion")

    @property
    def payment_ledger_accordion(self):
        selector = "//div[@class='ten wide column']//*[text()='Payment Ledger']"
        return self.locator(selector, "Payment Ledger accordion")

    @property
    def email_logs_accordion(self):
        selector = "//div[@class='ten wide column']//*[text()='Email Logs']"
        return self.locator(selector, "Email Logs accordion")

    @property
    def refund_history_accordion(self):
        selector = "//*[text()='Refund History']"
        return self.locator(selector, "Refund History accordion")

    @property
    def coupon_history_accordion(self):
        selector = "//*[text()='Coupon History']"
        return self.locator(selector, "Coupon History accordion")

    @property
    def order_notes_accordion(self):
        selector = "//div[@class='ten wide column']//span[text()='Notes']"
        return self.locator(selector, "Order Notes accordion")

    @property
    def customer_notes_accordion(self):
        selector = "//div[@class='six wide column']//span[text()='Notes']"
        return self.locator(selector, "Customer Notes accordion")

    @property
    def fin_notes_accordion(self):
        selector = "//div[@class='six wide column']//span[text()='Notes']"
        return self.locator(selector, "Financial Notes accordion")

    @property
    def order_items_accordion(self):
        selector = "//div[@class='accordion ui']"
        return self.locator(selector, "Order items accordion")

    # endregion

    # region Notes Elements

    @property
    def add_notes_btn(self):
        selector = "//button[@class='ui mini primary right floated button']"
        return self.locator(selector, "Add Notes button")

    @property
    def confirm_add_btn(self):
        selector = "//button[@class='ui blue right floated button']"
        return self.locator(selector, "Confirm Add button")

    @property
    def note_dd(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/span"
        return self.locator(selector, "Notes dropdown")

    @property
    def notes_txt_field(self):
        selector = "//textarea[@name='customerNote']"
        return self.locator(selector, "Notes text field")

    @property
    def note_confirm_message(self):
        selector = "//*[@id='noty_layout__topRight']"
        return self.locator(selector, "Note confirmation message")

    @property
    def note_added_message(self):
        selector = "//*[@id='noty_layout__topRight']"
        return self.locator(selector, "Note added message")

    @property
    def fin_note(self):
        selector = "//input[@name='finNote']"
        return self.locator(selector, "Financial Note field")

    @property
    def order_notes_btn(self):
        selector = "//button[@class='ui mini icon primary right floated button']"
        return self.locator(selector, "Order Notes button")

    @property
    def order_notes_text_field(self):
        selector = "//textarea[@name='orderNote']"
        return self.locator(selector, "Order Notes text field")

    @property
    def add_notes_confirm_btn(self):
        selector = "//button[@class='ui primary button']"
        return self.locator(selector, "Add Notes confirm button")

    @property
    def add_customer_notes_btn(self):
        selector = "//button[@class='ui mini primary right floated button']"
        return self.locator(selector, "Add Customer Notes button")

    @property
    def customer_notes_text_field(self):
        selector = "//textarea[@name='customerNote']"
        return self.locator(selector, "Customer Notes text field")

    @property
    def add_customer_notes_confirm_btn(self):
        selector = "//button[@class='ui blue right floated button']"
        return self.locator(selector, "Add Customer Notes confirm button")

    @property
    def add_fin_notes_btn(self):
        selector = "//button[@class='ui mini primary right floated button']"
        return self.locator(selector, "Add Financial Notes button")

    @property
    def fin_notes_text_field(self):
        selector = "//textarea[@name='customerNote']"
        return self.locator(selector, "Financial Notes text field")

    @property
    def add_fin_notes_confirm_btn(self):
        selector = "//button[@class='ui blue right floated button']"
        return self.locator(selector, "Add Financial Notes confirm button")

    # endregion

    # region Blacklist/Whitelist Elements

    @property
    def fraud_reason_list(self):
        selector = "//div[contains(text(),'Fraud Reason')]"
        return self.locator(selector, "Fraud reason list")

    @property
    def fraud_reason_selection(self):
        selector = "//span[contains(text(),'Returns abuse')]"
        return self.locator(selector, "Fraud reason selection")

    @property
    def confirm_blacklist(self):
        selector = "//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]"
        return self.locator(selector, "Confirm blacklist button")

    @property
    def confirm_whitelist(self):
        selector = "//button[@class='ui blue right floated button'][contains(text(),'Confirm')]"
        return self.locator(selector, "Confirm whitelist button")

    # endregion

    # region Cancellation Elements

    @property
    def cancellation_reason(self):
        selector = "//*[@name='reasonTypeID']"
        return self.locator(selector, "Cancellation reason dropdown")

    @property
    def customer_request_cancel_reason(self):
        selector = "//span[contains(text(),'Customer request')]"
        return self.locator(selector, "Customer request cancellation reason")

    @property
    def confirm_cancelling_btn(self):
        selector = "//button[contains(text(),'Confirm Cancelling')]"
        return self.locator(selector, "Confirm cancelling button")

    @property
    def close_cancel_modal(self):
        selector = "//*[@class='close icon']"
        return self.locator(selector, "Close cancel modal")

    @property
    def cancellation_results(self):
        selector = "//*[@class='ui celled striped table']/tbody/tr/td[2]"
        return self.locator(selector, "Cancellation results")

    # endregion

    # region Email Elements

    @property
    def email_template_selection(self):
        selector = "//span[contains(text(),'Identification not accepted')]"
        return self.locator(selector, "Email template selection")

    @property
    def email_template_ddl(self):
        selector = "//*[@name='emailTemplate']"
        return self.locator(selector, "Email template dropdown")

    @property
    def view_email_btn(self):
        selector = "//*[@class='blue mail outline icon']"
        return self.locator(selector, "View email button")

    @property
    def email_view(self):
        selector = "//*[@class='ui scrolling modal transition visible active']"
        return self.locator(selector, "Email view")

    # endregion

    # region Risk Elements

    @property
    def mark_as_risky_reason(self):
        selector = "//input[@name='reason']"
        return self.locator(selector, "Mark as risky reason field")

    @property
    def add_reason_btn(self):
        selector = "//button[contains(text(),'Add Reason')]"
        return self.locator(selector, "Add reason button")

    # endregion

    # region Audit/Log Elements

    @property
    def audit_log_action_type(self):
        selector = "//*[@class='ui striped basic very compact table']/tbody/tr/td[3]"
        return self.locator(selector, "Audit log action type")

    @property
    def authorise_now_modal_message(self):
        selector = "//div[@class='ui success message']/div/div"
        return self.locator(selector, "Authorise now modal message")

    @property
    def authorise_now_modal_close_icon(self):
        selector = "//i[@class='close icon']"
        return self.locator(selector, "Authorise now modal close icon")

    @property
    def order_tracking_heading(self):
        selector = "//h5[@class='ui header']"
        return self.locator(selector, "Order tracking heading")

    @property
    def order_tracking_user_info(self):
        selector = "//div[@class='ui info message']/div[1]"
        return self.locator(selector, "Order tracking user info")

    @property
    def event_log_results(self):
        selector = "//*[@class='ui red celled padded table']"
        return self.locator(selector, "Event log results")

    @property
    def logs_table(self):
        selector = "//*[@class='ui striped basic very compact table']"
        return self.locator(selector, "Logs table")

    # endregion

    # region Payment Elements

    @property
    def first_payment_method_badge(self):
        selector = "//div[@class='ui blue basic label']"
        return self.locator(selector, "First payment method badge")

    @property
    def second_payment_method_badge(self):
        selector = "//div[@class='ui orange basic label']"
        return self.locator(selector, "Second payment method badge")

    @property
    def payment_ledger_first_provider(self):
        selector = "//*[@class='ui celled fixed structured table']/tbody/tr/td[@rowspan='2']"
        return self.locator(selector, "Payment ledger first provider")

    @property
    def payment_ledger_second_provider(self):
        selector = "//*[@class='ui celled fixed structured table']/tbody/tr/td[@rowspan='3']"
        return self.locator(selector, "Payment ledger second provider")

    @property
    def payment_ledger_paid_total_amount(self):
        selector = "//tfoot/tr[@class='center aligned']/th[2]"
        return self.locator(selector, "Payment ledger paid total amount")

    @property
    def payment_ledger_payment_provider(self):
        selector = "//*[@class='ui celled fixed structured table']/tbody/tr[1]/td[1]"
        return self.locator(selector, "Payment ledger payment provider")

    @property
    def refunded_amount(self):
        selector = "//td[contains(text(),'RFN-pg3x-45rz')]/following-sibling::td[1]/div[2]/div"
        return self.locator(selector, "Refunded amount")

    @property
    def refunded_payment_method(self):
        selector = "//td[contains(text(),'RFN-pg3x-45rz')]/following::td[3]"
        return self.locator(selector, "Refunded payment method")

    # endregion

    # region Order Item Elements

    @property
    def select_item_checkbox(self):
        selector = "//div[@class='ui fitted checkbox']"
        return self.locator(selector, "Select item checkbox")

    @property
    def edit_order_item_menu(self):
        selector = "//*[@class='blue write square large icon']"
        return self.locator(selector, "Edit order item menu")

    @property
    def update_status_menu_option(self):
        selector = "//*[contains(text(),'Update to shipped')]"
        return self.locator(selector, "Update status menu option")

    @property
    def update_to_shipped_button(self):
        selector = "//button[@class='ui blue button'][contains(text(),'Update to shipped')]"
        return self.locator(selector, "Update to shipped button")

    @property
    def order_item(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[3]/a"
        return self.locator(selector, "Order item")

    @property
    def order_item_status(self):
        selector = "//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[1]"
        return self.locator(selector, "Order item status")

    @property
    def order_item_canceled_by(self):
        selector = "//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[3]/div/p[3]"
        return self.locator(selector, "Order item canceled by")

    @property
    def order_items_show_items(self):
        selector = "//div[@class='ui compact item dropdown']"
        return self.locator(selector, "Order items show items dropdown")

    @property
    def order_items_pagination_page_two(self):
        selector = "//*[@aria-label='Pagination Navigation']/a[3]"
        return self.locator(selector, "Order items pagination page two")

    # endregion

    # region Status Tags

    @property
    def shipped_tag(self):
        selector = "//div[@class='ui green tiny label'][contains(text(),'Shipped')]"
        return self.locator(selector, "Shipped tag")

    @property
    def return_canceled_tag(self):
        selector = "//div[@class='ui red tiny label'][contains(text(),'Return Canceled')]"
        return self.locator(selector, "Return Canceled tag")

    @property
    def delivered_tag(self):
        selector = "//div[@class='ui green tiny label'][contains(text(),'Delivered')]"
        return self.locator(selector, "Delivered tag")

    @property
    def cancelled_tag(self):
        selector = "//div[@class='ui red tiny label'][contains(text(),'Canceled')]"
        return self.locator(selector, "Cancelled tag")

    @property
    def cancelled_items(self):
        selector = "(//*[text()='Cancelled Item(s)'])"
        return self.locator(selector, "Cancelled items")

    # endregion

    # region Financial Elements

    @property
    def total_order_items_amount(self):
        selector = "//tbody/tr/td[text()='Total Order Items']/following-sibling::*[1]/div"
        return self.locator(selector, "Total order items amount")

    @property
    def shipping_amount(self):
        selector = "//tbody/tr/td[text()='Shipping']/following-sibling::*[1]/div"
        return self.locator(selector, "Shipping amount")

    @property
    def sub_total_amount(self):
        selector = "//tbody/tr/td[text()='Sub-Total']/following-sibling::*[1]/div"
        return self.locator(selector, "Sub-total amount")

    @property
    def discount_amount(self):
        selector = "//tbody/tr/td[text()='Discount']/following-sibling::*[1]/div"
        return self.locator(selector, "Discount amount")

    @property
    def order_total_amount(self):
        selector = "//tbody/tr/td[text()='Order Total']/following-sibling::*[1]/div"
        return self.locator(selector, "Order total amount")

    @property
    def total_paid_amount(self):
        selector = "//tbody/tr/td[text()='Total Paid']/following-sibling::*[1]/div"
        return self.locator(selector, "Total paid amount")

    # endregion

    # region Bookmark Elements

    @property
    def bookmark_icon(self):
        selector = "//*[@class='grey bookmark outline link icon']"
        return self.locator(selector, "Bookmark icon")

    @property
    def bookmark_notes(self):
        selector = "//textarea[@placeholder='Notes...']"
        return self.locator(selector, "Bookmark notes")

    @property
    def bookmark_counter(self):
        selector = "//*[@class='ui teal mini circular floating label label-on-corner']"
        return self.locator(selector, "Bookmark counter")

    @property
    def bookmarks_page(self):
        selector = "//*[@class='grey bookmark outline large icon']"
        return self.locator(selector, "Bookmarks page")

    @property
    def remove_bookmarks_checkbox(self):
        selector = "//*[@class='ui fitted checkbox']"
        return self.locator(selector, "Remove bookmarks checkbox")

    @property
    def remove_btn(self):
        selector = "//button[@class='ui mini icon negative right floated button']"
        return self.locator(selector, "Remove button")

    # endregion

    # region Address Elements

    @property
    def address_google_icon(self):
        selector = "//*[@class='google icon']"
        return self.locator(selector, "Address Google icon")

    @property
    def street_address(self):
        selector = "//div[@class='column'][contains(text(),'6 Birkenhead Road')]"
        return self.locator(selector, "Street address")

    @property
    def suburb_address(self):
        selector = "//div[@class='column'][contains(text(),'Umbilo')]"
        return self.locator(selector, "Suburb address")

    @property
    def city_address(self):
        selector = "//div[@class='column'][contains(text(),'Berea')]"
        return self.locator(selector, "City address")

    @property
    def province_address(self):
        selector = "//div[@class='column'][contains(text(),'KwaZulu-Natal')]"
        return self.locator(selector, "Province address")

    @property
    def code_address(self):
        selector = "//div[@class='column'][contains(text(),'4075')]"
        return self.locator(selector, "Code address")

    @property
    def copy_address_btn(self):
        selector = "//button[@class='ui blue mini right floated button']"
        return self.locator(selector, "Copy address button")

    @property
    def address_copied_btn(self):
        selector = "//button[@class='ui green mini right floated button']"
        return self.locator(selector, "Address copied button")

    @property
    def residential_txt(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div[1]"
        return self.locator(selector, "Residential text")

    @property
    def search_google_icon(self):
        selector = "//div[@class='header customer-card-header']//i[@class='google icon']"
        return self.locator(selector, "Search Google icon")

    # endregion

    # region Shipping/Delivery Elements

    @property
    def shipping_method(self):
        selector = "(//table[@class='ui small unstackable basic very compact table']//td[text()='Courier'])[1]"
        return self.locator(selector, "Shipping method")

    @property
    def shipping_plan(self):
        selector = "(//table[@class='ui small unstackable basic very compact table']//td[text()='Standard'])[1]"
        return self.locator(selector, "Shipping plan")

    @property
    def shipping_courier(self):
        selector = "(//table[@class='ui small unstackable basic very compact table']//td[text()='MDX133806010 - Takealot Delivery Team'])[1]"
        return self.locator(selector, "Shipping courier")

    @property
    def shipping_promised_date(self):
        selector = "(//table[@class='ui small unstackable basic very compact table']//td[text()='28 Aug 2024'])[1]"
        return self.locator(selector, "Shipping promised date")

    @property
    def shipping_delivered_date(self):
        selector = "(//table[@class='ui small unstackable basic very compact table']//td[text()='30 Aug 2024'])[1]"
        return self.locator(selector, "Shipping delivered date")

    @property
    def instruction_dropped_datetime(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div"
        return self.locator(selector, "Instruction dropped datetime")

    @property
    def shipped_from_warehouse_datetime(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div"
        return self.locator(selector, "Shipped from warehouse datetime")

    @property
    def delivered_to_customer_datetime(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div"
        return self.locator(selector, "Delivered to customer datetime")

    @property
    def instruction_dropped_date1(self):
        selector = "(//div[text()='27 May 2024 @ 17:46'])[1]"
        return self.locator(selector, "Instruction dropped date 1")

    @property
    def instruction_dropped_date2(self):
        selector = "(//div[text()='27 May 2024 @ 0:34'])"
        return self.locator(selector, "Instruction dropped date 2")

    @property
    def shipped_from_warehouse_date1(self):
        selector = "(//div[text()='28 May 2024 @ 1:31'])"
        return self.locator(selector, "Shipped from warehouse date 1")

    @property
    def shipped_from_warehouse_date2(self):
        selector = "(//div[text()='27 May 2024 @ 17:46'])[2]"
        return self.locator(selector, "Shipped from warehouse date 2")

    @property
    def delivered_date1(self):
        selector = "(//div[text()='30 May 2024 @ 11:40'])"
        return self.locator(selector, "Delivered date 1")

    @property
    def delivered_date2(self):
        selector = "(//div[text()='29 May 2024 @ 10:58'])"
        return self.locator(selector, "Delivered date 2")

    @property
    def estimated_collection_date(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/h5"
        return self.locator(selector, "Estimated collection date")

    @property
    def collection_estimate(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/div/span"
        return self.locator(selector, "Collection estimate")

    @property
    def collection_estimate_date(self):
        selector = "//div[@class='ui segment instruction-container']//h5"
        return self.locator(selector, "Collection estimate date")

    @property
    def collection_not_yet_ready_message(self):
        selector = "//div[@class='ui segment instruction-container']//div/span"
        return self.locator(selector, "Collection not yet ready message")

    @property
    def delivery_estimate_date(self):
        selector = "//div[@class='ui segment instruction-container']//h5"
        return self.locator(selector, "Delivery estimate date")

    @property
    def delivery_not_yet_ready_message(self):
        selector = "//div[@class='ui segment instruction-container']//div/span"
        return self.locator(selector, "Delivery not yet ready message")

    # endregion

    # region Waybill Elements

    @property
    def waybill_no(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]"
        return self.locator(selector, "Waybill number")

    @property
    def courier(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]"
        return self.locator(selector, "Courier")

    @property
    def parcel_block(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/a/div"
        return self.locator(selector, "Parcel block")

    @property
    def parcel(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/span/a"
        return self.locator(selector, "Parcel")

    @property
    def waybill_estimate_collection_date(self):
        selector = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]"
        return self.locator(selector, "Waybill estimate collection date")

    @property
    def waybill_number1(self):
        selector = "(//*[text()='MDX127668689'])"
        return self.locator(selector, "Waybill number 1")

    @property
    def waybill_number2(self):
        selector = "(//*[text()='MDX127583371'])"
        return self.locator(selector, "Waybill number 2")

    @property
    def waybill_number_link(self):
        selector = "(//*[text()='MDX133806010'])"
        return self.locator(selector, "Waybill number link")

    @property
    def tracking_waybill_number(self):
        selector = "//strong[text()='Waybill No: ']/following-sibling::*[1]"
        return self.locator(selector, "Tracking waybill number")

    # endregion

    # region Tracking Elements

    @property
    def order_tracking_heading1(self):
        selector = "(//*[text()='Delivered Thu, 30 May 2024'])"
        return self.locator(selector, "Order tracking heading 1")

    @property
    def order_tracking_heading2(self):
        selector = "(//*[text()='Delivered Wed, 29 May 2024'])"
        return self.locator(selector, "Order tracking heading 2")

    @property
    def signed_by(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/p"
        return self.locator(selector, "Signed by")

    @property
    def signed_by1(self):
        selector = "(//*[text()='Signed by: Slindile Mncwango (Customer)'])"
        return self.locator(selector, "Signed by 1")

    @property
    def signed_by2(self):
        selector = "(//*[text()='Signed by Slindile Mncwango'])"
        return self.locator(selector, "Signed by 2")

    @property
    def mr_dexpress_copyright(self):
        selector = "//*[@class='popup ui-dialog-content ui-widget-content']"
        return self.locator(selector, "Mr D Express copyright")

    @property
    def order_tracking_first_consignment(self):
        selector = "//div[@class='ui segment instruction-container'][1]"
        return self.locator(selector, "Order tracking first consignment")

    @property
    def first_consigment_delivered_date(self):
        selector = "//div[@class='ui segment instruction-container'][1]/div[1]/div/h5"
        return self.locator(selector, "First consignment delivered date")

    @property
    def first_consigment_signed_by(self):
        selector = "//div[@class='ui segment instruction-container'][1]/div[1]/div/p"
        return self.locator(selector, "First consignment signed by")

    @property
    def first_consigment_waybill_number(self):
        selector = "//div[@class='ui segment instruction-container'][1]/div[2]/div/div[1]/span/a"
        return self.locator(selector, "First consignment waybill number")

    @property
    def tracking_first_parcel_info(self):
        selector = "//div[@class='ui fluid vertical tabular menu']/a[1]"
        return self.locator(selector, "Tracking first parcel info")

    @property
    def tracking_first_parcel_number(self):
        selector = "//div[@class='ui fluid vertical tabular menu']/a[1]/div/div/strong"
        return self.locator(selector, "Tracking first parcel number")

    @property
    def tracking_first_parcel_item(self):
        selector = "//div[@class='stretched twelve wide computer sixteen wide mobile twelve wide tablet column']//*[@class='content']/span"
        return self.locator(selector, "Tracking first parcel item")

    @property
    def part_delivered_date(self):
        selector = "(//*[text()='Delivered Mon, 19 Sep 2022'])"
        return self.locator(selector, "Part delivered date")

    # endregion

    # region Coupon Elements

    @property
    def coupon_code(self):
        selector = "//div[text()='UAFORHER']"
        return self.locator(selector, "Coupon code")

    # endregion

    # region IP Address Elements

    @property
    def ip_address_icon(self):
        selector = "//*[@class='question circle outline icon link']"
        return self.locator(selector, "IP address icon")

    @property
    def ip_address(self):
        selector = "//input[@name='ipAddress']"
        return self.locator(selector, "IP address")

    @property
    def ip_address_model(self):
        selector = "//*[@class='ui tiny modal transition visible active']"
        return self.locator(selector, "IP address model")

    # endregion

    # region Modal Elements

    @property
    def close_icon(self):
        selector = "//*[@class='close icon']"
        return self.locator(selector, "Close icon")

    @property
    def close_modal(self):
        selector = "//*[@class='close icon']"
        return self.locator(selector, "Close modal")

    @property
    def cs_close_icon(self):
        selector = "/html/body/div[2]/div/i"
        return self.locator(selector, "CS close icon")

    @property
    def confirmation_msg(self):
        selector = "//*[@class='ui message']"
        return self.locator(selector, "Confirmation message")

    @property
    def done_button(self):
        selector = "//button[@class='ui primary right floated button']"
        return self.locator(selector, "Done button")

    @property
    def confirm_btn(self):
        selector = "//button[@class='ui primary button right floated']"
        return self.locator(selector, "Confirm button")

    @property
    def pop_up(self):
        selector = "//*[@id='noty_layout__topRight']"
        return self.locator(selector, "Pop-up")

    @property
    def progress_bar(self):
        selector = "//*[@class='ui green progress']"
        return self.locator(selector, "Progress bar")

    # endregion

    # region Search Elements

    @property
    def cs_search_txt(self):
        selector = "//*[@id='app']/div/div[1]/div[1]/div/input[1]"
        return self.locator(selector, "CS search text")

    @property
    def cs_search_btn(self):
        selector = "//*[@id='app']/div/div[1]/div[1]/div/button"
        return self.locator(selector, "CS search button")

    # endregion

    # region Other Elements

    @property
    def rrn(self):
        selector = "//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[7]/div[2]/a"
        return self.locator(selector, "RRN")

    @property
    def order_comments(self):
        selector = "//*[@class='ui mini comments']"
        return self.locator(selector, "Order comments")

    # endregion
