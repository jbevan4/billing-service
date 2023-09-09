from .commands import ChangeBalance
from .repository import Repository
from .wallet import Wallet


class WalletCommandHandler:
    def __init__(self, repository: Repository):
        self.repository = repository

    def handle_create_wallet(self, command):
        wallet = Wallet(create=command)
        self.repository.save(wallet)


class BalanceCommandHandler:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def handle_change_balance(self, command: ChangeBalance):
        wallet = self.repository.get(command.wallet_id)
        if not wallet:
            raise ValueError(f"No wallet found with id {command.wallet_id}")
        wallet.request_balance_change(command)
        self.repository.save(wallet)
