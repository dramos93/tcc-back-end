class Users:
    def __init__(
        self,
        user_id: int,
        user_name: str,
        user_nickname: str,
        user_role: int,
        user_active: bool,
    ) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.user_nickname = user_nickname
        self.user_role = user_role
        self.user_active = user_active
