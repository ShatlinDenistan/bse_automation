from playwright.sync_api import Page
from base.page_base import PageBase

# Locators for Deposit Match page
content_large_icon = ("//i[@aria-hidden='true' and @class='content large icon']", "Content Large Icon")
deposit_match_link = ("//body/div[@id='root']/div[1]/a[3]", "Deposit Match Link")
batches_heading = ("//h1[contains(text(),'Batches')]", "Batches Heading")
batch_download = ("//tbody/tr[1]/td[10]/div[1]/button[1]/i[1]", "Batch Download Button")
apply_filter = ("//button[contains(text(),'Apply Filter')]", "Apply Filter Button")
clear_filter = ("//button[contains(text(),'Clear Filter')]", "Clear Filter Button")
date_filter = ("//input[@name='dateRange']", "Date Filter Input")
batch_date = ("//td[contains(text(),'12-May-2023')]", "Batch Date")
payment_method_list = ("//tbody/tr[1]/td[5]", "Payment Method List")
payment_method_dropdown = ("//div[contains(text(),'Select payment method')]", "Payment Method Dropdown")
payfast_list = ("//span[contains(text(),'PayFast')]", "PayFast List")
customer_name_label = ("//th[contains(text(),'Customer Name')]", "Customer Name Label")
page_two_nav = ("//body/div[@id='root']/div[3]/div[1]/div[1]/table[1]/tfoot[1]/tr[1]/th[1]/div[1]/div[6]/div[2]/a[2]", "Page Two Navigation")
item_list_dropdown = ("//div[contains(text(),'Show 15 Items')]", "Item List Dropdown")
list_filter_30 = ("//span[contains(text(),'30')]", "List Filter 30")
list_filter_10 = ("//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[5]/div[1]/div[2]/div[1]", "List Filter 10")
refresh_button = ("//body/div[@id='root']/div[3]/div[1]/div[1]/div[4]/button[1]", "Refresh Button")
error_message = ("//*[contains(text(),'Error')]", "Error Message")
criteria_dropdown = ("//div[contains(text(),'Criteria')]", "Criteria Dropdown")
deposit_match_search = ("//input[@name='searchTerm']", "Deposit Match Search")
order_id_option = ("//span[contains(text(),'Order ID')]", "Order ID Option")
statement_amount_option = ("//span[contains(text(),'Statement Amount')]", "Statement Amount Option")
customer_id_option = ("//span[contains(text(),'Customer ID')]", "Customer ID Option")
customer_name_option = ("//span[contains(text(),'Customer Name')]", "Customer Name Option")
batch_id_option = ("//span[contains(text(),'Batch ID')]", "Batch ID Option")
order_no_text = ("//tbody/tr[1]/td[2]/a[1]", "Order Number Text")
cust_name_text = ("//tbody/tr[1]/td[3]/a[1]", "Customer Name Text")
statem_amount_text = ("//tbody/tr[1]/td[6]", "Statement Amount Text")
customer_name_link = ("//tbody/tr[1]/td[3]/a[1]", "Customer Name Link")
check_order = ("//*[@id='root']/div[3]/div/div/table/tbody/tr[2]/td[1]/div", "Check Order")
check_new_order = ("//*[@id='root']/div[3]/div/div/table/tbody/tr/td[1]/div", "Check New Order")
cancel_reason_dropdown = ("//div[@name='cancelReason']", "Cancel Reason Dropdown")
cancel_reason = ("//span[contains(text(),'Supplier out of stock')]", "Cancel Reason")
btn_cancel_order = ("//button[contains(text(),'Cancel Order')]", "Cancel Order Button")
btn_confirm_cancel_order = ("//button[contains(text(),'Cancel Orders')]", "Confirm Cancel Order Button")
btn_authorise_order = ("//button[contains(text(),'Authorise Order')]", "Authorise Order Button")
verify_authorise_order = ("//div[contains(text(),'Successfully processed 1 item(s)')]", "Verify Authorise Order")
txt_criteria_search = ("//input[@name='searchTerm' and @type='text']", "Criteria Search Text")
batch_id_value = ("//tbody/tr[1]/td[2]/a[1]", "Batch ID Value")
match_status = ("//div[@name='matchStatus' and @role='listbox']", "Match Status")
close_filter_button = ("//i[@aria-hidden='true' and @class='dropdown icon clear']", "Close Filter Button")
close_icon = ("//i[@aria-hidden='true' and @class='close icon']", "Close Icon")
remove_order = ("//button[contains(text(),'Remove Order')]", "Remove Order Button")
order_number_checkbox = ("//tbody/tr[1]/td[1]", "Order Number Checkbox")
order_number_text = ("//tbody/tr[1]/td[2]", "Order Number Text")
btn_unclaimed_payment = ("//button[contains(text(),'Unclaimed Payment')]", "Unclaimed Payment Button")
unclaimed_payments_tab = ("//a[contains(text(),'Unclaimed Payments ')]", "Unclaimed Payments Tab")
order_not_found = ("//span[contains(text(),'Order Not Found')]", "Order Not Found")
amount_differ = ("//span[contains(text(),'Amount Differ')]", "Amount Differ")
auto_match = ("//span[contains(text(),'Auto Match')]", "Auto Match")
btn_upload_csv = ("//button[contains(text(),'Upload CSV')]", "Upload CSV Button")
select_statement_type = ("//div[@name='statementType' and @role='listbox']", "Select Statement Type")
btn_match = ("//tbody/tr[1]/td[10]/div[1]/button[1]", "Match Button")
txt_match_order_id = ("//input[@name='order_id' and @type='number']", "Match Order ID Input")
btn_match_submit = ("//button[@class='ui blue button' and @type='submit']", "Match Submit Button")

