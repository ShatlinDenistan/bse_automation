from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
btn_manual_override = "xpath=//a[contains(text(),'Manual Override')]"
ddl_refund_method = "xpath=//div[contains(text(),'- - Select a refund method - -')]"
txt_refund_amount = "xpath=//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[2]/div[1]/input[1]"
txt_override_reason = "xpath=//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[3]/textarea[1]"
btn_refund_override = "xpath=//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/form[1]/div[1]/form[1]/div[4]/button[1]"
btn_confirm_override = "xpath=//body/div[2]/div[1]/div[2]/button[2]"
verification_message = "xpath=//div[contains(text(),'Successfully processed 1 item(s)')]"
close_success_message = "xpath=//i[@aria-hidden='true' and @class='close icon']"


class ManualOverridePage(PageBase):
    """Page object for Manual Override functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.btn_manual_override = self.locator(btn_manual_override)
        self.ddl_refund_method = self.locator(ddl_refund_method)
        self.txt_refund_amount = self.locator(txt_refund_amount)
        self.txt_override_reason = self.locator(txt_override_reason)
        self.btn_refund_override = self.locator(btn_refund_override)
        self.btn_confirm_override = self.locator(btn_confirm_override)
        self.verification_message = self.locator(verification_message)
        self.close_success_message = self.locator(close_success_message)

    def complete_override_form(self, payment_method: str, refund_amount: str, reason: str):
        self.btn_manual_override.click()
        self.page.wait_for_timeout(2000)
        self.ddl_refund_method.click()
        self.page.click(f"xpath=//span[contains(text(),'{payment_method}')]")
        self.txt_refund_amount.fill(refund_amount)
        self.txt_override_reason.fill(reason)
        self.btn_refund_override.click()

    def confirm_override(self):
        self.btn_confirm_override.click()
        self.page.wait_for_selector(self.verification_message)
        self.close_success_message.click()
