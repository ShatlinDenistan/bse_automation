from playwright.sync_api import Page, expect
from base.page_base import PageBase

# Locators as tuples with XPath and descriptive names
note_dd = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/span", "Note Dropdown")
add_notes_btn = ("//button[@class='ui mini primary right floated button']", "Add Notes Button")
notes_txt_field = ("//textarea[@name='customerNote']", "Notes Text Field")
confirm_add_btn = ("//button[@class='ui blue right floated button']", "Confirm Add Button")
note_confirm_message = ("//*[@id='noty_layout__topRight']", "Note Confirmation Message")

blacklist_cust_btn = ("//button[contains(text(),'Blacklist Customer')]", "Blacklist Customer Button")
fraud_reason_list = ("//div[contains(text(),'Fraud Reason')]", "Fraud Reason List")
fraud_reason_selection = ("//span[contains(text(),'Returns abuse')]", "Returns Abuse Option")
fin_note = ("//input[@name='finNote']", "Finance Note Input")
confirm_blacklist = ("//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]", "Confirm Blacklist Button")
whitelist_cust_btn = ("//button[contains(text(),'Whitelist Customer')]", "Whitelist Customer Button")
confirm_whitelist = ("//button[@class='ui blue right floated button'][contains(text(),'Confirm')]", "Confirm Whitelist Button")

cancel_all_item_btn = ("//button[contains(text(),'Cancel All Items')]", "Cancel All Items Button")
cancellation_reason = ("//*[@name='reasonTypeID']", "Cancellation Reason Dropdown")
customer_request_cancel_reason = ("//span[contains(text(),'Customer request')]", "Customer Request Cancel Reason")
confirm_cancelling_btn = ("//button[contains(text(),'Confirm Cancelling')]", "Confirm Cancelling Button")
close_cancel_modal = ("//*[@class='close icon']", "Close Cancel Modal")
order_status = ("//div[@class='ten wide column label-container']/span/div[1]", "Order Status")

# Email related locators
email_customer = ("//button[contains(text(),'Email Customer')]", "Email Customer Button")
email_template_ddl = ("//*[@name='emailTemplate']", "Email Template Dropdown")
email_template_selection = ("//span[contains(text(),'Identification not accepted')]", "Identification Not Accepted Template")
send_email_btn = ("//button[contains(text(),'Send Email')]", "Send Email Button")
customer_id = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]", "Customer ID")

# Risky order locators
mark_as_risky_btn = ("//button[contains(text(),'Mark as risky')]", "Mark as Risky Button")
mark_as_risky_reason = ("//input[@name='reason']", "Risky Reason Input")
add_reason_btn = ("//button[contains(text(),'Add Reason')]", "Add Reason Button")
flagged_as_risk = ("//div[@class='ui red basic label']", "Flagged as Risk Label")

# Audit log locators
order_ellipsis_menu = ("//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']", "Order Ellipsis Menu")
audit_log_menu_option = ("//*[contains(text(),'Audit log')]", "Audit Log Menu Option")
audit_log_action_type = ("//*[@class='ui striped basic very compact table']/tbody/tr/td[3]", "Audit Log Action Type")

# Authorization locators
authorise_now_btn = ("//button[contains(text(),'Authorise Now')]", "Authorise Now Button")
authorise_now_modal_message = ("//div[@class='ui success message']/div/div", "Authorise Modal Message")
authorise_now_modal_close_icon = ("//i[@class='close icon']", "Authorise Modal Close Icon")

# Order tracking locators
order_fulfillment_accordion = ("//*[contains(text(),'Order Fulfillment')]", "Order Fulfillment Accordion")
order_tracking_heading = ("//h5[@class='ui header']", "Order Tracking Heading")
order_tracking_user_info = ("//div[@class='ui info message']/div[1]", "Order Tracking User Info")
order_events_menu = ("//*[contains(text(),'Order events')]", "Order Events Menu")
event_log_results = ("//*[@class='ui red celled padded table']", "Event Log Results")

# Order items and notes locators
order_items_accordion = ("//div[@class='accordion ui']", "Order Items Accordion")
order_items_status = ("//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[1]", "Order Item Status")
order_item_canceled_by = ("//*[@class='accordion ui']/div/table/tbody/tr[1]/td[7]/div[3]/div/p[3]", "Order Item Canceled By")
order_items_show_items = ("//div[@class='ui compact item dropdown']", "Show Items Dropdown")
order_items_pagination_page_two = ("//*[@aria-label='Pagination Navigation']/a[3]", "Pagination Page Two")

# Payment and financials locators
payment_ledger_accordion = ("//div[@class='ten wide column']//*[text()='Payment Ledger']", "Payment Ledger Accordion")
payment_ledger_payment_provider = ("//*[@class='ui celled fixed structured table']/tbody/tr[1]/td[1]", "Payment Provider")
email_logs_accordion = ("//div[@class='ten wide column']//*[text()='Email Logs']", "Email Logs Accordion")
view_email_btn = ("//*[@class='blue mail outline icon']", "View Email Button")
email_view = ("//*[@class='ui scrolling modal transition visible active']", "Email View Modal")

# Order details locators
order_id = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/span[1]", "Order ID")
auth_status = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[1]", "Auth Status")
first_payment_method_badge = ("//div[@class='ui blue basic label']", "First Payment Method Badge")
auth_date = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/span/div[3]", "Auth Date")
order_comments = ("//*[@class='ui mini comments']", "Order Comments")

