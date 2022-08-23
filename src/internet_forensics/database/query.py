
from db import Users as users, engine, Privacy, PersonalData as pers
from sqlalchemy.orm import sessionmaker
from src.internet_forensics.encryption.encrypt import Encrypt
from ..logging.custom_logger import generate_custom_logger
import uuid

custom_logger = generate_custom_logger(name="DB queries")

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
        for instance in session.query(users).filter(users.user_id == user_id).first():
            if Encrypt.check_password(old_password, instance.password):
                instance.password = new_hashed_password


    def signup(self, first_name: str, last_name: str, address: str, email: str, mobile: int,
               password: str, privacy: bool, GDPR_necessary: bool, GDPR_marketing: bool) -> int:
        """
        This method lets a user signup inserting all their information and returns the id to the program
        """

        user_id = str(uuid.uuid4())
        pssw = Encrypt().hash_password(password)

        # user table record
        user = users(user_id, email, pssw)
        # privacy table record
        privacy_rec = Privacy(user_id, privacy, GDPR_necessary, GDPR_marketing)
        # creating personal data table record
        pdata = pers(user_id, first_name, last_name, address, mobile)

        try:
            session.add(user)
            session.add(privacy_rec)
            session.add(pdata)
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



