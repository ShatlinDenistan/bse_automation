import pytest
from base.test_base import TestBase


class TestManualAuthSanity(TestBase):
    """Sanity test class for Manual Auth functionality"""

    @pytest.mark.sanity
    def test_manual_auth_page_loads(self):
        """Verify that manual auth page loads correctly."""
        self.step("Navigate to manual auth page")
        assert self.manual_auth_page.verify_page_loaded(), "Manual Auth page failed to load"

    @pytest.mark.sanity
    def test_search_functionality(self):
        """Verify search functionality in manual auth screen."""
        self.step("Navigate to manual auth page")
        self.manual_auth_page.verify_page_loaded()

        self.step("Search for order")
        self.manual_auth_page.search_order("1234567")

        self.step("Verify search results")
        assert self.manual_auth_page.verify_order_exists(), "Order search did not return results"

        self.step("Verify search returns correct number of results")
        order_count = self.manual_auth_page.get_order_count()
        assert order_count > 0, "No orders found in search results"
