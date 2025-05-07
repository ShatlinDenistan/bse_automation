from playwright.sync_api import expect

from pos.deposit_match_po import DepositMatchPO


class DepositMatchPage(DepositMatchPO):

    def navigate_to_deposit_match(self):
        """Navigate to the Deposit Match page"""
        self.click(self.content_icon)
        self.click(self.deposit_match_link)
        expect(self.batches_heading).to_be_visible()

    def go_to_deposit_match_page(self):
        """Go to Deposit Match page"""
        self.click(self.deposit_match_link)
        expect(self.batches_heading).to_be_visible()

    def upload_valid_deposit_match_file(self, csv_file):
        """Upload a valid deposit match file"""
        self.click(self.btn_upload_csv)
        self.click(self.select_statement_type)
        self.click(self.generic_option)
        self.click(self.payment_method_dropdown)
        self.click(self.payment_method_option)
        self.file_input.set_input_files(csv_file)
        self.click(self.upload_button)
        self.wait_for_seconds(15)
        batch_id = self.get_text(self.batch_id_active_section)
        return batch_id

    def upload_invalid_deposit_match_file(self, deposit_match_file):
        """Upload an invalid deposit match file"""
        self.click(self.btn_upload_csv)
        self.click(self.select_statement_type)
        self.click(self.page.locator("//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[7]/span[1]"))
        self.file_input.set_input_files(deposit_match_file)
        expect(self.page.locator("//span[contains(text(),'GENERIC GLOBAL 1.csv')]")).to_be_visible()
        self.click(self.page.locator("//button[@class='ui blue compact right floated button']"))

    def verify_csv_error_occurred(self):
        """Verify that an error occurred with the CSV"""
        error_text = self.get_text(self.error_message)
        assert error_text == "Error Occurred", f"Expected 'Error Occurred', but got '{error_text}'"

    def download_batch_file(self):
        """Download the batch file"""
        self.click(self.batch_download)

    def click_the_refresh_button(self):
        """Click refresh button and wait for records to display"""
        self.wait_for_seconds(15)
        self.click(self.refresh_button)
        expect(self.customer_name_lbl).to_be_visible(timeout=40000)
        batch_id = self.get_text(self.batch_id_active_section)
        return batch_id

    def click_show_items_dropdown_and_select_30_items(self):
        """Click show items dropdown and select 30 items"""
        self.click(self.item_list_ddl)
        self.click(self.list_filter_30)

    def navigate_to_second_page(self):
        """Navigate to the second page"""
        self.click(self.page_two_nav)
        expect(self.customer_name_lbl).to_be_visible()

    def click_the_select_payment_method_dropdown_and_select_payfast_and_apply_filter(self):
        """Select PayFast from payment method dropdown and apply filter"""
        self.click(self.payment_method_ddl)
        self.click(self.payfast_lst)
        self.click(self.apply_filter)

    def verify_that_batches_are_filtered_by_payment_method(self):
        """Verify that batches are filtered by payment method"""
        expect(self.payment_method_lst).to_contain_text("PayFast")

    def click_the_clear_filter_button(self):
        """Click the clear filter button"""
        self.click(self.clear_filter)

    def click_the_select_date_range_field_and_select_date_from_the_previous_week(self):
        """Select date range and apply filter"""
        self.fill(self.date_filter, "01-05-2023 - 12-05-2023")
        self.click(self.apply_filter)
        expect(self.batch_date).to_be_visible(timeout=30000)

    def click_on_existing_batch(self):
        """Click on existing batch"""
        self.click(self.batch_id_header)
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Enter")

    def click_the_criteria_dropdown_list_and_select_orderid(self):
        """Click criteria dropdown and select Order ID"""
        self.click(self.criteria_dropdown)
        self.click(self.order_id_dm)

    def enter_order_id_on_searchbox_and_apply_filer(self):
        """Enter order ID on searchbox and apply filter"""
        order_id = self.get_text(self.order_no_text)
        customer_name = self.get_text(self.cust_name_text)
        amount = self.get_text(self.statem_amount_text)

        self.fill(self.deposit_match_search, order_id)
        self.click(self.apply_filter)
        expect(self.page.locator(f"//a[contains(text(),'{order_id}')]")).to_be_visible()
        self.click(self.clear_filter)

        return order_id, customer_name, amount

    def click_the_criteria_dropdown_list_and_select_statement_amount(self):
        """Click criteria dropdown and select Statement Amount"""
        self.click(self.criteria_dropdown)
        self.click(self.statement_amount_dm)

    def enter_statement_amount_on_searchbox_and_apply_filer(self, amount):
        """Enter statement amount on searchbox and apply filter"""
        self.fill(self.deposit_match_search, amount)
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_the_criteria_dropdown_list_and_select_customer_id(self):
        """Click criteria dropdown and select Customer ID"""
        self.click(self.criteria_dropdown)
        self.click(self.customer_id_dm)

    def enter_customer_id_on_searchbox_and_apply_filer(self):
        """Enter Customer ID on searchbox and apply filter"""
        self.fill(self.deposit_match_search, "2571878")
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_the_criteria_dropdown_list_and_select_customer_name(self):
        """Click criteria dropdown and select Customer Name"""
        self.click(self.criteria_dropdown)
        self.click(self.customer_name_dm)

    def enter_customer_name_on_searchbox_and_apply_filer(self, customer_name):
        """Enter Customer name on searchbox and apply filter"""
        self.fill(self.deposit_match_search, customer_name)
        self.click(self.apply_filter)
        self.click(self.customer_name_link)

    def select_authorised_order_and_cancel(self):
        """Select authorized order and cancel it"""
        expect(self.chk_new_order).to_be_enabled(timeout=30000)
        self.click(self.chk_new_order)
        self.click(self.btn_cancel_order)
        self.click(self.cancel_reason_dropdown)
        self.click(self.cancel_reason)
        self.click(self.btn_confirm_cancel_order)

    def select_batch_with_authorised_orders(self):
        """Go to the batch with authorized orders"""
        self.page.goto("http://fin-portal.master.env/all_batches/2007")

    def select_batch_with_new_status_orders(self, order_ids):
        """Select batch with new status orders"""

        self.order_data.get_orders(self.order_queries.new_order_ebucks_cc_sql)
        order_id_string = str(order_ids[0])

        with open(self.test_data_files.deposit_match_new_order_file, "w", encoding="utf-8") as f:
            f.write('"Description,Amount"\n')
            f.write(f"{order_id_string},100")

        # Upload file
        self.click(self.btn_upload_csv)
        self.click(self.select_statement_type)
        self.click(self.generic_option)
        self.click(self.payment_method_dropdown)
        self.click(self.payment_method_option)
        self.file_input.set_input_files(self.test_data_files.deposit_match_new_order_file)
        self.click(self.upload_button)

        batch_id = self.get_text(self.batch_id_active_section)
        return batch_id

    def select_new_order_and_authorise(self):
        """Select new order and authorize it"""
        expect(self.chk_new_order).to_be_enabled(timeout=30000)
        self.click(self.chk_new_order)
        self.click(self.btn_authorise_order)
        expect(self.verify_authorise_order).to_be_visible()

    def select_authorised_order_and_authorise(self):
        """Select authorized order and authorize it"""
        expect(self.chk_order).to_be_enabled(timeout=30000)
        self.click(self.chk_order)
        self.click(self.btn_authorise_order)
        expect(self.verify_authorise_order).to_be_visible()

    def click_match_status_dropdown_and_select_auto_match(self):
        """Click match status dropdown and select Auto Match"""
        self.click(self.match_status)
        self.click(self.auto_match)
        self.click(self.apply_filter)
        expect(self.page.get_by_text("AUTO MATCH")).to_be_visible()
        self.click(self.clear_filter)

    def click_match_status_dropdown_and_select_amount_differ(self):
        """Click match status dropdown and select Amount Differ"""
        self.click(self.match_status)
        self.click(self.amount_differ)
        self.click(self.apply_filter)
        expect(self.page.get_by_text("Amount Differ")).to_be_visible()
        self.click(self.close_filter_button)

    def click_match_status_dropdown_and_select_order_not_found(self):
        """Click match status dropdown and select Order Not Found"""
        self.click(self.match_status)
        self.click(self.order_not_found)
        self.click(self.apply_filter)
        expect(self.page.get_by_text("Order Not Found")).to_be_visible()

    def click_the_unclaimed_payment_tab(self):
        """Click the Unclaimed Payment tab"""
        self.click(self.unclaimed_payments_tab)

    def click_criteria_dropdown_list_and_select_customer_name(self):
        """Click criteria dropdown and select Customer Name"""
        self.click(self.criteria_dropdown)
        self.click(self.customer_name_dm)

    def enter_customer_name_and_apply_filter(self):
        """Enter customer name and apply filter"""
        self.fill(self.txt_criteria_search, "Jack")
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_criteria_dropdown_list_and_select_order_id(self):
        """Click criteria dropdown and select Order ID"""
        self.click(self.criteria_dropdown)
        self.click(self.order_id_dm)

    def enter_order_id_and_apply_filter(self):
        """Enter order ID and apply filter"""
        self.fill(self.txt_criteria_search, "972479")
        self.click(self.apply_filter)
        self.click(self.clear_filter)

    def click_criteria_dropdown_list_and_select_statement_amount(self):
        """Click criteria dropdown and select Statement Amount"""
        self.click(self.criteria_dropdown)
        self.click(self.statement_amount_dm)

    def enter_statement_amount_and_apply_filter(self):
        """Enter statement amount and apply filter"""
        self.fill(self.txt_criteria_search, "592.00")
        self.click(self.apply_filter)
        expect(self.page.get_by_text("R 592.00")).to_be_visible()
        self.click(self.clear_filter)

    def click_criteria_dropdown_list_and_select_batch_id(self):
        """Click criteria dropdown and select Batch ID"""
        self.click(self.criteria_dropdown)
        self.click(self.batch_id)

    def enter_batch_id_and_apply_filter(self):
        """Enter batch ID and apply filter"""
        self.fill(self.txt_criteria_search, "1905")
        self.click(self.apply_filter)
        expect(self.batch_id_value).to_contain_text("1905")
        self.click(self.clear_filter)

    def click_checkbox_next_to_first_order_in_the_batch(self):
        """Click checkbox next to first order in the batch"""
        self.click(self.order_number_checkbox)
        unclaimed_order_id = self.get_text(self.order_number_text)
        return unclaimed_order_id

    def click_the_unclaimed_payment_button(self):
        """Click the Unclaimed Payment button"""
        self.click(self.btn_unclaimed_payment)
        self.click(self.close_icon)

    def navigate_to_unclaimed_payment_page(self):
        """Navigate to the Unclaimed Payment page"""
        self.click(self.page.locator("//a[contains(text(),'Unclaimed Payments')]"))
        expect(self.page.get_by_text("All Batches")).to_be_visible()

    def enter_unclaimed_payment_order_id_and_apply_filter(self, unclaimed_order_id):
        """Enter unclaimed payment order ID and apply filter"""
        self.fill(self.txt_criteria_search, unclaimed_order_id)
        self.click(self.apply_filter)
        expect(self.page.locator(f"//a[contains(text(),'{unclaimed_order_id}')]")).to_be_visible()
        self.click(self.clear_filter)

    def click_the_remove_order_button(self):
        """Click the Remove Order button"""
        self.click(self.remove_order)
        self.click(self.close_icon)

    def click_the_match_button_and_type_in_the_order_id(self, order_id):
        """Click the Match button and type in the order ID"""
        self.click(self.btn_match)
        expect(self.txt_match_order_id).to_be_visible()
        self.fill(self.txt_match_order_id, order_id)

    def click_the_match_button_and_close_modal(self):
        """Click the Match button and close modal"""
        self.click(self.btn_match_submit)
        expect(self.page.get_by_text("Form data posted successfully")).to_be_visible()
        self.click(self.close_icon)

    def navigate_to_all_batches(self, batch_id):
        """Navigate to All Batches"""
        self.click(self.all_batches_link)
        expect(self.page.get_by_text("All Batches")).to_be_visible()
        expect(self.page.locator(f"//a[contains(text(),'{batch_id}')]")).to_be_visible()

    def click_send_email_button_and_send_email(self):
        """Click Send Email button and send email"""
        self.click(self.send_email_button)
        self.click(self.page.locator("//button[@class='ui blue button' and @type='submit']"))
        expect(self.page.locator("//div[contains(text(),'Successfully processed 1 item(s)')]")).to_be_visible()
        self.click(self.close_icon)
