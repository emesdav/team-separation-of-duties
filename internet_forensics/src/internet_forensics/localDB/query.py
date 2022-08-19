import db
from sqlalchemy import sessionmaker
from ..encryption.encrypt import Encrypt

# creatring session to talk to db
Session = sessionmaker(bind=db.engine)
session = Session()


class Queries():

    def login(username: str, password: str) -> int:
        """
        this method checks if the users exists, compares password with encrypted one and returns the id
        """
        for instance in session.query(db.users).filter(db.users.email == username):
            if Encrypt.check_pssw(password, instance.password):
                return instance.user_id

    def personal_data(user_id: int) -> object:
        """
        this method looks for a record corresponding to the user id and returns all his informations
        """
        for instance in session.query(db.users).filter(db.users.user_id == user_id):
            return instance
