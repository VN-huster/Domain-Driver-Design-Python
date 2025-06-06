# This file will contain the Order model class.
# Define attributes and methods related to the Order entity.
import uuid
from src.domain.events.order_created import OrderCreated


class Order:
    def __init__(self, customer_name: str, product: str):
        self.id = str(uuid.uuid4())
        self.customer_name = customer_name
        self.product = product
        self.events = [OrderCreated(self.id, self.customer_name, self.product)]
