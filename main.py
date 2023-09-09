from operator import add, sub

from billing_service.domain.wallet.command_handler import (
    BalanceCommandHandler,
    WalletCommandHandler,
)
from billing_service.domain.wallet.commands import ChangeBalance, CreateWallet
from billing_service.domain.wallet.repository import Repository

repository = Repository()
walletHandler = WalletCommandHandler(repository=repository)
balanceHandler = BalanceCommandHandler(repository=repository)


create_wallet_command = CreateWallet(
    id=123,
    user_id=123,
)
walletHandler.handle_create_wallet(create_wallet_command)
wallet = repository.get(123)
print(wallet)
print(wallet.balance)

balance_changed_command = ChangeBalance(amount=100, wallet_id=123, operation=add)
balanceHandler.handle_change_balance(balance_changed_command)
print(wallet.balance)
