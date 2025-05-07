from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class OrderModel:
    """Data class representing an order with properties extracted from JSON response."""

    order_id: Optional[str] = None
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

        # Handle case where json_content is not a list
        if not isinstance(json_content, list):
            json_content = [json_content]

        # Handle empty list case
        if len(json_content) == 0:
            return cls()

        items = json_content[0].get("items", [])

        orders = cls(
            order_id=json_content[0].get("idOrder"),
            id_order_item1=items[0].get("order_item_id") if len(items) > 0 else None,
            id_order_item2=items[1].get("order_item_id") if len(items) > 1 else None,
            order_discount=json_content[0].get("Discount"),
            order_shipping=json_content[0].get("Shipping"),
            order_total=json_content[0].get("Total"),
            donation_amount=json_content[0].get("donation"),
        )
        return orders

    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary."""
        return asdict(self)
