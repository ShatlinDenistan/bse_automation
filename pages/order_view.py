from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
add_notes_btn = "xpath=//button[@class='ui mini primary right floated button']"
confirm_add_btn = "xpath=//button[@class='ui blue right floated button']"
notes_txt_field = "xpath=//textarea[@name='customerNote']"
note_confirm_message = "xpath=//*[@id='noty_layout__topRight']"
blacklist_cust_btn = "xpath=//button[contains(text(),'Blacklist Customer')]"
fraud_reason_list = "xpath=//div[contains(text(),'Fraud Reason')]"
fraud_reason_selection = "xpath=//span[contains(text(),'Returns abuse')]"
fin_note = "xpath=//input[@name='finNote']"
confirm_blacklist = "xpath=//button[@class='ui negative right floated button'][contains(text(),'Blacklist')]"
whitelist_cust_btn = "xpath=//button[contains(text(),'Whitelist Customer')]"
confirm_whitelist = "xpath=//button[@class='ui blue right floated button'][contains(text(),'Confirm')]"


class OrderViewPage(PageBase):
    """Page object for Order View functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.add_notes_btn = self.locator(add_notes_btn)
        self.confirm_add_btn = self.locator(confirm_add_btn)
        self.notes_txt_field = self.locator(notes_txt_field)
        self.note_confirm_message = self.locator(note_confirm_message)
        self.blacklist_cust_btn = self.locator(blacklist_cust_btn)
        self.fraud_reason_list = self.locator(fraud_reason_list)
        self.fraud_reason_selection = self.locator(fraud_reason_selection)
        self.fin_note = self.locator(fin_note)
        self.confirm_blacklist = self.locator(confirm_blacklist)
        self.whitelist_cust_btn = self.locator(whitelist_cust_btn)
        self.confirm_whitelist = self.locator(confirm_whitelist)

    def add_admin_notes(self, note: str):
        self.add_notes_btn.click()
        self.notes_txt_field.fill(note)
        self.confirm_add_btn.click()
        self.page.wait_for_selector(self.note_confirm_message)

    def update_to_blacklist(self, reason: str, note: str):
        self.blacklist_cust_btn.click()
        self.fraud_reason_list.click()
        self.fraud_reason_selection.click()
        self.fin_note.fill(note)
        self.confirm_blacklist.click()
        self.page.wait_for_selector(self.note_confirm_message)

    def update_to_whitelist(self):
        self.whitelist_cust_btn.click()
        self.confirm_whitelist.click()
        self.page.wait_for_selector(self.note_confirm_message)
