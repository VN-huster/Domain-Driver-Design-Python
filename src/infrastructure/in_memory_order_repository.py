# This file will contain the InMemoryOrderRepository class.
# Implement the OrderRepository interface using in-memory storage.
from src.domain.repositories.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders = {}

    def save(self, order):
        self._orders[order.id] = order
        print(f"[Repository] Order saved: {order.id}")
