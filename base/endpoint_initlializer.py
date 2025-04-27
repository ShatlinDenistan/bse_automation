from requests import Session

from endpoints.cancel_order import CancelOrder
from endpoints.cancel_order_items import CancelOrderItems


class EndpointInitializer:
    """Handles page object initialization"""

    def initialise_endpoints(self, session: Session):
        """Test base functionality."""
        self.session = session
        self.cancel_order_ep = CancelOrder(session)
        self.cancel_order_items_ep = CancelOrderItems(session)
