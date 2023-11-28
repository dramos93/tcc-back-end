import pytest
from game.data.use_cases.multiplication_game_use_cases.multiplication_game_use_cases import (
    MultiplicationGameUseCase,
)
from game.infra.db.repositories.multiplication_game_repository.multiplication_game_repository_mock import (
    MultiplicationGameRepositoryFake,
)

sample_entity = {
    "user_id": 1,
    "class_id": 1,
    "multiplication_table": 2,
    "round": 1,
    "errors": 3,
}

multiplication_game_repository_game = MultiplicationGameRepositoryFake()
use_case = MultiplicationGameUseCase(multiplication_game_repository_game)


def test_get_all():
    data = use_case.get_multiplication_game(user_id=1, class_id=1)
    assert len(data) == 1
    assert data[0]["user_id"] == sample_entity["user_id"]
    assert data[0]["class_id"] == sample_entity["class_id"]
    assert data[0]["multiplication_table"] == sample_entity["multiplication_table"]
    assert data[0]["round"] == sample_entity["round"]
    assert data[0]["errors"] == sample_entity["errors"]


def test_get_all_when_erro_not_found_game():
    try:
        use_case.get_multiplication_game(user_id=999, class_id=999)
    except:
        assert pytest.raises(Exception, match="Histórico do jogo não encontrado.")
