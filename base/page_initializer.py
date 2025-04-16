from playwright.sync_api import Page

from pages.order_list import OrderListPage
from pages.login import LoginPage
from pages.side_nav import SideNav
from pages.top_nav import TopNav
from pages.customer_credit import CustomerCreditPage
from pages.customer_view import CustomerViewPage
from pages.deposit_match import DepositMatchPage
from pages.edit_order import EditOrderPage
from pages.eft_refund import EftRefundPage
from pages.manual_override import ManualOverridePage
from pages.order_credit import OrderCreditPage
from pages.order_view import OrderViewPage
from pages.reinstate_order import ReinstateOrderPage
from pages.risk_queue import RiskQueuePage
from pages.search import SearchPage
from pages.vouchers import VouchersPage


class PageInitializer:
    """Handles page object initialization"""

    def initialize_pages(self, page: Page):
        """Test base functionality."""
        self.login_page = LoginPage(page)
        self.side_nav = SideNav(page)
        self.top_nav = TopNav(page)
        self.order_list_page = OrderListPage(page)
        self.customer_credit_page = CustomerCreditPage(page)
        self.customer_view_page = CustomerViewPage(page)
        self.deposit_match_page = DepositMatchPage(page)
        self.edit_order_page = EditOrderPage(page)
        self.eft_refund_page = EftRefundPage(page)
        self.manual_override_page = ManualOverridePage(page)
        self.order_credit_page = OrderCreditPage(page)
        self.order_view_page = OrderViewPage(page)
        self.reinstate_order_page = ReinstateOrderPage(page)
        self.risk_queue_page = RiskQueuePage(page)
        self.search_page = SearchPage(page)
        self.vouchers_page = VouchersPage(page)
