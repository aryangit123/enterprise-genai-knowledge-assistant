import logging
import logging.config
from config import LOG_LEVEL

# Configure logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": LOG_LEVEL,
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": LOG_LEVEL,
            "formatter": "detailed",
            "filename": "logs/app.log",
            "encoding": "utf-8"
        }
    },
    "root": {
        "level": LOG_LEVEL,
        "handlers": ["console", "file"]
    }
}

# Create logs directory if it doesn't exist
import os
os.makedirs("logs", exist_ok=True)

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

def get_logger(name):
    """Get a logger instance for a module."""
    return logging.getLogger(name)
