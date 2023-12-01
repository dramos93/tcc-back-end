from abc import ABC, abstractmethod
from typing import Dict
from uuid import UUID


class AuthenticationUserCaseInterface(ABC):
    @abstractmethod
    def create_token(cls, user_id: int, user_password: str) -> Dict:
        pass

    @abstractmethod
    def get_token(cls, user_id: int) -> Dict:
        pass

    @abstractmethod
    def logout(cls, user_id: int, token: UUID) -> None:
        pass
