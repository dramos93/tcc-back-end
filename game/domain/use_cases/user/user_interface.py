from abc import ABC, abstractmethod
from typing import Dict


class UserInterface(ABC):
    @abstractmethod
    def register(
        cls,
        user_name: str,
        user_nickname: str,
        user_role: int,
        user_password: str,
    ) -> None:
        pass

    @abstractmethod
    def find(cls, user_id: int) -> Dict:
        pass
