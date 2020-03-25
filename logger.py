import logging
from logging.handlers import RotatingFileHandler
import inspect
import sys

def get_logger(filename, level, maxBytes=1048576):
    logger = logging.getLogger("Rotating Log")

    if level == "WARNING":
        level = logging.WARNING
    elif level == "DEBUG":
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger.setLevel(level)

    # add a rotating handler
    handler = RotatingFileHandler(filename, maxBytes=maxBytes,
                                  backupCount=5)
    logger.addHandler(handler)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    return logger

def mydebug(logger, message="function"):
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logger.debug("%s: %s in %s:%i" % (
        message,
        func.co_name,
        func.co_filename,
        func.co_firstlineno
    ))