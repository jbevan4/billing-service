from datetime import datetime

from billing_service.domain.wallet.commands.create_wallet import CreateWallet
from billing_service.domain.wallet.events import WalletCreated
from billing_service.domain.wallet.repository.in_memory import InMemory


class CreateWalletHandler:
    def __init__(self: "CreateWalletHandler", db: InMemory) -> None:
        self.db = db

    def handle(self: "CreateWalletHandler", command: CreateWallet) -> None:
        wallet_created_event = WalletCreated(
            user_id=command.user_id, created_at=datetime.utcnow()
        )
        self.db.save_wallet(wallet_created_event)
