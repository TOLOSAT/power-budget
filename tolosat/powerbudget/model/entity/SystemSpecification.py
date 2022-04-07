from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class SystemSpecification(DatabaseBase.get_base()):
    __tablename__: str = 'SYSTEM_SPEC'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    value = Column('F_VALUE', Float())
    variable_enum_id = Column(Integer, ForeignKey('VariableEnum.id'))
    variable_enum = relationship('VariableEnum')
    value_id = Column(Integer, ForeignKey('Value.id'))
    value = relationship('Value')

    def __init__(self):
        super(SystemSpecification, self).__init__()

    def __repr__(self):
        return f'SystemSpecification {self.value} {self.variable_enum}'
