"""
Tests for Fin-Portal Manual Refund functionality.
This file contains tests that verify the various manual refund scenarios
using different payment methods in Fin-Portal.
"""

import pytest
from base.test_base import TestBase


class TestFinPortalManualRefundSanity(TestBase):
    """Test cases for Fin-Portal Manual Refund functionality."""

    @pytest.mark.qaba_458
    def test_manual_refund_credit_card_payu(self):
        """
        Test manual refund with Credit Card using PayU.

        Steps:
        1. Get orders from database using paygate_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Click refund button and submit refund request
        7. Search for the order
        8. View refund log and verify details for PayU
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("paygate_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Clicking refund button and submitting refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Viewing refund log and verifying details for PayU")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("PayU")

    @pytest.mark.qaba_457
    def test_manual_refund_cannot_process_when_customer_blacklisted(self):
        """
        Test that manual refund cannot be processed when customer is blacklisted.

        Steps:
        1. Get customers from database using blacklisted_sql
        2. Create new TAL orders with Credit Card
        3. Cancel paid order
        4. Search for the order
        5. Expand customer credit accordion
        6. Expand order items accordion and click refund
        7. Verify order is not eligible for manual refund
        """
        self.step("Getting customers from database")
        self.database.get_customers_from_database("blacklisted_sql")

        self.step("Creating new TAL orders with Credit Card")
        customer_id = self.utils.get_env("customer_ids[0]")
        self.database.create_new_tal_orders(customer_id, "Credit Card")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying order is not eligible for manual refund")
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(order_id)

    @pytest.mark.qaba_459
    def test_manual_refund_masterpass(self):
        """
        Test manual refund with Masterpass payment.

        Steps:
        1. Get orders from database using masterpass_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Click refund button and enter banking details
        7. Click EFT refund button and submit refund request
        8. Search for the order
        9. View refund log and verify details for Paygate
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("masterpass_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Clicking refund button and entering banking details")
        self.manual_refund_page.click_the_refund_button_and_enter_banking_details()

        self.step("Clicking EFT refund button and submitting refund request")
        self.manual_refund_page.click_the_eft_refund_button_and_submit_refund_request()

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Viewing refund log and verifying details for Paygate")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_464
    def test_manual_refund_sbux_nsfas_wallet(self):
        """
        Test manual refund with sBux/NSFAS Wallet.

        Steps:
        1. Get orders from database using sbux_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Click refund button and submit refund request
        7. Search for the order
        8. View refund log and verify details for sBux
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("sbux_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Clicking refund button and submitting refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Viewing refund log and verifying details for sBux")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("sBux")

    @pytest.mark.qaba_464
    def test_manual_refund_excludes_coupon_amount(self):
        """
        Test that manual refund excludes coupon amount.

        Steps:
        1. Get orders from database using order_with_coupon_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand order items accordion and click refund
        5. Verify that refund amount excludes coupon amount
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("order_with_coupon_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying that refund amount excludes coupon amount")
        order_total = self.utils.get_env("order_total")
        order_discount = self.utils.get_env("order_discount")
        order_shipping = self.utils.get_env("order_shipping")
        self.manual_refund_page.verify_that_refund_amount_excludes_coupon_amount(order_total, order_discount, order_shipping)

    @pytest.mark.qaba_467
    def test_manual_refund_credit_card_and_ebucks_part_payment(self):
        """
        Test manual refund with Credit Card and eBucks part payment.

        Steps:
        1. Get orders from database using cc_ebucks_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Click refund button and submit refund request
        7. Search for the order
        8. View refund log and verify part-payment details for eBucks and Paygate
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("cc_ebucks_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Clicking refund button and submitting refund request")
        date_time = self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Viewing refund log and verifying part-payment details for eBucks and Paygate")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_part_payment_details("eBucks", "Paygate", date_time)

    @pytest.mark.qaba_460
    def test_manual_refund_instant_eft_ozow(self):
        """
        Test manual refund with Instant EFT (Ozow).

        Steps:
        1. Get orders from database using ozow_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Click refund button and enter banking details
        7. Click EFT refund button and submit refund request
        8. Search for the order
        9. View refund log and verify details for iPay
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("ozow_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Clicking refund button and entering banking details")
        self.manual_refund_page.click_the_refund_button_and_enter_banking_details()

        self.step("Clicking EFT refund button and submitting refund request")
        self.manual_refund_page.click_the_eft_refund_button_and_submit_refund_request()

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Viewing refund log and verifying details for iPay")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("iPay")

    @pytest.mark.qaba_454
    def test_manual_refund_donation_amount_not_refunded(self):
        """
        Test that manual refund excludes donation amount.

        Steps:
        1. Get orders from database using donation_amount_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Verify that refund amount excludes donation amount
        7. Click refund button and submit refund request
        8. Search for the order
        9. View refund log and verify details for Paygate
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("donation_amount_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying that refund amount excludes donation amount")
        order_total = self.utils.get_env("order_total")
        donation_amount = self.utils.get_env("donation_amount")
        order_shipping = self.utils.get_env("order_shipping")
        self.manual_refund_page.verify_that_refund_amount_excludes_coupon_amount(order_total, donation_amount, order_shipping)

        self.step("Clicking refund button and submitting refund request")
        self.manual_refund_page.click_the_refund_button_and_submit_refund_request()

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Viewing refund log and verifying details for Paygate")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_463
    def test_manual_refund_mobicred(self):
        """
        Test manual refund with Mobicred payment.

        Steps:
        1. Get orders from database using mobicred_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Verify that refund is not available
        7. Search for the order
        8. Expand customer credit accordion
        9. View refund log and verify details for Mobicred
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("mobicred_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying that refund is not available")
        self.manual_refund_page.verify_that_refund_not_available(order_id)

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Viewing refund log and verifying details for Mobicred")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Mobicred")

    @pytest.mark.qaba_480
    def test_manual_refund_staggered_mobicred_refunds(self):
        """
        Test staggered Mobicred refunds.

        Steps:
        1. Create new TAL orders with Mobicred
        2. Cancel order item
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Verify that refund is not available
        7. Cancel another order item
        8. Search for the order
        9. Expand customer credit accordion
        10. View refund log and verify details for Paygate
        """
        self.step("Creating new TAL orders with Mobicred")
        self.database.create_new_tal_orders("2420369", "Mobicred")

        self.step("Cancelling order item")
        order_item_id = self.utils.get_env("id_order_item1[0]")
        self.cancel_order.cancel_order_item(order_item_id)

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying that refund is not available")
        self.manual_refund_page.verify_that_refund_not_available(order_id)

        self.step("Cancelling another order item")
        order_item_id2 = self.utils.get_env("id_order_item2[0]")
        self.cancel_order.cancel_order_item(order_item_id2)

        self.step("Searching for the order")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Viewing refund log and verifying details for Paygate")
        self.manual_refund_page.click_the_view_refund_log_button_and_verify_details("Paygate")

    @pytest.mark.qaba_466
    def test_manual_refund_cannot_process_when_order_is_marked_as_risky(self):
        """
        Test that manual refund cannot be processed when order is marked as risky.

        Steps:
        1. Get orders from database using risky_orders_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Verify that order is not eligible for manual refund
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("risky_orders_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying order is not eligible for manual refund")
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(order_id)

    @pytest.mark.qaba_481
    def test_manual_refund_deposit(self):
        """
        Test manual refund with deposit payment.

        Steps:
        1. Get orders from database using deposit_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Verify that order is not eligible for manual refund
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("deposit_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.manual_refund_page.expand_the_customer_credit_accordion_under_customer_info()

        self.step("Expanding order items accordion and clicking refund")
        self.manual_refund_page.on_order_view_page_expand_the_order_items_accordion_and_click_refund(order_id)

        self.step("Verifying order is not eligible for manual refund")
        self.manual_refund_page.verify_that_order_is_not_eligible_for_manual_refund(order_id)