# Dynamic locators with format strings
batch_id_link = ("//a[@class='active section']", "Batch ID Link")
generic_option = ("//span[contains(text(),'{}')]", "Generic Option")
payment_method_option = ("//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]", "Payment Method")
upload_file_input = ("//input[@type='file']", "Upload File Input")
upload_button = ("//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[1]", "Upload Button")
order_id_link = ("//a[contains(text(),'{}')]", "Order ID Link")
send_email_button = ("//button[contains(text(),'Send Email')]", "Send Email Button")
submit_email_button = ("//button[@class='ui blue button' and @type='submit']", "Submit Email Button")
success_message = ("//div[contains(text(),'Successfully processed 1 item(s)')]", "Success Message")
file_uploaded = ("//span[contains(text(),'{}')]", "File Uploaded")
all_batches_link = ("//a[contains(text(),'All Batches')]", "All Batches Link")


class DepositMatchPage(PageBase):
    """Page object for Deposit Match functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.content_large_icon = self.locator(content_large_icon)
        self.deposit_match_link = self.locator(deposit_match_link)
        self.batches_heading = self.locator(batches_heading)
        self.batch_download = self.locator(batch_download)
        self.apply_filter = self.locator(apply_filter)
        self.clear_filter = self.locator(clear_filter)
        self.date_filter = self.locator(date_filter)
        self.batch_date = self.locator(batch_date)
        self.payment_method_list = self.locator(payment_method_list)
        self.payment_method_dropdown = self.locator(payment_method_dropdown)
        self.payfast_list = self.locator(payfast_list)
        self.customer_name_label = self.locator(customer_name_label)
        self.page_two_nav = self.locator(page_two_nav)
        self.item_list_dropdown = self.locator(item_list_dropdown)
        self.list_filter_30 = self.locator(list_filter_30)
        self.list_filter_10 = self.locator(list_filter_10)
        self.refresh_button = self.locator(refresh_button)
        self.error_message = self.locator(error_message)
        self.criteria_dropdown = self.locator(criteria_dropdown)
        self.deposit_match_search = self.locator(deposit_match_search)
        self.order_id_option = self.locator(order_id_option)
        self.statement_amount_option = self.locator(statement_amount_option)
        self.customer_id_option = self.locator(customer_id_option)
        self.customer_name_option = self.locator(customer_name_option)
        self.batch_id_option = self.locator(batch_id_option)
        self.order_no_text = self.locator(order_no_text)
        self.cust_name_text = self.locator(cust_name_text)
        self.statem_amount_text = self.locator(statem_amount_text)
        self.customer_name_link = self.locator(customer_name_link)
        self.check_order = self.locator(check_order)
        self.check_new_order = self.locator(check_new_order)
        self.cancel_reason_dropdown = self.locator(cancel_reason_dropdown)
        self.cancel_reason = self.locator(cancel_reason)
        self.btn_cancel_order = self.locator(btn_cancel_order)
        self.btn_confirm_cancel_order = self.locator(btn_confirm_cancel_order)
        self.btn_authorise_order = self.locator(btn_authorise_order)
        self.verify_authorise_order = self.locator(verify_authorise_order)
        self.txt_criteria_search = self.locator(txt_criteria_search)
        self.batch_id_value = self.locator(batch_id_value)
        self.match_status = self.locator(match_status)
        self.close_filter_button = self.locator(close_filter_button)
        self.close_icon = self.locator(close_icon)
        self.remove_order = self.locator(remove_order)
        self.order_number_checkbox = self.locator(order_number_checkbox)
        self.order_number_text = self.locator(order_number_text)
        self.btn_unclaimed_payment = self.locator(btn_unclaimed_payment)
        self.unclaimed_payments_tab = self.locator(unclaimed_payments_tab)
        self.order_not_found = self.locator(order_not_found)
        self.amount_differ = self.locator(amount_differ)
        self.auto_match = self.locator(auto_match)
        self.btn_upload_csv = self.locator(btn_upload_csv)
        self.select_statement_type = self.locator(select_statement_type)
        self.btn_match = self.locator(btn_match)
        self.txt_match_order_id = self.locator(txt_match_order_id)
        self.btn_match_submit = self.locator(btn_match_submit)
        self.batch_id_link = self.locator(batch_id_link)
        self.payment_method_option = self.locator(payment_method_option)
        self.upload_file_input = self.locator(upload_file_input)
        self.upload_button = self.locator(upload_button)
        self.send_email_button = self.locator(send_email_button)
        self.submit_email_button = self.locator(submit_email_button)
        self.success_message = self.locator(success_message)
        self.all_batches_link = self.locator(all_batches_link)

    def get_generic_option(self, option_text: str):
        """Get locator for a specific generic option"""
        return self.locator((generic_option[0].format(option_text), f"{option_text} Option"))

    def get_order_id_link(self, order_id: str):
        """Get locator for a specific order ID link"""
        return self.locator((order_id_link[0].format(order_id), f"Order ID {order_id} Link"))

    def get_file_uploaded_span(self, filename: str):
        """Get locator for uploaded file span"""
        return self.locator((file_uploaded[0].format(filename), f"{filename} Uploaded"))

    def navigate_to_deposit_match(self):
        """Navigate to Deposit Match page"""
        self.click(self.content_large_icon)
        self.click(self.deposit_match_link)
        self.expect_to_be_visible(self.batches_heading)

    def go_to_deposit_match_page(self):
        """Go to Deposit Match page"""
        self.click(self.deposit_match_link)
        self.expect_to_be_visible(self.batches_heading)

    def upload_valid_deposit_match_file(self, csv_file):
        """Upload a valid deposit match CSV file"""
        self.click(self.btn_upload_csv)
        self.click(self.select_statement_type)
        generic = self.get_generic_option("Generic")
        self.click(generic)
        self.click(self.payment_method_dropdown)
        self.click(self.payment_method_option)
        self.fill(self.upload_file_input, csv_file)
        self.click(self.upload_button)
        self.wait_for_seconds(15)
        batch_id = self.text_content(self.batch_id_link)
        return batch_id

    def upload_invalid_deposit_match_file(self, deposit_match_file):
        """Upload an invalid deposit match CSV file"""
        self.click(self.btn_upload_csv)
        self.click(self.select_statement_type)
        self.click(self.get_generic_option("GENERIC GLOBAL 1.csv"))
        self.fill(self.upload_file_input, deposit_match_file)
        self.expect_to_be_visible(self.get_file_uploaded_span("GENERIC GLOBAL 1.csv"))
        self.click(self.upload_button)

    def verify_csv_error_occurred(self):
        """Verify that a CSV error occurred"""
        error_text = self.text_content(self.error_message)
        assert error_text == "Error Occurred", f"Expected 'Error Occurred' but got '{error_text}'"

    def download_batch_file(self):
        """Download the batch file"""
        self.click(self.batch_download)

    def click_the_refresh_button(self):
        """Click the refresh button and wait for records to load"""
        self.wait_for_seconds(15)
        self.click(self.refresh_button)
        self.expect_to_be_visible(self.customer_name_label, timeout=40000)
        batch_id = self.text_content(self.batch_id_link)
        return batch_id

    def click_show_items_dropdown_and_select_30_items(self):
        """Click show items dropdown and select 30 items"""
        self.click(self.item_list_dropdown)
        self.click(self.list_filter_30)

    def navigate_to_second_page(self):
        """Navigate to the second page"""
        self.click(self.page_two_nav)
        self.expect_to_be_visible(self.customer_name_label)

    def click_the_select_payment_method_dropdown_and_select_payfast_and_apply_filter(self):
        """Click payment method dropdown, select PayFast, and apply filter"""
        self.click(self.payment_method_dropdown)
        self.click(self.payfast_list)
        self.click(self.apply_filter)

    def verify_that_batches_are_filtered_by_payment_method(self):
        """Verify that batches are filtered by payment method"""
        self.expect_to_be_visible(self.payment_method_list)
        payment_method_text = self.text_content(self.payment_method_list)
        assert "PayFast" in payment_method_text, f"Expected 'PayFast' in '{payment_method_text}'"

    def click_the_clear_filter_button(self):
        """Click the clear filter button"""
        self.click(self.clear_filter)

    def click_the_select_date_range_field_and_select_date_from_the_previous_week(self):
        """Click date range field and select a previous week date"""
        self.fill(self.date_filter, "01-05-2023 - 12-05-2023")
        self.click(self.apply_filter)
        self.expect_to_be_visible(self.batch_date)

    def click_on_existing_batch(self):
        """Click on an existing batch"""
        batch_id_header = self.locator(("//th[contains(text(),'Batch Id')]", "Batch ID Header"))
        self.click(batch_id_header)
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Enter")

    def click_the_criteria_dropdown_list_and_select_order_id(self):
        """Click criteria dropdown and select Order ID"""
        self.click(self.criteria_dropdown)
        self.click(self.order_id_option)

    def enter_order_id_on_searchbox_and_apply_filter(self):
        """Enter order ID on searchbox and apply filter"""
        order_id = self.text_content(self.order_no_text)
        customer_name = self.text_content(self.cust_name_text)
        amount = self.text_content(self.statem_amount_text)
        self.fill(self.deposit_match_search, order_id)
        self.click(self.apply_filter)
        self.expect_to_be_visible(self.get_order_id_link(order_id))
        self.click(self.clear_filter)
        return order_id, customer_name, amount

    def click_the_criteria_dropdown_list_and_select_statement_amount(self):
        """Click criteria dropdown and select Statement Amount"""
        self.click(self.criteria_dropdown)
        self.click(self.statement_amount_option)

    def enter_statement_amount_on_searchbox_and_apply_filter(self, amount):
        """Enter statement amount on searchbox and apply filter"""
        self.fill(self.deposit_match_search, amount)
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_the_criteria_dropdown_list_and_select_customer_id(self):
        """Click criteria dropdown and select Customer ID"""
        self.click(self.criteria_dropdown)
        self.click(self.customer_id_option)

    def enter_customer_id_on_searchbox_and_apply_filter(self):
        """Enter customer ID on searchbox and apply filter"""
        self.fill(self.deposit_match_search, "2571878")
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_the_criteria_dropdown_list_and_select_customer_name(self):
        """Click criteria dropdown and select Customer Name"""
        self.click(self.criteria_dropdown)
        self.click(self.customer_name_option)

    def enter_customer_name_on_searchbox_and_apply_filter(self, customer_name):
        """Enter customer name on searchbox and apply filter"""
        self.fill(self.deposit_match_search, customer_name)
        self.click(self.apply_filter)
        self.click(self.customer_name_link)

    def select_authorised_order_and_cancel(self):
        """Select authorized order and cancel it"""
        self.expect_to_be_visible(self.check_new_order)
        self.click(self.check_new_order)
        self.click(self.btn_cancel_order)
        self.click(self.cancel_reason_dropdown)
        self.click(self.cancel_reason)
        self.click(self.btn_confirm_cancel_order)

    def select_batch_with_authorised_orders(self):
        """Select batch with authorized orders"""
        self.go_to_page("all_batches/2007")

    def select_new_order_and_authorise(self):
        """Select new order and authorize"""
        self.expect_to_be_visible(self.check_new_order)
        self.click(self.check_new_order)
        self.click(self.btn_authorise_order)
        self.expect_to_be_visible(self.verify_authorise_order)

    def select_authorised_order_and_authorise(self):
        """Select authorized order and authorize"""
        self.expect_to_be_visible(self.check_order)
        self.click(self.check_order)
        self.click(self.btn_authorise_order)
        self.expect_to_be_visible(self.verify_authorise_order)

    def click_match_status_dropdown_and_select_auto_match(self):
        """Click match status dropdown and select Auto Match"""
        self.click(self.match_status)
        self.click(self.auto_match)
        self.click(self.apply_filter)
        # Check that "AUTO MATCH" text appears on the page
        self.page.content().find("AUTO MATCH")
        self.click(self.clear_filter)

    def click_match_status_dropdown_and_select_amount_differ(self):
        """Click match status dropdown and select Amount Differ"""
        self.click(self.match_status)
        self.click(self.amount_differ)
        self.click(self.apply_filter)
        # Check that "Amount Differ" text appears on the page
        self.page.content().find("Amount Differ")
        self.click(self.close_filter_button)

    def click_match_status_dropdown_and_select_order_not_found(self):
        """Click match status dropdown and select Order Not Found"""
        self.click(self.match_status)
        self.click(self.order_not_found)
        self.click(self.apply_filter)
        # Check that "Order Not Found" text appears on the page
        self.page.content().find("Order Not Found")

    def click_the_unclaimed_payment_tab(self):
        """Click the unclaimed payment tab"""
        self.click(self.unclaimed_payments_tab)

    def click_criteria_dropdown_list_and_select_customer_name(self):
        """Click criteria dropdown and select Customer Name"""
        self.click(self.criteria_dropdown)
        self.click(self.customer_name_option)

    def enter_customer_name_and_apply_filter(self):
        """Enter customer name and apply filter"""
        self.fill(self.txt_criteria_search, "Jack")
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_criteria_dropdown_list_and_select_order_id(self):
        """Click criteria dropdown and select Order ID"""
        self.click(self.criteria_dropdown)
        self.click(self.order_id_option)

    def enter_order_id_and_apply_filter(self):
        """Enter order id and apply filter"""
        self.fill(self.txt_criteria_search, "972479")
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_criteria_dropdown_list_and_select_statement_amount(self):
        """Click criteria dropdown and select Statement Amount"""
        self.click(self.criteria_dropdown)
        self.click(self.statement_amount_option)

    def enter_statement_amount_and_apply_filter(self):
        """Enter statement amount and apply filter"""
        self.fill(self.txt_criteria_search, "592.00")
        self.click(self.apply_filter)
        # Check that "R 592.00" text appears on the page
        self.page.content().find("R 592.00")
        self.click(self.clear_filter)

    def click_criteria_dropdown_list_and_select_batch_id(self):
        """Click criteria dropdown and select Batch ID"""
        self.click(self.criteria_dropdown)
        self.click(self.batch_id_option)

    def enter_batch_id_and_apply_filter(self):
        """Enter batch id and apply filter"""
        self.fill(self.txt_criteria_search, "1905")
        self.click(self.apply_filter)
        self.expect_to_be_visible(self.batch_id_value)
        batch_id_text = self.text_content(self.batch_id_value)
        assert "1905" in batch_id_text, f"Expected '1905' in '{batch_id_text}'"
        self.click(self.clear_filter)

    def click_checkbox_next_to_first_order_in_the_batch(self):
        """Click checkbox next to first order in the batch"""
        self.click(self.order_number_checkbox)
        unclaimed_order_id = self.text_content(self.order_number_text)
        return unclaimed_order_id

    def click_the_unclaimed_payment_button(self):
        """Click the unclaimed payment button"""
        self.click(self.btn_unclaimed_payment)
        self.click(self.close_icon)

    def navigate_to_unclaimed_payment_page(self):
        """Navigate to unclaimed payment page"""
        self.click(self.all_batches_link)
        self.page.content().find("All Batches")

    def enter_unclaimed_payment_order_id_and_apply_filter(self, unclaimed_order_id):
        """Enter unclaimed payment order id and apply filter"""
        self.fill(self.txt_criteria_search, unclaimed_order_id)
        self.click(self.apply_filter)
        self.expect_to_be_visible(self.get_order_id_link(unclaimed_order_id))
        self.click(self.clear_filter)

    def click_the_remove_order_button(self):
        """Click the remove order button"""
        self.click(self.remove_order)
        self.click(self.close_icon)

    def click_the_match_button_and_type_in_the_order_id(self, order_id):
        """Click the match button and type in the order ID"""
        self.click(self.btn_match)
        self.expect_to_be_visible(self.txt_match_order_id)
        self.fill(self.txt_match_order_id, order_id)

    def click_the_match_button_and_close_modal(self):
        """Click the match button and close modal"""
        self.click(self.btn_match_submit)
        self.page.content().find("Form data posted successfully")
        self.click(self.close_icon)

    def navigate_to_all_batches(self, batch_id):
        """Navigate to all batches"""
        self.click(self.all_batches_link)
        self.page.content().find("All Batches")
        self.expect_to_be_visible(self.get_order_id_link(batch_id))

    def click_send_email_button_and_send_email(self):
        """Click send email button and send email"""
        self.click(self.send_email_button)
        self.click(self.submit_email_button)
        self.expect_to_be_visible(self.success_message)
        self.click(self.close_icon)