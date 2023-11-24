from uuid import uuid4


class WalletCreated:
    def __init__(self: "WalletCreated", user_id: str) -> None:
        self.id = uuid4()
        self.user_id = user_id


class BalanceChanged:
    def __init__(
        self: "BalanceChanged", wallet_id: int, amount: int, operation: callable
    ) -> None:
        self.wallet_id = wallet_id
        self.operation = operation
        self.amount = amount
