import pytest
import random
from base.test_base import TestBase


class TestFinPortalRiskQueue(TestBase):
    """Test class for Risk Queue functionality in Fin-Portal."""

    @pytest.mark.regression
    @pytest.mark.QABA_639
    def test_risk_queue_show_items_and_pagination(self):
        """View all the records in the Risk Queue page via Show Items and Pagination."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Select 10 items from the show items dropdown")
        self.risk_queue_page.click_show_items_dropdown_and_select_10_items()

        self.step("Navigate to the next page")
        self.risk_queue_page.navigate_to_next_page()

    @pytest.mark.regression
    @pytest.mark.QABA_631
    def test_risk_queue_clear_risk(self):
        """Verify that a user can clear a risk label from the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Select an order and clear its risk status")
        self.risk_queue_page.select_an_order_to_clear_risk()

        self.step("Handle alert dialogs")
        self.risk_queue_page.handle_alerts()

    @pytest.mark.regression
    @pytest.mark.QABA_636
    def test_risk_queue_filter_by_payment_method(self):
        """Verify that a user can filter by Payment Method on the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Apply filter using payment method")
        self.risk_queue_page.filter_using_payment_method()

    @pytest.mark.regression
    @pytest.mark.QABA_636
    def test_risk_queue_filter_by_shipping_method(self):
        """Verify that a user can filter by Shipping Method on the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Apply filter using shipping method")
        self.risk_queue_page.filter_using_shipping_method()

    @pytest.mark.regression
    @pytest.mark.QABA_637
    def test_risk_queue_filter_by_minimum_maximum_order_total(self):
        """Verify that a user can filter by Minimum and Maximum Order Total on the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Filter using minimum order amount")
        self.risk_queue_page.filter_using_minimum_amount()

        self.step("Filter using maximum order amount")
        self.risk_queue_page.filter_using_maximum_amount()

    @pytest.mark.regression
    @pytest.mark.QABA_638
    def test_risk_queue_filter_by_multiple_filters(self):
        """Verify that a user can apply multiple filters at once on the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Apply multiple filters simultaneously")
        self.risk_queue_page.filter_using_multiple_filters()

    @pytest.mark.regression
    @pytest.mark.QABA_625
    def test_risk_queue_filter_by_daily_deals(self):
        """Verify that a user can filter for daily deals orders on the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Filter for daily deal orders")
        self.risk_queue_page.filter_using_daily_deal()

    @pytest.mark.regression
    @pytest.mark.QABA_635
    def test_risk_queue_filter_by_date_range(self):
        """Verify that a user can filter for a specific date range on the Risk Queue page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Filter by a specific date range")
        self.risk_queue_page.filter_using_date_range()

    @pytest.mark.regression
    @pytest.mark.QABA_633
    def test_risk_queue_send_email(self):
        """Verify that a user can send a random email from the Risk Queue Page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Select the first order on the grid")
        self.risk_queue_page.select_first_order_on_grid()

        self.step("Select an email template and send the email")
        self.risk_queue_page.select_email_template_and_send_email()

        self.step("Verify the email sent success message")
        self.risk_queue_page.verify_email_sent_success_message()

    @pytest.mark.regression
    @pytest.mark.QABA_632
    def test_risk_queue_cancel_order(self):
        """Verify that a user can cancel an order from the Risk Queue Page."""

        self.step("Navigate to the Risk Queue page")
        self.risk_queue_page.navigate_to_risk_queue()

        self.step("Select the first order on the grid")
        self.risk_queue_page.select_first_order_on_grid()

        self.step("Cancel the selected order")
        self.risk_queue_page.cancel_single_order()

        self.step("Verify the canceled order status")
        self.risk_queue_page.verify_canceled_order_status()
