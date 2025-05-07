import pytest
from base.test_base import TestBase


class TestFinPortalManualCredit(TestBase):
    """Test cases for Manual Credit functionality in Finance Portal"""

    @pytest.mark.regression
    def test_add_credit_breach_credit_to_customer(self):
        """Verify that a user can successfully allocate Credit breach credit to a customer"""

        self.step("Search for customer")
        self.top_nav.search_for_customer(100)

        self.step("Expand customer credit section and click the credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select credit breach reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_credit_breach)

        self.step("Enter JIRA number for Credit Breach reason")
        self.order_credit_page.enter_jira_number_for_credit_breach()

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify credit is applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Credit was not applied successfully"

    @pytest.mark.regression
    def test_validate_credit_breach_min_max_amount_rules(self):
        """Verify Credit breach credit reason min and max amount rules"""

        self.step("Search for customer")
        self.top_nav.search_for_customer(100)

        self.step("Expand customer credit section and click the credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select credit breach reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_credit_breach)

        self.step("Enter JIRA number for Credit Breach reason")
        self.order_credit_page.enter_jira_number_for_credit_breach()

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(10000001)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_goodwill_credit_to_order(self):
        """Verify that a user can successfully add Goodwill credit to an order"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Goodwill credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_goodwill)

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify credit is applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Credit was not applied successfully"

    @pytest.mark.regression
    def test_validate_goodwill_min_max_amount_rules(self):
        """Verify Goodwill credit reason min and max amount rules"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Goodwill credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_goodwill)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(-1)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(800)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_late_delivery_fee_credit_to_order(self):
        """Verify that a user can successfully add Late Delivery Fee credit to an order"""

        self.step("Get orders from database")
        order_data = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Late Delivery Fee credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_late_delivery_fee)

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify credit is applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Credit was not applied successfully"

    @pytest.mark.regression
    def test_validate_late_delivery_fee_min_max_amount_rules(self):
        """Verify Late Delivery Fee credit reason min and max amount rules"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Late Delivery Fee credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_late_delivery_fee)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(300)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_subscription_late_delivery_fee_credit_to_order(self):
        """Verify that a user can successfully add Subscription late delivery fee credit to an order"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Subscription late delivery fee credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_sub_late_delivery)

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify credit is applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Credit was not applied successfully"

    @pytest.mark.regression
    def test_validate_subscription_late_delivery_fee_min_max_amount_rules(self):
        """Verify Subscription late delivery fee credit reason min and max amount rules"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Subscription late delivery fee credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_sub_late_delivery)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(51)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_b2b_bulk_orders_credit_to_customer(self):
        """Verify that a user can successfully allocate B2B bulk orders credit to a customer"""

        self.step("Search for customer")
        self.top_nav.search_for_customer(100)

        self.step("Expand customer credit section and click the credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select B2B bulk orders credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_b2b_bulk_order)

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify credit is applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Credit was not applied successfully"

    @pytest.mark.regression
    def test_validate_b2b_bulk_orders_min_max_amount_rules(self):
        """Verify B2B bulk orders credit reason min and max amount rules"""

        self.step("Search for customer")
        self.top_nav.search_for_customer(100)

        self.step("Expand customer credit section and click the credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select B2B bulk orders credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_b2b_bulk_order)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(10000001)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_failed_eft_refunds_credit_to_order(self):
        """Verify that a user can successfully add Failed EFT refunds credit to an order"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Failed EFT refunds credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_failed_eft_refunds)

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify credit is applied")
        assert self.customer_credit_page.verify_order_credit_applied(), "Credit was not applied successfully"

    @pytest.mark.regression
    def test_validate_failed_eft_refunds_min_max_amount_rules(self):
        """Verify Failed EFT refunds credit reason min and max amount rules"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Failed EFT refunds credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_failed_eft_refunds)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(2000000)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_system_error_credit_to_order_item(self):
        """Verify that a user can successfully add System Error credit to an order item"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand order items section and click the credit item option")
        self.order_credit_page.expand_order_items_and_click_credit_item()

        self.step("Select System error credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_system_error)

        self.step("Enter RFN for System Error reason")
        self.order_credit_page.enter_rfn_for_system_error()

        self.step("Enter negative amount and admin note")
        self.order_credit_page.enter_negative_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

    @pytest.mark.regression
    def test_validate_system_error_min_max_amount_rules(self):
        """Verify System Error credit reason min and max amount rules"""

        self.step("Search for order")
        self.top_nav.search_for_order(74269681)

        self.step("Expand order items section and click the credit item option")
        self.order_credit_page.expand_order_items_and_click_credit_item()

        self.step("Select System error credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_system_error)

        self.step("Enter RFN for System Error reason")
        self.order_credit_page.enter_rfn_for_system_error()

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(-2000000)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(1)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_duplicate_payment_credit_to_order(self):
        """Verify that a user can successfully add Duplicate payment credit to an order"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Duplicate payment credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_duplicate_payment)

        # Calculate auth total from database values
        order_total = float(order_data["order_total"][0])
        order_shipping = float(order_data["order_shipping"][0])
        order_discount = float(order_data["order_discount"][0])
        calculated_auth_total = order_total + order_shipping - order_discount + 10000

        self.step("Enter calculated amount and admin note")
        self.order_credit_page.enter_calculated_amount(calculated_auth_total)

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

    @pytest.mark.regression
    def test_validate_duplicate_payment_min_max_amount_rules(self):
        """Verify Duplicate payment credit reason min and max amount rules"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Duplicate payment credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_duplicate_payment)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(5000000)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_cod_return_credit_to_order(self):
        """Verify that a user can successfully add COD return credit to an order"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("order_with_returned_canceled_order_item.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Get return cancelled amount from order financials")
        return_cancelled_amount = self.order_credit_page.get_return_cancelled_amount()

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select COD return credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_cod_return)

        self.step("Enter return cancelled amount and admin note")
        self.order_credit_page.enter_calculated_amount(return_cancelled_amount)

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

    @pytest.mark.regression
    def test_validate_cod_return_min_max_amount_rules(self):
        """Verify COD return credit reason min and max amount rules"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("order_with_returned_canceled_order_item.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Get return cancelled amount from order financials")
        return_cancelled_amount = float(self.order_credit_page.get_return_cancelled_amount())
        calculated_returned_cancelled_amount = return_cancelled_amount + 10000

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select COD return credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_cod_return)

        self.step("Enter invalid min amount and verify validation error")
        self.order_credit_page.enter_invalid_min_amount(0)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for min amount"

        self.step("Enter invalid max amount and verify validation error")
        self.order_credit_page.enter_invalid_max_amount(calculated_returned_cancelled_amount)
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for max amount"

    @pytest.mark.regression
    def test_add_credit_error_credit_to_order(self):
        """Verify that a user can successfully add Credit Error credit to an order"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("canceled_order_except_auto_canceled.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Get cancelled amount from order financials")
        cancelled_amount = self.order_credit_page.get_cancelled_amount()

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Credit error credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_credit_error)

        self.step("Enter cancelled amount and admin note")
        self.order_credit_page.enter_calculated_amount_and_admin_note(cancelled_amount)

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

    @pytest.mark.regression
    def test_validate_credit_error_cancelled_items_check(self):
        """Verify Credit error credit reason checks for cancelled items on order"""

        self.step("Get orders from database")

        order_data = self.order_data.get_orders("new_order_with_discount_and_shipping_amounts.sql")
        order_id = order_data["order_ids"][0]

        self.step("Search for order")
        self.top_nav.search_for_order(order_id)

        self.step("Expand customer credit section and click allocate credit button")
        self.order_credit_page.expand_customer_credit_section_and_click_allocate_credit()

        self.step("Select Credit error credit reason")
        self.order_credit_page.select_credit_reason(self.order_credit_page.reason_credit_error)

        self.step("Enter amount and admin note")
        self.order_credit_page.enter_amount_and_admin_note()

        self.step("Click Add Credit button and confirm")
        self.customer_credit_page.select_add_credit_button()
        self.customer_credit_page.select_ok_on_dialog()

        self.step("Verify validation error")
        assert self.order_credit_page.verify_validation_error(), "Validation error not shown for order without cancelled items"
