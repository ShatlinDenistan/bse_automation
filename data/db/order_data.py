from typing import List

import requests

from data.db.test_data_service import TestDataService
from models.order_model import OrderModel


class OrderData(TestDataService):
    """Order data for testing purposes."""

    def __init__(self):
        super().__init__()
        self.order_id = None
        self.order_item_id = None
        self.create_order_endpoint = f"{self.config.TEST_DATA_SERVICE}/create_new_order"

    # Order data for canceling an existing order
    CANCEL_ORDER_DATA = {"reasontype_id": 3, "username": ""}

    def create_order(self, pay_full_amount=True, complete_payment=True, cancel_order=False):
        """Helper method to create orders with different configurations"""
        response = requests.post(
            self.create_order_endpoint,
            json={
                "customer_id": int(self.customer_id),
                "products": [{"product_id": 27408192, "quantity": 1, "unit_price": 400.0}, {"product_id": 27408193, "quantity": 1, "unit_price": 600.0}],
                "address_id": "5dc905b49e440001d5dc3405",
                "delivery_method": "COURIER",
                "payment_method": self.payment_method,
                "pay_full_amount_due": pay_full_amount,
                "percentage_of_amount_due_to_pay": 100 if pay_full_amount else 0,
                "complete_payment": complete_payment,
                "add_donation": False,
                "cancel_order": cancel_order,
            },
            timeout=100,
        )
        return List(OrderModel().from_json(response.json()))

    def get_orders(self, query):
        """Get orders from database using query"""
        json_content = self._execute_query(query)
        orders = OrderModel.from_json(json_content)
        return orders

    # def create_new_tal_orders(self, pay_full_amount=True, complete_payment=True, cancel_order=False):
    #     """Create new TAL orders"""
    #     # Set environment variables

    #     # Create new order
    #     orders_content = self._create_order(pay_full_amount=pay_full_amount, complete_payment=complete_payment, cancel_order=cancel_order)

    #     # Extract values from JSON
    #     self.order_ids = orders_content.get("order_id")
    #     self.id_order_item1 = orders_content.get("items")[0].get("order_item_id") if orders_content.get("items") else None
    #     self.id_order_item2 = orders_content.get("items")[1].get("order_item_id") if len(orders_content.get("items", [])) > 1 else None
    #     self.order_total = orders_content.get("total_amount")

    #     return {"order_ids": self.order_ids, "id_order_item1": self.id_order_item1, "id_order_item2": self.id_order_item2, "order_total": self.order_total}

    # def create_new_tal_orders_not_paid(self, customer, payment_method):
    #     """
    #     Create new TAL orders that are not paid

    #     Args:
    #         customer: Customer ID
    #         payment_method: Payment method to use

    #     Returns:
    #         Dictionary with order details
    #     """
    #     # Set environment variables
    #     os.environ["CUSTOMER"] = str(customer)
    #     os.environ["PAYMENTMENTHOD"] = payment_method

    #     # Create new order not paid
    #     orders_content = self.api_library.create_new_order_tal_not_paid()

    #     # Extract values from JSON
    #     self.order_ids = orders_content.get("order_id")
    #     self.order_total = orders_content.get("total_amount")

    #     # Return the entire result for additional processing if needed
    #     return {"order_ids": self.order_ids, "order_total": self.order_total}

    # def create_new_tal_orders_cancelled(self, customer, payment_method):
    #     """
    #     Create new TAL orders that are cancelled

    #     Args:
    #         customer: Customer ID
    #         payment_method: Payment method to use

    #     Returns:
    #         Dictionary with order details
    #     """
    #     # Set environment variables
    #     os.environ["CUSTOMER"] = str(customer)
    #     os.environ["PAYMENTMENTHOD"] = payment_method

    #     # Create new cancelled order
    #     orders_content = self.api_library.create_new_order_tal_cancelled()

    #     # Extract values from JSON
    #     self.order_ids = orders_content.get("order_id")
    #     self.order_total = orders_content.get("total_amount")

    #     # Return the entire result for additional processing if needed
    #     return {"order_ids": self.order_ids, "order_total": self.order_total}
