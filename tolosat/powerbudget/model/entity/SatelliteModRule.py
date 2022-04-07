from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class SatelliteModRule(DatabaseBase.get_base()):
    __tablename__: str = 'SATELLITE_MOD_RULE'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    sat_mod_before_id = Column(Integer, ForeignKey('SatelliteMod.id'))
    sat_mod_before = relationship('SatelliteMod')
    sat_mod_after_id = Column(Integer, ForeignKey('SatelliteMod.id'))
    sat_mod_after = relationship('SatelliteMod')
    variable_enum_id = Column(Integer, ForeignKey('VariableEnum.id'))
    variable_enum = relationship('VariableEnum')
    comparator_enum_id = Column(Integer, ForeignKey('ComparatorEnum.id'))
    comparator_enum = relationship('ComparatorEnum')
    value_id = Column(Integer, ForeignKey('Value.id'))
    value = relationship('Value')

    def __init__(self):
        super(SatelliteModRule, self).__init__()

    def __repr__(self):
        return f'SatelliteModRule {self.id}'
