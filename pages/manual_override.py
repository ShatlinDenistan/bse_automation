from pos.manual_override_po import ManualOverridePO


class ManualOverridePage(ManualOverridePO):
    """Page class for Manual Override functionality"""

    def verify_page_loaded(self):
        """Verify that the manual override page is loaded"""
        self.step("Verifying manual override page is loaded")
        return self.is_visible(self.manual_override_header)

    def search_order(self, order_number):
        """Search for an order by order number"""
        self.step("Searching for order")
        self.fill(self.order_number_input, order_number)
        self.click(self.search_button)
        self.wait_till_page_is_loaded()

    def select_order_type(self, order_type):
        """Select order type from dropdown"""
        self.step("Selecting order type")
        self.select_option(self.order_type_dropdown, order_type)

    def select_order_status(self, status):
        """Select order status from dropdown"""
        self.step("Selecting order status")
        self.select_option(self.order_status_dropdown, status)

    def apply_override(self):
        """Apply the manual override"""
        self.step("Applying manual override")
        self.click(self.apply_button)
        self.wait_till_page_is_loaded()
        if self.is_visible(self.confirm_modal):
            self.click(self.confirm_ok_button)
            self.wait_till_page_is_loaded()

    def cancel_override(self):
        """Cancel the manual override"""
        self.step("Canceling manual override")
        self.click(self.cancel_button)
        self.wait_till_page_is_loaded()

    def add_notes(self, notes_text):
        """Add notes to the order"""
        self.step("Adding notes to the order")
        self.fill(self.notes_textarea, notes_text)

    def verify_order_exists(self):
        """Verify that the order exists in the table"""
        self.step("Verifying order exists in the table")
        return self.is_visible(self.order_rows)

    def get_order_count(self):
        """Get the number of orders in the table"""
        self.step("Getting order count")
        return self.order_rows.count()
