"""Tests for Manual Override functionality."""

import pytest
from base.test_base import TestBase


class TestManualOverride(TestBase):
    """Test class for Manual Override functionality in Finance Portal."""

    @pytest.mark.regression
    @pytest.mark.qaba_482
    def test_manual_override_credit_card(self):
        """Verify that a user can perform manual override with Credit Card payment method."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("paygate_sql")

        self.step("Cancel Paid Order")
        self.cancel_order.cancel_paid_order(order_ids[0])

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Accordion Under Customer Info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("On Order View Page Expand The Order Items Accordion And Click Refund")
        self.manual_override_page.expand_order_items_accordion_and_click_refund()

        self.step("Click The Manual Override Button And Complete The Override Form")
        self.manual_override_page.click_manual_override_button_and_complete_form("Credit Card")

        self.step("Confirm Manual Override And View Logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify Manual Override Details")
        assert self.manual_override_page.verify_manual_override_details("Paygate"), "Manual override details not correctly displayed"

    @pytest.mark.regression
    @pytest.mark.qaba_488
    def test_manual_override_instant_eft_payfast(self):
        """Verify that a user can perform manual override with Instant EFT PayFast payment method."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("payfast_sql")

        self.step("Cancel Paid Order")
        self.cancel_order.cancel_paid_order(order_ids[0])

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Accordion Under Customer Info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("On Order View Page Expand The Order Items Accordion And Click Refund")
        self.manual_override_page.expand_order_items_accordion_and_click_refund()

        self.step("Click The Manual Override Button And Complete The Override Form")
        self.manual_override_page.click_manual_override_button_and_complete_form("PayFast")

        self.step("Confirm Manual Override And View Logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify Manual Override Details")
        assert self.manual_override_page.verify_manual_override_details("PayFast"), "Manual override details not correctly displayed"

    @pytest.mark.regression
    @pytest.mark.qaba_484
    def test_manual_override_masterpass(self):
        """Verify that a user can perform manual override with Masterpass payment method."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("masterpass_sql")

        self.step("Cancel Paid Order")
        self.cancel_order.cancel_paid_order(order_ids[0])

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Accordion Under Customer Info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("On Order View Page Expand The Order Items Accordion And Click Refund")
        self.manual_override_page.expand_order_items_accordion_and_click_refund()

        self.step("Click The Manual Override Button And Complete The Override Form EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("EFT")

        self.step("Capture EFT Banking Details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm Manual Override And View Logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify Manual Override Details")
        assert self.manual_override_page.verify_manual_override_details("EFT"), "Manual override details not correctly displayed"

    @pytest.mark.regression
    @pytest.mark.qaba_484
    def test_manual_override_eft_original_payment_credit_card(self):
        """Verify that a user can perform manual override with EFT when original payment method is Credit Card."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("paygate_sql")

        self.step("Cancel Paid Order")
        self.cancel_order.cancel_paid_order(order_ids[0])

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Accordion Under Customer Info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("On Order View Page Expand The Order Items Accordion And Click Refund")
        self.manual_override_page.expand_order_items_accordion_and_click_refund()

        self.step("Click The Manual Override Button And Complete The Override Form EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("EFT")

        self.step("Capture EFT Banking Details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm Manual Override And View Logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify Manual Override Details")
        assert self.manual_override_page.verify_manual_override_details("EFT"), "Manual override details not correctly displayed"

    @pytest.mark.regression
    @pytest.mark.qaba_486
    def test_manual_override_eft_discovery_miles(self):
        """Verify that a user can perform manual override with EFT for Discovery Miles payment method."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("discovery_miles_sql")

        self.step("Cancel Paid Order")
        self.cancel_order.cancel_paid_order(order_ids[0])

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Accordion Under Customer Info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("On Order View Page Expand The Order Items Accordion And Click Refund")
        self.manual_override_page.expand_order_items_accordion_and_click_refund()

        self.step("Click The Manual Override Button And Complete The Override Form")
        self.manual_override_page.click_manual_override_button_and_complete_form("Discovery Miles")

        self.step("Confirm Manual Override And View Logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify Manual Override Details")
        assert self.manual_override_page.verify_manual_override_details("Discovery Miles"), "Manual override details not correctly displayed"

    @pytest.mark.regression
    @pytest.mark.qaba_483
    def test_manual_override_refund_amount_exceeds_settlement_amount(self):
        """Verify validation when refund amount exceeds settlement amount."""

        self.step("Get Orders From Database")
        order_ids = self.order_data.get_orders("paygate_sql")

        self.step("Cancel Paid Order")
        self.cancel_order.cancel_paid_order(order_ids[0])

        self.step("Search For Order")
        self.top_nav.search_for_order(order_ids[0])

        self.step("Expand The Customer Credit Accordion Under Customer Info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("On Order View Page Expand The Order Items Accordion And Click Refund")
        self.manual_override_page.expand_order_items_accordion_and_click_refund()

        self.step("Click The Manual Override Button And Complete The Override Form With Amount Exceeding Total")
        self.manual_override_page.click_manual_override_button_and_complete_form_with_excessive_amount("Credit Card")

        self.step("Confirm Manual Override And View Logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify That An Admin Note For The Failed Manual Override Was Created")
        assert self.manual_override_page.verify_admin_note_for_failed_manual_override(), "Admin note for failed manual override not found"
