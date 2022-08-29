"""
The purpose of this file is to maintain constants used throughout the
application.
"""
import os

CRIME_RECORDS_TABLE_NAME = 'CrimeRecords'

ENV_FILE_NAME = 'environment.yml'

# State for returning a result with multi-threading
STATE_FOR_THREAD = 'FINISHED'

ROOT_DIRECTORY = os.path.normpath(os.getcwd() + os.sep + os.pardir)

LOG_PATH_AND_FILE = f"{ROOT_DIRECTORY}/internet_forensics/app_log/custom_logs.log"

SQLITE_PATH_AND_FILE = f"sqlite:///{ROOT_DIRECTORY}/internet_forensics/datastore/local.db"


TOP_HEADER = \
    "##################################################################\n" \
    "#                       Dutch Police Portal                      #\n" \
    "##################################################################"

MAIN_MENU_OPTION_LIST = \
    "# SELECT MENU: [1]Login [2]New Account [3]Reset Password [4]Exit #"

END_OF_MENU = \
    "##################################################################"

SELECT_MENU_OPTION = \
    "\n\nWhat do you want to do?"

WRONG_MENU_OPTION_INPUT = \
    "\n" \
    "unexpected error. Please ensure you enter the right number value"

APPLICATION_EXIT_MESSAGE = \
    "\n" \
    "The application will now exit"

BOTTOM_HEADER = \
    "\n" \
    "##################################################################\n" \
    "#            Copyright 2022, All Rights Reserved                 #\n" \
    "##################################################################"

DASHBOARD_MENU_OPTION_LIST = \
    "# SELECT MENU: [1]Profile [2]Privacy [3]Notifications [4]Logout  #"


LOGIN_VALIDATION_FAILED = "We are unable to verify your Username or password. Please try again"
LOGIN_ATTEMPT_COUNT_REMAINING = "%(attempts_count)s out of %(allowed_attempts)s login attempts " \
                                "remaining "

# Prompt instructions
PROMPT_USERNAME = "Enter Your email"
PROMPT_PASSWORD = "Enter your password"
PROMPT_FIRSTNAME = "Enter your First name"
PROMPT_LASTNAME = "Enter your Last Name"
PROMPT_ADDRESS = "Enter your Address"
PROMPT_EMAIL = "Enter your Email"
PROMPT_MOBILE = "Enter your Mobile Number"
PROMPT_PRIVACY = "You must accept our privacy policies to continue"
PROMPT_GDPR_MARKETING = "Can we use your information to tailor marketing options for you?"
PROMPT_GDPR_NECESSARY = "You must accept mandatory information processing"
