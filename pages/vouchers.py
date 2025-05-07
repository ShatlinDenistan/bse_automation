from playwright.sync_api import expect

from pos.vouchers_po import VouchersPO


class VouchersPage(VouchersPO):
    """Vouchers page class with all voucher-related actions"""

    def __init__(self, page):
        super().__init__(page)
        self.voucher_code_text = None

    def navigate_to_vouchers(self):
        """Navigate to the vouchers page"""
        self.click(self.menu_btn)
        self.click(self.vouchers_menu_option)
        expect(self.results_table).to_be_visible()

    def filter_by_redeemed_and_paid_status(self):
        """Filter vouchers by redeemed and paid status"""
        expect(self.results_table).to_be_visible()
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_available)
        self.click(self.paid_status_dropdown)
        self.click(self.paid_status_option)
        self.click(self.apply_search_filter)

        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all redeemed status elements contain "Available"
        redeemed_status_elements = self.page.locator(self.all_order_status_columns)
        count = redeemed_status_elements.count()
        for i in range(count):
            expect(redeemed_status_elements.nth(i)).to_contain_text("Available")

        # Verify all paid status elements contain "True"
        paid_status_elements = self.page.locator(self.all_order_paid_columns)
        count = paid_status_elements.count()
        for i in range(count):
            expect(paid_status_elements.nth(i)).to_contain_text("True")

    def select_and_cancel_a_voucher(self):
        """Select and cancel a voucher"""
        self.click(self.order_id_checkbox)
        self.click(self.expire_btn)
        expect(self.verification_message).to_be_visible()
        self.click(self.close_icon)

    def filter_by_canceled_redeem_status(self):
        """Filter vouchers by canceled redeem status"""
        expect(self.results_table).to_be_visible()
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_cancelled)
        self.click(self.apply_search_filter)

        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all redeemed status elements contain "Cancelled"
        redeemed_status_elements = self.page.locator(self.all_order_status_columns)
        count = redeemed_status_elements.count()
        for i in range(count):
            expect(redeemed_status_elements.nth(i)).to_contain_text("Cancelled")

    def select_and_activate_a_voucher(self):
        """Select and activate a canceled voucher"""
        self.voucher_code_text = self.get_text(self.voucher_code)

        self.click(self.order_id_checkbox)
        self.click(self.active_btn)
        self.click(self.active_voucher_btn)
        expect(self.verify_activated_voucher).to_be_visible()
        self.click(self.close_icon)

    def verify_voucher_status(self):
        """Verify the status of a voucher after activation"""
        expect(self.clear_filter).to_be_visible(timeout=30000)
        self.scroll_to_element(self.clear_filter)
        self.click(self.clear_filter)

        expect(self.filter_by_field).to_be_visible()
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)

        self.fill(self.search_term_field, self.voucher_code_text)
        self.click(self.apply_search_filter)
        expect(self.voucher_status).to_contain_text("Available")

    def filter_by_not_paid_status(self):
        """Filter vouchers by not paid status"""
        expect(self.results_table).to_be_visible()
        self.click(self.paid_status_dropdown)
        self.click(self.not_paid_status_option)
        self.click(self.apply_search_filter)

        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all paid status elements contain "False"
        paid_status_elements = self.page.locator(self.all_order_paid_columns)
        count = paid_status_elements.count()
        for i in range(count):
            expect(paid_status_elements.nth(i)).to_contain_text("False")

    def select_and_update_to_paid(self):
        """Select and update a voucher to paid status"""
        self.voucher_code_text = self.get_text(self.voucher_code)
        self.click(self.order_id_checkbox)
        self.click(self.paid_btn)
        expect(self.verification_message).to_be_visible()
        self.click(self.close_icon)

        expect(self.clear_filter).to_be_visible(timeout=30000)
        self.scroll_to_element(self.clear_filter)
        self.click(self.clear_filter)

        expect(self.filter_by_field).to_be_visible()
        self.click(self.menu_btn)
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)

        self.fill(self.search_term_field, self.voucher_code_text)
        self.click(self.apply_search_filter)
        expect(self.paid_status).to_contain_text("True")

    def filter_by_paid_status(self):
        """Filter vouchers by paid status"""
        expect(self.results_table).to_be_visible()
        self.click(self.paid_status_dropdown)
        self.click(self.paid_status_option)
        self.click(self.apply_search_filter)

        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all paid status elements contain "True"
        paid_status_elements = self.page.locator(self.all_order_paid_columns)
        count = paid_status_elements.count()
        for i in range(count):
            expect(paid_status_elements.nth(i)).to_contain_text("True")

    def select_and_update_to_not_paid(self):
        """Select and update a voucher to not paid status"""
        self.voucher_code_text = self.get_text(self.voucher_code)
        self.click(self.order_id_checkbox)
        self.click(self.not_paid_btn)
        expect(self.verification_message).to_be_visible()
        self.click(self.close_icon)

        expect(self.clear_filter).to_be_visible(timeout=30000)
        self.scroll_to_element(self.clear_filter)
        self.click(self.clear_filter)

        expect(self.filter_by_field).to_be_visible()
        self.click(self.menu_btn)
        self.click(self.filter_by_field)
        self.click(self.filter_by_voucher_code)

        self.fill(self.search_term_field, self.voucher_code_text)
        self.click(self.apply_search_filter)
        expect(self.paid_status).to_contain_text("False")

    def filter_by_date_range(self):
        """Filter vouchers by date range"""
        self.click(self.clear_filter)
        self.click(self.date_filter)
        self.fill(self.date_filter, "01-05-2024 - 31-05-2024")
        self.click(self.apply_filter_btn)

        # Check that all dates contain May-2024
        rows = self.get_table_data()
        for row in rows:
            # Assuming 3rd column (index 2) contains date
            assert "May-2024" in row[2], f"Date {row[2]} does not contain May-2024"

    def filter_by_voucher_category(self):
        """Filter vouchers by voucher category"""
        expect(self.results_table).to_be_visible()
        self.click(self.voucher_category_dropdown)
        self.click(self.voucher_category_cv)
        self.click(self.apply_search_filter)

        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all voucher category elements contain "Corporate Voucher"
        voucher_category_elements = self.page.locator(self.voucher_category_list)
        count = voucher_category_elements.count()
        for i in range(count):
            expect(voucher_category_elements.nth(i)).to_contain_text("Corporate Voucher")

    def filter_by_redeemed_status(self):
        """Filter vouchers by redeemed status"""
        expect(self.results_table).to_be_visible()
        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_redeemed)
        self.click(self.apply_search_filter)

        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all redeemed status elements contain "Redeemed"
        redeemed_status_elements = self.page.locator(self.redeemed_status_list)
        count = redeemed_status_elements.count()
        for i in range(count):
            expect(redeemed_status_elements.nth(i)).to_contain_text("Redeemed")

    def filter_by_multiple_filter_options(self):
        """Filter vouchers by multiple filter options"""
        expect(self.results_table).to_be_visible()
        self.click(self.date_filter)
        self.fill(self.date_filter, "01-05-2024 - 31-05-2024")

        self.click(self.voucher_category_dropdown)
        self.click(self.voucher_category_cv)

        self.click(self.redeemed_status_dropdown)
        self.click(self.redeemed_status_cancelled)

        self.click(self.paid_status_dropdown)
        self.click(self.paid_status_option)

        self.click(self.apply_search_filter)
        expect(self.results_table).to_be_visible(timeout=30000)

        # Verify all redeemed status elements contain "Cancelled"
        redeemed_status_elements = self.page.locator(self.redeemed_status_list)
        count = redeemed_status_elements.count()
        for i in range(count):
            expect(redeemed_status_elements.nth(i)).to_contain_text("Cancelled")

        # Verify all voucher category elements contain "Corporate Voucher"
        voucher_category_elements = self.page.locator(self.voucher_category_list)
        count = voucher_category_elements.count()
        for i in range(count):
            expect(voucher_category_elements.nth(i)).to_contain_text("Corporate Voucher")

        # Check that all dates contain May-2024
        rows = self.get_table_data()
        for row in rows:
            # Assuming 3rd column (index 2) contains date
            assert "May-2024" in row[2], f"Date {row[2]} does not contain May-2024"

        # Verify all paid status elements contain "True"
        paid_status_elements = self.page.locator(self.all_order_paid_columns)
        count = paid_status_elements.count()
        for i in range(count):
            expect(paid_status_elements.nth(i)).to_contain_text("True")

    def filter_using_order_id(self):
        """Filter vouchers using order ID"""
        order_id = self.get_text(self.voucher_order_id)
        self.click(self.filter_by_field)
        self.click(self.search_criteria_option_order_id)
        self.fill(self.search_term_field, order_id)
        self.click(self.apply_filter_btn)

        # Get table data and verify order ID in each row
        table_data = self.get_table_data()
        for row in table_data:
            # Assuming 2nd column (index 1) contains order ID
            assert order_id in row[1], f"Order ID {order_id} not found in {row[1]}"

    def filter_by_voucher_code(self):
        """Filter vouchers by voucher code"""
        voucher_code = self.get_text(self.voucher_code_id)
        self.click(self.filter_by_field)
        self.click(self.filter_voucher_code)
        self.fill(self.search_term_field, voucher_code)
        self.click(self.apply_filter_btn)

        # Get table data and verify voucher code in each row
        table_data = self.get_table_data()
        for row in table_data:
            # Assuming 6th column (index 5) contains voucher code
            assert voucher_code in row[5], f"Voucher code {voucher_code} not found in {row[5]}"

    def filter_using_customer_id(self):
        """Filter vouchers using customer ID"""
        customer_name = self.get_text(self.open_customer_info)
        self.click(self.open_customer_info)
        self.wait_for_seconds(2)

        # Switch to new window
        pages = self.page.context.pages
        customer_page = pages[-1]
        customer_id = customer_page.locator(self.customer_info_id).text_content()
        customer_page.close()

        self.click(self.filter_by_field)
        self.click(self.filter_by_customer_id)
        self.fill(self.search_term_field, customer_id)
        self.click(self.apply_filter_btn)

        # Check if customer name appears in the results
        customer_elements = self.page.locator(self.open_customer_info)
        count = customer_elements.count()
        for i in range(count):
            expect(customer_elements.nth(i)).to_contain_text(customer_name)

    def filter_by_used_by_customer_id(self):
        """Filter vouchers by used by customer ID"""
        customer_name = self.get_text(self.open_used_by_customer_info)
        self.click(self.open_used_by_customer_info)
        self.wait_for_seconds(2)

        # Switch to new window
        pages = self.page.context.pages
        customer_page = pages[-1]
        customer_id = customer_page.locator(self.customer_info_id).text_content()
        customer_page.close()

        self.click(self.filter_by_field)
        self.click(self.filter_used_by_customer_id)
        self.fill(self.search_term_field, customer_id)
        self.click(self.apply_filter_btn)

        # Check if customer name appears in the results
        customer_elements = self.page.locator(self.open_used_by_customer_info)
        count = customer_elements.count()
        for i in range(count):
            expect(customer_elements.nth(i)).to_contain_text(customer_name)

    def select_and_send_email(self):
        """Select a voucher and send an email"""
        expect(self.order_id_checkbox).to_be_visible()
        self.click(self.order_id_checkbox)
        expect(self.email_btn).to_be_visible()
        self.click(self.email_btn)

    def verify_email_was_sent_successfully(self):
        """Verify that an email was sent successfully"""
        self.get_text(self.email_sent_modal)
        self.wait_for_seconds(2)

        # Check for success message
        success_message = self.page.locator("//div[contains(text(),'Successfully processed')]")
        expect(success_message).to_be_visible()

        self.click(self.email_sent_modal_close_icon)

    def get_voucher_table_data(self):
        """Helper method to get table data"""
        return self.get_table_data(table_xpath=self.results_table)
