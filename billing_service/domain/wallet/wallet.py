from .events import BalanceChanged, WalletCreated


class Wallet:
    def __init__(self, user_id):
        self.add_event(WalletCreated(user_id))

    def add_event(self, event):
        handlers = {
            WalletCreated: self.apply_wallet_created,
            BalanceChanged: self.apply_balance_changed,
        }
        handler = handlers.get(type(event))
        if handler:
            handler(event)
            self.events.append(event)
        else:
            raise ValueError(f"No handler found for event {type(event).__name__}")

    def apply_wallet_created(self, event: WalletCreated):
        self.id = event.id
        self.events = []
        self.current_balance = 0
        self.user_id = event.user_id

    def apply_balance_changed(self, event: BalanceChanged):
        self.current_balance = event.operation(self.current_balance, event.amount)

    def handle_balance_changed(self, event: BalanceChanged):
        proposed_balance = event.operation(self.current_balance, event.amount)
        if proposed_balance < 0:
            raise ValueError("balance can't go below 0")
        self.add_event(event)

    def handle_wallet_created(self, event: WalletCreated):
        self.add_event(event)

    def get_events(self):
        return self.events
