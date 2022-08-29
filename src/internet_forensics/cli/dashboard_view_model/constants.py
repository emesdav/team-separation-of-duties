"""
The purpose of this file is to maintain constants used for Main inputs.
"""
import time

t = time.localtime()
_current_time = time.strftime("%H:%M:%S", t)

DASHBOARD_MENU_OPTION_LIST = \
    f"# Current Time: {_current_time}                                        \n"\
    "# SELECT MENU: [1]Profile [2]Privacy [3]File a Report [4]Logout  #"\


DASHBOARD_PROFILE = \
    "\n" \
    "##################################################################\n" \
    "# First Name       : %(first_name)s \n" \
    "# Last Name        : %(last_name)s \n" \
    "# Email            : %(email)s \n" \
    "# Physical Address : %(physical_address)s \n" \
    "# Phone Number     : %(phone_number)s1 \n" \
    "##################################################################"

DASHBOARD_PRIVACY = \
    "\n" \
    "##################################################################\n" \
    "# Privacy Policy     : %(privacy)s \n" \
    "# Strictly Necessary : %(GDPR_necessary)s \n" \
    "# Marketing          : %(GDPR_marketing)s \n" \
    "##################################################################"

DASHBOARD_NOTIFICATIONS = \
    "\n" \
    "##################################################################\n" \
    "# There is no news item to display at the moment                 #" \
    "##################################################################"

#    "#  : %() \n" \
