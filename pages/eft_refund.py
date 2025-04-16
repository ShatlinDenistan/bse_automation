from playwright.sync_api import Page

from base.page_base import PageBase

# Locators
option1_xpath = ("//span[contains(text(),'Identification required: Credit card')]", "Option 1")
option2_xpath = ("//span[contains(text(),'Identification and card details required')]", "Option 2")
option3_xpath = ("//span[contains(text(),'Identification required: Payfast & Ozow')]", "Option 3")
option4_xpath = ("//span[contains(text(),'Identification not accepted')]", "Option 4")
option5_xpath = ("//span[contains(text(),'Identification not received: Payfast & Ozow')]", "Option 5")


class EftRefundPage(PageBase):
    """Page object for EFT Refund functionality"""

    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)
        self.option1_xpath = self.locator(option1_xpath)
        self.option2_xpath = self.locator(option2_xpath)
        self.option3_xpath = self.locator(option3_xpath)
        self.option4_xpath = self.locator(option4_xpath)
        self.option5_xpath = self.locator(option5_xpath)
