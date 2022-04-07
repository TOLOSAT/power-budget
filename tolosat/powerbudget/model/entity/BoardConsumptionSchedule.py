from sqlite3 import Timestamp

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase


class BoardConsumptionSchedule(DatabaseBase.get_base()):
    __tablename__: str = 'SATELLITE_MOD'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    start_time = Column('T_START', Timestamp)
    end_time = Column('T_END', Timestamp)
    value_id = Column(Integer, ForeignKey('Value.id'))
    value = relationship('Value')
    board_mod_id = Column(Integer, ForeignKey('BoardMod.id'), primary_key=True)
    board_mod = relationship('BoardMod')

    def __init__(self):
        super(BoardConsumptionSchedule, self).__init__()

    def __repr__(self):
        return f'BoardConsumptionSchedule {self.id}'
