from .aggregate_root import AggregateRoot
from .events import BalanceChanged, WalletCreated


class Wallet(AggregateRoot):
    def __init__(self, create):
        super().__init__()
        self.emit_event(WalletCreated(user_id=create.user_id, id=create.id))

    def apply(self, event):
        handlers = {
            WalletCreated: self.handle_walletcreated,
            BalanceChanged: self.handle_balancechanged,
        }
        handler = handlers.get(type(event))
        if handler:
            handler(event)
        else:
            raise ValueError(f"No handler found for event {type(event).__name__}")

    def request_balance_change(self, command):
        self.emit_event(
            BalanceChanged(
                wallet_id=command.wallet_id,
                amount=command.amount,
                operation=command.operation,
            )
        )

    def handle_walletcreated(self, event: WalletCreated):
        self.id = event.id
        self.balance = 0

    def handle_balancechanged(self, event: BalanceChanged):
        new_balance = event.operation(self.balance, event.amount)
        if new_balance < 0:
            raise ValueError("balance can't go below 0")
        self.balance = new_balance
