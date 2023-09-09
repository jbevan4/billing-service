class CreateWallet:
    def __init__(self, id, user_id):
        self.user_id = user_id
        self.id = id


class ChangeBalance:
    def __init__(self, amount, wallet_id, operation) -> None:
        self.amount = amount
        self.wallet_id = wallet_id
        self.operation = operation
