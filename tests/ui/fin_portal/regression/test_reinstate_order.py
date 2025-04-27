import pytest
from base.test_base import TestBase


class TestReinstateOrder(TestBase):
    """Test class for Reinstate Order functionality"""

    @pytest.mark.regression
    @pytest.mark.ReinstateOrder
    @pytest.mark.QABA_546
    def test_reinstate_fully_auto_canceled_order(self):
        """Verify that a user can reinstate a fully auto canceled order."""

        self.step("Get auto-canceled orders from database")
        order_ids = self.order_data.get_orders("auto_canceled_orders_sql")

        self.step("Search for the auto-canceled order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Reinstate the order")
        self.reinstate_order_page.reinstate_order()

        self.step("Verify that an admin note for order reinstatement was created")
        assert self.reinstate_order_page.verify_admin_note_for_reinstatement(), "Admin note for reinstatement not found"

    @pytest.mark.regression
    @pytest.mark.ReinstateOrder
    @pytest.mark.QABA_549
    def test_reinstate_auto_canceled_order_with_staff_discount(self):
        """Verify that a user can reinstate an auto cancelled order that has Staff discount."""

        self.step("Get auto-canceled orders with staff discount from database")
        order_ids = self.order_data.get_orders("auto_canceled_orders_with_staff_discount.sql")

        self.step("Search for the auto-canceled order with staff discount")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Reinstate the order")
        self.reinstate_order_page.reinstate_order()

        self.step("Verify that an admin note for order reinstatement was created")
        assert self.reinstate_order_page.verify_admin_note_for_reinstatement(), "Admin note for reinstatement not found"

        self.step("Get order financials amounts")
        self.reinstate_order_page.get_order_financials_amounts()

        self.step("Verify that staff discount on reinstate matches staff discount on order financials")
        assert self.reinstate_order_page.verify_staff_discount_match(), "Staff discount amounts don't match"

    @pytest.mark.regression
    @pytest.mark.ReinstateOrder
    @pytest.mark.QABA_547
    def test_reinstate_auto_canceled_order_with_shipping_and_coupon_discount(self):
        """Verify that a user can reinstate an auto cancelled order that has Shipping and Coupon Discount."""

        self.step("Get auto-canceled orders with shipping and coupon discount from database")
        order_ids = self.order_data.get_orders("auto_canceled_order_with_charges.sql")

        self.step("Search for the auto-canceled order with shipping and coupon discount")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Reinstate the order")
        self.reinstate_order_page.reinstate_order()

        self.step("Verify that reinstate order amounts are correct")
        assert self.reinstate_order_page.verify_reinstate_order_amounts(self.database.order_shipping, self.database.order_discount), "Reinstate order amounts are incorrect"

        self.step("Verify that an admin note for order reinstatement was created")
        assert self.reinstate_order_page.verify_admin_note_for_reinstatement(), "Admin note for reinstatement not found"

    @pytest.mark.regression
    @pytest.mark.ReinstateOrder
    @pytest.mark.QABA_548
    def test_reinstate_button_not_available_for_orders_not_auto_canceled(self):
        """Verify that when an order is NOT auto canceled the reinstate order button is not available."""

        self.step("Get orders canceled by other means than auto-cancel from database")
        order_ids = self.order_data.get_orders("canceled_order_except_auto_canceled.sql")

        self.step("Search for the order that was not auto-canceled")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Verify that reinstate button is not available")
        assert self.reinstate_order_page.verify_reinstate_button_not_available(order_ids[0]), "Reinstate button is visible but should not be"
