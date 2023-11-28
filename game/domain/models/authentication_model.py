from datetime import datetime
from uuid import UUID


class AuthenticationModel:
    def __init__(
        self, user_id: int, token: UUID, created_on: datetime, active: bool
    ) -> None:
        self.user_id = user_id
        self.token = token
        self.created_on = created_on
        self.active = active
