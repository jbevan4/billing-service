from billing_service.domain.wallet.events import WalletCreated
from billing_service.domain.wallet.queries.get_wallet import GetWallet
from billing_service.domain.wallet.repository.in_memory import InMemory


class GetWalletHandler:
    def __init__(self: "GetWalletHandler", db: InMemory) -> None:
        self.db = db

    def handle(self: "GetWalletHandler", query: GetWallet) -> WalletCreated:
        return self.db.get_wallet(query.user_id)
