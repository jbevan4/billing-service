import uuid

from billing_service.domain.wallet.events import WalletCreated


class InMemory:
    def __init__(self: "InMemory") -> None:
        self.wallets: dict[uuid.UUID, WalletCreated] = dict()

    def save_wallet(self: "InMemory", wallet: WalletCreated) -> None:
        self.wallets[wallet.user_id] = wallet

    def get_wallet(self: "InMemory", used_id: uuid.UUID) -> WalletCreated:
        return self.wallets.get(used_id)
