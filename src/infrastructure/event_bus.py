# This file will contain the EventBus class.
# Define methods for publishing and subscribing to events.
class EventBus:
    def __init__(self):
        self._handlers = {}

    def register(self, event_type, handler):
        self._handlers.setdefault(event_type, []).append(handler)

    def publish(self, event):
        for handler in self._handlers.get(type(event), []):
            handler.handle(event)
