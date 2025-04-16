"""
Tests for Fin-Portal Manual Override functionality.
This file contains tests that verify the various manual override scenarios
using different payment methods in Fin-Portal.
"""

import pytest
from base.test_base import TestBase


class TestFinPortalManualOverrideSanity(TestBase):
    """Test cases for Fin-Portal Manual Override functionality."""

    @pytest.mark.qaba_488
    def test_manual_override_blacklisted_customer(self):
        """
        Test manual override with EFT for a blacklisted customer.

        Steps:
        1. Get orders from database using blacklisted_sql
        2. Create new TAL orders with Credit Card
        3. Cancel paid order
        4. Search for the order
        5. Expand customer credit accordion
        6. Expand order items accordion and click refund
        7. Complete manual override form with EFT
        8. Capture EFT banking details
        9. Confirm override and view logs
        10. Verify manual override details for EFT
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("blacklisted_sql")

        self.step("Creating new TAL orders with Credit Card")
        customer_id = self.utils.get_env("customer_ids[0]")
        self.database.create_new_tal_orders(customer_id, "Credit Card")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form with EFT")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capturing EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for EFT")
        self.manual_override_page.verify_override_details("EFT")

    @pytest.mark.qaba_500
    def test_manual_override_ebucks_credit_card_and_tal_credit_part_payment(self):
        """
        Test manual override with eBucks, Credit Card and TAL credit part payment.

        Steps:
        1. Get orders from database using cc_ebucks_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Get refund amounts for payment methods
        7. Complete manual override form for Credit Card and eBucks
        8. Confirm override and view logs
        9. Verify manual override details for Paygate
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("cc_ebucks_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Getting refund amounts for payment methods")
        cc_amount, ebucks_amount = self.manual_override_page.get_refund_amounts_for_payment_methods()

        self.step("Completing manual override form for Credit Card and eBucks")
        self.manual_override_page.complete_override_form_for_credit_card_and_ebucks(cc_amount, ebucks_amount)

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for Paygate")
        self.manual_override_page.verify_override_details("Paygate")

    @pytest.mark.qaba_489
    def test_manual_override_ebucks_and_credit_card_part_payment(self):
        """
        Test manual override with eBucks and Credit Card part payment.

        Steps:
        1. Get orders from database using cc_ebucks_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Get refund amounts for payment methods
        7. Complete manual override form for Credit Card and eBucks
        8. Confirm override and view logs
        9. Verify manual override details for Paygate
        10. Verify admin notes for both manual overrides
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("cc_ebucks_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Getting refund amounts for payment methods")
        cc_amount, ebucks_amount = self.manual_override_page.get_refund_amounts_for_payment_methods()

        self.step("Completing manual override form for Credit Card and eBucks")
        self.manual_override_page.complete_override_form_for_credit_card_and_ebucks(cc_amount, ebucks_amount)

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for Paygate")
        self.manual_override_page.verify_override_details("Paygate")

        self.step("Verifying admin notes for both manual overrides")
        self.manual_override_page.verify_dual_payment_admin_notes()

    @pytest.mark.qaba_502
    def test_manual_override_deposit(self):
        """
        Test manual override with deposit payment.

        Steps:
        1. Get orders from database using deposit_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Complete manual override form with EFT
        7. Capture EFT banking details
        8. Confirm override and view logs
        9. Verify manual override details for Deposit
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("deposit_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form with EFT")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capturing EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for Deposit")
        self.manual_override_page.verify_override_details("Deposit")

    @pytest.mark.qaba_487
    def test_manual_override_instant_eft_ozow(self):
        """
        Test manual override with Instant EFT (Ozow).

        Steps:
        1. Get orders from database using ozow_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Complete manual override form with EFT
        7. Capture EFT banking details
        8. Confirm override and view logs
        9. Verify manual override details for iPay
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("ozow_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form with EFT")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capturing EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for iPay")
        self.manual_override_page.verify_override_details("iPay")

    @pytest.mark.qaba_485
    def test_manual_override_ebucks(self):
        """
        Test manual override with eBucks payment.

        Steps:
        1. Get orders from database using ebucks_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Complete manual override form for eBucks
        7. Confirm override and view logs
        8. Verify manual override details for eBucks
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("ebucks_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form for eBucks")
        refund_amount = self.manual_auth_page.get_refund_amount_for_ebucks()
        self.manual_override_page.complete_override_form("eBucks", refund_amount, "Test eBucks Override")

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for eBucks")
        self.manual_override_page.verify_override_details("eBucks")

    @pytest.mark.qaba_501
    def test_manual_override_sbux_nsfas_wallet(self):
        """
        Test manual override with sBux/NSFAS Wallet.

        Steps:
        1. Create new TAL orders with sBux
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Complete manual override form with EFT
        7. Capture EFT banking details
        8. Confirm override and view logs
        9. Verify manual override details for Deposit
        """
        self.step("Creating new TAL orders with sBux")
        self.database.create_new_tal_orders("13866233", "sBux")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form with EFT")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capturing EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for Deposit")
        self.manual_override_page.verify_override_details("Deposit")

    @pytest.mark.qaba_504
    def test_manual_override_refund_additional_donation_charge(self):
        """
        Test manual override with refund of additional donation charge.

        Steps:
        1. Get orders from database using credit_card_donation_order_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit section and click credit button
        5. Enter donation and comment
        6. Add credit and confirm
        7. Expand order items accordion and click refund
        8. Complete manual override form with EFT
        9. Capture EFT banking details
        10. Confirm override and view logs
        11. Verify manual override details for EFT
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("credit_card_donation_order_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding customer credit section and clicking credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_credit_button()

        self.step("Entering donation and comment")
        self.order_credit_page.enter_donation_and_comment()

        self.step("Adding credit and confirming")
        self.order_credit_page.select_add_credit_button_and_confirm()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form with EFT")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capturing EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for EFT")
        self.manual_override_page.verify_override_details("EFT")

    @pytest.mark.qaba_491
    def test_manual_override_eft_original_payment_credit_card_and_ebucks(self):
        """
        Test manual override with EFT when original payment was Credit Card and eBucks.

        Steps:
        1. Get orders from database using cc_ebucks_sql
        2. Cancel paid order
        3. Search for the order
        4. Expand customer credit accordion
        5. Expand order items accordion and click refund
        6. Complete manual override form with EFT
        7. Capture EFT banking details
        8. Confirm override and view logs
        9. Verify manual override details for EFT
        """
        self.step("Getting orders from database")
        self.database.get_orders_from_database("cc_ebucks_sql")

        self.step("Cancelling paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Searching for the order")
        order_id = self.utils.get_env("order_ids[0]")
        self.search_page.search_for_order(order_id)

        self.step("Expanding the customer credit accordion")
        self.order_view_page.expand_customer_credit_accordion()

        self.step("Expanding order items accordion and clicking refund")
        self.order_view_page.expand_order_items_accordion_and_click_refund()

        self.step("Completing manual override form with EFT")
        self.manual_override_page.click_manual_override_button_and_complete_override_form_eft()

        self.step("Capturing EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirming manual override and viewing logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verifying manual override details for EFT")
        self.manual_override_page.verify_override_details("EFT")
