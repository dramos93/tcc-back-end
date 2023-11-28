from abc import ABC, abstractmethod
from typing import Dict


class UserRegisterInterface(ABC):
    @abstractmethod
    def register(
        cls, user_name: str, user_nickname: str, user_class_id: int, user_role: int
    ) -> Dict:
        pass
