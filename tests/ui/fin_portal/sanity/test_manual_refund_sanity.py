"""Manual Refund Sanity Tests."""

import pytest
from base.test_base import TestBase


class TestManualRefundSanity(TestBase):
    """Manual Refund Sanity Test class."""

    @pytest.mark.qaba_458
    def test_process_refund_credit_card_payu(self):
        """Fin-Portal | Processing A Refund | Credit Card | PayU."""

        self.step("Get orders from database")
        self.order_data.get_orders("${paygate_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.manual_refund_page.expand_order_items_accordion_and_click_refund()

        self.step("Click refund button and submit refund request")
        self.manual_refund_page.click_refund_button_and_submit_refund_request()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("PayU")

    @pytest.mark.qaba_457
    def test_cannot_process_refund_when_customer_is_blacklisted(self):
        """Fin-Portal | Manual Refunds | Cannot Process Refund When Customer Is Blacklisted."""

        self.step("Get customers from database")
        self.utils.get_customers_from_database("${blacklisted_sql}")

        self.step("Create new TAL orders")
        self.utils.create_new_tal_orders("${customer_ids[0]}", "Credit Card")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify order is not eligible for manual refund")
        self.manual_refund_page.verify_order_not_eligible_for_manual_refund()

    @pytest.mark.qaba_459
    def test_process_refund_masterpass(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Masterpass."""

        self.step("Get orders from database")
        self.order_data.get_orders("${masterpass_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click refund button and enter banking details")
        self.manual_refund_page.click_refund_button_and_enter_banking_details()

        self.step("Click EFT refund button and submit refund request")
        self.manual_refund_page.click_eft_refund_button_and_submit_refund_request()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_464
    def test_process_refund_sbux_nsfas_wallet(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | sBux/NSFAS Wallet."""

        self.step("Get orders from database")
        self.order_data.get_orders("${sbux_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click refund button and submit refund request")
        self.manual_refund_page.click_refund_button_and_submit_refund_request()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("sBux")

    @pytest.mark.qaba_464
    def test_process_refund_excludes_coupon_amount(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Refund Excludes Coupon Amount."""

        self.step("Get orders from database")
        self.order_data.get_orders("${order_with_coupon_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify refund amount excludes coupon amount")
        self.manual_refund_page.verify_refund_amount_excludes_coupon_amount()

    @pytest.mark.qaba_467
    def test_process_refund_credit_card_and_ebucks_part_payment(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Credit Card and eBucks Part Payment."""

        self.step("Get orders from database")
        self.order_data.get_orders("${cc_ebucks_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click refund button and submit refund request")
        self.manual_refund_page.click_refund_button_and_submit_refund_request()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Click view refund log button and verify part-payment details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_part_payment_details("eBucks", "Paygate")

    @pytest.mark.qaba_460
    def test_process_refund_instant_eft_ozow(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Instant EFT Ozow."""

        self.step("Get orders from database")
        self.order_data.get_orders("${ozow_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click refund button and enter banking details")
        self.manual_refund_page.click_refund_button_and_enter_banking_details()

        self.step("Click EFT refund button and submit refund request")
        self.manual_refund_page.click_eft_refund_button_and_submit_refund_request()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("iPay")

    @pytest.mark.qaba_454
    def test_process_refund_donation_amount_not_refunded(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Donation Amount Not Refunded."""

        self.step("Get orders from database")
        self.order_data.get_orders("${donation_amount_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify refund amount excludes donation amount")
        self.manual_refund_page.verify_refund_amount_excludes_donation_amount()

        self.step("Click refund button and submit refund request")
        self.manual_refund_page.click_refund_button_and_submit_refund_request()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_463
    def test_process_refund_mobicred(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Mobicred."""

        self.step("Get orders from database")
        self.order_data.get_orders("${mobicred_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify that refund is not available")
        self.manual_refund_page.verify_that_refund_not_available()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("Mobicred")

    @pytest.mark.qaba_480
    def test_process_refund_staggered_mobicred_refunds(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Staggered Mobicred Refunds."""

        self.step("Create new TAL orders")
        self.utils.create_new_tal_orders("${2420369}", "Mobicred")

        self.step("Cancel order item")
        self.cancel_order_ep.cancel_order_item("${id_order_item1[0]}")

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify that refund is not available")
        self.manual_refund_page.verify_that_refund_not_available()

        self.step("Cancel order item")
        self.cancel_order_ep.cancel_order_item("${id_order_item2[0]}")

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Click view refund log button and verify details")
        self.manual_refund_page.click_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_466
    def test_cannot_process_refund_when_order_is_marked_as_risky(self):
        """Fin-Portal | Manual Refunds | Cannot Process Refund When Order Is Marked As Risky."""

        self.step("Get orders from database")
        self.order_data.get_orders("${risky_orders_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify order is not eligible for manual refund")
        self.manual_refund_page.verify_order_not_eligible_for_manual_refund()

    @pytest.mark.qaba_481
    def test_process_refund_deposit(self):
        """Fin-Portal | Manual Refunds | Processing A Refund | Deposit."""

        self.step("Get orders from database")
        self.order_data.get_orders("${deposit_sql}")

        self.step("Cancel paid order")
        self.cancel_order_ep.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Verify order is not eligible for manual refund")
        self.manual_refund_page.verify_order_not_eligible_for_manual_refund()
