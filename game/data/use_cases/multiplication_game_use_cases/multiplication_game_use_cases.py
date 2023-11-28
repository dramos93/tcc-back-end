from typing import Dict, List
from game.data.interfaces.multiplication_game_repository_interface import (
    MultiplicationGameRepositoryInterface,
)
from game.domain.models.multiplication_game_model import MultiplicationGameModel
from game.domain.user_cases.multiplication_game.multiplication_game_interface import (
    MultiplicationGameInterface,
)


class MultiplicationGameUseCase(MultiplicationGameInterface):
    def __init__(
        self, multiplication_game_repository: MultiplicationGameRepositoryInterface
    ) -> None:
        self.multiplication_game_repository = multiplication_game_repository

    def get_multiplication_game(self, user_id: int, class_id: int) -> List[Dict]:
        multiplicadion_games = self.multiplication_game_repository.get_all(
            user_id=user_id, class_id=class_id
        )
        if not multiplicadion_games:
            raise Exception("Histórico do jogo não encontrado.")

        response = self.__ajust_response(multiplicadion_games=multiplicadion_games)

        return response

    @classmethod
    def __ajust_response(
        cls, multiplicadion_games: List[MultiplicationGameModel]
    ) -> List[Dict]:
        response = []
        for multiplicadion_game in multiplicadion_games:
            response.append(
                {
                    "user_id": multiplicadion_game.user_id,
                    "class_id": multiplicadion_game.class_id,
                    "multiplication_table": multiplicadion_game.multiplication_table,
                    "round": multiplicadion_game.round,
                    "errors": multiplicadion_game.errors,
                }
            )

        return response
