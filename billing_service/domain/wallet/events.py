import uuid
from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class OperationType(str, Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"


class WalletCreated(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(nullable=False, index=True)
    balance: int = Field(default=0)
    created_at: datetime = Field(nullable=False)


class BalanceUpdated(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    wallet_id: uuid.UUID = Field(nullable=False)
    amount: int = Field(nullable=False)
    timestamp: datetime = Field(nullable=False)
