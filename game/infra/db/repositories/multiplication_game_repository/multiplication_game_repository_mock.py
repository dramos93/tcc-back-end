from typing import List
from game.data.interfaces.multiplication_game_repository_interface import (
    MultiplicationGameRepositoryInterface,
)
from game.domain.models.multiplication_game_model import MultiplicationGameModel


sample_entity = {
    "user_id": 1,
    "class_id": 1,
    "multiplication_table": 2,
    "round": 1,
    "errors": 3,
}


class MultiplicationGameRepositoryFake(MultiplicationGameRepositoryInterface):
    @classmethod
    def create(
        cls,
        user_id: int,
        class_id: int,
        multiplication_table: int,
        round: int,
        errors: int,
    ) -> None:
        pass

    @classmethod
    def get_all(cls, user_id: int, class_id: int) -> List[MultiplicationGameModel]:
        multiplication_games = [
            MultiplicationGameModel(
                user_id=sample_entity["class_id"],
                class_id=sample_entity["class_id"],
                multiplication_table=sample_entity["multiplication_table"],
                round=sample_entity["round"],
                errors=sample_entity["errors"],
            )
        ]

        return (
            multiplication_games
            if (
                user_id
                == sample_entity["user_id"] & class_id
                == sample_entity["class_id"]
            )
            else []
        )
