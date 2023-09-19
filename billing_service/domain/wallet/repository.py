from billing_service.domain.wallet.events import WalletCreated
from .wallet import Wallet


class Repository:
    # This example uses a dictionary to store Wallets by ID.
    def __init__(self):
        self.wallets = {}

    def get(self, user_id) -> Wallet:
        wallet = Wallet(user_id=user_id)
        wallet_events = self.wallets.get(user_id)
        if not wallet_events:
            return wallet
        for event in wallet_events:
            wallet.add_event(event)
        return wallet

    def save(self, wallet):
        self.wallets[wallet.user_id] = wallet.get_events()
