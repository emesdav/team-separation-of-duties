"""
The purpose of this file is to create a global custom logger
to leverage in all files of the application
to build an auditable and detailed trace of all operations
performed and/or warnings/errors occurred throughout it.
"""

import logging
import os
import sys

import yaml

from src.internet_forensics.constants import ENV_FILE_NAME
from src.internet_forensics.utils import get_project_root

from .constants import (DATE_TIME_FMT, EMPTY_STRING,
                        FORMAT_OF_LOG_MSG)
from src.internet_forensics.constants import ROOT_DIRECTORY, LOG_PATH_AND_FILE

# Get app's root directory
ROOT_DIR = str(get_project_root())
# Get the environment's file's directory
ENV_FILE_DIR = os.path.join(ROOT_DIR, ENV_FILE_NAME)

with open(ENV_FILE_DIR, "r") as stream:
    try:
        yaml_content_read = yaml.safe_load(stream)
        environment = yaml_content_read.get('variables')['ENV']
    except yaml.YAMLError as yaml_except:
        raise yaml_except


def generate_custom_logger(
        env: str = environment,
        output_folder: str = ROOT_DIRECTORY,
        name: str = EMPTY_STRING
):
    """
    This function creates a custom logger with the required
    level of log and formatting.

    Args:
        env: string
            the type of environment used to consume the
            application, e.g., 'dev' (by default in the environment.yml
            file), 'test', 'uat' (user acceptance testing),
            or 'prod' (production).
        output_folder: string
                    the output folder to save the log file into.
        name: string
            the name for or purpose of the logger.

    Returns:
        custom_logger: Logger
                  the custom logger.
    """

    custom_logger = logging.getLogger(name)

    # Instantiate initial logger and set log level based on
    # the type of environment set in the app's config (.yml
    # file).
    if env == 'dev':
        # In a dev environment, showing/recording only logs
        # whose level is debug or above
        # (info, warning, error, and critical)
        logging_level = logging.DEBUG
    elif env == 'test':
        # In a test environment, showing/recording only logs
        # whose level is info or above
        # (warning, error, and critical)
        logging_level = logging.INFO
    elif env == 'uat':
        # In a user acceptance testing (UAT) environment,
        # showing/recording only logs whose level is warning or above
        # (error and critical)
        logging_level = logging.WARNING
    elif env == 'prod':
        # In a production environment, showing/recording only
        # logs whose level is error or above (critical)
        logging_level = logging.ERROR

    custom_logger.setLevel(logging_level)
    custom_logger.propagate = False

    # Set formatter to be as detailed as per the constant
    # 'FORMAT_OF_LOG_MSG' (see constants.py for further details
    # on this).
    format_log = FORMAT_OF_LOG_MSG

    # Add console handler.
    handler_console = logging.StreamHandler(sys.stdout)
    handler_console.setLevel(logging_level)
    handler_console.setFormatter(logging.Formatter(
        fmt=format_log, datefmt=DATE_TIME_FMT))
    custom_logger.addHandler(handler_console)

    # Add file handler.
    handler_file = logging.FileHandler(f"{LOG_PATH_AND_FILE}")
    handler_file.setLevel(logging_level)
    handler_file.setFormatter(logging.Formatter(
        fmt=format_log, datefmt=DATE_TIME_FMT))
    custom_logger.addHandler(handler_file)

    return custom_logger
