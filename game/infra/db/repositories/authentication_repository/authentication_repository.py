from uuid import UUID, uuid1
from sqlalchemy import insert, select, update
from game.data.interfaces.authentication_repository_interface import (
    AuthenticationRepositoryInterface,
)
from game.domain.models.authentication_model import AuthenticationModel
from game.infra.db.entities.authentication_entity import AuthenticationEntity
from game.infra.db.entities.user_entity import UsersEntity
from game.infra.db.settings.connection import DBConnectionHandler


class AuthenticationRepository(AuthenticationRepositoryInterface):
    @classmethod
    def create(cls, user_id: int) -> AuthenticationModel:
        with DBConnectionHandler() as db:
            engine = db.get_engine()
            UsersEntity.create_table(engine)
            AuthenticationEntity.create_table(engine=engine)
            inse = insert(AuthenticationEntity).values(user_id=user_id, token=uuid1()).returning(AuthenticationEntity)
            new_data = db.session.execute(inse).scalar()
            try:
                db.session.commit()
                db.session.refresh(new_data)
            except Exception as exception:
                breakpoint()
                db.session.rollback()
                raise exception
        return new_data

    @classmethod
    def get_token(cls, user_id: int) -> AuthenticationModel:
        with DBConnectionHandler() as db:
            try:
                query = select(AuthenticationEntity).filter(
                    (AuthenticationEntity.active)
                    & (AuthenticationEntity.user_id == user_id)
                )
                data = db.session.execute(query).scalar()

                return data
            except Exception as exception:
                breakpoint()
                db.session.rollback()
                raise exception

    @classmethod
    def logout(cls, user_id: int, token: UUID) -> None:
        with DBConnectionHandler() as db:
            try:
                query = (
                    update(AuthenticationEntity)
                    .filter(
                        (AuthenticationEntity.user_id == user_id)
                        & (AuthenticationEntity.token == token)
                    )
                    .values(active=False)
                )
                db.session.execute(query)
                db.session.commit()
            except Exception as exception:
                breakpoint()
                db.session.rollback()
                raise exception
