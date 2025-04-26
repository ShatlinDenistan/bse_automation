from typing import Dict
from requests import Session

from base.endpoints_base import EndpointsBase
from data.db.order_data import OrderData


class CancelOrder(EndpointsBase):
    def __init__(self, session: Session = None, order_id: str = None):
        endpoint = f"orders/{order_id}/cancel"
        super().__init__(session=session, endpoint=endpoint)

    def cancel_paid_order(self) -> Dict:
        """Cancel a paid order"""
        cancel_data = OrderData.CANCEL_ORDER_DATA
        response = self.post(data=cancel_data)
        return response
