from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class CustomerModel:
    """Data class representing an order with properties extracted from JSON response."""

    customer_ids: Optional[str] = None

    @classmethod
    def from_json(cls, json_content=None):
        """Create an OrderModel instance from JSON content."""
        if not json_content:
            return cls()

        return cls(customer_ids=json_content[0].get("idCustomer"))

    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary."""
        return asdict(self)
