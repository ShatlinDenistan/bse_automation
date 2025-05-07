from typing import Dict
from requests import Session

from base.endpoints_base import EndpointsBase
from data.db.order_data import OrderData


class CancelOrder(EndpointsBase):
    def __init__(self, session: Session = None):
        endpoint = "orders"
        super().__init__(session=session, endpoint=endpoint)

    def cancel_paid_order(self, order_id: str = None) -> Dict:
        """Cancel a paid order"""
        self.endpoint = f"{self.endpoint}/{order_id}/cancel"
        cancel_data = OrderData.CANCEL_ORDER_DATA
        response = self.post(data=cancel_data)
        return response
