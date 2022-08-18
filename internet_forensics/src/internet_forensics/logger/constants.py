"""
The purpose of this file is to maintain constants used for logger.
"""

DATE_TIME_FMT = '%Y-%m-%d %H:%M:%S'

# The format of each log message includes the timestamp, the logger's name or purpose, the filename,
# the line number at which the log occurs, the logger level (e.g., debug/info/warning/error/critical), and
# the log message.
FORMAT_OF_LOG_MSG = '[%(asctime)s %(name)s] (%(filename)s %(lineno)d): %(levelname)s %(message)s'

LOG_FILE_NAME_W_EXT = 'custom_logs.log'
