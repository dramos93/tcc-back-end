from typing import List
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.users import Users


class UsersRepositoryMock(UsersRepositoryInterface):
    @classmethod
    def insert_user(
        cls,
        user_name: str,
        user_nickname: str,
        user_role: int,
        user_password: str,
    ) -> None:
        pass

    @classmethod
    def get_all_users(cls) -> List[Users]:
        return [Users(1, "Daniel", "dramos93", 1, True)]

    @classmethod
    def get_user_by_id(cls, user_id: int) -> Users | None:
        if user_id == 1:
            return Users(1, "Daniel", "dramos93", 1, True)
        else:
            return None

    @classmethod
    def nick_name_exists(cls, user_nick_name: str) -> bool:
        return True if user_nick_name == "dramos93" else False

    @classmethod
    def login(cls, user_id: int, user_password: str) -> bool:
        if (user_id == 1) & (user_password == "123456"):
            return True
        else:
            return False
