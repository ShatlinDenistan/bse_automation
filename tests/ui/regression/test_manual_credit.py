"""Tests for Financial Portal Manual Credit functionality."""

import pytest
from base.test_base import TestBase


class TestManualCredit(TestBase):
    """Test class for Financial Portal Manual Credit functionality."""

    @pytest.mark.QABSE1339
    def test_add_credit_breach_credit_to_customer(self):
        """Verify that a user can successfully allocate Credit breach credit to a customer."""
        # Search for customer
        self.search_page.search_for_customer("100")

        # Add credit to customer
        self.customer_credit_page.expand_customer_credit_section_and_click_credit_button()
        self.order_credit_page.select_a_credit_reason("Credit breach")
        self.order_credit_page.enter_jira_number_for_credit_breach_reason()
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify credit is applied
        self.order_credit_page.verify_that_order_credit_is_applied(credit_amount)

    @pytest.mark.QABSE1339
    def test_validate_credit_breach_min_and_max_amount_rules(self):
        """Verify Credit breach credit reason min and max amount rules."""
        # Search for customer
        self.search_page.search_for_customer("100")

        # Test minimum amount validation
        self.customer_credit_page.expand_customer_credit_section_and_click_credit_button()
        self.order_credit_page.select_a_credit_reason("Credit breach")
        self.order_credit_page.enter_jira_number_for_credit_breach_reason()
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("10000001")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1354
    def test_add_goodwill_credit_to_order(self):
        """Verify that a user can successfully add Goodwill credit to an order."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Add goodwill credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Goodwill")
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify credit is applied
        self.order_credit_page.verify_that_order_credit_is_applied(credit_amount)

    @pytest.mark.QABSE1354
    def test_validate_goodwill_min_and_max_amount_rules(self):
        """Verify Goodwill credit reason min and max amount rules."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Test minimum amount validation
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Goodwill")
        self.order_credit_page.enter_invalid_min_amount("-1")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("800")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1344
    def test_add_late_delivery_fee_credit_to_order(self):
        """Verify that a user can successfully add Late Delivery Fee credit to an order."""
        # Get order from database
        self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Add late delivery fee credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Late delivery fee")
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify credit is applied
        self.order_credit_page.verify_that_order_credit_is_applied(credit_amount)

    @pytest.mark.QABSE1344
    def test_validate_late_delivery_fee_min_and_max_amount_rules(self):
        """Verify Late Delivery Fee credit reason min and max amount rules."""
        # Get order from database
        self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Test minimum amount validation
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Late delivery fee")
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("300")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1405
    def test_add_subscription_late_delivery_fee_credit_to_order(self):
        """Verify that a user can successfully add Subscription late delivery fee credit to an order."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Add subscription late delivery fee credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Subscription late delivery fee")
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify credit is applied
        self.order_credit_page.verify_that_order_credit_is_applied(credit_amount)

    @pytest.mark.QABSE1354
    def test_validate_subscription_late_delivery_fee_min_and_max_amount_rules(self):
        """Verify Subscription late delivery fee credit reason min and max amount rules."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Test minimum amount validation
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Subscription late delivery fee")
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("51")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1335
    def test_add_b2b_bulk_orders_credit_to_customer(self):
        """Verify that a user can successfully allocate B2B bulk orders credit to a customer."""
        # Search for customer
        self.search_page.search_for_customer("100")

        # Add B2B bulk orders credit to customer
        self.customer_credit_page.expand_customer_credit_section_and_click_credit_button()
        self.order_credit_page.select_a_credit_reason("B2B bulk orders")
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify credit is applied
        self.order_credit_page.verify_that_order_credit_is_applied(credit_amount)

    @pytest.mark.QABSE1335
    def test_validate_b2b_bulk_orders_min_and_max_amount_rules(self):
        """Verify B2B bulk orders credit reason min and max amount rules."""
        # Search for customer
        self.search_page.search_for_customer("100")

        # Test minimum amount validation
        self.customer_credit_page.expand_customer_credit_section_and_click_credit_button()
        self.order_credit_page.select_a_credit_reason("B2B bulk orders")
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("10000001")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1404
    def test_add_failed_eft_refunds_credit_to_order(self):
        """Verify that a user can successfully add Failed EFT refunds credit to an order."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Add failed EFT refunds credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Failed EFT refunds")
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify credit is applied
        self.order_credit_page.verify_that_order_credit_is_applied(credit_amount)

    @pytest.mark.QABSE1404
    def test_validate_failed_eft_refunds_min_and_max_amount_rules(self):
        """Verify Failed EFT refunds credit reason min and max amount rules."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Test minimum amount validation
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Failed EFT refunds")
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("2000000")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1353
    def test_add_system_error_credit_to_order_item(self):
        """Verify that a user can successfully add System Error credit to an order item."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Add system error credit to order item
        self.order_credit_page.expand_order_items_section_and_click_the_credit_item_option()
        self.order_credit_page.select_a_credit_reason("System error: Credit removal failed")
        self.order_credit_page.enter_rfn_for_system_error_reason()
        credit_amount = self.order_credit_page.enter_a_negative_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

    @pytest.mark.QABSE1353
    def test_validate_system_error_min_and_max_amount_rules(self):
        """Verify System Error credit reason min and max amount rules."""
        # Search for order
        self.search_page.search_for_order("74269681")

        # Test minimum amount validation
        self.order_credit_page.expand_order_items_section_and_click_the_credit_item_option()
        self.order_credit_page.select_a_credit_reason("System error: Credit removal failed")
        self.order_credit_page.enter_rfn_for_system_error_reason()
        self.order_credit_page.enter_invalid_min_amount("-2000000")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("1")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1349
    def test_add_duplicate_payment_credit_to_order(self):
        """Verify that a user can successfully add Duplicate payment credit to an order."""
        # Get order from database
        order_data = self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Add duplicate payment credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Duplicate payment")
        self.order_credit_page.enter_calculated_amount_and_enter_an_admin_note_for_order_credit(self.database.order_total, self.database.order_shipping, self.database.order_discount)
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

    @pytest.mark.QABSE1349
    def test_validate_duplicate_payment_min_and_max_amount_rules(self):
        """Verify Duplicate payment credit reason min and max amount rules."""
        # Get order from database
        self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Test minimum amount validation
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Duplicate payment")
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount("5000000")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1403
    def test_add_cod_return_credit_to_order(self):
        """Verify that a user can successfully add COD return credit to an order."""
        # Get order from database
        self.database.get_orders_from_database(self.database.order_with_returned_canceled_order_item_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Get return cancelled amount
        return_cancelled_amount, _ = self.order_credit_page.get_return_cancelled_amount_from_order_financials()

        # Add COD return credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("COD return")
        self.order_credit_page.enter_return_canceled_amount_and_enter_an_admin_note_for_order_credit(return_cancelled_amount)
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

    @pytest.mark.QABSE1403
    def test_validate_cod_return_min_and_max_amount_rules(self):
        """Verify COD return credit reason min and max amount rules."""
        # Get order from database
        self.database.get_orders_from_database(self.database.order_with_returned_canceled_order_item_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Get return cancelled amount and calculated amount
        _, calculated_returned_cancelled_amount = self.order_credit_page.get_return_cancelled_amount_from_order_financials()

        # Test minimum amount validation
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("COD return")
        self.order_credit_page.enter_invalid_min_amount("0")
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

        # Test maximum amount validation
        self.order_credit_page.enter_invalid_max_amount(str(calculated_returned_cancelled_amount))
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()
        self.order_credit_page.verify_validation_error()

    @pytest.mark.QABSE1340
    def test_add_credit_error_return_credit_to_order(self):
        """Verify that a user can successfully add Credit Error credit to an order."""
        # Get order from database
        self.database.get_orders_from_database(self.database.canceled_order_except_auto_canceled_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Get cancelled amount
        cancelled_amount, _ = self.order_credit_page.get_cancelled_amount_from_order_financials()

        # Add credit error credit to order
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Credit error")
        self.order_credit_page.enter_canceled_amount_and_enter_an_admin_note_for_order_credit(cancelled_amount)
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

    @pytest.mark.QABSE1340
    def test_validate_credit_error_cancelled_items_check(self):
        """Verify Credit error credit reason checks for cancelled items on order."""
        # Get order from database
        self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        # Search for order
        self.search_page.search_for_order(self.database.order_ids)

        # Try to add credit error credit to order without cancelled items
        self.customer_credit_page.expand_the_customer_credit_section_and_click_the_allocate_credit_button()
        self.order_credit_page.select_a_credit_reason("Credit error")
        credit_amount = self.order_credit_page.enter_an_amount_and_enter_an_admin_note_for_order_credit()
        self.order_credit_page.select_add_credit_button()
        self.order_credit_page.select_ok_on_dialog()

        # Verify validation error
        self.order_credit_page.verify_validation_error()
