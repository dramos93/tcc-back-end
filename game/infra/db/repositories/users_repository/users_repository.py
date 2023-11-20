from typing import List

from sqlalchemy import select
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.users import Users
from game.infra.db.settings.connection import DBConnectionHandler
from game.infra.db.entities.user import UsersEntity


class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, user_name: str, user_nickname: str, user_class_id: int, user_role: int) -> None:
        with DBConnectionHandler() as db:
            try:
                engine = db.get_engine()
                # new_register.__table__.drop(bind=db.get_engine(), checkfirst=True)
                UsersEntity.create_table(engine=engine)

                new_register = UsersEntity(
                    user_name =user_name,
                    user_nickname = user_nickname,
                    user_class_id= user_class_id,
                    user_role = user_role
                )
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
                query = db.session.query(UsersEntity).filter(UsersEntity.user_nickname == user_nick_name).exists()
                return db.session.query(query).scalar()
            except Exception as exception:
                db.session.rollback()
                raise exception