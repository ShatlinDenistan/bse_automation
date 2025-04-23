import pytest
from base.test_base import TestBase


class TestEditOrder(TestBase):
    """Test class for Edit Order functionality."""

    @pytest.mark.QABA_546
    def test_update_payment_method(self):
        """Verify that a user can update payment method on an Authorized order."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Get orders from database")
        self.utils.database_utils.get_orders_from_database(self.config.PAYGATE_SQL)

        self.step("Search for order")
        self.utils.search_for_order(self.order_ids[0])

        self.step("Navigate to Edit Order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Update payment method")
        self.edit_order_page.update_payment_method()

        self.step("Verify payment method difference warning banner displays")
        assert self.edit_order_page.verify_that_payment_method_difference_warning_banner_displays()

        self.step("Verify admin note for payment method update")
        assert self.edit_order_page.verify_that_an_admin_note_for_payment_method_update()

    @pytest.mark.QABA_546
    def test_add_discount_amount_greater_than_order_total_amount(self):
        """Verify that a user cannot apply discount amount more than order total amount."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Get orders from database")
        self.utils.database_utils.get_orders_from_database(self.config.NEW_ORDER_WITH_NO_DISCOUNT_AMOUNT_SQL)

        self.step("Search for order")
        self.utils.search_for_order(self.order_ids[0])

        self.step("Navigate to Edit Order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Calculate and input discount amount exceeding order total")
        self.edit_order_page.calculate_discount_amount_input_value(self.order_total)

        self.step("Verify invalid discount amount message")
        error_message = self.edit_order_page.verify_that_invalid_discount_amount_message()
        assert "Discount amount cannot exceed the order item total of" in error_message

    @pytest.mark.QABA_532
    @pytest.mark.QABA_536
    def test_add_discount_and_shipping_amounts(self):
        """Verify that applying discount and shipping fee to a new order updates the Order's Auth Amount."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Get orders from database")
        self.utils.database_utils.get_orders_from_database(self.config.NEW_ORDER_WITH_NO_DISCOUNT_AND_SHIPPING_AMOUNT_SQL)

        self.step("Search for order")
        self.utils.search_for_order(self.order_ids[0])

        self.step("Navigate to Edit Order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Add shipping fee and discount amounts")
        discount_amount, shipping_fee = self.edit_order_page.add_shipping_fee_and_discount_amounts()

        self.step("Verify discount and shipping amounts are added to order financials")
        shipping_amount, discount_amount = self.edit_order_page.verify_that_discount_and_shipping_amounts_are_added_to_order_financials()

        self.step("Verify discount and shipping fee update admin notes")
        self.edit_order_page.verify_discount_and_shipping_fee_update_admin_notes()

        self.step("Verify discount and shipping fee update audit logs")
        action_type, data = self.edit_order_page.verify_discount_and_shipping_fee_update_audit_logs()
        assert "edit_order" in action_type
        assert "updated_values" in data
        assert "discount_update" in data
        assert "shipping_update" in data

    @pytest.mark.QABA_544
    def test_order_item_update_to_shipped(self):
        """Verify that a user can update an order items status from Returned Canceled to Shipped."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Get orders from database")
        self.utils.database_utils.get_orders_from_database(self.config.ORDER_WITH_RETURNED_CANCELED_ORDER_ITEM_SQL)

        self.step("Search for order")
        self.utils.search_for_order(self.order_ids[0])

        self.step("Navigate to Update To Shipped screen")
        self.edit_order_page.navigate_to_update_to_shipped_screen()

        self.step("Update order item status from Returned Canceled to Shipped")
        self.edit_order_page.update_order_item_status_from_returned_canceled_to_shipped()

        self.step("Verify update from Return Canceled to Shipped admin note and audit log entry")
        action_type = self.edit_order_page.verify_update_from_return_canceled_to_shipped_admin_note_and_audit_log_entry()
        assert "update_order_item_to_shipped" in action_type

    @pytest.mark.QABA_534
    def test_update_shipping_amount(self):
        """Verify that updating the shipping amount and the order total."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Get orders from database")
        self.utils.database_utils.get_orders_from_database(self.config.NEW_ORDER_WITH_DISCOUNT_AND_SHIPPING_AMOUNTS_SQL)

        self.step("Search for order")
        self.utils.search_for_order(self.order_ids[0])

        self.step("Navigate to Edit Order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Update shipping amount")
        self.edit_order_page.update_shipping_amount()

        self.step("Verify that the shipping amount is updated on order financials")
        shipping_amount = self.edit_order_page.verify_that_the_shipping_amount_is_updated_on_order_financials()
        assert shipping_amount == "75.00"

    @pytest.mark.QABA_543
    def test_payment_method_options(self):
        """Verify that the Payment Method drop-down list has all the available payment methods."""

        self.step("Login to Fin-Portal")
        self.login_page.login_finance_portal()

        self.step("Search for order")
        self.utils.search_for_order("98278540")

        self.step("Navigate to Edit Order screen")
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
        assert sorted(payment_options) == sorted(expected_options)
