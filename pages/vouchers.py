from playwright.sync_api import Page
from base.page_base import PageBase

# Locators as tuples with (xpath, description)
menu_btn = ("//i[@aria-hidden='true' and @class='content large icon']", "Menu Button")
vouchers_menu_option = ("//body/div[@id='root']/div[1]/a[2]", "Vouchers Menu Option")
results_table = ("//*[@class='ui small celled compact table']", "Results Table")
redeemed_status_dropdown = ("//*[@id='root']/div[3]/div/div/div/form/div/div/div[4]/div/div/div[1]", "Redeemed Status Dropdown")
redeemed_status_available = ("//span[text()='Available']", "Available Status Option")
redeemed_status_cancelled = ("//span[text()='Cancelled']", "Cancelled Status Option")
redeemed_status_redeemed = ("//span[text()='Redeemed']", "Redeemed Status Option")
paid_status_dropdown = ("//*[@id='root']/div[3]/div/div/div/form/div/div/div[5]/div/div", "Paid Status Dropdown")
paid_status_option = ("//span[text()='Paid']", "Paid Option")
not_paid_status_option = ("//span[text()='Not Paid']", "Not Paid Option")
apply_search_filter = ("//button[contains(text(), 'Filter')]", "Apply Filter Button")
order_id_checkbox = ("//*[@id='root']/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div", "First Order ID Checkbox")
expire_btn = ("//*[@id='root']/div[3]/div/div/div/table/tfoot/tr/th/div/div[3]/button", "Expire Button")
active_btn = ("//*[@id='root']/div[3]/div/div[2]/button", "Activate Button")
active_voucher_btn = ("//html/body/div[2]/div/div[2]/div/div[2]", "Confirm Activate Button")
verification_message = ("//div[contains(text(),'Successfully processed 1 item(s)')]", "Success Message")
close_icon = ("//i[@aria-hidden='true' and @class='close icon']", "Close Icon")
clear_filter = ("//button[contains(text(), 'Clear Filter')]", "Clear Filter Button")
filter_by_field = ("//div[@name='searchCriteria']", "Search Criteria Dropdown")
filter_by_voucher_code = ("//span[contains(text(), 'Voucher Code')]", "Voucher Code Filter Option")
search_term_field = ("//*[@name='searchTerm']", "Search Term Input")
voucher_code = ("//*[@id='root']/div[3]/div/div/div/table/tbody/tr[1]/td[6]/a", "Voucher Code")
voucher_status = ("//*[@id='root']/div[3]/div/div/div/table/tbody/tr/td[10]/div", "Voucher Status")
paid_btn = ("//*[@id='root']/div[3]/div/div/div/table/tfoot/tr/th/div/div[4]/button", "Paid Button")
not_paid_btn = ("//*[@id='root']/div[3]/div/div/div/table/tfoot/tr/th/div/div[5]/button", "Not Paid Button")
paid_status = ("//*[@id='root']/div[3]/div/div/div/table/tbody/tr/td[8]/div", "Paid Status")
date_filter = ("//input[@name='dateRange']", "Date Range Filter")
voucher_category_dropdown = ("//*[@id='root']/div[3]/div/div/div/form/div/div/div[3]/div", "Voucher Category Dropdown")
voucher_category_cv = ("//span[contains(text(), 'Corporate Voucher')]", "Corporate Voucher Option")
search_criteria_order_id = ("//span[contains(text(), 'Order ID')]", "Order ID Search Option")
filter_by_customer_id = ("//span[contains(text(), 'Customer ID')]", "Customer ID Filter Option")
open_customer_info = ("//*[@id='root']/div[3]/div/div/div/table/tbody/tr[1]/td[4]/a", "Customer Info Link")
open_used_by_customer_info = ("//*[@id='root']/div[3]/div/div/div/table/tbody/tr[1]/td[12]/a", "Used By Customer Info Link")
filter_by_used_by_customer_id = ("//span[contains(text(), 'Used By Customer ID')]", "Used By Customer ID Filter")
email_btn = ("//*[@class='mail icon']", "Email Button")
email_sent_modal = ("/html/body/div[2]/div", "Email Sent Modal")
email_sent_modal_close_icon = ("//body/div[2]/div[1]/i[1]", "Email Sent Modal Close Icon")

