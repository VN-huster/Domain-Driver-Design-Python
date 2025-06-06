# This file will contain the OrderService class.
# Define business logic related to orders.
from src.domain.models.order import Order


class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def create_order(self, customer_name: str, product: str):
        order = Order(customer_name, product)
        self.repository.save(order)
        return order
