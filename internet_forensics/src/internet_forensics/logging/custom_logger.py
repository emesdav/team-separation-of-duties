"""
The purpose of this file is to create a global custom logger to leverage in all files of the application
to build an auditable and detailed trace of all operations performed and/or warnings/errors occurred throughout it.
"""

import os
import sys
import logging

from .constants import (
    DATE_TIME_FMT,
    EMPTY_STRING,
    FOLDER_NAME_LOG_FILE,
    LOG_FILE_NAME_W_EXT,
    FORMAT_OF_LOG_MSG
)


def generate_custom_logger(output_folder: str = FOLDER_NAME_LOG_FILE, name: str = EMPTY_STRING) -> logging.Logger:
    """
    This function creates a custom logger with the required level of logging and formatting.

    Args:
        output_folder: string
                    the output folder to save the log file into.
        name: string
            the name for or purpose of the logger.

    Returns:
        custom_logger: Logger
                  the custom logger.
    """

    # Get current working directory's path and then create output folder to save .log file.
    current_wd_path = os.path.abspath(os.getcwd())
    output_dir_log = os.path.join(current_wd_path, FOLDER_NAME_LOG_FILE)
    os.makedirs(output_dir_log, exist_ok=True)

    # Instantiate initial logger and set logging level as debug.
    custom_logger = logging.getLogger(name)
    custom_logger.setLevel(logging.DEBUG)
    custom_logger.propagate = False

    # Set formatter to be as detailed as per the constant 'FORMAT_OF_LOG_MSG' (see constants.py for further details
    # on this).
    format_log = FORMAT_OF_LOG_MSG

    # Add console handler.
    handler_console = logging.StreamHandler(sys.stdout)
    handler_console.setLevel(logging.DEBUG)
    handler_console.setFormatter(logging.Formatter(fmt=format_log, datefmt=DATE_TIME_FMT))
    custom_logger.addHandler(handler_console)

    # Add file handler.
    handler_file = logging.FileHandler(os.path.join(output_folder, LOG_FILE_NAME_W_EXT))
    handler_file.setLevel(logging.DEBUG)
    handler_file.setFormatter(logging.Formatter(fmt=format_log, datefmt=DATE_TIME_FMT))
    custom_logger.addHandler(handler_file)

    return custom_logger
