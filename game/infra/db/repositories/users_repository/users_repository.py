from typing import List
from sqlalchemy import select
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.users import Users
from game.infra.db.settings.connection import DBConnectionHandler
from game.infra.db.entities.user_entity import UsersEntity


class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def insert_user(
        cls,
        user_name: str,
        user_nickname: str,
        user_role: int,
        user_password: str,
        user_active: bool = True,
    ) -> None:
        with DBConnectionHandler() as db:
            try:
                engine = db.get_engine()
                UsersEntity.create_table(engine=engine)

                new_register = UsersEntity(
                    user_name=user_name,
                    user_nickname=user_nickname,
                    user_password=user_password,
                    user_role=user_role,
                    user_active=user_active,
                )
                # new_register.__table__.drop(bind=db.get_engine(), checkfirst=True)

                db.session.add(new_register)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def get_all_users(cls) -> List[Users]:
        with DBConnectionHandler() as db:
            try:
                query = select(UsersEntity)
                entities = db.session.execute(query).scalars().all()
                return list(entities)

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def get_user_by_id(cls, user_id: int) -> Users:
        with DBConnectionHandler() as db:
            try:
                query = select(UsersEntity).where(UsersEntity.user_id == user_id)
                entity = db.session.execute(query).scalar()
                return entity

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def nick_name_exists(cls, user_nick_name: str) -> bool:
        with DBConnectionHandler() as db:
            try:
                query = (
                    db.session.query(UsersEntity)
                    .filter(UsersEntity.user_nickname == user_nick_name)
                    .exists()
                )
                return db.session.query(query).scalar()
            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def login(cls, user_id: int, user_password: str) -> bool:
        with DBConnectionHandler() as db:
            try:
                query = (
                    db.session.query(UsersEntity)
                    .filter(
                        (UsersEntity.user_id == user_id)
                        & (UsersEntity.user_password == user_password)
                    )
                    .exists()
                )
                return db.session.query(query).scalar()

            except Exception as exception:
                db.session.rollback()
                raise exception
