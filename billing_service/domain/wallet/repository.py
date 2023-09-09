from .wallet import Wallet


class Repository:
    # This example uses a dictionary to store Wallets by ID.
    def __init__(self):
        self.wallets = {}

    def get(self, id) -> Wallet:
        return self.wallets.get(id)

    def save(self, wallet):
        self.wallets[wallet.id] = wallet
