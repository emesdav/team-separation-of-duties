
from db import Users as users, engine
from sqlalchemy.orm import sessionmaker
from src.internet_forensics.encryption.encrypt import Encrypt
from ..logging.custom_logger import generate_custom_logger

custom_logger = generate_custom_logger("DB queries")

# creating session to talk to db
Session = sessionmaker(bind=engine)
session = Session()


class Queries:

    def login(self, username: str, password: str) -> int:
        """
        this method checks if the users exists, compares password with encrypted one and returns the id
        """
        for instance in session.query(users).filter(users.email == username).first():
            if Encrypt.check_password(password, instance.password):
                return instance.user_id

    def personal_data(self, user_id: int) -> object:
        """
        this method looks for a record corresponding to the user id and returns all their informations
        """
        for instance in session.query(users).filter(users.user_id == user_id).first():
            return instance

    def signup(self, user_id: int, first_name: str, last_name: str, address: str, email: str, mobile: int,
               password: str, privacy: bool, GDPR_necessary: bool, GDPR_marketing: bool) -> int:
        """
        This method lets a user signup inserting all their information and returns the id to the program
        """


        pssw = Encrypt().hash_password(password)

        user = users(user_id, first_name, last_name, address, email, mobile,
                        pssw, privacy, GDPR_necessary, GDPR_marketing)

        try:
            session.add(user)
            session.commit()
        except Exception as ex:
            custom_logger.info(ex)


        return user.user_id

    def privacy(self, user_id: int, bool_p: bool) -> bool:
        """
        This method sets the preference for user privacy True = yes, False = no to privacy conditions
        """
        for instance in session.query(users).filter(users.user_id == user_id).first():
            instance.privacy = bool_p
            session.commit()
            return instance.privacy

    def GDPR(self, user_id: int, bool_nec: bool, bool_mark: bool) -> bool:
        """
        This method sets the preference for user GDPRs True = yes, False = no to GDPR privacy conditions,
        nec stands for necessary and mark for marketing
        """
        for instance in session.query(users).filter(users.user_id == user_id).first():
            instance.GDPR_necessary = bool_nec
            instance.GDPR_marketing = bool_mark
            session.commit()
            return instance.GDPR_necessary, instance.GDPR_marketing



