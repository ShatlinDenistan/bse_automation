from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
addresses_accordion = "xpath=//span[contains(text(),'Addresses')]"
address_google_icon = "xpath=//*[@class='map small icon']"
allocate_credit_btn = "xpath=//button[contains(text(),'Allocate credit')]"
credit_history_table = "xpath=//*[@class='ui small celled compact table']"
available_credit = "xpath=//*[@class='ui green small circular horizontal label']"
customer_credit_accordion = "xpath=//span[contains(text(),'Customer Credit')]"
email_google_icon = "xpath=//*[@class='google icon']"
notes_dropdown = "xpath=//span[contains(text(),'Notes')]"
notes_edit_btn = "xpath=//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/button"
fin_notes_dropdown = "xpath=//span[contains(text(),'Fin Notes')]"
fin_notes_edit_btn = "xpath=//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/button"
verified_cellphone_icon = "xpath=//*[@id='root']/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div"


class CustomerViewPage(PageBase):
    """Page object for Customer View functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.addresses_accordion = self.locator(addresses_accordion)
        self.address_google_icon = self.locator(address_google_icon)
        self.allocate_credit_btn = self.locator(allocate_credit_btn)
        self.credit_history_table = self.locator(credit_history_table)
        self.available_credit = self.locator(available_credit)
        self.customer_credit_accordion = self.locator(customer_credit_accordion)
        self.email_google_icon = self.locator(email_google_icon)
        self.notes_dropdown = self.locator(notes_dropdown)
        self.notes_edit_btn = self.locator(notes_edit_btn)
        self.fin_notes_dropdown = self.locator(fin_notes_dropdown)
        self.fin_notes_edit_btn = self.locator(fin_notes_edit_btn)
        self.verified_cellphone_icon = self.locator(verified_cellphone_icon)

    def verify_customer_details(self):
        self.page.wait_for_selector(self.addresses_accordion)
        self.page.click(self.email_google_icon)
        self.page.wait_for_timeout(2000)
        window_handles = self.page.context.pages
        self.page = window_handles[0]
        self.page.wait_for_selector(self.email_google_icon)
        self.page.click(self.email_google_icon)
        self.page.wait_for_timeout(2000)
        window_handles = self.page.context.pages
        self.page = window_handles[0]
        assert self.page.is_visible(self.verified_cellphone_icon)

    def verify_notes_section_with_edit_option(self):
        self.page.wait_for_selector(self.notes_dropdown)
        self.page.click(self.notes_dropdown)
        assert self.page.is_visible(self.notes_edit_btn)
        self.page.click(self.notes_edit_btn)

    def verify_fin_notes_section_with_edit_option(self):
        self.page.wait_for_selector(self.fin_notes_dropdown)
        self.page.click(self.fin_notes_dropdown)
        assert self.page.is_visible(self.fin_notes_edit_btn)
        self.page.click(self.fin_notes_edit_btn)

    def verify_customer_credit(self):
        self.page.wait_for_selector(self.customer_credit_accordion)
        assert self.page.is_visible(self.available_credit)
        assert self.page.is_visible(self.allocate_credit_btn)
        assert self.page.is_visible(self.credit_history_table)
