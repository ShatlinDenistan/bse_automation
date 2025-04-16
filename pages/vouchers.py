from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
menu_btn = "xpath=//i[@aria-hidden='true' and @class='content large icon']"
vouchers_menu_option = "xpath=//body/div[@id='root']/div[1]/a[2]"
results_table = "xpath=//*[@class='ui small celled compact table']"
redeemed_status_dropdown = "xpath=//*[@id='root']/div[3]/div/div/div/form/div/div/div[4]/div/div/div[1]"
redeemed_status_available = "xpath=//span[text()='Available']"
paid_status_dropdown = "xpath=//*[@id='root']/div[3]/div/div/div/form/div/div/div[5]/div/div"
paid_status_option = "xpath=//span[text()='Paid']"
apply_search_filter = "xpath=//button[contains(text(), 'Filter')]"
order_id_checkbox = "xpath=//*[@id='root']/div[3]/div/div/div/table/tbody/tr[1]/td[1]/div"
expire_btn = "xpath=//*[@id='root']/div[3]/div/div/div/table/tfoot/tr/th/div/div[3]/button"
verification_message = "xpath=//div[contains(text(),'Successfully processed 1 item(s)')]"
close_icon = "xpath=//i[@aria-hidden='true' and @class='close icon']"


class VouchersPage(PageBase):
    """Page object for Vouchers functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.menu_btn = self.locator(menu_btn)
        self.vouchers_menu_option = self.locator(vouchers_menu_option)
        self.results_table = self.locator(results_table)
        self.redeemed_status_dropdown = self.locator(redeemed_status_dropdown)
        self.redeemed_status_available = self.locator(redeemed_status_available)
        self.paid_status_dropdown = self.locator(paid_status_dropdown)
        self.paid_status_option = self.locator(paid_status_option)
        self.apply_search_filter = self.locator(apply_search_filter)
        self.order_id_checkbox = self.locator(order_id_checkbox)
        self.expire_btn = self.locator(expire_btn)
        self.verification_message = self.locator(verification_message)
        self.close_icon = self.locator(close_icon)

    def navigate_to_vouchers(self):
        self.menu_btn.click()
        self.vouchers_menu_option.click()
        self.page.wait_for_selector(self.results_table)

    def filter_by_redeemed_and_paid_status(self):
        self.page.wait_for_selector(self.results_table)
        self.redeemed_status_dropdown.click()
        self.redeemed_status_available.click()
        self.paid_status_dropdown.click()
        self.paid_status_option.click()
        self.apply_search_filter.click()
        self.page.wait_for_selector(self.results_table)

    def select_and_cancel_a_voucher(self):
        self.order_id_checkbox.click()
        self.expire_btn.click()
        self.page.wait_for_selector(self.verification_message)
        self.close_icon.click()
