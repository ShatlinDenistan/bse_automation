"""Tests for Risk Queue functionality in Financial Portal."""

import pytest
from base.test_base import TestBase


class TestRiskQueue(TestBase):
    """Tests for Risk Queue functionality in Financial Portal."""

    @pytest.mark.QABA_639
    def test_show_items_and_pagination(self):
        """
        Test viewing all records in the Risk Queue via Show Items and Pagination.

        This test verifies that users can change the number of items displayed
        per page and navigate between pages in the Risk Queue.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Click Show Items Dropdown And Select 10 Items")
        self.risk_queue_page.select_items_per_page()

        self.step("Navigate To Next Page")
        self.risk_queue_page.navigate_to_next_page()

    @pytest.mark.QABA_631
    def test_clear_risk(self):
        """
        Test that a user can clear a risk label from the Risk Queue page.

        This test verifies the functionality to remove risk flags from orders
        in the risk queue.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Select an order to clear risk")
        self.risk_queue_page.select_order_and_clear_risk()

    @pytest.mark.QABA_636
    def test_filter_by_payment_method(self):
        """
        Test filtering by Payment Method on the Risk Queue page.

        This test verifies that users can filter orders by payment method
        and that the filtered results are correct.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Filter using Payment Method")
        self.risk_queue_page.filter_by_payment_method("Credit Card")

    @pytest.mark.QABA_636
    def test_filter_by_shipping_method(self):
        """
        Test filtering by Shipping Method on the Risk Queue page.

        This test verifies that users can filter orders by shipping method
        and that the filtered results are correct.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Filter Using Shipping Method")
        self.risk_queue_page.filter_by_shipping_method()

    @pytest.mark.QABA_637
    def test_filter_by_min_max_order_total(self):
        """
        Test filtering by Minimum and Maximum Order Total on the Risk Queue page.

        This test verifies that users can filter orders by order total range
        and that the filtered results are correct.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Filter Using Minimum Amount")
        self.risk_queue_page.filter_by_amount_range(minimum="R 100")

        self.step("Clear filter and then filter using Maximum Amount")
        self.risk_queue_page.filter_by_amount_range(maximum="R 2000")

    @pytest.mark.QABA_638
    def test_filter_by_multiple_filters(self):
        """
        Test applying multiple filters at once on the Risk Queue page.

        This test verifies that users can apply multiple filter criteria
        simultaneously and that the filtered results are correct.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Apply multiple filters")
        self.risk_queue_page.apply_multiple_filters()

    @pytest.mark.QABA_625
    def test_filter_by_daily_deals(self):
        """
        Test filtering for daily deals orders on the Risk Queue page.

        This test verifies that users can filter for orders tagged as daily deals
        and that the filtered results are correct.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Filter Using Daily Deal")
        self.risk_queue_page.filter_by_daily_deals()

    @pytest.mark.QABA_635
    def test_filter_by_date_range(self):
        """
        Test filtering for a specific date range on the Risk Queue page.

        This test verifies that users can filter orders by date range
        and that the filtered results are correct.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Filter Using Date Range")
        self.risk_queue_page.filter_by_date_range("01/01/2023 - 01/01/2024")

    @pytest.mark.QABA_633
    def test_send_email(self):
        """
        Test sending an email from the Risk Queue Page.

        This test verifies that users can select an email template and send
        an email to the customer from the Risk Queue page.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Select First Order on Grid")
        self.risk_queue_page.select_first_order()

        self.step("Select Email Template and Send Email")
        self.risk_queue_page.select_email_template_and_send()

        self.step("Verify Email Sent Success Message")
        self.risk_queue_page.verify_email_sent()

    @pytest.mark.QABA_632
    def test_cancel_order(self):
        """
        Test canceling an order from the Risk Queue Page.

        This test verifies that users can cancel an order from the Risk Queue page
        and that the order status is updated correctly.
        """
        self.step("Navigate to Risk Queue")
        self.side_nav.click_risk_queue()

        self.step("Select First Order on Grid")
        order_id = self.risk_queue_page.select_first_order()

        self.step("Cancel Single Order")
        selected_reason = self.risk_queue_page.cancel_selected_order()

        self.step("Verify Canceled Order Status")
        self.risk_queue_page.verify_canceled_order_status(order_id, selected_reason)
