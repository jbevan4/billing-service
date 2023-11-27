from operator import add, sub

import pytest
from billing_service.domain.wallet.events import BalanceChanged, WalletCreated
from billing_service.domain.wallet.wallet import Wallet


@pytest.fixture
def wallet() -> Wallet:
    user_id = "123"
    wallet = Wallet(user_id=user_id)
    return wallet


def test_wallet_creation(wallet: Wallet) -> None:
    assert wallet.user_id == "123"
    assert wallet.current_balance == 0


def test_balance_change(wallet: Wallet) -> None:
    wallet.handle_wallet_created(WalletCreated("123"))
    wallet.handle_balance_changed(BalanceChanged(wallet.id, 50, add))
    wallet.handle_balance_changed(BalanceChanged(wallet.id, 50, add))
    assert wallet.current_balance == 100


def test_negative_balance(wallet: Wallet) -> None:
    wallet.handle_wallet_created(WalletCreated("123"))
    with pytest.raises(ValueError):
        wallet.handle_balance_changed(BalanceChanged(wallet.id, 50, sub))


def test_get_events(wallet: Wallet) -> None:
    events = wallet.get_events()
    assert isinstance(events, list)


def test_bad_event_handling(wallet: Wallet) -> None:
    class BadEvent:
        pass

    with pytest.raises(ValueError):
        wallet.add_event(BadEvent())
