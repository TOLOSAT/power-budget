from sqlalchemy import Column, Integer, String

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class VariableEnum(DatabaseBase.get_base()):
    __tablename__: str = 'VARIABLE_ENUM'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    label = Column('C_LABEL', String(50))

    def __init__(self, label: str):
        super(VariableEnum, self).__init__()

        self.label = label

    def __repr__(self):
        return f'VariableEnum {self.label}'
