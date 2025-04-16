from playwright.sync_api import Page

from base.page_base import PageBase

# Locators
batch_download = ("//tbody/tr[1]/td[10]/div[1]/button[1]/i[1]", "Batch Download Button")
apply_filter = ("//button[contains(text(),'Apply Filter')]", "Apply Filter Button")
clear_filter = ("//button[contains(text(),'Clear Filter')]", "Clear Filter Button")
date_filter = ("//input[@name='dateRange']", "Date Filter Input")
batch_date = ("//td[contains(text(),'12-May-2023')]", "Batch Date")


class DepositMatchPage(PageBase):
    """Page object for Deposit Match functionality"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.batch_download = self.locator(batch_download)
        self.apply_filter = self.locator(apply_filter)
        self.clear_filter = self.locator(clear_filter)
        self.date_filter = self.locator(date_filter)
        self.batch_date = self.locator(batch_date)
