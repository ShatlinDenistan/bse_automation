from base.page_base import PageBase


class SideNavPO(PageBase):
    """Page object for the Side Navigation functionality."""

    # region Navigation Properties
    @property
    def home_link(self):
        locator = self.page.get_by_role("link", name="Home")
        return self.locator(locator, "Home link")

    # region Order Related Links
    @property
    def order_list_link(self):
        locator = self.page.get_by_role("link", name="Order List")
        return self.locator(locator, "Order List link")

    @property
    def financial_orders_link(self):
        locator = self.page.get_by_role("link", name="Financial Orders")
        return self.locator(locator, "Financial Orders link")

    # endregion

    # region Refund Related Links

    @property
    def eft_refunds_link(self):
        locator = self.page.get_by_role("link", name="EFT Refunds")
        return self.locator(locator, "EFT Refunds link")

    @property
    def escalated_refunds_link(self):
        locator = self.page.get_by_role("link", name="Escalated Refunds")
        return self.locator(locator, "Escalated Refunds link")

    # endregion

    # region Payment Related Links

    @property
    def deposit_match_link(self):
        locator = self.page.get_by_role("link", name="Deposit Match")
        return self.locator(locator, "Deposit Match link")

    # endregion

    # region Risk Management Links

    @property
    def risk_queue_link(self):
        locator = self.page.get_by_role("link", name="Risk Queue")
        return self.locator(locator, "Risk Queue link")

    # endregion
