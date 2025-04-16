import pytest
from base.test_base import TestBase


@pytest.mark.ui
class TestEditOrder(TestBase):
    """Tests for Edit Order functionality in the Financial Portal."""

    @pytest.mark.EditOrder
    @pytest.mark.Regression
    @pytest.mark.QABA_546
    def test_update_payment_method(self):
        """Verify that a user can update payment method on an Authorized order."""
        self.step("Get orders from database using paygate sql")
        order_details = self.database.get_orders_from_database(self.database.paygate_sql)

        self.step("Search for the order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigate to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Update payment method")
        self.edit_order_page.update_payment_method()

        self.step("Verify that payment method difference warning banner displays")
        warning_text = self.edit_order_page.verify_that_payment_method_difference_warning_banner_displays()
        assert warning_text, "Payment method warning banner was not displayed"

        self.step("Verify that an admin note for payment method update")
        admin_note = self.edit_order_page.verify_that_an_admin_note_for_payment_method_update()
        assert "Payment method updated" in admin_note, "Admin note for payment method update was not displayed"

    @pytest.mark.EditOrder
    @pytest.mark.Regression
    @pytest.mark.QABA_546
    def test_add_discount_amount_greater_than_order_total_amount(self):
        """Verify that a user cannot apply discount amount more than order total amount."""
        self.step("Get orders from database with no discount amount")
        order_details = self.database.get_orders_from_database(self.database.new_order_with_no_discount_amount_sql)

        self.step("Search for the order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigate to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Calculate discount amount input value greater than order total")
        discount_amount = self.edit_order_page.calculate_discount_amount_input_value([self.database.order_total] if self.database.order_total else ["100"])

        self.step("Verify that invalid discount amount message is displayed")
        error_message = self.edit_order_page.verify_that_invalid_discount_amount_message()
        assert "Discount amount cannot exceed the order item total" in error_message, "Invalid discount message not displayed"

    @pytest.mark.EditOrder
    @pytest.mark.Regression
    @pytest.mark.QABA_532
    @pytest.mark.QABA_536
    def test_add_discount_and_shipping_amounts(self):
        """Verify that applying discount and shipping fee to a new order updates the Order's Auth Amount."""
        self.step("Get orders from database with no discount and shipping amount")
        order_details = self.database.get_orders_from_database(self.database.new_order_with_no_discount_and_shipping_amount_sql)

        self.step("Search for the order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigate to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Add shipping fee and discount amounts")
        discount_amount, shipping_fee = self.edit_order_page.add_shipping_fee_and_discount_amounts()

        self.step("Verify that discount and shipping amounts are added to order financials")
        shipping_amount, discount_amount = self.edit_order_page.verify_that_discount_and_shipping_amounts_are_added_to_order_financials()
        assert shipping_amount and discount_amount, "Shipping and/or discount amounts not added to order financials"

        self.step("Verify discount and shipping fee update admin notes")
        discount_note, shipping_note = self.edit_order_page.verify_discount_and_shipping_fee_update_admin_notes()
        assert "Discount applied" in discount_note, "Discount admin note not found"
        assert "Shipping fee applied" in shipping_note, "Shipping fee admin note not found"

        self.step("Verify discount and shipping fee update audit logs")
        action_type, data = self.edit_order_page.verify_discount_and_shipping_fee_update_audit_logs()
        assert "edit_order" in action_type, "Audit log action type is incorrect"
        assert "discount_update" in data and "shipping_update" in data, "Audit log data is missing updates"

    @pytest.mark.EditOrder
    @pytest.mark.Regression
    @pytest.mark.QABA_544
    def test_order_item_update_to_shipped(self):
        """Verify that a user can update an order items stauts from Returned Canceled to Shipped."""
        self.step("Get orders from database with returned canceled order item")
        order_details = self.database.get_orders_from_database(self.database.order_with_returned_canceled_order_item_sql)

        self.step("Search for the order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigate to update to shipped screen")
        self.edit_order_page.navigate_to_update_to_shipped_screen()

        self.step("Update order item status from returned canceled to shipped")
        message_text = self.edit_order_page.update_order_item_status_from_returned_canceled_to_shipped()
        assert "Update status for order" in message_text, "Update status message not displayed correctly"

        self.step("Verify update from return canceled to shipped admin note and audit log entry")
        admin_note, action_type = self.edit_order_page.verify_update_from_return_canceled_to_shipped_admin_note_and_audit_log_entry()
        assert "status updated from Return Canceled to Shipped" in admin_note, "Admin note for update not found"
        assert "update_order_item_to_shipped" in action_type, "Audit log action type is incorrect"

    @pytest.mark.EditOrder
    @pytest.mark.Regression
    @pytest.mark.QABA_534
    def test_update_shipping_amount(self):
        """Verify that updating the shipping amount and the order total."""
        self.step("Get orders from database with discount and shipping amounts")
        order_details = self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        self.step("Search for the order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigate to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Update shipping amount")
        self.edit_order_page.update_shipping_amount()

        self.step("Verify that the shipping amount is updated on order financials")
        shipping_amount = self.edit_order_page.verify_that_the_shipping_amount_is_updated_on_order_financials()
        assert shipping_amount == "75.00", f"Shipping amount not updated correctly. Expected 75.00, got {shipping_amount}"

    @pytest.mark.EditOrder
    @pytest.mark.Regression
    @pytest.mark.QABA_543
    def test_payment_method_options(self):
        """Verify that the Payment Method drop-down list has all the available payment methods."""
        self.step("Search for order 98278540")
        self.search_page.search_for_order("98278540")

        self.step("Navigate to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Verify that payment method options are displayed")
        payment_options = self.edit_order_page.verify_that_payment_method_options_are_displayed()

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

        for option in expected_options:
            assert option in payment_options, f"Payment method option '{option}' not found"
