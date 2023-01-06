import logging
import logging.config

logger = logging.getLogger(__name__)

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default_formatter': {
            'format': '✨%(levelname)s - %(asctime)s // %(message)s✨'
        } ,
        'default_file_formatter': {
            'format': '[%(levelname)s - %(asctime)s // %(message)s]'
        }
    },

    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'default_file_formatter',
            'filename': 'todoitapi.log',
        },
    },

    'loggers': {
        'demoapi': {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)