from abc import ABC, abstractmethod
from typing import List
from game.domain.models.users import Users
from game.infra.db.entities.user import UsersEntity


class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(cls, user_name: str, user_nickname: str, user_class_id: int, user_role: int) -> None: pass

    @abstractmethod
    def get_all_users(cls) -> List[UsersEntity]: pass

    @abstractmethod
    def get_user_by_id(cls, user_id: int) -> Users: pass