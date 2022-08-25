from src.internet_forensics.database.query import Queries
from src.internet_forensics.logging.custom_logger import generate_custom_logger
from constants import *

_log = generate_custom_logger(name=PACKAGE_NAME)
query = Queries()


class UserManager:
    """
    For managing users
    """

    def __init__(self, email="", password="", firstname="", lastname="", address="", mobile="", privacy="",
                 gdpr_necessary="", gdpr_marketing=""):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.privacy = privacy
        self.gdpr_necessary = gdpr_necessary
        self.gdpr_marketing = gdpr_marketing

    def user_login(self) -> int:
        """
        Returns: None if the provided credentials are wrong and a UserID if credentials were found
        """
        try:
            _log.info("Login process started")

            user_id = query.login(email=self.email, password=self.password)

            _log.info("Login process completed")

            return user_id
        except Exception as e:
            _log.warning(e)
            return 0

    def user_password_reset(self) -> bool:
        """
        Returns: a boolean for whether the reset process was successful or not
        """
        try:
            _log.info("Password reset process started")
            return True
        except Exception as e:
            _log.warning(e)
            return False

    def user_creation(self) -> int:
        """
        Returns: UserID if user creation was successful else 0
        """
        try:
            _log.info("User creation process started")
            user_id = query.signup(first_name=self.firstname, last_name=self.lastname, address=self.address,
                                   email=self.email, mobile=self.mobile, password=self.password, privacy=self.privacy,
                                   gdpr_marketing=self.gdpr_marketing, gdpr_necessary=self.gdpr_necessary)

            _log.info("user creation process completed")

            return user_id
        except Exception as e:
            _log.warning(e)
            return None


try:
    u = UserManager(firstname="human", lastname="being", address="earth", email="Tony.bond@gmail.com",
                    mobile="123456789", password="secret", privacy=True, gdpr_marketing=True, gdpr_necessary=True)

    result = u.user_creation()
    print(result)
except Exception as e:
    print("Eror: " + str(e))