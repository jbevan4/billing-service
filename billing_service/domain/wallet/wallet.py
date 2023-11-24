from uuid import uuid4

from .events import BalanceChanged, WalletCreated


class Wallet:
    def __init__(self: "Wallet", user_id: uuid4) -> None:
        self.add_event(WalletCreated(user_id))

    def add_event(self: "Wallet", event: WalletCreated | BalanceChanged) -> None:
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

    def apply_wallet_created(self: "Wallet", event: WalletCreated) -> None:
        self.id = event.id
        self.events = []
        self.current_balance = 0
        self.user_id = event.user_id

    def apply_balance_changed(self: "Wallet", event: BalanceChanged) -> None:
        self.current_balance = event.operation(self.current_balance, event.amount)

    def handle_balance_changed(self: "Wallet", event: BalanceChanged) -> None:
        proposed_balance = event.operation(self.current_balance, event.amount)
        if proposed_balance < 0:
            raise ValueError("balance can't go below 0")
        self.add_event(event)

    def handle_wallet_created(self: "Wallet", event: WalletCreated) -> None:
        self.add_event(event)

    def get_events(self: "Wallet") -> list[WalletCreated | BalanceChanged]:
        return self.events
