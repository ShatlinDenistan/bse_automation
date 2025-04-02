from playwright.sync_api import Page, expect


class OrderListPage:
    def __init__(self, page: Page):
        self.page = page
        self.auth_status_label = page.locator("//label[.='Auth Status']")
        self.first_order_checkbox = page.locator("//tr[td[9]][1]//td[div[contains(@class, 'ui fitted checkbox')]/input[@type='checkbox']]")
        self.cancel_button= page.get_by_text("Cancel Order(s)")
        self.cancellation_reasons_dropdown= page.get_by_role("listbox").filter(has_text="-- none --Stock accuracy (")
        self.cancellation_reason= page.get_by_text("Stock accuracy (pick fails")
        self.modal_cancel_button= page.get_by_role("button", name="Cancel Orders")
        self.confirmation_message=page.get_by_text("Successfully processed 1 item")

    def confirm_if_in_page(self):
        expect(self.auth_status_label).to_be_visible(timeout=5000)

    def cancel_order(self):
        self.first_order_checkbox.click()
        self.cancel_button.click()
        self.cancellation_reasons_dropdown.click()
        self.cancellation_reason.click()
        self.modal_cancel_button.click()
        expect(self.confirmation_message).to_be_visible(timeout=5000)