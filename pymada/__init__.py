import sys, logging, pathlib
from . import settings

log_level = "DEBUG" if settings.debug_mode else "INFO"
log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "CRITICAL": logging.CRITICAL,
}

logger = logging.getLogger(__name__)  # use __name__ to avoid naming conflicts
logger.setLevel(log_levels[log_level])

if settings.logging_stream_type == "file":
    open(settings.logging_file_path, "w").close()  # clear the log file
    logging_handler = logging.FileHandler(filename=settings.logging_file_path)
elif settings.logging_stream_type == "terminal":
    logging_handler = logging.StreamHandler(stream=sys.stdout)
logging_handler.terminator = "\n"
logging_handler.setLevel(log_levels[log_level])

formatter = logging.Formatter(
    "%(name)s_log %(levelname)s: %(message)s"
)  # default "%(name)s - %(levelname)s - %(message)s - %(asctime)s\n", datefmt="%d-%b-%y %H:%M:%S"
logging_handler.setFormatter(formatter)

logger.addHandler(logging_handler)


def log(message, *args, **kwargs):  # create logging decorator
    def decorator(function):
        def inner(*args, **kwargs):
            logger.info(message)
            return function(*args, **kwargs)

        return inner

    return decorator
