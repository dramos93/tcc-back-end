from abc import ABC, abstractmethod

from game.domain.models.authentication_model import AuthenticationModel


class AuthenticationUserCaseInterface(ABC):
    @abstractmethod
    def create_token(cls) -> None:
        pass

    @abstractmethod
    def get_token(cls) -> AuthenticationModel:
        pass

    @abstractmethod
    def logout(cls) -> None:
        pass