# Dynamic table column references
all_order_paid_columns = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 7)]", "All Paid Status Columns")
all_order_status_columns = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]", "All Order Status Columns")
voucher_category_list = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 4)]", "All Voucher Category Columns")
redeemed_status_list = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 9)]", "All Redeemed Status Columns")
voucher_order_id = ("//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]", "Order ID Column")


class VouchersPage(PageBase):
    """Page object for Vouchers functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Initialize locators
        self.menu_btn = self.locator(menu_btn)
        self.vouchers_menu_option = self.locator(vouchers_menu_option)
        self.results_table = self.locator(results_table)
        self.redeemed_status_dropdown = self.locator(redeemed_status_dropdown)
        self.redeemed_status_available = self.locator(redeemed_status_available)
        self.redeemed_status_cancelled = self.locator(redeemed_status_cancelled)
        self.redeemed_status_redeemed = self.locator(redeemed_status_redeemed)
        self.paid_status_dropdown = self.locator(paid_status_dropdown)
        self.paid_status_option = self.locator(paid_status_option)
        self.not_paid_status_option = self.locator(not_paid_status_option)
        self.apply_search_filter = self.locator(apply_search_filter)
        self.order_id_checkbox = self.locator(order_id_checkbox)
        self.expire_btn = self.locator(expire_btn)
        self.active_btn = self.locator(active_btn)
        self.active_voucher_btn = self.locator(active_voucher_btn)
        self.verification_message = self.locator(verification_message)
        self.close_icon = self.locator(close_icon)
        self.clear_filter = self.locator(clear_filter)
        self.filter_by_field = self.locator(filter_by_field)
        self.filter_by_voucher_code = self.locator(filter_by_voucher_code)
        self.search_term_field = self.locator(search_term_field)
        self.voucher_code = self.locator(voucher_code)
        self.voucher_status = self.locator(voucher_status)
        self.paid_btn = self.locator(paid_btn)
        self.not_paid_btn = self.locator(not_paid_btn)
        self.paid_status = self.locator(paid_status)
        self.date_filter = self.locator(date_filter)
        self.voucher_category_dropdown = self.locator(voucher_category_dropdown)
        self.voucher_category_cv = self.locator(voucher_category_cv)
        self.search_criteria_order_id = self.locator(search_criteria_order_id)
        self.filter_by_customer_id = self.locator(filter_by_customer_id)
        self.open_customer_info = self.locator(open_customer_info)
        self.open_used_by_customer_info = self.locator(open_used_by_customer_info)
        self.filter_by_used_by_customer_id = self.locator(filter_by_used_by_customer_id)
        self.email_btn = self.locator(email_btn)
        self.email_sent_modal = self.locator(email_sent_modal)
        self.email_sent_modal_close_icon = self.locator(email_sent_modal_close_icon)

        # Initialize dynamic table columns
        self.all_order_paid_columns = self.locator(all_order_paid_columns)
        self.all_order_status_columns = self.locator(all_order_status_columns)
        self.voucher_category_list = self.locator(voucher_category_list)
        self.redeemed_status_list = self.locator(redeemed_status_list)
        self.voucher_order_id = self.locator(voucher_order_id)

    def navigate_to_vouchers(self):
        """Navigate to the Vouchers page"""
        self.click(self.menu_btn)
        self.click(self.vouchers_menu_option)
        self.expect_to_be_visible(self.results_table)

    def filter_by_redeemed_and_paid_status(self):
        """Filter vouchers by Redeemed (Available) and Paid status"""
        self.expect_to_be_visible(self.results_table)
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_available)
        self.click(self.paid_status_dropdown)
        self.click(self.paid_status_option)
        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify statuses
        elements = self.all_order_status_columns.all()
        for element in elements:
            assert "Available" in element.text_content()

        elements = self.all_order_paid_columns.all()
        for element in elements:
            assert "True" in element.text_content()

    def select_and_cancel_voucher(self):
        """Select and cancel a voucher"""
        self.click(self.order_id_checkbox)
        self.click(self.expire_btn)
        self.expect_to_be_visible(self.verification_message)
        self.click(self.close_icon)

    def filter_by_canceled_redeem_status(self):
        """Filter vouchers by Cancelled status"""
        self.expect_to_be_visible(self.results_table)
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_cancelled)
        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify status
        elements = self.all_order_status_columns.all()
        for element in elements:
            assert "Cancelled" in element.text_content()

    def select_and_activate_voucher(self):
        """Select and activate a voucher"""
        voucher_code_text = self.get_text(self.voucher_code)
        self.voucher_code_text = voucher_code_text  # Store for later use

        self.click(self.order_id_checkbox)
        self.click(self.active_btn)
        self.click(self.active_voucher_btn)
        self.expect_to_be_visible(self.verification_message)
        self.click(self.close_icon)

    def verify_voucher_status(self):
        """Verify the voucher status after activation"""
        self.expect_to_be_visible(self.clear_filter)
        self.click(self.clear_filter)

        self.expect_to_be_visible(self.filter_by_field)
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)

        self.fill(self.search_term_field, self.voucher_code_text)
        self.click(self.apply_search_filter)
        assert "Available" in self.get_text(self.voucher_status)

    def filter_by_not_paid_status(self):
        """Filter vouchers by Not Paid status"""
        self.expect_to_be_visible(self.results_table)
        self.click(self.paid_status_dropdown)
        self.click(self.not_paid_status_option)
        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify status
        elements = self.all_order_paid_columns.all()
        for element in elements:
            assert "False" in element.text_content()

    def select_and_update_to_paid(self):
        """Select a voucher and update it to Paid status"""
        voucher_code_text = self.get_text(self.voucher_code)
        self.click(self.order_id_checkbox)
        self.click(self.paid_btn)
        self.expect_to_be_visible(self.verification_message)
        self.click(self.close_icon)

        self.expect_to_be_visible(self.clear_filter)
        self.click(self.clear_filter)

        self.expect_to_be_visible(self.filter_by_field)
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)

        self.fill(self.search_term_field, voucher_code_text)
        self.click(self.apply_search_filter)
        assert "True" in self.get_text(self.paid_status)

    def filter_by_paid_status(self):
        """Filter vouchers by Paid status"""
        self.expect_to_be_visible(self.results_table)
        self.click(self.paid_status_dropdown)
        self.click(self.paid_status_option)
        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify status
        elements = self.all_order_paid_columns.all()
        for element in elements:
            assert "True" in element.text_content()

    def select_and_update_to_not_paid(self):
        """Select a voucher and update it to Not Paid status"""
        voucher_code_text = self.get_text(self.voucher_code)
        self.click(self.order_id_checkbox)
        self.click(self.not_paid_btn)
        self.expect_to_be_visible(self.verification_message)
        self.click(self.close_icon)

        self.expect_to_be_visible(self.clear_filter)
        self.click(self.clear_filter)

        self.expect_to_be_visible(self.filter_by_field)
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)

        self.fill(self.search_term_field, voucher_code_text)
        self.click(self.apply_search_filter)
        assert "False" in self.get_text(self.paid_status)

    def filter_by_date_range(self):
        """Filter vouchers by date range"""
        self.click(self.clear_filter)
        self.click(self.date_filter)
        self.fill(self.date_filter, "01-05-2024 - 31-05-2024")
        self.click(self.apply_search_filter)

        # Verify dates in results
        elements = self.voucher_order_id.all()
        for element in elements:
            assert "May-2024" in element.text_content()

    def filter_by_voucher_category(self):
        """Filter vouchers by voucher category"""
        self.expect_to_be_visible(self.results_table)
        self.click(self.voucher_category_dropdown)
        self.click(self.voucher_category_cv)
        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify category
        elements = self.voucher_category_list.all()
        for element in elements:
            assert "Corporate Voucher" in element.text_content()

    def filter_by_multiple_filter_options(self):
        """Apply multiple filter options at once"""
        self.expect_to_be_visible(self.results_table)

        # Set date range
        self.click(self.date_filter)
        self.fill(self.date_filter, "01-05-2024 - 31-05-2024")

        # Set voucher category
        self.click(self.voucher_category_dropdown)
        self.click(self.voucher_category_cv)

        # Set redeemed status
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_cancelled)

        # Set paid status
        self.click(self.paid_status_dropdown)
        self.click(self.paid_status_option)

        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify all filters
        redeemed_elements = self.redeemed_status_list.all()
        for element in redeemed_elements:
            assert "Cancelled" in element.text_content()

        category_elements = self.voucher_category_list.all()
        for element in category_elements:
            assert "Corporate Voucher" in element.text_content()

        date_elements = self.voucher_order_id.all()
        for element in date_elements:
            assert "May-2024" in element.text_content()

        paid_elements = self.all_order_paid_columns.all()
        for element in paid_elements:
            assert "True" in element.text_content()

    def select_and_send_email(self):
        """Select a voucher and send email"""
        self.expect_to_be_visible(self.order_id_checkbox)
        self.click(self.order_id_checkbox)
        self.expect_to_be_visible(self.email_btn)
        self.click(self.email_btn)

    def verify_email_was_sent_successfully(self):
        """Verify that the email was sent successfully"""
        self.wait_for_seconds(2)
        self.expect_to_be_visible(self.email_sent_modal)
        email_text = self.text_content(self.email_sent_modal)
        assert "Successfully processed" in email_text
        self.click(self.email_sent_modal_close_icon)

    def filter_by_redeemed_status(self):
        """Filter vouchers by Redeemed status"""
        self.expect_to_be_visible(self.results_table)
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_redeemed)
        self.click(self.apply_search_filter)
        self.expect_to_be_visible(self.results_table)

        # Verify status
        elements = self.redeemed_status_list.all()
        for element in elements:
            assert "Redeemed" in element.text_content()

    def filter_using_order_id(self):
        """Filter vouchers by Order ID"""
        # Get the first order ID from the table
        order_id_text = self.get_text(self.voucher_order_id)

        # Apply filter
        self.click(self.filter_by_field)
        self.click(self.search_criteria_order_id)
        self.fill(self.search_term_field, order_id_text)
        self.click(self.apply_search_filter)

        # Verify results contain the order ID
        elements = self.voucher_order_id.all()
        for element in elements:
            assert order_id_text in element.text_content()

    def filter_by_voucher_code(self):
        """Filter vouchers by voucher code"""
        # Get voucher code from first row
        voucher_code_text = self.get_text(self.voucher_code)

        # Apply filter
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)
        self.fill(self.search_term_field, voucher_code_text)
        self.click(self.apply_search_filter)

        # Verify results
        result_voucher_code = self.get_text(self.voucher_code)
        assert voucher_code_text in result_voucher_code

    def filter_using_customer_id(self):
        """Filter vouchers by customer ID"""
        # Get customer info from first row
        customer_name = self.get_text(self.open_customer_info)
        self.click(self.open_customer_info)

        # Wait for customer info page to open in new tab and get customer ID
        self.page.wait_for_timeout(2000)  # Wait for new tab
        pages = self.page.context.pages
        customer_page = pages[-1]  # Get the last opened page

        # Extract customer ID from the page
        customer_id_element = customer_page.locator("//div[contains(@class, 'customer-id')]//span")
        customer_id = customer_page.evaluate("el => el.textContent", customer_id_element)

        # Close the customer info tab and go back to vouchers
        customer_page.close()
        self.page.bring_to_front()

        # Apply filter using customer ID
        self.click(self.filter_by_field)
        self.click(self.filter_by_customer_id)
        self.fill(self.search_term_field, customer_id)
        self.click(self.apply_search_filter)

        # Verify results
        result_customer = self.get_text(self.open_customer_info)
        assert customer_name in result_customer

    def filter_by_used_by_customer_id(self):
        """Filter vouchers by Used By Customer ID"""
        # Get used by customer info from first row
        customer_name = self.get_text(self.open_used_by_customer_info)
        self.click(self.open_used_by_customer_info)

        # Wait for customer info page to open in new tab and get customer ID
        self.page.wait_for_timeout(2000)  # Wait for new tab
        pages = self.page.context.pages
        customer_page = pages[-1]  # Get the last opened page

        # Extract customer ID from the page
        customer_id_element = customer_page.locator("//div[contains(@class, 'customer-id')]//span")
        customer_id = customer_page.evaluate("el => el.textContent", customer_id_element)

        # Close the customer info tab and go back to vouchers
        customer_page.close()
        self.page.bring_to_front()

        # Apply filter using used by customer ID
        self.click(self.filter_by_field)
        self.click(self.filter_by_used_by_customer_id)
        self.fill(self.search_term_field, customer_id)
        self.click(self.apply_search_filter)

        # Verify results
        result_customer = self.get_text(self.open_used_by_customer_info)
        assert customer_name in result_customer
