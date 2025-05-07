from base.page_base import PageBase


class TopNavPO(PageBase):
    """Page object for the Top Navigation functionality."""

    # region Search Container

    @property
    def search_bar(self):
        selector = "//div[@id='root']"
        return self.locator(selector, "Search bar")

    # endregion

    # region Search Inputs and Buttons

    @property
    def txt_search(self):
        selector = "//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/input[1]"
        return self.locator(selector, "Search text field")

    @property
    def btn_search_button(self):
        selector = "//body/div[@id='root']/div[2]/div[1]/form[1]/div[1]/button[1]"
        return self.locator(selector, "Search button")

    # endregion

    # region Search Dropdown Options

    @property
    def ddl_search(self):
        selector = "//div[contains(text(),'-- all --')]"
        return self.locator(selector, "Search dropdown")

    @property
    def ddl_customer(self):
        selector = "//span[contains(text(),'Customer')]"
        return self.locator(selector, "Customer dropdown option")

    @property
    def ddl_order(self):
        selector = "//span[contains(text(),'Order Number')]"
        return self.locator(selector, "Order dropdown option")

    # endregion

    # region Customer Search Elements

    @property
    def cs_close_icon(self):
        selector = "//button[@class='close-icon']"
        return self.locator(selector, "Close icon")

    @property
    def cs_search_txt(self):
        selector = "//input[@id='search-text']"
        return self.locator(selector, "Customer search text field")

    @property
    def cs_search_btn(self):
        selector = "//button[@id='search-button']"
        return self.locator(selector, "Customer search button")

    # endregion

    # region Navigation Links

    @property
    def expand_side_bar_link(self):
        locator = self.page.get_by_text("Finance Portal")
        return self.locator(locator, "Expand side bar link")

    # endregion
