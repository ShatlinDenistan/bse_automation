import pytest
from base.test_base import TestBase


@pytest.mark.ui
class TestOrderList(TestBase):
    """Tests for Order List functionality in the Financial Portal."""

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_622
    def test_authorise_order(self):
        """Verify that a user can Authorise an order from the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Authorise Single Order")
        order_id = self.order_list_page.authorise_single_order()
        assert order_id, "Order ID should not be empty"

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_622
    def test_authorise_multiple_orders(self):
        """Verify that a user can Authorise multiple orders from the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Authorise Multiple Orders")
        order_ids = self.order_list_page.authorise_multiple_orders()
        assert len(order_ids) == 3, "Should have authorized 3 orders"

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_623
    def test_cancel_order(self):
        """Verify that a user can cancel an order from the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Cancel Single Order")
        order_id, reason = self.order_list_page.cancel_single_order()
        assert order_id, "Order ID should not be empty"
        assert reason, "Cancellation reason should not be empty"

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_623
    def test_cancel_multiple_orders(self):
        """Verify that a user can cancel multiple orders from the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Cancel Multiple Orders")
        order_ids = self.order_list_page.cancel_multiple_orders()
        assert len(order_ids) == 3, "Should have canceled 3 orders"

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_623
    def test_cancel_already_cancelled_order(self):
        """Verify that a user cant cancel an already cancelled order from the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Cancel Already Cancelled Order")
        order_id = self.order_list_page.cancel_already_cancelled_order()
        assert order_id, "Order ID should not be empty"

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_625
    def test_filter_by_daily_deals(self):
        """Verify that a user can filter for daily deals orders on the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Daily Deal")
        self.order_list_page.filter_by_daily_deal()

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_626
    def test_filter_by_auth_status(self):
        """Verify that a user can filter by Auth Status on the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Auth Status")
        self.order_list_page.filter_by_auth_status()

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_626
    def test_filter_by_payment_method(self):
        """Verify that a user can filter by Payment Method on the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Payment Method")
        self.order_list_page.filter_by_payment_method()

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_626
    def test_filter_by_shipping_method(self):
        """Verify that a user can filter by Shipping Method on the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Shipping Method")
        self.order_list_page.filter_by_shipping_method()

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_626
    def test_filter_by_min_max_order_total(self):
        """Verify that a user can filter by Minumum and Maximum Order Total on the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Minimum Order Total")
        self.order_list_page.filter_by_minimum_order_total()

        self.step("Navigate to Order List Page again")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Maximum Order Total")
        self.order_list_page.filter_by_maximum_order_total()

    @pytest.mark.OrderList
    @pytest.mark.Regression
    @pytest.mark.QABA_626
    def test_filter_by_multiple_filters(self):
        """Verify that a user can apply multiple filters at once on the order list page"""
        self.step("Navigate to Order List Page")
        self.side_nav.navigate_to_order_list_page()

        self.step("Filter By Multiple Filters")
        self.order_list_page.filter_by_multiple_filters()
