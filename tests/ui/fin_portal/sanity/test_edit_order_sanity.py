import pytest
from base.test_base import TestBase


class TestEditOrderSanity(TestBase):
    """Sanity test class for Edit Order functionality."""

    @pytest.mark.QABA_531
    def test_cannot_update_shipping_and_discount_on_authd_orders(self):
        """Verify that a user cannot update Shipping and Discount on Auth'd orders."""

        self.step("Get orders from database")
        order_ids = self.order_data.get_orders(self.order_queries.paygate_sql)

        self.step("Search for order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Navigate to Edit Order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Verify that both shipping and discount disabled fields are visible")
        self.edit_order_page.verify_that_both_shipping_and_discount_disabled_fields_are_on_edit_order_screen()

    @pytest.mark.QABA_534
    def test_update_discount_amount(self):
        """Verify that user can update the discount amount."""

        self.step("Get orders from database")
        order_ids = self.order_data.get_orders(self.order_queries.new_order_with_discount_and_shipping_amounts_sql)

        self.step("Search for order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Navigate to Edit Order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Update discount amount")
        self.edit_order_page.update_discount_amount()

        self.step("Verify that the discount amount is updated on order financials")
        discount_amount = self.edit_order_page.verify_that_the_discount_amount_is_updated_on_order_financials()
        assert discount_amount == "10.00"
