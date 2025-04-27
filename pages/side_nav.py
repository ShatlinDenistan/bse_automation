from pos.sidenav_po import SideNavPO


class SideNavComponent(SideNavPO):

    def click_deposit_match(self):
        self.click(self.deposit_match_link)

    def click_risk_queue(self):
        self.click(self.risk_queue_link)

    def click_home(self):
        self.click(self.home_link)

    def click_order_list(self):
        self.click(self.order_list_link)

    def click_financial_orders(self):
        self.click(self.financial_orders_link)

    def click_eft_refunds(self):
        self.click(self.eft_refunds_link)

    def click_escalated_refunds(self):
        self.click(self.escalated_refunds_link)
