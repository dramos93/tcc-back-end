from abc import ABC, abstractmethod

from game.domain.models.classModel import ClassModel


class ClassRepositoryInterface(ABC):

    @abstractmethod
    def create(cls, class_name: str) -> None: pass

    @abstractmethod
    def get_by_id(cls, class_id: int) -> ClassModel: pass

    @abstractmethod
    def exists(cls, class_id: int) -> bool: pass