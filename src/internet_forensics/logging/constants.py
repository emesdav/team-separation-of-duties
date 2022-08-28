"""
The purpose of this file is to maintain constants used for logging.
"""
import os

DATE_TIME_FMT = '%Y-%m-%d %H:%M:%S'

EMPTY_STRING = ''

LOG_FILE_NAME_W_EXT = 'custom_logs.log'

FOLDER_NAME_LOG_FILE = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'app_log')

# The format of each log message includes the timestamp, the
# logger's name or purpose, the filename,
# the line number at which the log occurs, the logging level
# (e.g., debug/info/warning/error/critical), and
# the log message.
FORMAT_OF_LOG_MSG = \
    '[%(asctime)s %(name)s] (%(filename)s %(lineno)d): ' \
    '%(levelname)s %(message)s'


