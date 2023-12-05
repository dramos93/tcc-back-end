from abc import ABC, abstractmethod
from typing import Dict, List


class ClassesInterface(ABC):
    @abstractmethod
    def get_class(cls, class_id: int) -> List[Dict]:
        ...
