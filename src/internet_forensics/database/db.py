from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

# this connects to db
engine = create_engine('sqlite:///../datastore/local.db')

# this is to manage tables
base = declarative_base()


class Users(base):

    __tablename__ = 'users'

    '''
    these are the rows to be created inside the users table the privacy part represents:
    False if not agreed, True if agreed
    GDPR privacy follows the same reasoning but is divided in two levels, marketing and necessary
    '''
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __init__(self, user_id, email, password):

        self.user_id = user_id
        self.email = email
        self.password = password


class Privacy(base):

    __tablename__ = 'privacy'

    user_id = Column(Integer, primary_key=True)
    privacy = Column(Boolean)
    GDPR_necessary = Column(Boolean)
    GDPR_marketing = Column(Boolean)

    def __init__(self, user_id, privacy, GDPR_necessary, GDPR_marketing):
        self.user_id = user_id
        self.privacy = privacy
        self.GDPR_necessary = GDPR_necessary
        self.GDPR_marketing = GDPR_marketing

class PersonalData(base):

    __tablename__ = 'personalData'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    mobile = Column(Integer)

    def __init__(self, user_id, first_name, last_name, address, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile = mobile


class CrimeRecords(base):

    __tablename__ = 'crimeRecords'

    name_of_suspect = Column(String, primary_key=True)
    num_of_repeated_crimes = Column(Integer)
    type_of_crime = Column(String)
    address_of_suspect = Column(String)

    def __init__(self, num_of_repeated_crimes, type_of_crime, name_of_suspect, address_of_suspect):

        self.num_of_repeated_crimes = num_of_repeated_crimes
        self.type_of_crime = type_of_crime
        self.name_of_suspect = name_of_suspect
        self.address_of_suspect = address_of_suspect


# creating DB and table that resembles the class just created, only if not created yet
base.metadata.create_all(engine)
