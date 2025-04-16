import os
import json
import requests


class CancelOrderUtils:
    def __init__(self):
        self.master_env = "https://cs-admin-bff.master.env"
        self.test_data_baseurl = "http://tal-test-data-service.master.env"
        self.token = None

    def create_auth_token(self):
        """Create Authentication Token For Cancel Order"""
        session = requests.Session()
        auth_file_path = os.path.join(os.getcwd(), "data", "create_auth_token.json")

        with open(auth_file_path, "r", encoding="utf-8") as f:
            body = json.load(f)

        headers = {"Content-Type": "application/json"}
        response = session.post(f"{self.master_env}/authenticate", json=body, headers=headers)
        response.raise_for_status()
        self.token = response.json().get("token")
        return self.token

    def cancel_order_item(self, order_id, order_item_id):
        """Cancel Order Item"""
        if not self.token:
            self.create_auth_token()

        session = requests.Session()
        cancel_file_path = os.path.join(os.getcwd(), "data", "cancel_order.json")

        with open(cancel_file_path, "r", encoding="utf-8") as f:
            body = json.load(f)

        headers = {"Content-Type": "application/json", "Authorization": self.token}

        response = session.post(f"{self.master_env}/orders/{order_id}/items/{order_item_id}/cancel", json=body, headers=headers)

        if response.status_code != 200:
            raise requests.RequestException(f"Failed to cancel order item. Status code: {response.status_code}")

        response_data = response.json()
        if not response_data:
            raise ValueError("Expected 'true' in response but got empty response")

        return response_data
