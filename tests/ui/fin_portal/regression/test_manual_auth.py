import pytest
from base.test_base import TestBase


class TestManualAuth(TestBase):
    """Test class for Manual Auth functionality"""

    @pytest.mark.regression
    def test_search_order(self):
        """Search for an order in the manual auth screen."""
        self.step("Navigate to manual auth page")
        self.manual_auth_page.verify_page_loaded()

        self.step("Search for order")
        self.manual_auth_page.search_order("1234567")

        self.step("Verify order exists")
        assert self.manual_auth_page.verify_order_exists(), "Order was not found"

    @pytest.mark.regression
    def test_authorize_order(self):
        """Test authorizing an order through manual auth."""
        self.step("Navigate to manual auth page")
        self.manual_auth_page.verify_page_loaded()

        self.step("Search for order")
        self.manual_auth_page.search_order("1234567")

        self.step("Select and authorize order")
        self.manual_auth_page.select_order()
        self.manual_auth_page.authorize_order()

        self.step("Verify authorization confirmation")
        assert self.manual_auth_page.confirm_success_message(), "Authorization confirmation was not displayed"

    @pytest.mark.regression
    def test_reject_order(self):
        """Test rejecting an order through manual auth."""
        self.step("Navigate to manual auth page")
        self.manual_auth_page.verify_page_loaded()

        self.step("Search for order")
        self.manual_auth_page.search_order("1234567")

        self.step("Select and reject order")
        self.manual_auth_page.select_order()
        self.manual_auth_page.reject_order("Suspicious Activity", "Test rejection comment")

        self.step("Verify rejection confirmation")
        assert self.manual_auth_page.confirm_success_message(), "Rejection confirmation was not displayed"

    @pytest.mark.regression
    def test_cancel_authorization(self):
        """Test canceling an authorization process."""
        self.step("Navigate to manual auth page")
        self.manual_auth_page.verify_page_loaded()

        self.step("Search for order")
        self.manual_auth_page.search_order("1234567")

        self.step("Select order and start authorization")
        self.manual_auth_page.select_order()
        self.manual_auth_page.click(self.manual_auth_page.authorize_button)

        self.step("Cancel the authorization")
        self.manual_auth_page.cancel_authorization()

        self.step("Verify we are back at the order list")
        assert self.manual_auth_page.verify_order_exists(), "Order list is not displayed after cancellation"
