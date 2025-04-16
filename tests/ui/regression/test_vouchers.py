import pytest
from base.test_base import TestBase


@pytest.mark.ui
class TestVouchers(TestBase):
    """Vouchers page tests for the Finance Portal"""

    @pytest.mark.QABA_178
    def test_cancel_voucher(self):
        """Verify that a user can cancel a voucher on the vouchers page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by redeemed and paid status")
        self.vouchers_page.filter_by_redeemed_and_paid_status()

        self.step("Select and cancel a voucher")
        self.vouchers_page.select_and_cancel_voucher()

    @pytest.mark.QABA_176
    def test_activate_voucher(self):
        """Verify that a user can activate a canceled voucher"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by canceled redeem status")
        self.vouchers_page.filter_by_canceled_redeem_status()

        self.step("Select and activate a voucher")
        self.vouchers_page.select_and_activate_voucher()

        self.step("Verify voucher status")
        self.vouchers_page.verify_voucher_status()

    @pytest.mark.QABA_192
    def test_update_voucher_to_not_paid(self):
        """Verify that a user can Update a Voucher from Paid to Not Paid"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by paid status")
        self.vouchers_page.filter_by_paid_status()

        self.step("Select and update to not paid")
        self.vouchers_page.select_and_update_to_not_paid()

    @pytest.mark.QABA_192
    def test_update_voucher_to_paid(self):
        """Verify that a user can Update a Voucher from Not Paid to Paid"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by not paid status")
        self.vouchers_page.filter_by_not_paid_status()

        self.step("Select and update to paid")
        self.vouchers_page.select_and_update_to_paid()

    @pytest.mark.QABSE_1384
    def test_filter_by_custom_date_range(self):
        """Verify that a user can filter using a custom date range on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by date range")
        self.vouchers_page.filter_by_date_range()

    @pytest.mark.QABSE_1384
    def test_filter_by_voucher_category(self):
        """Verify that a user can filter by a voucher category on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by voucher category")
        self.vouchers_page.filter_by_voucher_category()

    @pytest.mark.QABSE_1384
    def test_filter_by_redeemed_status(self):
        """Verify that a user can filter by Redeemed Status on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by redeemed status")
        self.vouchers_page.filter_by_redeemed_status()

    @pytest.mark.QABSE_1384
    def test_filter_by_combination_of_multiple_filter_options(self):
        """Verify that a user can apply multiple filters at once on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by multiple filter options")
        self.vouchers_page.filter_by_multiple_filter_options()

    @pytest.mark.QABSE_1384
    def test_filter_by_order_id(self):
        """Verify that a user can filter by Order ID on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter using order ID")
        self.vouchers_page.filter_using_order_id()

    @pytest.mark.QABSE_195
    def test_filter_by_voucher_code(self):
        """Verify that a user can filter by voucher code on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by voucher code")
        self.vouchers_page.filter_by_voucher_code()

    @pytest.mark.QABSE_193
    def test_filter_by_customer_id(self):
        """Verify that a user can search for customer who purchased a voucher on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter using customer ID")
        self.vouchers_page.filter_using_customer_id()

    @pytest.mark.QABSE_195
    def test_filter_by_used_by_customer_id(self):
        """Verify that a user can filter by customer ID on the voucher page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Filter by redeemed status")
        self.vouchers_page.filter_by_redeemed_status()

        self.step("Filter by used by customer ID")
        self.vouchers_page.filter_by_used_by_customer_id()

    @pytest.mark.QABSE_175
    def test_send_email(self):
        """Verify that a user can send an email from the Vouchers page"""
        self.step("Navigate to vouchers page")
        self.vouchers_page.navigate_to_vouchers()

        self.step("Select and send email")
        self.vouchers_page.select_and_send_email()

        self.step("Verify email was sent successfully")
        self.vouchers_page.verify_email_was_sent_successfully()
