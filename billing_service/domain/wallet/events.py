class WalletCreated:
    def __init__(self, id, user_id):
        self.user_id = user_id
        self.id = id


class BalanceChanged:
    def __init__(self, wallet_id: int, amount: int, operation: callable):
        self.wallet_id = wallet_id
        self.operation = operation
        self.amount = amount
