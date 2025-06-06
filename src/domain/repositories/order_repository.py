# This file will contain the OrderRepository interface.
# Define methods for interacting with order data.
from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass
