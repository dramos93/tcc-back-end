from typing import Dict, List
from game.data.interfaces.class_repository_interface import ClassRepositoryInterface
from game.data.interfaces.multiplication_game_repository_interface import (
    MultiplicationGameRepositoryInterface,
)
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.multiplication_game_model import MultiplicationGameModel
from game.domain.use_cases.multiplication_game.multiplication_game_interface import (
    MultiplicationGameInterface,
)


class MultiplicationGameUseCase(MultiplicationGameInterface):
    def __init__(
        self,
        multiplication_game_repository: MultiplicationGameRepositoryInterface,
        user_repository: UsersRepositoryInterface,
        class_repository: ClassRepositoryInterface,
    ) -> None:
        self.multiplication_game_repository = multiplication_game_repository
        self.user_repository = user_repository
        self.class_repository = class_repository

    def create_multiplication_game(
        self,
        user_id: int,
        class_id: int,
        multiplication_table: int,
        round: int,
        errors: int,
    ) -> None:
        self.__exist_class(class_id=class_id)
        self.__exist_user(user_id=user_id)
        self.multiplication_game_repository.create(
            user_id=user_id,
            class_id=class_id,
            multiplication_table=multiplication_table,
            round=round,
            errors=errors,
        )

    def get_multiplication_game(self, user_id: int, class_id: int) -> List[Dict]:
        self.__exist_class(class_id=class_id)
        self.__exist_user(user_id=user_id)
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

    def __exist_class(self, class_id: int) -> None:
        if not self.class_repository.exists(class_id=class_id):
            raise Exception("Classe não encontrada.")

    def __exist_user(self, user_id: int) -> None:
        if not self.user_repository.get_user_by_id(user_id=user_id):
            raise Exception("Usuário não encontrado.")
