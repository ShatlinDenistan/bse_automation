import os
from playwright.sync_api import Page

from pages.order_list import OrderListPage
from pages.login import LoginPage
from pages.side_nav import SideNav
from pages.top_nav import TopNav


class TestBase:
    page: Page
    login_page: LoginPage
    side_nav: SideNav
    top_nav: TopNav
    order_list_page: OrderListPage
