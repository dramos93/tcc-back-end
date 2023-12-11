from abc import ABC, abstractmethod
from typing import List

from game.domain.models.class_user_model import ClassUserModel


class ClassUserRepositoryInterface(ABC):
    @abstractmethod
    def create(cls, class_id: int, user_id: int) -> ClassUserModel:
        ...

    @abstractmethod
    def get_classes(cls, user_id: int) -> List[ClassUserModel]:
        ...

    @abstractmethod
    def get_users_from_class(cls, class_id: int) -> List[ClassUserModel]:
        ...
