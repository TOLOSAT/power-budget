from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection


class DatabaseEngine:
    """ The Engine is how SQLAlchemy communicates with a database """
    # TODO: replace raw path reference to a const reference
    # TODO: replace echo parameter to an environment properties file
    # 'echo' parameter: shows actions of the engine on the database if True
    __engine: MockConnection = create_engine('sqlite:///:memory:', echo=True)

    @staticmethod
    def get_engine():
        return DatabaseEngine.__engine
