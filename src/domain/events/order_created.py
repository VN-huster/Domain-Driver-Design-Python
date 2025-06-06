# This file will define the OrderCreated event class.
# Include attributes and methods for the event.

from src.shared.events import DomainEvent

class OrderCreated(DomainEvent):
    def __init__(self, order_id: str, customer_name: str, product: str):
        super().__init__()
        self.order_id = order_id
        self.customer_name = customer_name
        self.product = product
