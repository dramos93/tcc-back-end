from typing import Dict, List
from game.data.interfaces.class_repository_interface import ClassRepositoryInterface
from game.data.interfaces.multiplication_game_repository_interface import (
    MultiplicationGameRepositoryInterface,
)
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.use_cases.classes.class_interface import ClassesInterface


class Classes(ClassesInterface):
    def __init__(
        self,
        class_repository: ClassRepositoryInterface,
        user_repository: UsersRepositoryInterface,
        game_repository: MultiplicationGameRepositoryInterface,
    ):
        self.class_repository = class_repository
        self.user_repository = user_repository
        self.game_repository = game_repository

    def get_class(self, class_id: int) -> Dict:
        """Retorna uma lista de todas as turmas de um dado professor.
        O professor pode ter uma turma.


        Args:
            class_id (int): O id do professor que pode ter mais de uma turma.

        Returns:
            List[Dict]: Todos os alunos de cada turma com o resultado do jogo em cada rodada e cada tabuada.
        """
        user_data = self.user_repository.get_students_by_class(class_id=class_id)

        # a = {}
        # for use in user_data:
        #     a= {

        #     }

        return {
            "className": self.__get_class_name(class_id=class_id),
            "students": [
                {
                    "name": "Daniel",
                    "rounds": [
                        {
                            "round": 1,
                            "sum_of_round_errors": 13,
                            "resultsRounds": [
                                {"table": 1, "errors": 1},
                                {"table": 2, "errors": 7},
                                {"table": 3, "errors": 5},
                            ],
                        }
                    ],
                },
                {
                    "name": "Daniel Filho",
                    "rounds": [
                        {
                            "round": 1,
                            "sum_of_round_errors": 20,
                            "resultsRounds": [
                                {"table": 1, "errors": 8},
                                {"table": 2, "errors": 7},
                                {"table": 3, "errors": 5},
                            ],
                        }
                    ],
                },
                {
                    "name": "Artur",
                    "rounds": [
                        {
                            "round": 1,
                            "sum_of_round_errors": 23,
                            "resultsRounds": [
                                {"table": 1, "errors": 1},
                                {"table": 2, "errors": 7},
                                {"table": 3, "errors": 15},
                            ],
                        }
                    ],
                },
            ],
        }

    def __get_class_name(self, class_id: int) -> str:
        class_data = self.class_repository.get_by_id(class_id=class_id)
        return class_data.class_name
