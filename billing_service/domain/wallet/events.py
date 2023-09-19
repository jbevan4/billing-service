from uuid import uuid4


class WalletCreated:
    def __init__(self, user_id):
        self.id = uuid4()
        self.user_id = user_id


class BalanceChanged:
    def __init__(self, wallet_id: int, amount: int, operation: callable):
        self.wallet_id = wallet_id
        self.operation = operation
        self.amount = amount