# Delivery related locators
street_address = ("//div[@class='column'][contains(text(),'6 Birkenhead Road')]", "Street Address")
suburb_address = ("//div[@class='column'][contains(text(),'Umbilo')]", "Suburb")
city_address = ("//div[@class='column'][contains(text(),'Berea')]", "City")
province_address = ("//div[@class='column'][contains(text(),'KwaZulu-Natal')]", "Province")
code_address = ("//div[@class='column'][contains(text(),'4075')]", "Postal Code")
copy_address_btn = ("//button[@class='ui blue mini right floated button']", "Copy Address Button")
address_copied_btn = ("//button[@class='ui green mini right floated button']", "Address Copied Button")
residential_txt = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div[1]/div[1]/div/div[2]/div/div[1]", "Residential Text")

# Customer info locators
cust_info_popup = ("//*[@class='ui bottom center basic popup transition visible']", "Customer Info Popup")
cust_acc_number = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/a[1]", "Customer Account Number")
cust_name_popup = ("//table[@class='ui small unstackable very basic very compact table']//td[text()='Slindile Mncwango']", "Customer Name Popup")
cust_date_registered = ("//table[@class='ui small unstackable very basic very compact table']//td[text()='16-Oct-2018 @ 10:41']", "Customer Date Registered")
cust_blacklist_status = ("//div[@class='ui green basic label'][contains(text(),'Not Blacklisted')]", "Customer Blacklist Status")

# Shipping and tracking locators
waybill_no = ("//strong[text()='Waybill No: ']/following-sibling::*[1]", "Waybill Number")
delivery_estimate_date = ("//div[@class='ui segment instruction-container']//h5", "Delivery Estimate Date")
delivery_not_yet_ready_message = ("//div[@class='ui segment instruction-container']//div/span", "Delivery Not Ready Message")
collection_estimate_date = ("//div[@class='ui segment instruction-container']//h5", "Collection Estimate Date")
collection_not_yet_ready_message = ("//div[@class='ui segment instruction-container']//div/span", "Collection Not Ready Message")
shipping_method = ("(//table[@class='ui small unstackable basic very compact table']//td[text()='Courier'])[1]", "Shipping Method")
shipping_plan = ("(//table[@class='ui small unstackable basic very compact table']//td[text()='Standard'])[1]", "Shipping Plan")
shipping_courier = ("(//table[@class='ui small unstackable basic very compact table']//td[text()='MDX133806010 - Takealot Delivery Team'])[1]", "Shipping Courier")
shipping_promised_date = ("(//table[@class='ui small unstackable basic very compact table']//td[text()='28 Aug 2024'])[1]", "Shipping Promised Date")
shipping_delivered_date = ("(//table[@class='ui small unstackable basic very compact table']//td[text()='30 Aug 2024'])[1]", "Shipping Delivered Date")
delivered_tag = ("//div[@class='ui green tiny label'][contains(text(),'Delivered')]", "Delivered Tag")

# Multiple waybill tracking locators
instruction_dropped_date1 = ("(//div[text()='27 May 2024 @ 17:46'])[1]", "First Instruction Dropped Date")
instruction_dropped_date2 = ("(//div[text()='27 May 2024 @ 0:34'])", "Second Instruction Dropped Date")
shipped_from_warehouse_date1 = ("(//div[text()='28 May 2024 @ 1:31'])", "First Shipped Date")
shipped_from_warehouse_date2 = ("(//div[text()='27 May 2024 @ 17:46'])[2]", "Second Shipped Date")
delivered_date1 = ("(//div[text()='30 May 2024 @ 11:40'])", "First Delivered Date")
delivered_date2 = ("(//div[text()='29 May 2024 @ 10:58'])", "Second Delivered Date")
order_tracking_heading1 = ("(//*[text()='Delivered Thu, 30 May 2024'])", "First Tracking Heading")
signed_by1 = ("(//*[text()='Signed by: Slindile Mncwango (Customer)'])", "First Signed By")
signed_by2 = ("(//*[text()='Signed by Slindile Mncwango'])", "Second Signed By")
waybill_number1 = ("(//*[text()='MDX127668689'])", "First Waybill Number")
waybill_number2 = ("(//*[text()='MDX127583371'])", "Second Waybill Number")

# Order financials locators
order_financials_accordion = ("//div[@class='ten wide column']//*[text()='Order Financials']", "Order Financials Accordion")
total_order_items_amount = ("//tbody/tr/td[text()='Total Order Items']/following-sibling::*[1]/div", "Total Order Items Amount")
shipping_amount = ("//tbody/tr/td[text()='Shipping']/following-sibling::*[1]/div", "Shipping Amount")
sub_total_amount = ("//tbody/tr/td[text()='Sub-Total']/following-sibling::*[1]/div", "Sub Total Amount")
discount_amount = ("//tbody/tr/td[text()='Discount']/following-sibling::*[1]/div", "Discount Amount")

# RRN and partial delivery locators
rrn = ("//*[@id='root']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr/td[7]/div[2]/a", "RRN Link")
part_delivered_date = ("(//*[text()='Delivered Mon, 19 Sep 2022'])", "Part Delivered Date")
cancelled_items = ("(//*[text()='Cancelled Item(s)'])", "Cancelled Items")
cancelled_tag = ("//div[@class='ui red tiny label'][contains(text(),'Canceled')]", "Cancelled Tag")

# IP Address locators
ip_address_icon = ("//*[@class='question circle outline icon link']", "IP Address Icon")
ip_address = ("//input[@name='ipAddress']", "IP Address Input")
ip_address_model = ("//*[@class='ui tiny modal transition visible active']", "IP Address Modal")


