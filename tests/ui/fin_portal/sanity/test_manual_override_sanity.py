"""Manual Override Sanity Tests."""

import pytest
from base.test_base import TestBase


class TestManualOverrideSanity(TestBase):
    """Manual Override Sanity Test class."""

    @pytest.mark.qaba_488
    def test_manual_override_blacklisted_customer(self):
        """Fin-Portal | Manual Override | Blacklisted Customer."""

        self.step("Get orders from database")
        self.order_data.get_orders("${blacklisted_sql}")

        self.step("Create new TAL orders")
        self.utils.create_new_tal_orders("${customer_ids[0]}", "Credit Card")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form for EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("${lstEFT}")

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("EFT")

    @pytest.mark.qaba_500
    def test_manual_override_ebucks_credit_card_tal_credit_part_payment(self):
        """Fin-Portal | Manual Override | eBucks, Credit Card And Tal Credit Part Payment."""

        self.step("Get orders from database")
        self.order_data.get_orders("${cc_ebucks_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Get refund amount for payment methods")
        self.manual_override_page.get_refund_amount_for_payment_methods()

        self.step("Click manual override button and complete override form for Credit Card and eBucks")
        self.manual_override_page.click_manual_override_button_and_complete_form_cc_ebucks("${lstCreditCard}", "${lsteBucks}")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("Paygate")

    @pytest.mark.qaba_489
    def test_manual_override_ebucks_and_credit_card_part_payment(self):
        """Fin-Portal | Manual Override | eBucks And Credit Card Part Payment."""

        self.step("Get orders from database")
        self.order_data.get_orders("${cc_ebucks_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Get refund amount for payment methods")
        self.manual_override_page.get_refund_amount_for_payment_methods()

        self.step("Click manual override button and complete override form for Credit Card and eBucks")
        self.manual_override_page.click_manual_override_button_and_complete_form_cc_ebucks("${lstCreditCard}", "${lsteBucks}")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("Paygate")

        self.step("Verify admin notes for manual overrides")
        self.manual_override_page.verify_two_admin_notes_for_manual_overrides()

    @pytest.mark.qaba_502
    def test_manual_override_deposit(self):
        """Fin-Portal | Manual Override | Deposit."""

        self.step("Get orders from database")
        self.order_data.get_orders("${deposit_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form for EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("${lstEFT}")

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("Deposit")

    @pytest.mark.qaba_487
    def test_manual_override_instant_eft_ozow(self):
        """Fin-Portal | Manual Override | Instant EFT | Ozow."""

        self.step("Get orders from database")
        self.order_data.get_orders("${ozow_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form for EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("${lstEFT}")

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("iPay")

    @pytest.mark.qaba_485
    def test_manual_override_ebucks(self):
        """Fin-Portal | Manual Override | eBucks."""

        self.step("Get orders from database")
        self.order_data.get_orders("${ebucks_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form")
        self.manual_override_page.click_manual_override_button_and_complete_form("${lsteBucks}")

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("eBucks")

    @pytest.mark.qaba_501
    def test_manual_override_sbux_nsfas_wallet(self):
        """Fin-Portal | Manual Override | sBux/NSFAS Wallet."""

        self.step("Create new TAL orders")
        self.utils.create_new_tal_orders("${13866233}", "sBux")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.customer_view.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form for EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("${lstEFT}")

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("Deposit")

    @pytest.mark.qaba_504
    def test_manual_override_refund_additional_donation_charge(self):
        """Fin-Portal | Manual Override | Refund Additional Donation Charge."""

        self.step("Get orders from database")
        self.order_data.get_orders("${credit_card_donation_order_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand customer credit and click credit button for order")
        self.customer_view.expand_customer_credit_section_and_click_credit_button()

        self.step("Enter donation and comment")
        self.order_credit.enter_donation_and_comment()

        self.step("Select add credit button")
        self.order_credit.select_add_credit_button()

        self.step("Select OK on dialog")
        self.order_credit.select_ok_on_dialog()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form for EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("${lstEFT}")

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("EFT")

    @pytest.mark.qaba_491
    def test_manual_override_eft_original_payment_credit_card_and_ebucks(self):
        """Fin-Portal | Manual Override | EFT | Original Payment Method Is Credit Card And eBucks."""

        self.step("Get orders from database")
        self.order_data.get_orders("${cc_ebucks_sql}")

        self.step("Cancel paid order")
        self.cancel_order.cancel_paid_order()

        self.step("Search for order")
        self.top_nav.search_for_order("${order_ids[0]}")

        self.step("Expand the customer credit accordion under customer info")
        self.manual_refund_page.expand_customer_credit_accordion()

        self.step("Expand order items accordion and click refund")
        self.order_view.expand_order_items_accordion_and_click_refund()

        self.step("Click manual override button and complete override form for EFT")
        self.manual_override_page.click_manual_override_button_and_complete_form_eft("${lstEFT}")

        self.step("Capture EFT banking details")
        self.manual_override_page.capture_eft_banking_details()

        self.step("Confirm manual override and view logs")
        self.manual_override_page.confirm_manual_override_and_view_logs()

        self.step("Verify manual override details")
        self.manual_override_page.verify_manual_override_details("EFT")
