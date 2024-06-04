from abc import ABC, abstractmethod
from typing import Dict, List


class ClassesUseCaseInterface(ABC):
    @abstractmethod
    def get_class(cls, user_id: int) -> List[Dict]:
        ...
    @abstractmethod
    def get_classes(cls) -> List[Dict]:
        ...
