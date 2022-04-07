from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class Value(DatabaseBase.get_base()):
    __tablename__: str = 'VALUE'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    value = Column('F_VALUE', Float())
    unit_enum_id = Column(Integer, ForeignKey('UnitEnum.id'))
    unit_enum = relationship('UnitEnum')

    def __init__(self, value: float):
        super(Value, self).__init__()

        self.value = value

    def __repr__(self):
        return f'Value {self.value}'
