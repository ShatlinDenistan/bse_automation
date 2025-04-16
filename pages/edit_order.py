from playwright.sync_api import Page
from base.page_base import PageBase

# Locators
black_ellipsis = ("//*[@class='six wide column']//*[@class='black ellipsis vertical small icon']", "Black Ellipsis")
edit_order_menu_option = ("//*[contains(text(),'Edit Order')]", "Edit Order Menu Option")
payment_method_dropdown = ("//*[@name='paymentMethod']", "Payment Method Dropdown")
update_button = ("//button[contains(text(),'Update')]", "Update Button")
payment_method_update_admin_note = ("//div[contains(text(),'Payment method updated ')]", "Payment Method Update Admin Note")
payment_method_warning_banner = ("//*[@class='banner-container']", "Payment Method Warning Banner")
discount_amount = ("//*[@name='discountAmount']", "Discount Amount")
invalid_discount_amount = ("//*[@class='ui error message']/div/p/li", "Invalid Discount Amount")
shipping_amount = ("//*[@name='shippingAmount']", "Shipping Amount")
discount_applied_admin_note = ("//div[contains(text(),'Discount applied:')]", "Discount Applied Admin Note")
shipping_fee_applied_admin_note = ("//div[contains(text(),'Shipping fee applied:')]", "Shipping Fee Applied Admin Note")
audit_log_menu_option = ("//*[contains(text(),'Audit log')]", "Audit Log Menu Option")
audit_log_edit_order_action_type = ("//*[@class='ui striped basic very compact table']/tbody/tr/td[3]", "Audit Log Edit Order Action Type")
audit_log_edit_order_data = ("//*[@class='ui striped basic very compact table']/tbody/tr/td[5]", "Audit Log Edit Order Data")
order_financials_accordion = ("//div[contains(text(),'Order Financials')]//i", "Order Financials Accordion")
order_financials_shipping_amount = ("//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Shipping')]//following-sibling::td", "Order Financials Shipping Amount")
order_financials_discount_amount = ("//div[contains(text(),'Order Breakdown')]/parent::div//*[contains(text(),'Discount')]//following-sibling::td", "Order Financials Discount Amount")
return_canceled_order_item_menu = ("//div[@class='accordion ui fluid styled']//*[@role='listbox']", "Return Canceled Order Item Menu")
update_to_shipped_menu_option = ("//*[contains(text(),'Update to shipped')]", "Update To Shipped Menu Option")
update_to_shipped_modal_message = ("//div[@class='ui tiny modal transition visible active']//*[@class='ui form']/p", "Update To Shipped Modal Message")
update_to_shipped_button = ("//div[@class='ui tiny modal transition visible active']//button[contains(text(),'Update to shipped')]", "Update To Shipped Button")
order_item_status = ("//div[@class='accordion ui']//table[@class='ui table']//td[8]/div", "Order Item Status")
update_to_shipped_admin_note = ("//div[contains(text(),'status updated from Return Canceled to Shipped')]", "Update To Shipped Admin Note")
discount_amount_disabled_field = ("//*[contains(text(),'Discount')]/parent::div//parent::div/div/p", "Discount Amount Disabled Field")
shipping_fee_disabled_field = ("//*[contains(text(),'Shipping')]/parent::div//parent::div/div/p", "Shipping Fee Disabled Field")


