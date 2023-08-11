import uuid

from billing_service.domain.wallet.commands.create_wallet import CreateWallet
from billing_service.domain.wallet.commands.handlers import CreateWalletHandler
from billing_service.domain.wallet.events import WalletCreated
from billing_service.domain.wallet.queries.get_wallet import GetWallet
from billing_service.domain.wallet.queries.handlers import GetWalletHandler
from billing_service.domain.wallet.repository.in_memory import InMemory
from fastapi import APIRouter, HTTPException

router = APIRouter()
db = InMemory()


@router.post("/wallet")
def create_wallet(user_id: uuid.UUID) -> dict[str, str]:
    command = CreateWallet(user_id=user_id)
    command_handler = CreateWalletHandler(db)
    command_handler.handle(command)
    return {"status": "success"}


@router.get("/wallet/{user_id}", response_model=WalletCreated)
def get_wallet(user_id: uuid.UUID) -> WalletCreated:
    query = GetWallet(user_id=user_id)
    query_handler = GetWalletHandler(db)
    wallet = query_handler.handle(query)
    if wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet
