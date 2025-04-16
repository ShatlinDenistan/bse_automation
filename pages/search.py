from playwright.sync_api import Page
from base.page_base import PageBase

# Locators as tuples with (xpath, description)
search_bar = ("//div[@id='root']", "Search Bar")
search_textbox = ("//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/input[1]", "Search Textbox")
search_dropdown = ("//div[contains(text(),'-- all --')]", "Search Type Dropdown")
customer_option = ("//span[contains(text(),'Customer')]", "Customer Option")
order_option = ("//span[contains(text(),'Order Number')]", "Order Number Option")
search_button = ("//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/button[1]", "Search Button")
cs_close_icon = ("//button[@class='close-icon']", "Close Icon")
cs_search_txt = ("//input[@placeholder='Search']", "Search Input")
cs_search_btn = ("//button[@type='submit']", "Search Submit Button")
customer_info_text = ("//div[contains(text(),'Customer Info')]", "Customer Info Text")


class SearchPage(PageBase):
    """Page object for Search functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        # Initialize all locators
        self.search_bar = self.locator(search_bar)
        self.search_textbox = self.locator(search_textbox)
        self.search_dropdown = self.locator(search_dropdown)
        self.customer_option = self.locator(customer_option)
        self.order_option = self.locator(order_option)
        self.search_button = self.locator(search_button)
        self.cs_close_icon = self.locator(cs_close_icon)
        self.cs_search_txt = self.locator(cs_search_txt)
        self.cs_search_btn = self.locator(cs_search_btn)
        self.customer_info_text = self.locator(customer_info_text)

    def search_for_customer(self, search_term: str):
        """Search for a customer using the given search term."""
        self.click(self.search_bar)
        self.click(self.search_textbox)
        self.fill(self.search_textbox, search_term)
        self.click(self.search_dropdown)
        self.click(self.customer_option)
        self.click(self.search_button)
        self.expect_to_be_visible(self.customer_info_text)

    def search_for_order(self, search_term: str):
        """Search for an order using the given search term."""
        self.click(self.search_bar)
        self.click(self.search_textbox)
        self.fill(self.search_textbox, search_term)
        self.click(self.search_dropdown)
        self.click(self.order_option)
        self.click(self.search_button)
        self.expect_to_be_visible(self.customer_info_text)

    def search_for_rrn(self, search_term: str):
        """Search for RRN using the given search term."""
        self.click(self.cs_close_icon)
        self.click(self.cs_search_txt)
        self.fill(self.cs_search_txt, search_term)
        self.click(self.cs_search_btn)
