import logging.config
import logging
from logging.handlers import RotatingFileHandler

log_file_handler = RotatingFileHandler('api.log', maxBytes=10485760, backupCount=10)
log_file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
log_file_handler.setLevel(logging.INFO)

dict_log_config = {
    'version': 1,
    'handlers': {
        'RotatingFileHandler': {
            'filename': 'api.log',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 50000000,
            'backupCount': 10,
            'formatter': 'api_formatter',
        },
    },
    'loggers': {
        'finline': {
            'handlers': ['RotatingFileHandler'],
            'level': 'INFO'
        },
    },
    'formatters': {
        'api_formatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    }
}

logging.config.dictConfig(dict_log_config)
logger_finline= logging.getLogger('finline')