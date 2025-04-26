from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class OrderModel:
    """Data class representing an order with properties extracted from JSON response."""

    order_ids: Optional[str] = None
    id_order_item1: Optional[str] = None
    id_order_item2: Optional[str] = None
    order_discount: Optional[float] = None
    order_shipping: Optional[float] = None
    order_total: Optional[float] = None
    donation_amount: Optional[float] = None

    @classmethod
    def from_json(cls, json_content=None):
        """Create an OrderModel instance from JSON content."""
        if not json_content:
            return cls()

        return cls(
            order_ids=json_content[0].get("idOrder"),
            id_order_item1=json_content[0].get("items")[0].get("order_item_id"),
            id_order_item2=json_content[0].get("items")[1].get("order_item_id"),
            order_discount=json_content[0].get("Discount"),
            order_shipping=json_content[0].get("Shipping"),
            order_total=json_content[0].get("Total"),
            donation_amount=json_content[0].get("donation"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary."""
        return asdict(self)
