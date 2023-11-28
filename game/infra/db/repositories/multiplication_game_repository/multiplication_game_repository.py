from typing import List
from sqlalchemy import select
from game.data.interfaces.multiplication_game_repository_interface import (
    MultiplicationGameRepositoryInterface,
)
from game.domain.models.multiplication_game_model import MultiplicationGameModel
from game.infra.db.entities.multiplication_game_entity import MultiplicationGameEntity
from game.infra.db.settings.connection import DBConnectionHandler


class MultiplicationGameRepository(MultiplicationGameRepositoryInterface):
    @classmethod
    def create(
        cls,
        user_id: int,
        class_id: int,
        multiplication_table: int,
        round: int,
        errors: int,
    ) -> None:
        with DBConnectionHandler() as db:
            try:
                engine = db.get_engine()
                MultiplicationGameEntity.create_table(engine=engine)

                new_data = MultiplicationGameEntity(
                    user_id=user_id,
                    class_id=class_id,
                    multiplication_table=multiplication_table,
                    round=round,
                    errors=errors,
                )

                db.session.add(new_data)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def get_all(cls, user_id: int, class_id: int) -> List[MultiplicationGameModel]:
        """Get all multiplication game from user_id and class_id"""
        with DBConnectionHandler() as db:
            try:
                query = select(MultiplicationGameEntity).filter(
                    MultiplicationGameEntity.user_id == user_id,
                    MultiplicationGameEntity.class_id == class_id,
                )
                data = db.session.execute(query).scalars().all()
                return list(data)
            except Exception as exception:
                db.session.rollback()
                raise exception
