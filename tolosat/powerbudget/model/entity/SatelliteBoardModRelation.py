from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class SatelliteBoardModRelation(DatabaseBase.get_base()):
    __tablename__: str = 'SAT_BOARD_MOD_RELATION'

    satellite_mod_id = Column(Integer, ForeignKey('SatelliteMod.id'), primary_key=True)
    #satellite_mod = relationship('SatelliteMod')
    board_mod_id = Column(Integer, ForeignKey('BoardMod.id'), primary_key=True)
    #board_mod = relationship('BoardMod')

    def __init__(self):
        super(SatelliteBoardModRelation, self).__init__()

    def __repr__(self):
        return f'SatelliteBoardModRelation {self.satellite_mod_id} / {self.board_mod_id}'
