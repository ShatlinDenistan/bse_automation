import pytest
from base.test_base import TestBase


class TestSearch(TestBase):
    """Test class for search functionality."""

    @pytest.mark.regression
    def test_search_for_customer(self):
        """Test searching for a customer."""
        customer_id = "12345678"  # Example customer ID

        self.step("Search for a customer")
        self.search_page.search_for_customer(customer_id)

    @pytest.mark.regression
    def test_search_for_order(self):
        """Test searching for an order."""
        order_number = "ORD123456"  # Example order number

        self.step("Search for an order")
        self.search_page.search_for_order(order_number)

    @pytest.mark.regression
    def test_search_for_rrn(self):
        """Test searching for a RRN."""
        rrn = "RRN987654"  # Example RRN

        self.step("Search for a RRN")
        self.search_page.search_for_rrn(rrn)
