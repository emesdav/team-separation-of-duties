from src.internet_forensics.logging.custom_logger import generate_custom_logger
from src.internet_forensics.database.query import Queries
from constants import *

_log = generate_custom_logger(name=PACKAGE_NAME)


class UserManager:
    """
    For managing users
    """

    def __init__(self, username, password="", firstname="", lastname="", address="", email=""):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email

    def user_login(self) -> int:
        """
        Returns: None if the provided credentials are wrong and a UserID if credentials were found
        """
        try:
            _log.info("Login process started")
            query = Queries()
            result = query.login(username=self.username, password=self.password)
            _log.info("Login process completed with: " + result)

            return result
        except Exception as e:
            _log.warning(e)
            return None

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
            return self.user_id
        except Exception as e:
            _log.warning(e)
            return None


