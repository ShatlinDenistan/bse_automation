from base.test_base import TestBase


class TestOrders(TestBase):

    def test_authorize_order(self):
        """This test verifies if a valid order can be authorised"""
        self.step("Open order list page")
        self.top_nav.expand_side_bar()
        self.side_nav.click_order_list()

        self.step("Confirm if in order list page")
        self.order_list_page.confirm_if_in_page()

        self.step("Authorise Order")
        is_order_authoirized = self.order_list_page.authorize_order()
        assert is_order_authoirized is True, "Order was not authorized"

    def test_cancel_order(self):
        """Test cancel order"""

        self.step("Open order list page")
        self.top_nav.expand_side_bar()
        self.side_nav.click_order_list()

        self.step("Confirm if in order list page")
        self.order_list_page.confirm_if_in_page()

        self.step("Cancel Order")
        is_order_canceled = self.order_list_page.cancel_order()
        assert is_order_canceled is True, "Order was not canceled"

    def test_create_order(self):
        """Test create order"""

        self.step("Open order list page")
        self.top_nav.expand_side_bar()
        self.side_nav.click_order_list()

        self.step("Confirm if in order list page")
        self.order_list_page.confirm_if_in_page()

        # Sli: Fin-Portal | Order List | Cancel an order
        # Thandeka: Fin-Portal | Order List | Authorise Multiple Orders
