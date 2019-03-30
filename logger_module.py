import os
import inspect
import logging
import logging.handlers


class Logger():
    def __init__(self, name=None, level='info', write_file=True, file_name=None, format=None):
        self._name = name
        self._level = level
        self._write_file = write_file

        if file_name is None:
            self._file_name = "log.log"
        else:
            self._file_name = file_name

        if format is None:
            # self._format = '%(asctime)s %(levelname)-{length}s : %(message)s'.format(length=len(self._level))
            self._format = self._get_default_format()
        else:
            self._format = format

        self._set_logger()

    def _get_default_format(self):
        color_map = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
        }

        level_color_map = {
            'info': color_map['blue'],
            'error': color_map['red'],
            'debug': color_map['green'],
            'warning': color_map['yellow'],
        }

        color = level_color_map[self._level]
        end_char = '\033[0m'
        default_format = '%(asctime)s {start}%(levelname)-{length}s {end}: %(message)s'.format(start=color,
                                                                                               length=len(self._level),
                                                                                               end=end_char)

        return default_format

    def _set_logger(self):
        if self._name is None:
            # Get global logger
            self._logger = logging.getLogger(__name__)
        else:
            # Get unique logger by each class instance
            self._logger = logging.getLogger("{0}.{1}".format(self.__class__.__qualname__, 
                                                              self._name))

        self._set_logger_level()

        formatter = logging.Formatter(self._format)
        self._add_stream_handler(formatter)
        if self._write_file:
            self._add_file_handler(formatter)

    def _set_logger_level(self):
        level_map = {
            'info': logging.INFO,
            'error': logging.ERROR,
            'debug': logging.DEBUG,
            'warning': logging.WARNING,
        }
        level = level_map[self._level]

        self._logger.setLevel(level)

    def _add_stream_handler(self, formatter):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

    def _get_file_handler_config(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        log_dir = dir_path + "/../logs/"
        os.makedirs(log_dir, exist_ok=True)
        file_path = log_dir + self._file_name

        max_byte = 1024 * 1024 * 100  # 100MB

        return file_path, max_byte

    def _add_file_handler(self, formatter):
        file_path, max_byte = self._get_file_handler_config()

        file_handler = logging.handlers.RotatingFileHandler(file_path,
                                                            maxBytes=max_byte,
                                                            backupCount=3)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

    def infolog(self, cls, msg):
        """
        example usage:
            mylogger.infolog(__file__, message)
        """
        message = "[{file_name}:{func}:{line}] {msg}"
        file_name = inspect.stack()[1][1]
        line_num = inspect.stack()[1][2]
        func_name = inspect.stack()[1][3]

        message = message.format(file_name=file_name.split('/')[-1],
                                 func=func_name,
                                 line=line_num,
                                 msg=msg)
        self._logger.info(message)

    def debuglog(self, cls, msg):
        message = "[{file_name}:{func}:{line}] {msg}"
        file_name = inspect.stack()[1][1]
        line_num = inspect.stack()[1][2]
        func_name = inspect.stack()[1][3]

        message = message.format(file_name=file_name.split('/')[-1],
                                 func=func_name,
                                 line=line_num,
                                 msg=msg)
        self._logger.debug(message)

    def errorlog(self, cls, msg):
        message = "[{file_name}:{func}:{line}] {msg}"
        file_name = inspect.stack()[1][1]
        line_num = inspect.stack()[1][2]
        func_name = inspect.stack()[1][3]

        message = message.format(file_name=file_name.split('/')[-1],
                                 func=func_name,
                                 line=line_num,
                                 msg=msg)
        self._logger.error(message)

    def warninglog(self, cls, msg):
        message = "[{file_name}:{func}:{line}] {msg}"
        file_name = inspect.stack()[1][1]
        line_num = inspect.stack()[1][2]
        func_name = inspect.stack()[1][3]

        message = message.format(file_name=file_name.split('/')[-1],
                                 func=func_name,
                                 line=line_num,
                                 msg=msg)
        self._logger.warning(message)
