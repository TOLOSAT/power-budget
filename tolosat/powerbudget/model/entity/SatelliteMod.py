from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class SatelliteMod(DatabaseBase.get_base()):
    __tablename__: str = 'SATELLITE_MOD'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    name = Column('C_NAME', String(20))
    active_rate = Column('P_ACTIVE_RATE', Integer)

    related_board_mods = relationship("SatelliteBoardModRelation")

    def __init__(self, name: str):
        super(SatelliteMod, self).__init__()

        self.name = name
        self.active_rate = 50

    def __repr__(self):
        return f'SatelliteMod {self.name}'
