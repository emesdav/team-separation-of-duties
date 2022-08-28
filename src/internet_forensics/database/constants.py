import os

DB_FILE_NAME = 'local.db'
SQLITE_PATH_PREFIX = 'sqlite:///'

ROOT_DIRECTORY = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'internet_forensics/datastore')

SQLITE_PATH = SQLITE_PATH_PREFIX + os.path.join(ROOT_DIRECTORY, DB_FILE_NAME)
