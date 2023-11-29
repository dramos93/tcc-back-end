from abc import ABC, abstractmethod
from typing import Dict


class MultiplicationGameInterface(ABC):
    @abstractmethod
    def get_multiplication_game(cls, user_id: int, class_id: int) -> Dict:
        pass

    @abstractmethod
    def create_multiplication_game(
        cls,
        user_id: int,
        class_id: int,
        multiplication_table: int,
        round: int,
        errors: int,
    ) -> None:
        pass
