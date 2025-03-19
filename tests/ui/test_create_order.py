from base.test_base import TestBase


class TestLogin(TestBase):

    def test_create_order(self):
        """Test create order"""
        # Shatlin

        # step 1: Open order list page
        self.top_nav.expand_side_bar()
        self.side_nav.click_order_list()

        # step 2: Confirm if in order list page
        self.order_list_page.confirm_if_in_page()

        # Sli: Fin-Portal | Order List | Cancel an order
        # Thandeka: Fin-Portal | Order List | Authorise Multiple Orders
