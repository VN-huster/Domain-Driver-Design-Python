# This file will contain the main entry point for the application.
# Define the application startup logic.
from src.application.commands.create_order_command import CreateOrderCommand
from src.application.handlers.create_order_handler import CreateOrderHandler
from src.domain.services.order_service import OrderService
from src.infrastructure.in_memory_order_repository import InMemoryOrderRepository
from src.infrastructure.event_bus import EventBus
from src.infrastructure.event_handlers.send_email_on_order_created import (
    SendEmailOnOrderCreated,
)
from domain.events.order_created import OrderCreated


def main():
    # Setup
    repository = InMemoryOrderRepository()
    event_bus = EventBus()
    event_bus.register(OrderCreated, SendEmailOnOrderCreated())

    order_service = OrderService(repository)
    handler = CreateOrderHandler(order_service, event_bus)

    # Use Case
    command = CreateOrderCommand("Alice", "Laptop")
    handler.handle(command)


