from sqlalchemy.orm import sessionmaker

from src.internet_forensics.encryption.encrypt import Encrypt

from ..logging.custom_logger import generate_custom_logger
from .db import engine, Users as users

custom_logger = generate_custom_logger(name="DB queries")

# creating session to talk to db
Session = sessionmaker(bind=engine)
session = Session()


class Queries:

    def login(self, email: str, password: str) -> int:
        """
        this method checks if the users exists, compares password with encrypted one and returns the id
        """
        for instance in session.query(users).filter(users.email == email):
            if Encrypt().check_password(password, instance.password):
                return instance.user_id

    def personal_data(self, user_id: int) -> object:
        """
        this method looks for a record corresponding to the user id and returns all their information
        """
        for instance in session.query(users).filter(users.user_id == user_id):
            return instance

    def password_reset(self, user_id: int, old_password, new_password):
        """
        this method checks for the old password and if correct replaces it with new password after hashing it
        Args:
            user_id: int
            old_password: string
            new_password: string

        Returns:

        """
        new_hashed_password = Encrypt().hash_password(new_password)
        for instance in session.query(users).filter(users.user_id == user_id):
            if Encrypt.check_password(old_password, instance.password):
                instance.password = new_hashed_password

    def signup(self, first_name: str, last_name: str, address: str, email: str, mobile: int,
               password: str, privacy: bool, gdpr_necessary: bool, gdpr_marketing: bool) -> int:
        """
        This method lets a user signup inserting all their information and returns the id to the program
        """

        if not Queries().if_exists(email):

            pssw = Encrypt().hash_password(password)

            user = users(first_name, last_name, address, email, mobile,
                         pssw, privacy, gdpr_necessary, gdpr_marketing)

            try:
                session.add(user)
                session.commit()
            except Exception as ex:
                custom_logger.info(ex)

            return user.user_id
        else:
            raise ValueError("Email already exists")
            return 0

    def privacy(self, user_id: int, bool_p: bool) -> bool:
        """
        This method sets the preference for user privacy True = yes, False = no to privacy conditions
        """
        for instance in session.query(users).filter(users.user_id == user_id):
            instance.privacy = bool_p
            session.commit()
            return instance.privacy

    def GDPR(self, user_id: int, bool_nec: bool, bool_mark: bool) -> bool:
        """
        This method sets the preference for user GDPRs True = yes, False = no to GDPR privacy conditions,
        nec stands for necessary and mark for marketing
        """
        for instance in session.query(users).filter(users.user_id == user_id):
            instance.gdpr_necessary = bool_nec
            instance.gdpr_marketing = bool_mark
            session.commit()
            return instance.gdpr_necessary, instance.gdpr_marketing

    def if_exists(self, value: str) -> bool:
        """
        This method lets a user signup inserting all their information and returns the id to the program
        """

        if session.query(users).filter(users.email == value).first():
            return True
        else:
            return False
