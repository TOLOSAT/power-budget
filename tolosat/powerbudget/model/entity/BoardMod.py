from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class BoardMod(DatabaseBase.get_base()):
    __tablename__: str = 'BOARD_MOD'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    name = Column('C_NAME', String(20))
    is_consumption_linear = Column('B_IS_CONSUMPTION_LINEAR', Boolean)
    linear_consumption_id = Column(Integer, ForeignKey('Value.id'))
    linear_consumption = relationship('Value')
    active_rate = Column('P_ACTIVE_RATE', Integer)

    related_satellite_mods = relationship("SatelliteBoardModRelation")

    def __init__(self, name: str):
        super(BoardMod, self).__init__()

        self.name = name
        self.active_rate = 50

    def __repr__(self):
        return f'BoardMod {self.name}'
