from typing import Dict
from requests import Session

from base.endpoints_base import EndpointsBase
from data.db.order_data import OrderData


class CancelOrderItems(EndpointsBase):
    def __init__(self, session: Session = None, order_id: str = None, order_item_id: str = None):
        endpoint = f"orders/{order_id}/items/{order_item_id}/cancel"
        super().__init__(session=session, endpoint=endpoint)

    def cancel_order_item(self) -> Dict:
        """Cancel a specific order item"""
        cancel_data = OrderData.CANCEL_ORDER_DATA
        response = self.post(data=cancel_data)
        return response
