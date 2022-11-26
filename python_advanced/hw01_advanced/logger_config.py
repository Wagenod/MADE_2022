import os

LOG_CONFIG = {
    'version': 1, # required
    'formatters': {
        'simple_formatter': {
            'format': '%(asctime)s\t%(levelname)s\t%(name)s\t%(module)s\t%(message)s',
            'datefmt': '%d.%m.%Y %H:%M:%S'
        },
        'stdout_formatter': {
            'format': '{asctime}\t|\t{levelname}\t|\t{name}\t|\t{message}',
            'datefmt': '%d.%m.%Y %H:%M:%S',
            'style': '{'
        }
    },
    'handlers': {
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler', # required
            'formatter': 'simple_formatter',
            'filename': os.path.join(os.path.dirname(__file__), 'lru_cache.log')
        },
        'stdout_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', # required
            'formatter': 'stdout_formatter'
        }
    },
    'loggers': {
        'main': {
            'level': 'DEBUG',
            'handlers': ['stdout_handler', 'file_handler']
        }
    }
}