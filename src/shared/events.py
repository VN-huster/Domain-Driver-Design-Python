# This file will contain shared event-related classes and methods.
# Define base classes or utilities for events.
from datetime import datetime
from abc import ABC


class DomainEvent(ABC):
    def __init__(self):
        self.occurred_on = datetime.utcnow()
