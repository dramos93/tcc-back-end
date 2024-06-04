from abc import ABC, abstractmethod
from typing import List
from game.domain.models.users import Users
from game.infra.db.entities.user_entity import UsersEntity


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(
        cls,
        user_name: str,
        user_nickname: str,
        user_role: int,
        user_password: str,
        user_active: bool = True,
    ) -> None:
        pass

    @abstractmethod
    def get_all_users(cls) -> List[UsersEntity]:
        pass

    @abstractmethod
    def get_user_by_id(cls, user_id: int) -> Users:
        pass

    @abstractmethod
    def nick_name_exists(cls, user_nickname: str) -> bool:
        pass

    @abstractmethod
    def login(cls, user_id: int, user_password: str) -> bool:
        ...
