import uuid


class GetWallet:
    def __init__(self: "GetWallet", user_id: uuid.UUID) -> None:
        self.user_id = user_id
