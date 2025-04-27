from pos.topnav_po import TopNavPO


class TopNavComponent(TopNavPO):

    def expand_side_bar(self):
        """Expand side bar"""
        self.step("Expanding the side bar")
        self.click(self.expand_side_bar_link)

    def search_for_customer(self, search_term):
        """Search for a customer using the provided search term."""
        self.click(self.search_bar)
        self.click(self.txt_search)
        self.fill(self.txt_search, search_term)
        self.click(self.ddl_search)
        self.click(self.ddl_customer)
        self.click(self.btn_search_button)
        self.wait_for_text("Customer Info", timeout=self.config.MIN_TIMEOUT)

    def search_for_order(self, search_term):
        """Search for an order using the provided search term."""
        self.click(self.search_bar)
        self.click(self.txt_search)
        self.fill(self.txt_search, search_term)
        self.click(self.ddl_search)
        self.click(self.ddl_order)
        self.click(self.btn_search_button)
        self.wait_for_text("Customer Info", timeout=self.config.MIN_TIMEOUT)

    def search_for_rrn(self, search_term):
        """Search for a RRN using the provided search term."""
        self.click(self.cs_close_icon)
        self.click(self.cs_search_txt)
        self.fill(self.cs_search_txt, search_term)
        self.click(self.cs_search_btn)
