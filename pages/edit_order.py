import random
from playwright.sync_api import expect

from pos.edit_order_po import EditOrderPO


class EditOrderPage(EditOrderPO):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to_edit_order_screen(self):
        """Navigate to the Edit Order screen."""
        expect(self.black_ellipsis).to_be_visible()
        self.hover(self.black_ellipsis)
        self.click(self.edit_order_menu_option)

    def update_payment_method(self):
        """Update the payment method randomly."""
        expect(self.payment_method_dropdown).to_be_visible()
        self.click(self.payment_method_dropdown)
        random_number = random.randint(3, 8)
        for _ in range(random_number):
            self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.click(self.update_button)

    def verify_that_an_admin_note_for_payment_method_update(self):
        """Verify that an admin note for the payment method update is visible."""
        expect(self.payment_method_update_admin_note).to_be_visible()
        return self.payment_method_update_admin_note.is_visible()

    def verify_that_payment_method_difference_warning_banner_displays(self):
        """Verify that the payment method difference warning banner displays."""
        self.wait_for_seconds(1)
        expect(self.payment_method_warning_banner).to_be_visible()
        return self.payment_method_warning_banner.is_visible()

    def calculate_discount_amount_input_value(self, order_total):
        """Calculate and input discount amount exceeding the order total."""
        # Get Current Order Total Amount
        order_total_amount = float(order_total[0])

        # Add 500 to Current Order Total to create Discount Amount
        add_discount_amount = order_total_amount + 500

        # Type calculated Discount Amount into Discount field and submit
        expect(self.discount_amount).to_be_visible()
        self.fill(self.discount_amount, str(add_discount_amount))
        self.click(self.update_button)

    def verify_that_invalid_discount_amount_message(self):
        """Verify that an invalid discount amount message is displayed."""
        expect(self.invalid_discount_amount).to_be_visible()
        invalid_discount_amount_text = self.text_content(self.invalid_discount_amount)
        assert "Discount amount cannot exceed the order item total of" in invalid_discount_amount_text
        return invalid_discount_amount_text

    def add_shipping_fee_and_discount_amounts(self):
        """Add random shipping fee and discount amounts."""
        # Random discount amount between 5 and 10
        random_discount_amount = random.randint(5, 10)

        # Choose a shipping fee among the 3 shipping fee amounts
        shipping_fees = [65, 200, 30]
        random_shipping_fee = random.choice(shipping_fees)

        # Send the random values to the input fields
        expect(self.discount_amount).to_be_visible()
        self.fill(self.discount_amount, str(random_discount_amount))

        expect(self.shipping_amount).to_be_visible()
        self.fill(self.shipping_amount, str(random_shipping_fee))
        self.click(self.update_button)

        return random_discount_amount, random_shipping_fee

    def verify_discount_and_shipping_fee_update_admin_notes(self):
        """Verify discount and shipping fee update admin notes are visible."""
        self.wait_for_seconds(1)
        assert self.discount_applied_admin_note.is_visible(), "Discount applied admin note is not visible"
        assert self.shipping_fee_applied_admin_note.is_visible(), "Shipping fee applied admin note is not visible"

    def verify_discount_and_shipping_fee_update_audit_logs(self):
        """Verify discount and shipping fee updates in the audit logs."""
        self.wait_for_seconds(5)
        expect(self.black_ellipsis).to_be_visible()
        self.hover(self.black_ellipsis)
        expect(self.audit_log_menu_option).to_be_visible()
        self.click(self.audit_log_menu_option)

        self.wait_for_seconds(1)
        # Get Audit Log entry action type
        expect(self.audit_log_edit_order_action_type).to_be_visible()
        action_type = self.text_content(self.audit_log_edit_order_action_type)
        # Verify Action Type Equals to Edit Order
        assert "edit_order" in action_type

        # Get Audit Log entry data
        data = self.text_content(self.audit_log_edit_order_data)
        # Verify Edit Order Data
        assert "updated_values" in data
        assert "discount_update" in data
        assert "shipping_update" in data

        return action_type, data

    def verify_that_discount_and_shipping_amounts_are_added_to_order_financials(self):
        """Verify that discount and shipping amounts are added to order financials."""
        expect(self.order_financials_accordion).to_be_visible()
        self.click(self.order_financials_accordion)

        # Verify Shipping is added
        shipping_amount_text = self.text_content(self.order_financials_shipping_amount)
        shipping_amount = shipping_amount_text.replace("R ", "")

        # Verify Discount is added
        discount_amount_text = self.text_content(self.order_financials_discount_amount)
        discount_amount = discount_amount_text.replace("R ", "")

        return shipping_amount, discount_amount

    def navigate_to_update_to_shipped_screen(self):
        """Navigate to the Update To Shipped screen."""
        expect(self.return_canceled_order_item_menu).to_be_visible()
        self.click(self.return_canceled_order_item_menu)
        self.click(self.update_to_shipped_menu_option)

    def update_order_item_status_from_returned_canceled_to_shipped(self):
        """Update order item status from Returned Canceled to Shipped."""
        expect(self.update_to_shipped_menu_option).to_be_visible()

        message_text = self.text_content(self.update_to_shipped_modal_message)
        assert "Update status for order" in message_text
        self.click(self.update_to_shipped_button)

    def verify_update_from_return_canceled_to_shipped_admin_note_and_audit_log_entry(self):
        """Verify admin note and audit log entry for update from Return Canceled to Shipped."""
        self.wait_for_seconds(1)
        # Verify Admin Note has been added
        assert self.update_to_shipped_admin_note.is_visible()

        # Verify the update to shipped audit log
        self.wait_for_seconds(10)
        expect(self.black_ellipsis).to_be_visible()
        self.hover(self.black_ellipsis)
        expect(self.audit_log_menu_option).to_be_visible()
        self.click(self.audit_log_menu_option)

        # Get Audit Log entry action type
        self.wait_for_seconds(10)
        expect(self.audit_log_edit_order_action_type).to_be_visible()
        action_type = self.text_content(self.audit_log_edit_order_action_type)
        # Verify Action Type Equals to Edit Order
        assert "update_order_item_to_shipped" in action_type

        return action_type

    def verify_that_both_shipping_and_discount_disabled_fields_are_on_edit_order_screen(self):
        """Verify that both shipping and discount disabled fields are on Edit Order screen."""
        assert not self.discount_amount.is_visible(), "Discount amount field should not be visible"
        assert not self.shipping_amount.is_visible(), "Shipping amount field should not be visible"
        assert self.discount_amount_disabled_field.is_visible(), "Discount amount disabled field should be visible"
        assert self.shipping_fee_disabled_field.is_visible(), "Shipping fee disabled field should be visible"

    def update_shipping_amount(self):
        """Update the shipping amount."""
        expect(self.shipping_amount).to_be_visible()
        self.fill(self.shipping_amount, "75")
        self.click(self.update_button)

    def verify_that_the_shipping_amount_is_updated_on_order_financials(self):
        """Verify that the shipping amount is updated on order financials."""
        expect(self.order_financials_accordion).to_be_visible()
        self.click(self.order_financials_accordion)

        shipping_amount_text = self.text_content(self.order_financials_shipping_amount)
        shipping_amount = shipping_amount_text.replace("R ", "")

        assert shipping_amount == "75.00", f"Expected shipping amount to be 75.00, but got {shipping_amount}"
        return shipping_amount

    def update_discount_amount(self):
        """Update the discount amount."""
        expect(self.discount_amount).to_be_visible()
        self.fill(self.discount_amount, "10")
        self.click(self.update_button)

    def verify_that_the_discount_amount_is_updated_on_order_financials(self):
        """Verify that the discount amount is updated on order financials."""
        expect(self.order_financials_accordion).to_be_visible()
        self.click(self.order_financials_accordion)

        discount_amount_text = self.text_content(self.order_financials_discount_amount)
        discount_amount = discount_amount_text.replace("R ", "")

        assert discount_amount == "10.00", f"Expected discount amount to be 10.00, but got {discount_amount}"
        return discount_amount

    def verify_that_payment_method_options_are_displayed(self):
        """Verify that payment method options are displayed."""
        expected_options = [
            "COD",
            "Credit Card",
            "Credit Card Token",
            "MasterPass",
            "PayFast",
            "iPay",
            "OneVoucher",
            "eBucks",
            "Discovery Miles",
            "Mobicred",
            "NSFAS Wallet | Celbux eVoucher",
            "Deposit",
            "Credit",
            "Payflex",
            "Nedbank Personal Loan",
            "TakealotCredit",
        ]

        self.click(self.payment_method_dropdown)
        payment_options_text = self.text_content(self.payment_method_dropdown)
        actual_options = [option.strip() for option in payment_options_text.split("\n") if option.strip() and option.strip() != "-- none --"]

        assert sorted(actual_options) == sorted(expected_options), f"Expected {expected_options}, but got {actual_options}"
        return actual_options
