import logging
import sys

class Logger:
    COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'RESET': '\033[0m'      # Reset
    }

    _instance = None

    def __new__(cls, name='AppLogger', level=logging.DEBUG):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._init_logger(name, level)
        return cls._instance

    def _init_logger(self, name, level):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(self.CustomFormatter())
        self.logger.addHandler(handler)

    class CustomFormatter(logging.Formatter):
        def format(self, record):
            log_color = Logger.COLORS.get(record.levelname, Logger.COLORS['RESET'])
            reset_color = Logger.COLORS['RESET']
            return f"{log_color}{record.levelname}: {record.getMessage()}{reset_color}"

    def d(self, message):
        self.logger.debug(message)

    def i(self, message):
        self.logger.info(message)

    def w(self, message):
        self.logger.warning(message)

    def e(self, message):
        self.logger.error(message)

# Crée une instance globale
log = Logger()
