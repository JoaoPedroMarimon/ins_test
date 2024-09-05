import sys
import logging
from logging import config


def init_logging(file_level: int, log_directory: str, stream_handler=False, debug=False):
    log_config = {
        "version": 1,
        "root": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        },
        "handlers": {
            "console": {
                "formatter": "std_out1",
                "class": "logging.StreamHandler",
                "level": "ERROR" if not debug else "DEBUG"
            },
            "file": {
                "formatter": "std_out1",
                "class": "logging.FileHandler",
                "level": file_level,
                "filename": f'{log_directory}/.logfile.log'
            }
        },
        "formatters": {
            "std_out1": {
                "format": '%(asctime)s - %(levelname)s - %(message)s',
                "datefmt": "%d/%m/%y %H:%M:%S %p"
            }
        },
    }
    if not stream_handler:
        log_config['handlers'].pop('console')
        log_config['root']['handlers'].remove('console')

    config.dictConfig(log_config)
    sys.excepthook = handle_uncaught_exception


def handle_uncaught_exception(errtype, value, traceback):
    """ Handle all uncaught exceptions """
    logger = logging.getLogger('')
    logger.error('Uncaught exception occurred', exc_info=(errtype, value, traceback))


def handle_exception(exit_code=0):
    """ Use: @land.logger.handle_exception(0)
        before every function which could cast an exception """

    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                logging.exception(error)
                if exit_code != 0:  # if zero, don't exit from the program
                    sys.exit(exit_code)  # exit from the program

        return inner

    return wrapper