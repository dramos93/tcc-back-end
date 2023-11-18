from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "postgresql://postgres:123456@localhost:5432/game"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        
        if not database_exists(engine.url):
            create_database(engine.url)

        return engine

    def get_engine(self):
        return self.__engine
    
    # def create_table_when_does_not(self, TableEntity) -> None:
    #     # ins = inspect(self.__engine)
    #     # ret = ins.has_table(table_name=TableEntity.__tablename__)

    #     # if (not ret):
    #     #     table = TableEntity.__table__
    #     #     table.create(bind=self.__engine, checkfirst=True)
    #     table = TableEntity.__table__
    #     rt = table.create(bind=self.__engine, checkfirst=True)
    #     print(f"\n\n\nCRIOU A TABELA {TableEntity.__tablename__} ---- {rt}\n\n\n")
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tab) -> None:
        self.session.close()