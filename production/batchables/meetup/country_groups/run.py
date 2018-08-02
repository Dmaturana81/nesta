import logging
from meetup.country_groups import MeetupCountryGroups
from orms.orm_utils import get_mysql_engine
from orms.meetup_orm import Base
from orms.meetup_orm import Group

def run():
    logging.getLogger().setLevel(logging.INFO)

    # Load connection to the input db, and create the tables
    engine = get_mysql_engine("BATCHPAR_outinfo",
                              "mysqldb", "production")
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    
    mcg = MeetupCountryGroups(iso2=self.iso2, category=self.category)
    mcg.get_groups_recursive()
    output = meetup_utils.flatten_data(mcg.groups,
                                       country_name=mcg.country_name,
                                       country_code=mcg.country_code,
                                       keys=[('category', 'name'),
                                             ('category', 'shortname'),
                                             ('category', 'id'),
                                             'description',
                                             'created',
                                             'country',
                                             'city',
                                             'id',
                                             'lat',
                                             'lon',
                                             'members',
                                             'name',
                                             'topics',
                                             'urlname'])