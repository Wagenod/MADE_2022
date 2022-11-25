LOG_PATH = "lru_cache.log"

LOG_CONFIG = {
    "version": 1, # required
    "formatters": {
        "simple_formatter": {
            "format": "%(asctime)s\t%(levelname)s\t%(name)s\t%(module)s\t%(message)s",
            "datefmt": "%d.%m.%Y %H:%M:%S"
        },
        "stdout_formatter": {
            "format": "{asctime}\t|\t{levelname}\t|\t{name}\t|\t{message}|",
            "datefmt": "%d.%m.%Y %H:%M:%S",
            "style": "{"
        }
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler", # required
            "level": "INFO",
            "formatter": "simple_formatter",
            "filename": LOG_PATH
        },
        "stdout_handler": {
            "class": "logging.StreamHandler", # required
            "level": "DEBUG",
            "formatter": "stdout_formatter"
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["file_handler", "stdout_handler"]
        }
    }
}