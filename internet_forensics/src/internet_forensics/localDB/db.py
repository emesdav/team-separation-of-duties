from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

# this connects to db
engine = create_engine('sqlite:///local.db')

# this is to manage tables
base = declarative_base()


class users (base):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    email = Column(String)
    mobile = Column(Integer)
    password = Column(String)
    privacy = Column(Boolean)
    GDPR_necessary = Column(Boolean)
    GDPR_marketing = Column(Boolean)

    def __init__(self, user_id, first_name, last_name, address, email, mobile,
                 password, privacy, GDPR_necessary, GDPR_marketing):

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.mobile = mobile
        self.password = password
        self.privacy = privacy
        self.GDPR_necessary = GDPR_necessary
        self.GDPR_marketing = GDPR_marketing


# creating DB and table that resembles the class just created, only if not created yet
base.metadata.create_all(engine)
