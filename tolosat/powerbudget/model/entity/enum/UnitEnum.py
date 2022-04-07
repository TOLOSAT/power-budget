from sqlalchemy import Column, Integer, String

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class UnitEnum(DatabaseBase.get_base()):
    __tablename__: str = 'UNIT_ENUM'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    label = Column('C_LABEL', String(10))

    def __init__(self, label: str):
        super(UnitEnum, self).__init__()

        self.label = label

    def __repr__(self):
        return f'UnitEnum {self.label}'
