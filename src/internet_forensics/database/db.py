from sqlalchemy import Boolean, Column, Integer, String, create_engine
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
    user_id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    email = Column(String, unique=True)
    mobile = Column(Integer)
    password = Column(String)
    privacy = Column(Boolean)
    gdpr_necessary = Column(Boolean)
    gdpr_marketing = Column(Boolean)

    def __init__(self, first_name, last_name, address, email, mobile,
                 password, privacy, gdpr_necessary, gdpr_marketing):

        #self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.mobile = mobile
        self.password = password
        self.privacy = privacy
        self.gdpr_necessary = gdpr_necessary
        self.gdpr_marketing = gdpr_marketing


class CrimeRecords(base):

    __tablename__ = 'CrimeRecords'

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
