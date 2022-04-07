from sqlalchemy.orm import sessionmaker, Session, scoped_session

from tolosat.powerbudget.model.database.engine.DatabaseEngine import DatabaseEngine


class DatabaseSession:
    """ The Object - relational Mapper (ORM) must have a session to make the middle-ground between
        the objects we will deal with in Python and the engine that actually communicates with the database. """
    __session: Session = None

    @staticmethod
    def __init__():
        """Initialize db session"""
        DatabaseSession.__session: sessionmaker = scoped_session(sessionmaker())
        DatabaseSession.__session.configure(bind=DatabaseEngine.get_engine())
        #session_factory: sessionmaker = sessionmaker(bind=DatabaseEngine.get_engine())
        #DatabaseSession.__session = session_factory()

    @staticmethod
    def get_session():
        return DatabaseSession.__session
