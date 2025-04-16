"""Test cases for Edit Order sanity tests."""

import pytest
from base.test_base import TestBase


class TestEditOrderSanity(TestBase):
    """Test cases for Edit Order sanity tests."""

    @pytest.mark.EditOrder
    @pytest.mark.Sanity
    @pytest.mark.QABA_531
    def test_cannot_update_shipping_and_discount_on_authed_orders(self):
        """Verify that a user cannot update Shipping and Discount on Auth'd orders."""
        self.step("Getting orders from database")
        self.database.get_orders_from_database(self.database.paygate_sql)

        self.step("Searching for order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigating to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Verifying that both shipping and discount disabled fields are on edit order screen")
        self.edit_order_page.verify_that_both_shipping_and_discount_disabled_fields_are_on_edit_order_screen()

    @pytest.mark.EditOrder
    @pytest.mark.Sanity
    @pytest.mark.QABA_534
    def test_update_discount_amount(self):
        """Verify that user can update the discount amount."""
        self.step("Getting orders from database")
        self.database.get_orders_from_database(self.database.new_order_with_discount_and_shipping_amounts_sql)

        self.step("Searching for order")
        self.search_page.search_for_order(self.database.order_ids)

        self.step("Navigating to edit order screen")
        self.edit_order_page.navigate_to_edit_order_screen()

        self.step("Updating discount amount")
        self.edit_order_page.update_discount_amount()

        self.step("Verifying that the discount amount is updated on order financials")
        self.edit_order_page.verify_that_the_discount_amount_is_updated_on_order_financials()
