from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
search_bar = "xpath=//div[@id='root']"
txt_search = "xpath=//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/input[1]"
ddl_search = "xpath=//div[contains(text(),'-- all --')]"
ddl_customer = "xpath=//span[contains(text(),'Customer')]"
ddl_order = "xpath=//span[contains(text(),'Order Number')]"
btn_search_button = "xpath=//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/button[1]"


class SearchPage(PageBase):
    """Page object for Search functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.search_bar = self.locator(search_bar)
        self.txt_search = self.locator(txt_search)
        self.ddl_search = self.locator(ddl_search)
        self.ddl_customer = self.locator(ddl_customer)
        self.ddl_order = self.locator(ddl_order)
        self.btn_search_button = self.locator(btn_search_button)

    def search_for_customer(self, search: str):
        self.search_bar.click()
        self.txt_search.click()
        self.txt_search.fill(search)
        self.ddl_search.click()
        self.ddl_customer.click()
        self.btn_search_button.click()
        self.page.wait_for_selector("text=Customer Info")

    def search_for_order(self, search: str):
        self.search_bar.click()
        self.txt_search.click()
        self.txt_search.fill(search)
        self.ddl_search.click()
        self.ddl_order.click()
        self.btn_search_button.click()
        self.page.wait_for_selector("text=Customer Info")

    def search_for_rrn(self, search: str):
        self.page.click("xpath=//button[@class='csCloseIcon']")
        self.page.click("xpath=//input[@class='csSearchTxt']")
        self.page.fill("xpath=//input[@class='csSearchTxt']", search)
        self.page.click("xpath=//button[@class='csSearchBtn']")
