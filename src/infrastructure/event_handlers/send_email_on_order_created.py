# This file will contain the SendEmailOnOrderCreated class.
# Define methods for handling the OrderCreated event and sending emails.
from src.domain.events.order_created import OrderCreated


class SendEmailOnOrderCreated:
    def handle(self, event: OrderCreated):
        print(
            f"[EventHandler] Sending email: Order {event.order_id} for {event.customer_name} - {event.product}"
        )
