from .wallet import Wallet


class Repository:
    # This example uses a dictionary to store Wallets by ID.
    def __init__(self: "Repository") -> None:
        self.wallets = {}

    def get(self: "Repository", user_id: str) -> Wallet:
        wallet = Wallet(user_id=user_id)
        wallet_events = self.wallets.get(user_id)
        if not wallet_events:
            return wallet
        for event in wallet_events:
            wallet.add_event(event)
        return wallet

    def save(self: "Repository", wallet: Wallet) -> None:
        self.wallets[wallet.user_id] = wallet.get_events()
