# This file will define the CreateOrderCommand class.
# Include attributes and methods for the command.
class CreateOrderCommand:
    def __init__(self, customer_name: str, product: str):
        self.customer_name = customer_name
        self.product = product
