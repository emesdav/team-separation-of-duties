"""
The purpose of this file is to maintain constants used throughout the application.
"""

ENV_FILE_NAME = 'environment.yml'

# State for returning a result with multi-threading
STATE_FOR_THREAD = 'FINISHED'

TOP_HEADER = \
    "##################################################################\n" \
    "#                       Dutch Police Portal                      #\n" \
    "##################################################################"

MAIN_MENU_OPTION_LIST = \
    "\n" \
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

DASHBOARD_PROFILE = \
    "\n" \
    "##################################################################\n" \
    "# First Name       : %(first_name) \n" \
    "# Last Name        : %(last_name) \n" \
    "# Email            : %(email) \n" \
    "# Physical Address : %(physical_address) \n" \
    "# Phone Number     : %(phone_number) \n" \
    "##################################################################"

DASHBOARD_PRIVACY = \
    "\n" \
    "##################################################################\n" \
    "# Strictly Necessary : %(first_name) \n" \
    "# Marketing          : %(last_name) \n" \
    "##################################################################"

DASHBOARD_NOTIFICATIONS = \
    "\n" \
    "##################################################################\n" \
    "# There is no news item to display at the moment                 #" \
    "##################################################################"

#    "#  : %() \n" \

LOGIN_VALIDATION_FAILED = "We are unable to verify your Username or password. Please try again"
LOGIN_ATTEMPT_COUNT_REMAINING = "%(attempts_count)s out of %(allowed_attempts)s login attempts " \
                                "remaining "

# Prompt instructions
PROMPT_USERNAME = "Please enter Your email"
PROMPT_PASSWORD = "Please enter your password"