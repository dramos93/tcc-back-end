from game.infra.db.settings.connection import DBConnectionHandler
from game.infra.db.entities.user import UsersEntity


class UsersRepository():

    @classmethod
    def insert_user(cls, user_name: str, user_nickname: str, user_class_id: int, user_role: int) -> None:
        with DBConnectionHandler() as db:
            try:
                # new_register.__table__.drop(bind=db.get_engine(), checkfirst=True)
                UsersEntity.create_table(db.get_engine())

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
    def get_all_users(cls) -> any:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(UsersEntity).all()
               
            except Exception as exception:
                db.session.rollback()
                return exception
            
    @classmethod
    def get_user_by_id(cls, user_id: int) -> any:
        with DBConnectionHandler() as db:
            try:
                return db.session.query(UsersEntity).filter(UsersEntity.user_id == user_id).first()
                
            except Exception as exception:
                db.session.rollback()
                return exception
