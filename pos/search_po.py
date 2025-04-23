from base.page_base import PageBase

# Module-level constants for locators
SEARCH_BAR = "//div[@id='root']"
TXT_SEARCH = "//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/input[1]"
DDL_SEARCH = "//div[contains(text(),'-- all --')]"
DDL_CUSTOMER = "//span[contains(text(),'Customer')]"
DDL_ORDER = "//span[contains(text(),'Order Number')]"
BTN_SEARCH_BUTTON = "//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/button[1]"
CS_CLOSE_ICON = "//button[@class='close-icon']"  # Assumed based on usage in kwSearch.robot
CS_SEARCH_TXT = "//input[@id='search-text']"  # Assumed based on usage in kwSearch.robot
CS_SEARCH_BTN = "//button[@id='search-button']"  # Assumed based on usage in kwSearch.robot


class SearchPO(PageBase):
    """Page object for the Search functionality."""

    def __init__(self, page):
        super().__init__(page)
        self.search_bar = self.locator(SEARCH_BAR, "Search bar")
        self.txt_search = self.locator(TXT_SEARCH, "Search text field")
        self.ddl_search = self.locator(DDL_SEARCH, "Search dropdown")
        self.ddl_customer = self.locator(DDL_CUSTOMER, "Customer dropdown option")
        self.ddl_order = self.locator(DDL_ORDER, "Order dropdown option")
        self.btn_search_button = self.locator(BTN_SEARCH_BUTTON, "Search button")
        self.cs_close_icon = self.locator(CS_CLOSE_ICON, "Close icon")
        self.cs_search_txt = self.locator(CS_SEARCH_TXT, "Customer search text field")
        self.cs_search_btn = self.locator(CS_SEARCH_BTN, "Customer search button")
