class AggregateRoot:
    def __init__(self):
        self.events = []
        self.new_events = []
        self.version = 0

    def emit_event(self, event):
        self.apply(event)
        self.events.append(event)
        self.version += 1
        print(self.events)
