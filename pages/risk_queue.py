from playwright.sync_api import Page

from base.page_base import PageBase

# Locators
all_order_id_columns = "//td[position() = (count(//th[text()='Order ID']/preceding-sibling::th) + 1)]"
apply_filter_btn = "//button[contains(text(), 'Filter')]"
checkbox_daily_deals = "//*[@id='root']/div[3]/div/div/form/div/div/div[1]/div/div/div[1]/div"
clear_filter_btn = "//button[contains(text(), 'Clear Filter')]"
clear_risk_btn = "//body/div[@id='root']/div[3]/div/div/table/tfoot/tr/th/div/div[1]"


class RiskQueuePage(PageBase):
    """Page object for Risk Queue functionality"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.all_order_id_columns = self.locator(all_order_id_columns)
        self.apply_filter_btn = self.locator(apply_filter_btn)
        self.checkbox_daily_deals = self.locator(checkbox_daily_deals)
        self.clear_filter_btn = self.locator(clear_filter_btn)
        self.clear_risk_btn = self.locator(clear_risk_btn)
