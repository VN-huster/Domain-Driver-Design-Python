# This file will contain the CreateOrderHandler class.
# Define methods for handling the CreateOrderCommand.
class CreateOrderHandler:
    def __init__(self, order_service, event_bus):
        self.order_service = order_service
        self.event_bus = event_bus

    def handle(self, command):
        order = self.order_service.create_order(command.customer_name, command.product)
        for event in order.events:
            self.event_bus.publish(event)
