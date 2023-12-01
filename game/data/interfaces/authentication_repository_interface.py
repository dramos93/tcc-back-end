from abc import ABC, abstractmethod
from uuid import UUID
from game.domain.models.authentication_model import AuthenticationModel


class AuthenticationRepositoryInterface(ABC):
    @abstractmethod
    def create(cls, user_id: int) -> AuthenticationModel:
        pass

    @abstractmethod
    def get_token(cls, user_id: int) -> AuthenticationModel:
        pass

    @abstractmethod
    def logout(cls, user_id: int, token: UUID) -> None:
        pass
