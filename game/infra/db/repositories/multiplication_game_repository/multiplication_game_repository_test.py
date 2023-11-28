import pytest
from game.infra.db.repositories.multiplication_game_repository.multiplication_game_repository import (
    MultiplicationGameRepository,
)


sample_entity = {
    "user_id": 1,
    "class_id": 1,
    "multiplication_table": 2,
    "round": 1,
    "errors": 3,
}


@pytest.mark.skip("Já era.")
def test_create_multiplication_game_table():
    multiplication_game_repository = MultiplicationGameRepository()
    multiplication_game_repository.create(**sample_entity)


def test_get_all_from_multiplication_game_table():
    multiplication_game_repository = MultiplicationGameRepository()
    data = multiplication_game_repository.get_all(
        user_id=sample_entity["user_id"], class_id=sample_entity["class_id"]
    )
    assert data[0].user_id == sample_entity["user_id"]
    assert data[0].class_id == sample_entity["class_id"]
    assert data[0].multiplication_table == sample_entity["multiplication_table"]
    assert data[0].round == sample_entity["round"]
    assert data[0].errors == sample_entity["errors"]


def test_get_all_if_not_exists():
    multiplication_game_repository = MultiplicationGameRepository()
    data = multiplication_game_repository.get_all(user_id=999, class_id=999)
    assert data == []
