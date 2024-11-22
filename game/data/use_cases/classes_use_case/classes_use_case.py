from typing import Dict, List
from game.data.interfaces.class_repository_interface import ClassRepositoryInterface
from game.data.interfaces.class_user_repository_interface import (
    ClassUserRepositoryInterface,
)
from game.data.interfaces.multiplication_game_repository_interface import (
    MultiplicationGameRepositoryInterface,
)
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.class_user_model import ClassUserModel
from game.domain.models.users import Users
from game.domain.use_cases.classes.class_interface import ClassesUseCaseInterface


class ClassesUseCase(ClassesUseCaseInterface):
    def __init__(
        self,
        class_repository: ClassRepositoryInterface,
        user_repository: UsersRepositoryInterface,
        game_repository: MultiplicationGameRepositoryInterface,
        class_user_repository: ClassUserRepositoryInterface,
    ):
        self.class_repository = class_repository
        self.user_repository = user_repository
        self.game_repository = game_repository
        self.class_user_repository = class_user_repository

    def get_class(self, user_id: int) -> List[Dict]:
        """Retorna uma lista de todas as turmas de um dado professor.
        O professor pode ter uma turma.


        Args:
            class_id (int): O id do professor que pode ter mais de uma turma.

        Returns:
            List[Dict]: Todos os alunos de cada turma com o resultado do jogo em cada rodada e cada tabuada.
        """
        class_from_teacher = self.class_user_repository.get_classes(user_id=user_id)
        classes = []
        for c in class_from_teacher:
            users_id: List[
                ClassUserModel
            ] = self.class_user_repository.get_users_from_class(class_id=c.class_id)
            users: List[Users] = [
                self.user_repository.get_user_by_id(user_id=user.user_id)
                for user in users_id
            ]
            classes.append(
                {
                    "className": self.__get_class_name(class_id=c.class_id),
                    "students": [
                        {
                            "name": user.user_name,
                            "rounds": list(
                                self.__get_results(c.class_id, user.user_id)
                            ),
                        }
                        for user in users 
                        if user.user_role == 2
                    ],
                }
            )

        return classes
    
    def get_classes(self) -> List[Dict]:
        classes_from_repo = self.class_repository.get_all()
        classes = []
        for class_  in classes_from_repo:
            classes.append({
                "class_id": class_.class_id,
                "class_name": class_.class_name,
                "class_active": class_.class_active,
                })
        # return self.class_repository.get_all()
        return classes

    def __get_class_name(self, class_id: int) -> str:
        class_data = self.class_repository.get_by_id(class_id=class_id)
        return class_data.class_name

    def __get_results(self, class_id, user_id):
        results_from_user = self.game_repository.get_all(
            class_id=class_id, user_id=user_id
        )
        round_results: dict = {}
        for result in results_from_user:
            round_results.update(
                {
                    result.round: [
                        *round_results.get(result.round),
                        {"table": result.multiplication_table, "errors": result.errors},
                    ]
                    if round_results.get(result.round)
                    else [
                        {"table": result.multiplication_table, "errors": result.errors}
                    ]
                }
            )
        for round_num, results in round_results.items():
            sum_of_round_errors = sum(result["errors"] for result in results)
            yield {
                "round": round_num,
                "sum_of_round_errors": sum_of_round_errors,
                "resultsRounds": results,
            }
