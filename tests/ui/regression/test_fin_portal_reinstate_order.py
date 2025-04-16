"""Tests for reinstating orders in the Financial Portal."""

import pytest
from base.test_base import TestBase


class TestFinPortalReinstateOrder(TestBase):
    """Test class for reinstating orders in the Financial Portal."""

    @pytest.mark.qaba_546
    @pytest.mark.reinstate_order
    @pytest.mark.regression
    def test_reinstate_fully_auto_canceled_order(self):
        """
        Verify that a user can reinstate a fully auto canceled order.
        """
        # Get orders from the database that were auto-canceled
        self.step("Get orders from database with auto-canceled status")
        self.database.get_orders_from_database(self.database.auto_canceled_orders_sql)

        # Search for the order
        self.step("Search for the auto-canceled order")
        self.search_page.search_for_order(self.database.order_ids)

        # Reinstate the order
        self.step("Reinstate the order")
        self.reinstate_order_page.reinstate_order()

        # Verify an admin note was created
        self.step("Verify that an admin note for order reinstatement was created")
        admin_note = self.reinstate_order_page.verify_admin_note_created()
        assert "Order reinstated" in admin_note, "Admin note for order reinstatement was not found"

    @pytest.mark.qaba_549
    @pytest.mark.reinstate_order
    @pytest.mark.regression
    def test_reinstate_auto_canceled_order_with_staff_discount(self):
        """
        Verify that a user can reinstate an auto cancelled order that has Staff discount.
        """
        # Get orders from the database that were auto-canceled with staff discount
        self.step("Get orders from database with auto-canceled status and staff discount")
        self.database.get_orders_from_database(self.database.auto_canceled_orders_with_staff_discount_sql)

        # Search for the order
        self.step("Search for the auto-canceled order with staff discount")
        self.search_page.search_for_order(self.database.order_ids)

        # Reinstate the order
        self.step("Reinstate the order")
        self.reinstate_order_page.reinstate_order()

        # Verify an admin note was created
        self.step("Verify that an admin note for order reinstatement was created")
        admin_note = self.reinstate_order_page.verify_admin_note_created()
        assert "Order reinstated" in admin_note, "Admin note for order reinstatement was not found"

        # Get order financials amounts
        self.step("Get order financials amounts")
        self.reinstate_order_page.get_order_financials_amounts()

        # Verify staff discount matches
        self.step("Verify that staff discount on reinstate matches staff discount on order financials")
        self.reinstate_order_page.verify_staff_discount_matches()

    @pytest.mark.qaba_547
    @pytest.mark.reinstate_order
    @pytest.mark.regression
    def test_reinstate_auto_canceled_order_with_shipping_and_coupon_discount(self):
        """
        Verify that a user can reinstate an auto cancelled order that has Shipping and Coupon Discount.
        """
        # Get orders from the database that were auto-canceled with shipping and coupon discount
        self.step("Get orders from database with auto-canceled status and shipping and coupon discount")
        self.database.get_orders_from_database(self.database.auto_canceled_order_with_charges_sql)

        # Search for the order
        self.step("Search for the auto-canceled order with shipping and coupon discount")
        self.search_page.search_for_order(self.database.order_ids)

        # Reinstate the order
        self.step("Reinstate the order")
        self.reinstate_order_page.reinstate_order()

        # Verify that reinstate order amounts are correct
        self.step("Verify that reinstate order amounts are correct")
        self.reinstate_order_page.verify_order_amounts_correct(order_shipping=[self.database.order_shipping], order_discount=[self.database.order_discount])

        # Verify an admin note was created
        self.step("Verify that an admin note for order reinstatement was created")
        admin_note = self.reinstate_order_page.verify_admin_note_created()
        assert "Order reinstated" in admin_note, "Admin note for order reinstatement was not found"

    @pytest.mark.qaba_548
    @pytest.mark.reinstate_order
    @pytest.mark.regression
    def test_reinstate_button_not_available_for_orders_not_auto_canceled(self):
        """
        Verify that when an order is NOT auto canceled the reinstate order button is not available.
        """
        # Get orders from the database that were canceled but not auto-canceled
        self.step("Get orders from database that were canceled but not auto-canceled")
        self.database.get_orders_from_database(self.database.canceled_order_except_auto_canceled_sql)

        # Search for the order
        self.step("Search for the order that was not auto-canceled")
        self.search_page.search_for_order(self.database.order_ids)

        # Verify that reinstate button is not available
        self.step("Verify that reinstate button is not available")
        canceled_by_text = self.reinstate_order_page.verify_reinstate_button_not_available()
        assert "auto_cancel" not in canceled_by_text, "Order was auto-canceled but should not have been"
