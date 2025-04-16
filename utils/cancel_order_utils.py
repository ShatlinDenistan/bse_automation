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
        with open(os.path.join(os.getcwd(), "data/create_auth_token.json"), encoding="utf-8") as f:
            body = json.load(f)

        headers = {"Content-Type": "application/json"}
        response = session.post(f"{self.master_env}/authenticate", json=body, headers=headers)

        json_content = response.json()
        self.token = json_content["token"]
        return self.token

    def cancel_paid_order(self, order_ids):
        """Cancel Paid Order"""
        if not self.token:
            self.create_auth_token()

        session = requests.Session()
        with open(os.path.join(os.getcwd(), "data/cancel_order.json"), encoding="utf-8") as f:
            body = json.load(f)

        headers = {"Content-Type": "application/json", "Authorization": self.token[0]}

        response = session.post(f"{self.master_env}/orders/{order_ids[0]}/cancel", json=body, headers=headers)

        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        assert response.json() is True, "Expected response body to be true"

        print(order_ids)
        return response
