from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta

from tolosat.powerbudget.model.database.engine.DatabaseEngine import DatabaseEngine


class DatabaseBase:
    """ To map which table in the db will be related to each class in our files, we will use a SQLAlchemy system
        called Declarative. To use this, the first thing we must do is to instantiate a Base.
        Each of our dataclass will in inherit our Base declarative. """
    __base: DeclarativeMeta = declarative_base()
    # TODO: change to const/enum reference
    __is_base_created: bool = False

    @staticmethod
    def create_base():
        """ Create the tables (which inherit from this base) on the engine database """
        if not DatabaseBase.__is_base_created:
            DatabaseBase.__base.metadata.bind = DatabaseEngine.get_engine()
            DatabaseBase.__base.metadata.create_all(DatabaseEngine.get_engine())
            DatabaseBase.__is_base_created = True

    @staticmethod
    def get_base():
        #if not DatabaseBase.__is_base_created:
        #    DatabaseBase.__base.metadata.create_all(DatabaseEngine.get_engine())
        #    DatabaseBase.__is_base_created = True

        return DatabaseBase.__base
