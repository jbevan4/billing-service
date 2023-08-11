import uuid


class CreateWallet:
    def __init__(self: "CreateWallet", user_id: uuid.UUID) -> None:
        self.user_id = user_id
