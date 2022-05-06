import logging

from helpers.metaclasses import Singleton


class CustomFormatter(logging.Formatter):
    """
    Custom formatter to add ANSI escape code colors and
    timestamps to wrapping lines to standard out logging
    """

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt, datefmt=None, *args, **kwargs):
        super().__init__(fmt, datefmt, *args, **kwargs)
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset,
        }

    def format(self, record):
        record.msecs = record.msecs * 1000
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatter.default_msec_format = '%s.%03d'
        message = formatter.format(record)
        if record.message != '':
            msg_parts = message.split(record.message)
            message = message.replace('\n', '\n' + msg_parts[0])
        return formatter.format(record)


class CustomLogger(logging.Logger, metaclass=Singleton):
    """
    Custom logger instance to standard out log messages
    """

    def __init__(self, name, level):
        fmt = '%(asctime)s|%(levelname)8s|%(filename)s|%(funcName)s:%(lineno)s| %(msg)s'
        stream_handler = logging.StreamHandler()
        formatter = CustomFormatter(
            fmt=fmt,
            datefmt='%Y-%m-%d %H:%M:%S',
        )
        super().__init__(name=name, level=level)
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)
        self.propagate = False
