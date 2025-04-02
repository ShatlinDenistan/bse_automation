from base.test_base import TestBase


class TestLogin(TestBase):

    def test_cancel_order(self):
        """Test cancel order"""

        # step 1: Open order list page
        self.top_nav.expand_side_bar()
        self.side_nav.click_order_list()

        # step 2: Confirm if in order list page
        self.order_list_page.confirm_if_in_page()

        # step 3: Cancel Order
        self.order_list_page.cancel_order()
