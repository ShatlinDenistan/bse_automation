"""Tests for Manual Credit functionality."""

import pytest
from base.test_base import TestBase


class TestManualCredit(TestBase):
    """Test class for Manual Credit functionality in Finance Portal."""

    @pytest.mark.qabse_1339
    def test_add_credit_breach_to_customer(self):
        """Verify that a user can successfully allocate Credit breach credit to a customer."""

        self.step("Search For Customer")
        self.top_nav.search_for_customer("100")

        self.step("Expand The Customer Credit Section And Click The Credit Button")
        self.customer_credit_page.expand_credit_section_and_click_credit_button()

        self.step("Select A Credit Reason")
        self.order_credit_page.select_credit_reason("Credit Breach")

        self.step("Enter Jira Number for Credit Breach Reason")
        self.order_credit_page.enter_jira_number_for_credit_breach()

        self.step("Enter An Amount And Enter An Admin Note For Order Credit")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify That Order Credit Is Applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Order credit was not applied correctly"

    @pytest.mark.qabse_1339
    def test_validate_credit_breach_min_max_amount_rules(self):
        """Verify Credit breach credit reason min and max amount rules."""

        self.step("Search For Customer")
        self.top_nav.search_for_customer("100")

        self.step("Expand The Customer Credit Section And Click The Credit Button")
        self.customer_credit_page.expand_credit_section_and_click_credit_button()

        self.step("Select A Credit Reason")
        self.order_credit_page.select_credit_reason("Credit Breach")

        self.step("Enter Jira Number for Credit Breach Reason")
        self.order_credit_page.enter_jira_number_for_credit_breach()

        self.step("Enter Invalid Min Amount")
        self.order_credit_page.enter_invalid_min_amount("0")

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify Validation Error")
        assert self.order_credit_page.verify_validation_error(), "Validation error not displayed for min amount"

        self.step("Enter Invalid Max Amount")
        self.order_credit_page.enter_invalid_min_amount("10000001")

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify Validation Error")
        assert self.order_credit_page.verify_validation_error(), "Validation error not displayed for max amount"

    @pytest.mark.qabse_1354
    def test_add_goodwill_credit_to_order(self):
        """Verify that a user can successfully add Goodwill credit to an order."""

        self.step("Search For Order")
        self.top_nav.search_for_order("74269681")

        self.step("Expand The Customer Credit Section And Click The Allocate Credit Button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select A Credit Reason")
        self.order_credit_page.select_credit_reason("Goodwill")

        self.step("Enter An Amount And Enter An Admin Note For Order Credit")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify That Order Credit Is Applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Order credit was not applied correctly"

    @pytest.mark.qabse_1354
    def test_validate_goodwill_min_max_amount_rules(self):
        """Verify Goodwill credit reason min and max amount rules."""

        self.step("Search For Order")
        self.top_nav.search_for_order("74269681")

        self.step("Expand The Customer Credit Section And Click The Allocate Credit Button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select A Credit Reason")
        self.order_credit_page.select_credit_reason("Goodwill")

        self.step("Enter Invalid Min Amount")
        self.order_credit_page.enter_invalid_min_amount("-1")

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify Validation Error")
        assert self.order_credit_page.verify_validation_error(), "Validation error not displayed for min amount"

        self.step("Enter Invalid Max Amount")
        self.order_credit_page.enter_invalid_min_amount("800")

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify Validation Error")
        assert self.order_credit_page.verify_validation_error(), "Validation error not displayed for max amount"

    @pytest.mark.qabse_1344
    def test_add_late_delivery_fee_credit_to_order(self):
        """Verify that a user can successfully add Late Delivery Fee credit to an order."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Section And Click The Allocate Credit Button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select A Credit Reason")
        self.order_credit_page.select_credit_reason("Late Delivery Fee")

        self.step("Enter An Amount And Enter An Admin Note For Order Credit")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Select The Add Credit Button")
        self.customer_credit_page.select_add_credit_button()

        self.step("Select OK On The Dialog")
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify That Order Credit Is Applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Order credit was not applied correctly"