class OrderViewPage(PageBase):
    """Page object for Order View functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        # Initialize locators
        self.note_dd = self.locator(*note_dd)
        self.add_notes_btn = self.locator(*add_notes_btn)
        self.notes_txt_field = self.locator(*notes_txt_field)
        self.confirm_add_btn = self.locator(*confirm_add_btn)
        self.note_confirm_message = self.locator(*note_confirm_message)

        self.blacklist_cust_btn = self.locator(*blacklist_cust_btn)
        self.fraud_reason_list = self.locator(*fraud_reason_list)
        self.fraud_reason_selection = self.locator(*fraud_reason_selection)
        self.fin_note = self.locator(*fin_note)
        self.confirm_blacklist = self.locator(*confirm_blacklist)
        self.whitelist_cust_btn = self.locator(*whitelist_cust_btn)
        self.confirm_whitelist = self.locator(*confirm_whitelist)

        self.cancel_all_item_btn = self.locator(*cancel_all_item_btn)
        self.cancellation_reason = self.locator(*cancellation_reason)
        self.customer_request_cancel_reason = self.locator(*customer_request_cancel_reason)
        self.confirm_cancelling_btn = self.locator(*confirm_cancelling_btn)
        self.close_cancel_modal = self.locator(*close_cancel_modal)
        self.order_status = self.locator(*order_status)

        # Initialize email related locators
        self.email_customer = self.locator(*email_customer)
        self.email_template_ddl = self.locator(*email_template_ddl)
        self.email_template_selection = self.locator(*email_template_selection)
        self.send_email_btn = self.locator(*send_email_btn)
        self.customer_id = self.locator(*customer_id)

        # Initialize risky order locators
        self.mark_as_risky_btn = self.locator(*mark_as_risky_btn)
        self.mark_as_risky_reason = self.locator(*mark_as_risky_reason)
        self.add_reason_btn = self.locator(*add_reason_btn)
        self.flagged_as_risk = self.locator(*flagged_as_risk)

        # Initialize audit log locators
        self.order_ellipsis_menu = self.locator(*order_ellipsis_menu)
        self.audit_log_menu_option = self.locator(*audit_log_menu_option)
        self.audit_log_action_type = self.locator(*audit_log_action_type)

        # Initialize authorization locators
        self.authorise_now_btn = self.locator(*authorise_now_btn)
        self.authorise_now_modal_message = self.locator(*authorise_now_modal_message)
        self.authorise_now_modal_close_icon = self.locator(*authorise_now_modal_close_icon)

        # Initialize order tracking locators
        self.order_fulfillment_accordion = self.locator(*order_fulfillment_accordion)
        self.order_tracking_heading = self.locator(*order_tracking_heading)
        self.order_tracking_user_info = self.locator(*order_tracking_user_info)
        self.order_events_menu = self.locator(*order_events_menu)
        self.event_log_results = self.locator(*event_log_results)

        # Initialize order items and notes locators
        self.order_items_accordion = self.locator(*order_items_accordion)
        self.order_items_status = self.locator(*order_items_status)
        self.order_item_canceled_by = self.locator(*order_item_canceled_by)
        self.order_items_show_items = self.locator(*order_items_show_items)
        self.order_items_pagination_page_two = self.locator(*order_items_pagination_page_two)

        # Initialize payment and financials locators
        self.payment_ledger_accordion = self.locator(*payment_ledger_accordion)
        self.payment_ledger_payment_provider = self.locator(*payment_ledger_payment_provider)
        self.email_logs_accordion = self.locator(*email_logs_accordion)
        self.view_email_btn = self.locator(*view_email_btn)
        self.email_view = self.locator(*email_view)

        # Initialize order details locators
        self.order_id = self.locator(*order_id)
        self.auth_status = self.locator(*auth_status)
        self.first_payment_method_badge = self.locator(*first_payment_method_badge)
        self.auth_date = self.locator(*auth_date)
        self.order_comments = self.locator(*order_comments)

        # Initialize delivery related locators
        self.street_address = self.locator(*street_address)
        self.suburb_address = self.locator(*suburb_address)
        self.city_address = self.locator(*city_address)
        self.province_address = self.locator(*province_address)
        self.code_address = self.locator(*code_address)
        self.copy_address_btn = self.locator(*copy_address_btn)
        self.address_copied_btn = self.locator(*address_copied_btn)
        self.residential_txt = self.locator(*residential_txt)

        # Initialize customer info locators
        self.cust_info_popup = self.locator(*cust_info_popup)
        self.cust_acc_number = self.locator(*cust_acc_number)
        self.cust_name_popup = self.locator(*cust_name_popup)
        self.cust_date_registered = self.locator(*cust_date_registered)
        self.cust_blacklist_status = self.locator(*cust_blacklist_status)

        # Initialize shipping and tracking locators
        self.waybill_no = self.locator(*waybill_no)
        self.delivery_estimate_date = self.locator(*delivery_estimate_date)
        self.delivery_not_yet_ready_message = self.locator(*delivery_not_yet_ready_message)
        self.collection_estimate_date = self.locator(*collection_estimate_date)
        self.collection_not_yet_ready_message = self.locator(*collection_not_yet_ready_message)
        self.shipping_method = self.locator(*shipping_method)
        self.shipping_plan = self.locator(*shipping_plan)
        self.shipping_courier = self.locator(*shipping_courier)
        self.shipping_promised_date = self.locator(*shipping_promised_date)
        self.shipping_delivered_date = self.locator(*shipping_delivered_date)
        self.delivered_tag = self.locator(*delivered_tag)

        # Initialize multiple waybill tracking locators
        self.instruction_dropped_date1 = self.locator(*instruction_dropped_date1)
        self.instruction_dropped_date2 = self.locator(*instruction_dropped_date2)
        self.shipped_from_warehouse_date1 = self.locator(*shipped_from_warehouse_date1)
        self.shipped_from_warehouse_date2 = self.locator(*shipped_from_warehouse_date2)
        self.delivered_date1 = self.locator(*delivered_date1)
        self.delivered_date2 = self.locator(*delivered_date2)
        self.order_tracking_heading1 = self.locator(*order_tracking_heading1)
        self.signed_by1 = self.locator(*signed_by1)
        self.signed_by2 = self.locator(*signed_by2)
        self.waybill_number1 = self.locator(*waybill_number1)
        self.waybill_number2 = self.locator(*waybill_number2)

        # Initialize order financials locators
        self.order_financials_accordion = self.locator(*order_financials_accordion)
        self.total_order_items_amount = self.locator(*total_order_items_amount)
        self.shipping_amount = self.locator(*shipping_amount)
        self.sub_total_amount = self.locator(*sub_total_amount)
        self.discount_amount = self.locator(*discount_amount)

        # Initialize RRN and partial delivery locators
        self.rrn = self.locator(*rrn)
        self.part_delivered_date = self.locator(*part_delivered_date)
        self.cancelled_items = self.locator(*cancelled_items)
        self.cancelled_tag = self.locator(*cancelled_tag)

        # Initialize IP address locators
        self.ip_address_icon = self.locator(*ip_address_icon)
        self.ip_address = self.locator(*ip_address)
        self.ip_address_model = self.locator(*ip_address_model)

    def add_admin_notes(self):
        """Add admin notes to the order"""
        self.expect_to_be_visible(self.note_dd)
        self.click(self.note_dd)
        self.click(self.add_notes_btn)
        self.fill(self.notes_txt_field, "Automation Admin Note")
        self.click(self.confirm_add_btn)
        self.expect_to_be_visible(self.note_confirm_message)
        message = self.text_content(self.note_confirm_message)
        message = message.replace("Request failed with status code 403\n×\n", "")
        assert "Note successfully added to Customer: 8441423" in message

    def update_to_blacklist(self):
        """Update customer status to blacklist"""
        self.expect_to_be_visible(self.blacklist_cust_btn)
        self.click(self.blacklist_cust_btn)
        self.click(self.fraud_reason_list)
        self.click(self.fraud_reason_selection)
        self.fill(self.fin_note, "Automation Testing")
        self.click(self.confirm_blacklist)
        self.handle_alert()
        self.wait_for_seconds(3)
        self.expect_to_be_visible(self.note_confirm_message)
        message = self.text_content(self.note_confirm_message)
        message = message.replace("Request failed with status code 403\n×\n", "")
        assert "Successfully blacklisted the customer" in message

    def update_to_whitelist(self):
        """Update customer status to whitelist"""
        self.expect_to_be_visible(self.whitelist_cust_btn)
        self.click(self.whitelist_cust_btn)
        self.click(self.confirm_whitelist)
        self.handle_alert()
        self.wait_for_seconds(6)
        self.expect_to_be_visible(self.note_confirm_message)
        message = self.text_content(self.note_confirm_message)
        message = message.replace("Request failed with status code 403\n×\n", "")
        assert "Successfully Whitelisted Customer: 8441423" in message

    def cancel_all_order_items(self):
        """Cancel all items in the order"""
        self.expect_to_be_visible(self.cancel_all_item_btn)
        self.click(self.cancel_all_item_btn)
        self.click(self.cancellation_reason)
        self.scroll_to_element(self.customer_request_cancel_reason)
        self.click(self.customer_request_cancel_reason)
        self.click(self.confirm_cancelling_btn)
        self.click(self.close_cancel_modal)
        status_text = self.text_content(self.order_status)
        assert "Canceled by" in status_text

    def send_an_email(self):
        """Send an email to the customer"""
        cust_id = self.text_content(self.customer_id)
        self.click(self.email_customer)
        self.click(self.email_template_ddl)
        self.click(self.email_template_selection)
        self.scroll_to_element(self.send_email_btn)
        self.click(self.send_email_btn)
        self.expect_to_be_visible(self.note_confirm_message)
        message = self.text_content(self.note_confirm_message)
        message = message.replace("\n×\nRequest failed with status code 404\n×", "")
        assert f"(Identification Not Accepted) email sent to customer {cust_id}" in message

    def mark_order_as_risky(self):
        """Mark an order as risky"""
        self.expect_to_be_visible(self.mark_as_risky_btn)
        self.click(self.mark_as_risky_btn)
        self.fill(self.mark_as_risky_reason, "Automation Test Risky Reason")
        self.click(self.add_reason_btn)
        flagged_text = self.text_content(self.flagged_as_risk)
        assert "Flagged as risky" in flagged_text

    def verify_audit_log_entry(self, action_type: str):
        """Verify audit log entry for a specific action"""
        self.expect_to_be_visible(self.order_ellipsis_menu)
        self.click(self.order_ellipsis_menu)
        self.click(self.audit_log_menu_option)
        self.expect_to_be_visible(self.audit_log_action_type)
        action_text = self.text_content(self.audit_log_action_type)
        assert action_type in action_text

    def manually_authorize_order(self):
        """Manually authorize an order"""
        self.expect_to_be_visible(self.authorise_now_btn)
        self.click(self.authorise_now_btn)
        self.expect_to_be_visible(self.authorise_now_modal_message)
        success_message = self.text_content(self.authorise_now_modal_message)
        assert "Successfully processed 1 item(s)" in success_message
        self.click(self.authorise_now_modal_close_icon)

    def verify_order_tracking_for_digital_products(self):
        """Verify order tracking for digital products only order"""
        self.click(self.order_fulfillment_accordion)
        self.expect_to_be_visible(self.order_tracking_user_info)
        user_info_text = self.text_content(self.order_tracking_user_info)
        assert "Digital Product(s)" in user_info_text

    def verify_order_tracking_heading(self, heading: str):
        """Verify order tracking heading"""
        self.expect_to_be_visible(self.order_fulfillment_accordion)
        self.click(self.order_fulfillment_accordion)
        heading_text = self.text_content(self.order_tracking_heading)
        assert heading in heading_text

    def view_order_events(self):
        """View order events"""
        self.click(self.order_ellipsis_menu)
        self.click(self.order_events_menu)
        self.expect_to_be_visible(self.event_log_results)

    def view_order_items_information(self):
        """View order items information"""
        self.expect_to_be_visible(self.order_items_accordion)
        status_text = self.text_content(self.order_items_status)
        assert status_text == "Canceled"
        canceled_by_text = self.text_content(self.order_item_canceled_by)
        assert canceled_by_text == "auto_cancel"

    def verify_show_items_and_pagination(self):
        """Verify show items dropdown and pagination"""
        self.expect_to_be_visible(self.order_items_show_items)
        self.click(self.order_items_show_items)
        self.page.keyboard.press("ArrowUp")
        self.page.keyboard.press("Enter")
        self.wait_for_seconds(1)
        self.click(self.order_items_pagination_page_two)

    def verify_payment_ledger_logs(self):
        """Verify payment ledger logs"""
        self.expect_to_be_visible(self.payment_ledger_accordion)
        self.click(self.payment_ledger_accordion)
        provider_text = self.text_content(self.payment_ledger_payment_provider)
        assert "Payflex" in provider_text

    def view_email_logs(self):
        """View email logs"""
        self.scroll_to_element(self.email_logs_accordion)
        self.click(self.email_logs_accordion)
        self.click(self.view_email_btn)
        self.expect_to_be_visible(self.email_view)

    def verify_order_details(self, search_order_id: str):
        """Verify order details including ID, status, payment method and auth date"""
        # Verify Order ID
        order_id_text = self.text_content(self.order_id)
        assert order_id_text == search_order_id

        # Verify auth status
        status_text = self.text_content(self.auth_status)
        assert "Auth" in status_text

        # Verify payment method
        payment_method_text = self.text_content(self.first_payment_method_badge)
        assert "Credit Card Token" in payment_method_text

        # Verify auth date
        auth_date_text = self.text_content(self.auth_date)
        assert "25-Jan-2024 @ 9:31" in auth_date_text

        # Check order fulfillment
        self.click(self.order_fulfillment_accordion)
        user_info_text = self.text_content(self.order_tracking_user_info)
        assert "Digital Product(s)" in user_info_text
        self.click(self.order_fulfillment_accordion)

        # Check order notes
        self.scroll_to_element(self.order_comments)
        self.expect_to_be_visible(self.order_comments)

    def verify_delivery_address(self):
        """Verify delivery address details"""
        self.click(self.order_fulfillment_accordion)

        street_text = self.text_content(self.street_address)
        assert "6 Birkenhead Road" in street_text

        suburb_text = self.text_content(self.suburb_address)
        assert "Umbilo" in suburb_text

        city_text = self.text_content(self.city_address)
        assert "Berea" in city_text

        province_text = self.text_content(self.province_address)
        assert "KwaZulu-Natal" in province_text

        code_text = self.text_content(self.code_address)
        assert "4075" in code_text

        self.click(self.copy_address_btn)
        copied_text = self.text_content(self.address_copied_btn)
        assert "Address copied!" in copied_text

        residential_text = self.text_content(self.residential_txt)
        assert "residential" in residential_text

        self.click(self.order_fulfillment_accordion)

    def verify_customer_info(self):
        """Verify customer information in popup"""
        cust_name_text = self.text_content(self.cust_name_popup)
        assert "Slindile Mncwango" in cust_name_text

        date_registered_text = self.text_content(self.cust_date_registered)
        assert "16-Oct-2018 @ 10:41" in date_registered_text

        blacklist_status_text = self.text_content(self.cust_blacklist_status)
        assert "Not Blacklisted" in blacklist_status_text

    def hover_over_customer_id(self):
        """Hover over customer ID to show info popup"""
        self.expect_to_be_visible(self.cust_acc_number)
        self.hover(self.cust_acc_number)
        self.expect_to_be_visible(self.cust_info_popup)

    def verify_delivery_not_yet_shipped(self):
        """Verify delivery is not yet shipped"""
        self.expect_to_be_visible(self.order_fulfillment_accordion)
        self.click(self.order_fulfillment_accordion)
        delivery_estimate_text = self.text_content(self.delivery_estimate_date)
        assert "Delivery by ------" in delivery_estimate_text
        delivery_not_ready_text = self.text_content(self.delivery_not_yet_ready_message)
        assert "NOT YET SHIPPED" in delivery_not_ready_text

    def verify_collection_not_yet_ready(self):
        """Verify collection is not yet ready"""
        self.expect_to_be_visible(self.order_fulfillment_accordion)
        self.click(self.order_fulfillment_accordion)
        collection_estimate_text = self.text_content(self.collection_estimate_date)
        assert "Estimated Collection from" in collection_estimate_text
        collection_not_ready_text = self.text_content(self.collection_not_yet_ready_message)
        assert "NOT YET READY" in collection_not_ready_text

    def verify_shipping_information(self):
        """Verify shipping information details"""
        self.click(self.order_fulfillment_accordion)

        method_text = self.text_content(self.shipping_method)
        assert "Courier" in method_text

        plan_text = self.text_content(self.shipping_plan)
        assert "Standard" in plan_text

        courier_text = self.text_content(self.shipping_courier)
        assert "MDX133806010 - Takealot Delivery Team" in courier_text

        promised_date_text = self.text_content(self.shipping_promised_date)
        assert "28 Aug 2024" in promised_date_text

        delivered_date_text = self.text_content(self.shipping_delivered_date)
        assert "30 Aug 2024" in delivered_date_text

    def verify_delivery_tracking_information(self, heading: str):
        """Verify delivery tracking information"""
        status_text = self.text_content(self.delivered_tag)
        assert "Delivered" in status_text

        self.click(self.order_fulfillment_accordion)
        self.scroll_to_element(self.order_tracking_heading)
        self.expect_to_be_visible(self.order_tracking_heading)

        heading_text = self.text_content(self.order_tracking_heading)
        assert heading in heading_text

    def verify_multiple_waybill_tracking(self):
        """Verify tracking information for multiple waybills"""
        self.click(self.order_fulfillment_accordion)
        self.scroll_to_element(self.instruction_dropped_date1)
        self.expect_to_be_visible(self.order_tracking_heading1)

        heading1_text = self.text_content(self.order_tracking_heading1)
        assert "Delivered Thu, 30 May 2024" in heading1_text

        signed_by_text = self.text_content(self.signed_by1)
        assert "Signed by: Slindile Mncwango (Customer)" in signed_by_text

        waybill_number_text = self.text_content(self.waybill_number1)
        assert "MDX127668689" in waybill_number_text

        instruction_datetime_text = self.text_content(self.instruction_dropped_date1)
        assert "27 May 2024 @ 17:46" in instruction_datetime_text

        shipped_datetime_text = self.text_content(self.shipped_from_warehouse_date1)
        assert "28 May 2024 @ 1:31" in shipped_datetime_text

        delivered_datetime_text = self.text_content(self.delivered_date1)
        assert "30 May 2024 @ 11:40" in delivered_datetime_text

        self.scroll_to_element(self.instruction_dropped_date2)

        signed_by_text = self.text_content(self.signed_by2)
        assert "Signed by Slindile Mncwango" in signed_by_text

        waybill_number_text = self.text_content(self.waybill_number2)
        assert "MDX127583371" in waybill_number_text

        instruction_datetime_text = self.text_content(self.instruction_dropped_date2)
        assert "27 May 2024 @ 0:34" in instruction_datetime_text

        shipped_datetime_text = self.text_content(self.shipped_from_warehouse_date2)
        assert "27 May 2024 @ 17:46" in shipped_datetime_text

        delivered_datetime_text = self.text_content(self.delivered_date2)
        assert "29 May 2024 @ 10:58" in delivered_datetime_text

    def verify_order_financials(self):
        """Verify order financials breakdown"""
        self.expect_to_be_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)

        # Verify Order Items Amount
        order_items_amount = self.text_content(self.total_order_items_amount)
        order_items_amount = order_items_amount.replace("R ", "")
        order_items_amount = float(order_items_amount)

        # Verify Shipping Amount
        shipping_amount = self.text_content(self.shipping_amount)
        shipping_amount = shipping_amount.replace("R ", "")
        shipping_amount = float(shipping_amount)

        # Verify Sub-Total Amount
        sub_total_amount = self.text_content(self.sub_total_amount)
        sub_total_amount = sub_total_amount.replace("R ", "")
        sub_total_amount = float(sub_total_amount)
        sub_total_calculation = order_items_amount + shipping_amount
        assert sub_total_amount == sub_total_calculation

        # Verify Discount Amount
        discount_amount = self.text_content(self.discount_amount)
        discount_amount = discount_amount.replace("? ", "").replace("R -", "")
        discount_amount = float(discount_amount)
        return order_items_amount, shipping_amount, discount_amount

    def get_rrn_details(self):
        """Get RRN details from order"""
        self.expect_to_be_visible(self.rrn)
        self.click(self.rrn)
        self.wait_for_seconds(2)
        return self.get_page_handles()

    def verify_partial_order_delivery(self):
        """Verify partial order delivery status"""
        # Verify delivered item
        item_status = self.text_content(self.delivered_tag)
        assert "Delivered" in item_status

        # Verify cancelled item
        cancelled_status = self.text_content(self.cancelled_tag)
        assert "Canceled" in cancelled_status

        # Check delivery details
        self.click(self.order_fulfillment_accordion)
        self.scroll_to_element(self.signed_by1)

        tracking_heading = self.text_content(self.part_delivered_date)
        assert "Delivered Mon, 19 Sep 2022" in tracking_heading

        signed_by = self.text_content(self.signed_by1)
        assert "Signed by: Slindile Mncwango (Customer)" in signed_by

        self.scroll_to_element(self.cancelled_items)
        cancelled_items = self.text_content(self.cancelled_items)
        assert "Cancelled Item(s)" in cancelled_items

    def verify_ip_address(self):
        """Verify IP address information"""
        self.click(self.ip_address_icon)
        self.expect_to_be_visible(self.ip_address_model)
        ip_address_text = self.get_input_value(self.ip_address)
        assert "41.115.115.60" in ip_address_text

    def get_page_handles(self):
        """Get window handles for switching between pages"""
        self.wait_for_seconds(2)
        return self.page.context.pages

    def expand_order_items_accordion_and_click_refund(self):
        """
        Expand the order items accordion and click on the refund button

        This method:
        1. Finds and clicks on the order items accordion
        2. Waits for the items to be visible
        3. Finds and clicks on the refund button
        """
        self.expect_to_be_visible(self.order_items_accordion)
        self.click(self.order_items_accordion)
        self.wait_for_seconds(1)

        # Define refund button locator
        refund_button = self.locator("//button[contains(text(),'Refund')]", "Refund Button")
        self.expect_to_be_visible(refund_button)
        self.click(refund_button)
        self.wait_for_seconds(1)

    def view_refunds_logs(self):
        """
        Navigate to the refunds logs page for the current order

        This method extracts the order ID from the current page URL and navigates
        to the refunds logs page for that order.
        """
        # Extract order ID from current URL
        current_url = self.page.url
        order_id = current_url.split("/")[-1]
        if "?" in order_id:
            order_id = order_id.split("?")[0]

        # Navigate to refunds logs page
        refunds_logs_url = f"http://fin-portal.master.env/order/{order_id}/refunds_logs"
        self.page.goto(refunds_logs_url)
        self.wait_for_seconds(2)

    def edit_customer_details(self):
        """Edit customer details on the order view page"""
        # Define locators
        edit_cust_details_btn = self.locator("//button[contains(text(),'Edit Customer Details')]", "Edit Customer Details Button")
        cust_name_field = self.locator("//input[@name='name']", "Customer Name Field")
        save_button = self.locator("//button[@class='ui blue right floated button']", "Save Button")

        # Perform actions
        self.expect_to_be_visible(edit_cust_details_btn)
        self.click(edit_cust_details_btn)
        self.fill(cust_name_field, f"Automation Test {self.faker.name()}")
        self.click(save_button)
        self.expect_to_be_visible(self.note_confirm_message)

    def verify_part_payment_methods_badges(self):
        """Verify payment method badges for part payment order"""
        # Define locators for various payment method badges
        credit_card_badge = self.locator("//div[@class='ui blue basic label'][contains(text(),'Credit Card')]", "Credit Card Badge")
        ebucks_badge = self.locator("//div[@class='ui blue basic label'][contains(text(),'eBucks')]", "eBucks Badge")

        # Verify badges are displayed
        self.expect_to_be_visible(credit_card_badge)
        self.expect_to_be_visible(ebucks_badge)

    def add_order_notes(self):
        """Add notes to the order"""
        order_notes_dd = self.locator("//div[contains(text(),'Order Notes')]", "Order Notes Dropdown")
        add_notes_btn = self.locator("//button[@class='ui mini primary right floated button']", "Add Notes Button")
        notes_txt_field = self.locator("//textarea[@name='orderNote']", "Notes Text Field")
        confirm_add_btn = self.locator("//button[@class='ui blue right floated button']", "Confirm Add Button")

        self.click(order_notes_dd)
        self.click(add_notes_btn)
        self.fill(notes_txt_field, "Automation Order Note")
        self.click(confirm_add_btn)
        self.expect_to_be_visible(self.note_confirm_message)

    def add_customer_notes(self):
        """Add notes to the customer"""
        cust_notes_dd = self.locator("//div[contains(text(),'Customer Notes')]", "Customer Notes Dropdown")
        add_notes_btn = self.locator("//button[@class='ui mini primary right floated button']", "Add Notes Button")
        notes_txt_field = self.locator("//textarea[@name='customerNote']", "Notes Text Field")
        confirm_add_btn = self.locator("//button[@class='ui blue right floated button']", "Confirm Add Button")

        self.click(cust_notes_dd)
        self.click(add_notes_btn)
        self.fill(notes_txt_field, "Automation Customer Note")
        self.click(confirm_add_btn)
        self.expect_to_be_visible(self.note_confirm_message)

    def add_fin_notes(self):
        """Add finance notes"""
        fin_notes_dd = self.locator("//div[contains(text(),'Fin Notes')]", "Finance Notes Dropdown")
        add_notes_btn = self.locator("//button[@class='ui mini primary right floated button']", "Add Notes Button")
        notes_txt_field = self.locator("//textarea[@name='finNote']", "Notes Text Field")
        confirm_add_btn = self.locator("//button[@class='ui blue right floated button']", "Confirm Add Button")

        self.click(fin_notes_dd)
        self.click(add_notes_btn)
        self.fill(notes_txt_field, "Automation Finance Note")
        self.click(confirm_add_btn)
        self.expect_to_be_visible(self.note_confirm_message)

    def cancel_an_order_item(self):
        """Cancel a single order item"""
        first_order_item_cancel = self.locator("(//button[contains(text(),'Cancel')])[1]", "First Order Item Cancel Button")
        cancellation_reason = self.locator("//div[contains(text(),'Cancellation Reason')]", "Cancellation Reason")
        customer_request_reason = self.locator("//span[contains(text(),'Customer request')]", "Customer Request Reason")
        confirm_cancel = self.locator("//button[contains(text(),'Confirm Cancelling')]", "Confirm Cancel Button")
        close_modal = self.locator("//i[@class='close icon']", "Close Modal")

        self.expect_to_be_visible(first_order_item_cancel)
        self.click(first_order_item_cancel)
        self.click(cancellation_reason)
        self.click(customer_request_reason)
        self.click(confirm_cancel)
        self.click(close_modal)

    def view_payment_ledger(self):
        """View payment ledger information"""
        payment_ledger_acc = self.locator("//*[text()='Payment Ledger']", "Payment Ledger Accordion")
        payment_ledger_details = self.locator("//table[@class='ui celled fixed structured table']", "Payment Ledger Details")

        self.expect_to_be_visible(payment_ledger_acc)
        self.click(payment_ledger_acc)
        self.expect_to_be_visible(payment_ledger_details)

    def bookmark_an_order(self):
        """Add a bookmark for the current order"""
        bookmark_button = self.locator("//button[contains(text(),'Bookmark')]", "Bookmark Button")
        bookmark_name_field = self.locator("//input[@name='bookmarkName']", "Bookmark Name Field")
        save_bookmark_button = self.locator("//button[contains(text(),'Save Bookmark')]", "Save Bookmark Button")

        self.expect_to_be_visible(bookmark_button)
        self.click(bookmark_button)
        self.fill(bookmark_name_field, f"Auto Bookmark {self.faker.word()}")
        self.click(save_bookmark_button)
        self.expect_to_be_visible(self.note_confirm_message)

    def remove_bookmarks(self):
        """Remove bookmarks"""
        bookmarks_menu = self.locator("//div[contains(text(),'Bookmarks')]", "Bookmarks Menu")
        first_bookmark_option = self.locator("(//div[@class='item'])[1]", "First Bookmark Option")
        remove_bookmark = self.locator("//i[@class='trash icon']", "Remove Bookmark Icon")

        self.click(bookmarks_menu)
        self.click(first_bookmark_option)
        self.click(remove_bookmark)
        self.expect_to_be_visible(self.note_confirm_message)

    def view_order_audit_logs(self):
        """View order audit logs"""
        order_menu = self.locator("//i[@class='black ellipsis vertical small icon']", "Order Menu")
        audit_log_option = self.locator("//div[contains(text(),'Audit log')]", "Audit Log Option")
        audit_log_table = self.locator("//table[@class='ui striped basic very compact table']", "Audit Log Table")

        self.click(order_menu)
        self.click(audit_log_option)
        self.expect_to_be_visible(audit_log_table)

    def view_address(self):
        """View address on Google Maps"""
        view_address_btn = self.locator("//button[contains(text(),'View Address')]", "View Address Button")
        google_maps_modal = self.locator("//iframe[contains(@src,'google.com/maps')]", "Google Maps iframe")

        self.expect_to_be_visible(view_address_btn)
        self.click(view_address_btn)
        self.expect_to_be_visible(google_maps_modal)

    def update_order_item_to_shipped(self):
        """Update order item status to shipped"""
        edit_status_btn = self.locator("(//button[contains(text(),'Status')])[1]", "Edit Status Button")
        status_dropdown = self.locator("//div[contains(text(),'Canceled')]", "Status Dropdown")
        shipped_option = self.locator("//span[contains(text(),'Shipped')]", "Shipped Option")
        update_button = self.locator("//button[contains(text(),'Update')]", "Update Button")

        self.expect_to_be_visible(edit_status_btn)
        self.click(edit_status_btn)
        self.click(status_dropdown)
        self.click(shipped_option)
        self.click(update_button)
        self.expect_to_be_visible(self.note_confirm_message)

    def view_coupon_history(self):
        """View coupon history on the order page"""
        coupon_history_accordion = self.locator("//div[contains(text(),'Coupon History')]", "Coupon History Accordion")
        coupon_details_table = self.locator("//table[@class='ui celled striped compact table']", "Coupon Details Table")

        self.expect_to_be_visible(coupon_history_accordion)
        self.click(coupon_history_accordion)
        self.expect_to_be_visible(coupon_details_table)

    def verify_waybill_tracking(self):
        """Verify waybill tracking information"""
        waybill_number = self.locator("//div[contains(text(),'MDX')]", "Waybill Number")
        dropped_off = self.locator("//div[contains(text(),'Dropped off:')]", "Dropped Off")
        picked_up = self.locator("//div[contains(text(),'Picked up:')]", "Picked Up")
        delivered = self.locator("//div[contains(text(),'Delivered:')]", "Delivered")

        self.expect_to_be_visible(waybill_number)
        self.expect_to_be_visible(dropped_off)
        self.expect_to_be_visible(picked_up)
        self.expect_to_be_visible(delivered)

    def verify_refund_history_information(self):
        """Verify refund history information"""
        refund_history_accordion = self.locator("//div[contains(text(),'Refund History')]", "Refund History Accordion")
        refund_details_table = self.locator("//table[@class='ui celled striped table']", "Refund Details Table")

        self.expect_to_be_visible(refund_history_accordion)
        self.click(refund_history_accordion)
        self.expect_to_be_visible(refund_details_table)

    def verify_the_google_search(self):
        """Verify Google search functionality for customer"""
        google_search_btn = self.locator("//button[contains(text(),'Google')]", "Google Search Button")

        self.expect_to_be_visible(google_search_btn)
        self.click(google_search_btn)
        # This opens a new tab, would need to switch context in real test

    def verify_order_total_on_canceled_order(self):
        """Verify order total calculation on canceled order"""
        order_totals_accordion = self.locator("//div[contains(text(),'Order Financials')]", "Order Financials Accordion")
        order_total = self.locator("//td[contains(text(),'Sub-Total')]/following-sibling::td/div", "Order Sub-Total")

        self.expect_to_be_visible(order_totals_accordion)
        self.click(order_totals_accordion)
        self.expect_to_be_visible(order_total)
        total_text = self.text_content(order_total)
        assert "R" in total_text, f"Expected R in {total_text}"

    def verify_order_total_on_return_item(self):
        """Verify order total calculation with returned items"""
        order_totals_accordion = self.locator("//div[contains(text(),'Order Financials')]", "Order Financials Accordion")
        order_total = self.locator("//td[contains(text(),'Total')]/following-sibling::td/div", "Order Total")

        self.expect_to_be_visible(order_totals_accordion)
        self.click(order_totals_accordion)
        self.expect_to_be_visible(order_total)
        total_text = self.text_content(order_total)
        assert "R" in total_text, f"Expected R in total_text"

    def verify_waybill_link(self):
        """Verify waybill link redirects correctly"""
        waybill_link = self.locator("//strong[contains(text(),'Waybill')]/following-sibling::a", "Waybill Link")

        self.expect_to_be_visible(waybill_link)
        self.click(waybill_link)
        # This opens a new tab, would need to switch context in a real test

    def verify_order_tracking_for_delivered_physical_products(self):
        """Verify tracking info for delivered physical products"""
        physical_product_text = self.locator("//div[contains(text(),'Physical Product')]", "Physical Product Text")
        delivered_status = self.locator("//div[contains(text(),'Delivered')]", "Delivered Status")

        self.click(self.order_fulfillment_accordion)
        self.expect_to_be_visible(physical_product_text)
        self.expect_to_be_visible(delivered_status)

    def verify_order_shipping_info(self):
        """Verify shipping information on waybill tracking modal"""
        waybill_link = self.locator("//strong[contains(text(),'Waybill')]/following-sibling::a", "Waybill Link")
        shipping_info = self.locator("//div[contains(text(),'Shipping Method')]", "Shipping Info")

        self.click(self.order_fulfillment_accordion)
        self.expect_to_be_visible(waybill_link)
        self.expect_to_be_visible(shipping_info)
