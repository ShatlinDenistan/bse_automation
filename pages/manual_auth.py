from pos.manual_auth_po import ManualAuthPO


class ManualAuthPage(ManualAuthPO):
    """Page class for Manual Authorization functionality"""

    def verify_page_loaded(self):
        """Verify that the manual authorization page is loaded"""
        self.step("Verifying manual authorization page is loaded")
        return self.is_visible(self.manual_auth_header)

    def search_order(self, order_id):
        """Search for an order by order ID"""
        self.step("Searching for order")
        self.fill(self.search_order_input, order_id)
        self.click(self.search_button)
        self.wait_till_page_is_loaded()

    def verify_order_exists(self):
        """Verify that the order exists in the table"""
        self.step("Verifying order exists in the table")
        return self.is_visible(self.order_rows)

    def select_order(self, order_index=0):
        """Select an order from the table by index"""
        self.step("Selecting order from the table")
        self.click(self.order_rows.nth(order_index))

    def authorize_order(self):
        """Authorize the selected order"""
        self.step("Authorizing order")
        self.click(self.authorize_button)
        self.wait_till_page_is_loaded()
        if self.is_visible(self.confirmation_modal):
            self.click(self.confirm_auth_button)
            self.wait_till_page_is_loaded()

    def reject_order(self, reason, comments=""):
        """Reject the selected order with reason and comments"""
        self.step("Rejecting order")
        self.click(self.reject_button)
        self.wait_till_page_is_loaded()

        self.select_option(self.reason_dropdown, reason)

        if comments:
            self.fill(self.comments_textarea, comments)

        self.click(self.confirm_auth_button)
        self.wait_till_page_is_loaded()

    def cancel_authorization(self):
        """Cancel the authorization process"""
        self.step("Canceling authorization")
        self.click(self.cancel_auth_button)
        self.wait_till_page_is_loaded()

    def confirm_success_message(self):
        """Confirm success message and close modal"""
        self.step("Confirming success message")
        is_visible = self.is_visible(self.confirmation_modal)
        if is_visible:
            self.click(self.modal_ok_button)
            self.wait_till_page_is_loaded()
        return is_visible

    def get_order_count(self):
        """Get the number of orders in the table"""
        self.step("Getting order count")
        return self.order_rows.count()
