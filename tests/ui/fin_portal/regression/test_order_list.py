import pytest
from base.test_base import TestBase


class TestOrderList(TestBase):
    """Test class for Order List functionality."""

    @pytest.mark.regression
    @pytest.mark.qaba622
    def test_authorise_single_order(self):
        """Verify that a user can Authorise an order from the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Authorise Single Order")
        order_id = self.order_list_page.authorise_single_order()

        self.step(f"Verified order {order_id} was successfully authorized")

    @pytest.mark.regression
    @pytest.mark.qaba622
    def test_authorise_multiple_orders(self):
        """Verify that a user can Authorise multiple orders from the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Authorise Multiple Orders")
        order_ids = self.order_list_page.authorise_multiple_orders()

        self.step(f"Verified orders {order_ids} were successfully authorized")

    @pytest.mark.regression
    @pytest.mark.qaba623
    def test_cancel_single_order(self):
        """Verify that a user can cancel an order from the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Cancel Single Order")
        order_id, selected_reason = self.order_list_page.cancel_single_order()

        self.step(f"Verified order {order_id} was successfully canceled with reason '{selected_reason}'")

    @pytest.mark.regression
    @pytest.mark.qaba623
    def test_cancel_multiple_orders(self):
        """Verify that a user can cancel multiple orders from the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Cancel Multiple Orders")
        order_ids, selected_reason = self.order_list_page.cancel_multiple_orders()

        self.step(f"Verified orders {order_ids} were successfully canceled with reason '{selected_reason}'")

    @pytest.mark.regression
    @pytest.mark.qaba623
    def test_cancel_already_cancelled_order(self):
        """Verify that a user cant cancel an already cancelled order from the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Clear Today Filter")
        self.order_list_page.clear_today_filter()

        self.step("Try to cancel an already cancelled order")
        order_id = self.order_list_page.cancel_already_cancelled_order()

        self.step(f"Verified that order {order_id} could not be canceled again")

    @pytest.mark.regression
    @pytest.mark.qaba625
    def test_filter_by_daily_deals(self):
        """Verify that a user can filter for daily deals orders on the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter By Daily Deal")
        count = self.order_list_page.filter_by_daily_deal()

        self.step(f"Verified {count} daily deal orders displayed")

    @pytest.mark.regression
    @pytest.mark.qaba626
    def test_filter_by_auth_status(self):
        """Verify that a user can filter by Auth Status on the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter By Auth Status")
        status, count = self.order_list_page.filter_by_auth_status()

        self.step(f"Verified {count} orders with auth status '{status}' displayed")

    @pytest.mark.regression
    @pytest.mark.qaba626
    def test_filter_by_payment_method(self):
        """Verify that a user can filter by Payment Method on the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter By Payment Method")
        method, count = self.order_list_page.filter_by_payment_method()

        self.step(f"Verified {count} orders with payment method '{method}' displayed")

    @pytest.mark.regression
    @pytest.mark.qaba626
    def test_filter_by_shipping_method(self):
        """Verify that a user can filter by Shipping Method on the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter By Shipping Method")
        count = self.order_list_page.filter_by_shipping_method()

        self.step(f"Verified {count} orders with Collection shipping method displayed")

    @pytest.mark.regression
    @pytest.mark.qaba626
    def test_filter_by_order_totals(self):
        """Verify that a user can filter by Minimum and Maximum Order Total on the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Filter By Minimum Order Total")
        min_count = self.order_list_page.filter_by_minimum_order_total()

        self.step(f"Verified {min_count} orders with total greater than R500 displayed")

        self.step("Filter By Maximum Order Total")
        max_count = self.order_list_page.filter_by_maximum_order_total()

        self.step(f"Verified {max_count} orders with total less than R500 displayed")

    @pytest.mark.regression
    @pytest.mark.qaba626
    def test_filter_by_multiple_filters(self):
        """Verify that a user can apply multiple filters at once on the order list page."""

        self.step("Navigate to Order List Page")
        self.order_list_page.navigate_to_order_list_page()

        self.step("Apply Multiple Filters")
        count = self.order_list_page.filter_by_multiple_filters()

        self.step(f"Verified {count} orders matching all filter criteria displayed")
