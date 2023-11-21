from abc import ABC, abstractmethod
from typing import List
from game.domain.models.multiplication_game_model import MultiplicationGameModel


class MultiplicationGameRepositoryInterface(ABC):

    @abstractmethod
    def create(cls, user_id: int, class_id: int, multiplication_table: int, round: int, errors: int) -> None: pass

    @abstractmethod
    def get_all(cls, user_id: int, class_id: int) -> List[MultiplicationGameModel]: pass
