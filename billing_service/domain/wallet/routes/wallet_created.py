from billing_service.domain.wallet.commands.add_credits_to_balance import (
    AddCreditsToBalance,
)
from billing_service.domain.wallet.commands.remove_credits_from_balance import (
    RemoveCreditsFromBalance,
)
from billing_service.domain.wallet.repository.in_memory import InMemory
from fastapi import APIRouter

router = APIRouter()


@router.post("/add_credits_to_wallet/")
async def add_credits_to_wallet_route() -> None:
    repo = InMemory()
    command = AddCreditsToBalance()
    return command.apply()


@router.post("/remove_credits_from_wallet/")
async def remove_credits_from_wallet() -> None:
    repo = InMemory()
    command = RemoveCreditsFromBalance()
    return command.apply()
