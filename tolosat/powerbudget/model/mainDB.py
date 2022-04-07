from tolosat.powerbudget.model.database.base.DatabaseBase import DatabaseBase
from tolosat.powerbudget.model.database.session.DatabaseSession import DatabaseSession
from tolosat.powerbudget.model.entity.SatelliteMod import SatelliteMod


if __name__ == '__main__':
    DatabaseBase.create_base()

    session = DatabaseSession().get_session()

    # create instances
    satelliteMod1 = SatelliteMod(name='init')
    satelliteMod1.active_rate = 75

    satelliteMod2 = SatelliteMod('eco')
    satelliteMod2.active_rate = 25
    print(satelliteMod1)
    # testing
    session.add(satelliteMod1)
    session.add_all([satelliteMod1, satelliteMod2])
    session.commit()
    print(satelliteMod2)

    print(session.query(SatelliteMod).filter_by(name='eco').first().active_rate)

    for satMod in session.query(SatelliteMod):
        print(satMod.name)
