import os
from playwright.sync_api import expect, Page

from pages.order_list import OrderListPage
from pages.login import LoginPage
from pages.side_nav import SideNav
from pages.top_nav import TopNav


class TestLogin:

    page: Page
    login_page: LoginPage
    side_nav: SideNav
    top_nav: TopNav
    order_list_page: OrderListPage

    def test_create_order(self):

        # step 1: Open order list page
        self.top_nav.expand_side_bar()
        self.side_nav.click_order_list()

        # step 2: Confirm if in order list page
        self.order_list_page.confirm_if_in_page()

        pass
