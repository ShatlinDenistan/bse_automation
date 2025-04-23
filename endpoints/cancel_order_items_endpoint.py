import json
import os
from typing import Dict, Optional

from base.endpoints_base import EndpointsBase
from requests import Session


class CancelOrderItemsEndpoint(EndpointsBase):
    """CancelOrderItemsEndpoint - Class for cancelling order items"""

    def __init__(self, session: Session = None):
        """Initialize the CancelOrderItemsEndpoint class

        Parameters
        ----------
        session : Session, optional
            The session to use for the requests. If not provided, a new session will be created.
        """
        self.session = session
        self.master_env = "https://cs-admin-bff.master.env"
        self.url = f"{self.master_env}/orders"
        self.token = None

    def create_auth_token(self) -> str:
        """Create authentication token for cancelling order items

        Returns
        -------
        str
            The authentication token
        """
        # Read the auth token JSON data
        data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "create_auth_token.json")
        with open(data_file_path, "r") as file:
            auth_data = json.load(file)

        # Use the post method from EndpointsBase to authenticate
        auth_url = f"{self.master_env}/authenticate"
        response = self.post(url=auth_url, data=auth_data, expected_status_code=200, log_results=True, force_json_response=True, return_raw_response=True)

        # Extract the token from the response
        response_json = response.json()
        self.token = response_json.get("token")

        return self.token

    def cancel_order_item(self, order_id: str, order_item_id: str) -> Dict:
        """Cancel a specific order item

        Parameters
        ----------
        order_id : str
            The ID of the order
        order_item_id : str
            The ID of the order item to cancel

        Returns
        -------
        Dict
            The response from the cancel order item request
        """
        # Ensure we have a token
        if not self.token:
            self.create_auth_token()

        # Read the cancel order JSON data
        data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cancel_order.json")
        with open(data_file_path, "r") as file:
            cancel_data = json.load(file)

        # Prepare headers with authentication token
        headers = {"Content-Type": "application/json", "Authorization": self.token}

        # Use the post method from EndpointsBase to cancel the order item
        cancel_url = f"{self.url}/{order_id}/items/{order_item_id}/cancel"
        response = self.post(url=cancel_url, data=cancel_data, headers=headers, expected_status_code=200, log_results=True, force_json_response=True)

        return response
