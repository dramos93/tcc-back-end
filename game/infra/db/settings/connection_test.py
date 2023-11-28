from game.infra.db.settings.connection import DBConnectionHandler


def test_connection_handler():
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()
    print(engine.connect())
    print(engine.url)
    # assert engine is not None