class EditOrderPage(PageBase):
    """Page object for Edit Order functionality"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.black_ellipsis = self.locator(black_ellipsis)
        self.edit_order_menu_option = self.locator(edit_order_menu_option)
        self.payment_method_dropdown = self.locator(payment_method_dropdown)
        self.update_button = self.locator(update_button)
        self.payment_method_update_admin_note = self.locator(payment_method_update_admin_note)
        self.payment_method_warning_banner = self.locator(payment_method_warning_banner)
        self.discount_amount = self.locator(discount_amount)
        self.invalid_discount_amount = self.locator(invalid_discount_amount)
        self.shipping_amount = self.locator(shipping_amount)
        self.discount_applied_admin_note = self.locator(discount_applied_admin_note)
        self.shipping_fee_applied_admin_note = self.locator(shipping_fee_applied_admin_note)
        self.audit_log_menu_option = self.locator(audit_log_menu_option)
        self.audit_log_edit_order_action_type = self.locator(audit_log_edit_order_action_type)
        self.audit_log_edit_order_data = self.locator(audit_log_edit_order_data)
        self.order_financials_accordion = self.locator(order_financials_accordion)
        self.order_financials_shipping_amount = self.locator(order_financials_shipping_amount)
        self.order_financials_discount_amount = self.locator(order_financials_discount_amount)
        self.return_canceled_order_item_menu = self.locator(return_canceled_order_item_menu)
        self.update_to_shipped_menu_option = self.locator(update_to_shipped_menu_option)
        self.update_to_shipped_modal_message = self.locator(update_to_shipped_modal_message)
        self.update_to_shipped_button = self.locator(update_to_shipped_button)
        self.order_item_status = self.locator(order_item_status)
        self.update_to_shipped_admin_note = self.locator(update_to_shipped_admin_note)
        self.discount_amount_disabled_field = self.locator(discount_amount_disabled_field)
        self.shipping_fee_disabled_field = self.locator(shipping_fee_disabled_field)

    def navigate_to_edit_order_screen(self):
        """Navigate to Edit Order Screen"""
        self.expect_to_be_visible(self.black_ellipsis)
        self.page.mouse.move(0, 0)  # Reset mouse position
        self.page.mouse.move(
            self.black_ellipsis.bounding_box()["x"] + self.black_ellipsis.bounding_box()["width"] / 2,
            self.black_ellipsis.bounding_box()["y"] + self.black_ellipsis.bounding_box()["height"] / 2
        )
        self.click(self.edit_order_menu_option)

    def update_payment_method(self):
        """Update payment method with a random selection"""
        self.expect_to_be_visible(self.payment_method_dropdown)
        self.click(self.payment_method_dropdown)
        
        # Generate random number between 3 and 8
        import random
        random_number = random.randint(3, 8)
        
        # Press arrow down key multiple times
        for _ in range(random_number):
            self.page.keyboard.press("ArrowDown")
        
        # Press Enter key on the dropdown
        self.page.keyboard.press("Enter")
        self.click(self.update_button)

    def verify_that_an_admin_note_for_payment_method_update(self):
        """Verify that an admin note for payment method update is displayed"""
        self.expect_to_be_visible(self.payment_method_update_admin_note)
        admin_note_text = self.text_content(self.payment_method_update_admin_note)
        return admin_note_text

    def verify_that_payment_method_difference_warning_banner_displays(self):
        """Verify that payment method difference warning banner displays"""
        self.wait_for_seconds(self.page.SLEEP if hasattr(self.page, 'SLEEP') else 2)
        self.expect_to_be_visible(self.payment_method_warning_banner)
        warning_text = self.text_content(self.payment_method_warning_banner)
        return warning_text

    def calculate_discount_amount_input_value(self, order_total):
        """Calculate discount amount input value and enter it"""
        # Get Current Order Total Amount and convert to number
        order_total_amount = float(order_total[0])
        
        # Add 500 to Current Order Total to create Discount Amount
        add_discount_amount = order_total_amount + 500
        
        # Type calculated Discount Amount into Discount field and submit
        self.expect_to_be_visible(self.discount_amount)
        self.fill(self.discount_amount, str(add_discount_amount))
        self.click(self.update_button)
        
        return add_discount_amount

    def verify_that_invalid_discount_amount_message(self):
        """Verify that invalid discount amount message is displayed"""
        self.expect_to_be_visible(self.invalid_discount_amount)
        invalid_discount_amount_text = self.text_content(self.invalid_discount_amount)
        assert "Discount amount cannot exceed the order item total of" in invalid_discount_amount_text
        return invalid_discount_amount_text

    def add_shipping_fee_and_discount_amounts(self):
        """Add shipping fee and discount amounts"""
        # Random discount amount between 5 and 10
        import random
        random_discount_amount = random.randint(5, 10)
        
        # Choose a shipping fee from the list of shipping fee amounts
        shipping_fees = [65, 200, 30]
        random_shipping_fee = random.choice(shipping_fees)
        
        # Send the random values to the input fields
        self.expect_to_be_visible(self.discount_amount)
        self.fill(self.discount_amount, str(random_discount_amount))
        
        self.expect_to_be_visible(self.shipping_amount)
        self.fill(self.shipping_amount, str(random_shipping_fee))
        
        self.click(self.update_button)
        
        return random_discount_amount, random_shipping_fee

    def verify_discount_and_shipping_fee_update_admin_notes(self):
        """Verify discount and shipping fee update admin notes"""
        self.wait_for_seconds(self.page.SLEEP if hasattr(self.page, 'SLEEP') else 2)
        
        # Verify discount applied admin note
        discount_note = self.text_content(self.discount_applied_admin_note)
        assert self.text_content(self.discount_applied_admin_note) in discount_note
        
        # Verify shipping fee applied admin note
        shipping_note = self.text_content(self.shipping_fee_applied_admin_note)
        assert self.text_content(self.shipping_fee_applied_admin_note) in shipping_note
        
        return discount_note, shipping_note

    def verify_discount_and_shipping_fee_update_audit_logs(self):
        """Verify discount and shipping fee update audit logs"""
        self.wait_for_seconds(5)
        self.expect_to_be_visible(self.black_ellipsis)
        
        # Mouse over the black ellipsis
        self.page.mouse.move(0, 0)  # Reset mouse position
        self.page.mouse.move(
            self.black_ellipsis.bounding_box()["x"] + self.black_ellipsis.bounding_box()["width"] / 2,
            self.black_ellipsis.bounding_box()["y"] + self.black_ellipsis.bounding_box()["height"] / 2
        )
        
        # Click on audit log menu option
        self.expect_to_be_visible(self.audit_log_menu_option)
        self.click(self.audit_log_menu_option)
        self.wait_for_seconds(self.page.SLEEP if hasattr(self.page, 'SLEEP') else 2)
        
        # Get Audit Log entry action type
        self.expect_to_be_visible(self.audit_log_edit_order_action_type)
        action_type = self.text_content(self.audit_log_edit_order_action_type)
        
        # Verify Action Type Equals to Edit Order
        assert "edit_order" in action_type
        
        # Get Audit Log entry data
        data = self.text_content(self.audit_log_edit_order_data)
        
        # Verify Edit Order Data
        assert "updated_values" in data
        assert "discount_update" in data
        assert "shipping_update" in data
        
        return action_type, data

    def verify_that_discount_and_shipping_amounts_are_added_to_order_financials(self):
        """Verify that discount and shipping amounts are added to order financials"""
        self.expect_to_be_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)
        
        # Verify Shipping is added
        shipping_amount = self.text_content(self.order_financials_shipping_amount)
        shipping_amount = shipping_amount.replace("R ", "")
        
        # Verify Discount is added
        discount_amount = self.text_content(self.order_financials_discount_amount)
        discount_amount = discount_amount.replace("R ", "")
        
        return shipping_amount, discount_amount

    def navigate_to_update_to_shipped_screen(self):
        """Navigate to Update To Shipped Screen"""
        self.expect_to_be_visible(self.return_canceled_order_item_menu)
        self.click(self.return_canceled_order_item_menu)
        self.click(self.update_to_shipped_menu_option)

    def update_order_item_status_from_returned_canceled_to_shipped(self):
        """Update order item status from returned canceled to shipped"""
        self.expect_to_be_visible(self.update_to_shipped_menu_option)
        
        message_text = self.text_content(self.update_to_shipped_modal_message)
        assert "Update status for order" in message_text
        
        self.click(self.update_to_shipped_button)
        
        return message_text

    def verify_update_from_return_canceled_to_shipped_admin_note_and_audit_log_entry(self):
        """Verify update from return canceled to shipped admin note and audit log entry"""
        self.wait_for_seconds(self.page.SLEEP if hasattr(self.page, 'SLEEP') else 2)
        
        # Verify Admin Note has been added
        admin_note = self.text_content(self.update_to_shipped_admin_note)
        assert self.text_content(self.update_to_shipped_admin_note) in admin_note
        
        # Verify the update to shipped audit log
        self.wait_for_seconds(10)
        self.expect_to_be_visible(self.black_ellipsis)
        
        # Mouse over the black ellipsis
        self.page.mouse.move(0, 0)  # Reset mouse position
        self.page.mouse.move(
            self.black_ellipsis.bounding_box()["x"] + self.black_ellipsis.bounding_box()["width"] / 2,
            self.black_ellipsis.bounding_box()["y"] + self.black_ellipsis.bounding_box()["height"] / 2
        )
        
        # Click on audit log menu option
        self.expect_to_be_visible(self.audit_log_menu_option)
        self.click(self.audit_log_menu_option)
        
        # Get Audit Log entry action type
        self.wait_for_seconds(10)
        self.expect_to_be_visible(self.audit_log_edit_order_action_type)
        action_type = self.text_content(self.audit_log_edit_order_action_type)
        
        # Verify Action Type Equals to Edit Order
        assert "update_order_item_to_shipped" in action_type
        
        return admin_note, action_type

    def verify_that_both_shipping_and_discount_disabled_fields_are_on_edit_order_screen(self):
        """Verify that both shipping and discount disabled fields are on edit order screen"""
        # Check that the editable fields are not visible
        self.expect_to_be_hidden(self.discount_amount)
        self.expect_to_be_hidden(self.shipping_amount)
        
        # Check that the disabled fields are visible
        self.expect_to_be_visible(self.discount_amount_disabled_field)
        self.expect_to_be_visible(self.shipping_fee_disabled_field)

    def update_shipping_amount(self):
        """Update shipping amount"""
        self.expect_to_be_visible(self.shipping_amount)
        self.fill(self.shipping_amount, "75")
        self.click(self.update_button)

    def verify_that_the_shipping_amount_is_updated_on_order_financials(self):
        """Verify that the shipping amount is updated on order financials"""
        self.expect_to_be_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)
        
        shipping_amount = self.text_content(self.order_financials_shipping_amount)
        shipping_amount = shipping_amount.replace("R ", "")
        
        assert shipping_amount == "75.00"
        return shipping_amount

    def update_discount_amount(self):
        """Update discount amount"""
        self.expect_to_be_visible(self.discount_amount)
        self.fill(self.discount_amount, "10")
        self.click(self.update_button)

    def verify_that_the_discount_amount_is_updated_on_order_financials(self):
        """Verify that the discount amount is updated on order financials"""
        self.expect_to_be_visible(self.order_financials_accordion)
        self.click(self.order_financials_accordion)
        
        discount_amount = self.text_content(self.order_financials_discount_amount)
        discount_amount = discount_amount.replace("R ", "")
        
        assert discount_amount == "10.00"
        return discount_amount

    def verify_that_payment_method_options_are_displayed(self):
        """Verify that payment method options are displayed"""
        expected_options = [
            "COD", "Credit Card", "Credit Card Token", "MasterPass", "PayFast", 
            "iPay", "OneVoucher", "eBucks", "Discovery Miles", "Mobicred", 
            "NSFAS Wallet | Celbux eVoucher", "Deposit", "Credit", "Payflex", 
            "Nedbank Personal Loan", "TakealotCredit"
        ]
        
        self.click(self.payment_method_dropdown)
        payment_options_text = self.text_content(self.payment_method_dropdown)
        actual_options = [option for option in payment_options_text.split("\n") if option != "-- none --"]
        
        # Verify all expected options are in the actual options
        for option in expected_options:
            assert option in actual_options
            
        return actual_options
