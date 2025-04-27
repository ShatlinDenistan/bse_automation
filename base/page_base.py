from playwright.sync_api import Page, expect

from base.playwright_utils import PlaywrightUtils
from data.db.customer_data import CustomerData
from data.db.order_data import OrderData
from data.queries.customer_queries import CustomerQueries
from data.queries.donation_queries import DonationQueries
from data.queries.order_item_queries import OrderItemQueries
from data.queries.order_queries import OrderQueries
from data.test_data_files import TestDataFiles

# Module-level constants

PAGE_SIZE_DROPDOWN = "//div[.='Show 15 Items']"
SHOW_50_ITEMS_SPAN = "//span[.='50']"
SHOW_15_ITEMS_SPAN = "//span[.='15']"
SHOW_30_ITEMS_SPAN = "//span[.='30']"
SHOW_10_ITEMS_SPAN = "//span[.='10']"


class PageBase(PlaywrightUtils):

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.page_size_dropdown = self.locator(PAGE_SIZE_DROPDOWN, "Page Size Dropdown")
        self.show_50_items_span = self.locator(SHOW_50_ITEMS_SPAN, "Show 50 Items Option")
        self.show_15_items_span = self.locator(SHOW_15_ITEMS_SPAN, "Show 15 Items Option")
        self.show_30_items_span = self.locator(SHOW_30_ITEMS_SPAN, "Show 30 Items Option")
        self.show_10_items_span = self.locator(SHOW_10_ITEMS_SPAN, "Show 10 Items Option")
        self.customer_data = CustomerData()
        self.order_data = OrderData()
        self.customer_queries = CustomerQueries()
        self.donation_queries = DonationQueries()
        self.order_item_queries = OrderItemQueries()
        self.order_queries = OrderQueries()
        self.test_data_files = TestDataFiles()

    def set_page_size(self, page_size=50):
        self.page_size_dropdown.scroll_into_view_if_needed()
        self.page_size_dropdown.click()
        match page_size:
            case 50:
                expect(self.show_50_items_span).to_be_visible(timeout=5000)
                self.show_50_items_span.click()
            case 15:
                expect(self.show_15_items_span).to_be_visible(timeout=5000)
                self.show_15_items_span.click()
            case 30:
                expect(self.show_30_items_span).to_be_visible(timeout=5000)
                self.show_30_items_span.click()
            case 10:
                expect(self.show_10_items_span).to_be_visible(timeout=5000)
                self.show_10_items_span.click()
            case _:
                raise ValueError("Page size not supported")
