"""
logger = Logger()

logger.log_info("This is an informational message.")
logger.log_warning("This is a warning message.")
logger.log_error("This is an error message.")
try:
    ... code that might raise an exception ...
    raise ValueError("An example exception.")
except ValueError as e:
    logger.log_exception("An exception occurred: {}".format(e))
"""
import atexit
import logging
import os


class Logger:

    def __init__(self, file_name="application_log.log"):
        self._configure_logging(file_name)
        atexit.register(self.close_log)

        def __init__(self, name=__name__,
                     log_file='my_log.log', log_level=logging.INFO):


    def _secure_path(self, file):
        project_folder = "Szakdolgozat_gwjz4t"
        project_dir = os.getcwd().rsplit(project_folder, 1)[0] + project_folder
        log_dir = os.path.join(project_dir, 'log')
        path = os.path.join(log_dir, file)

        if not os.path.exists(path):
            with open(path, 'w'):
                pass

        return path

    def _configure_logging(self, file) -> None:
        """
        Date-time, formatting, and basic configuraiton for logging.
        :return: None
        """
        logging.basicConfig(
            filename=self._secure_path(file),
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    # def _configure_log_file(self, file):
    #     cwd = os.getcwd()
    #
    #     log_directory = os.path.join(root_dir, 'log')
    #     path = os.path.join(log_directory, file)
    #
    #     if not os.path.exists(path):
    #         with open(path, 'w'):
    #             pass
    #
    #     return path



    # _instance = None
    #
    # def __init__(self, log_file="application_log.log"):
    #     self.log_file = log_file
    #     self._configure_logging()
    #     atexit.register(self.close_log)
    #
    # # def __new__(cls, log_file="application_log.log"):
    # #     if cls._instance:
    # #         cls._instance.close_log()
    # #
    # #     cls._instance = super(Logger, cls).__new__(cls)
    # #     cls._instance.log_file = cls._configure_log_file()
    # #     cls._instance._configure_logging()
    # #     return cls._instance
    #
    # @classmethod
    # def _configure_log_file(self):
    #     root_dir = os.path.dirname(os.path.abspath(__file__))
    #     log_directory = os.path.join(root_dir, 'log')
    #     return os.path.join(log_directory, self._instance.log_file)
    #
    # def _configure_logging(self) -> None:
    #     """
    #     Date-time, formatting, and basic configuration for logging.
    #     :return: None
    #     """
    #     logging.basicConfig(
    #         filename=self.log_file,
    #         level=logging.INFO,
    #         format='%(asctime)s [%(levelname)s] - %(message)s',
    #         datefmt='%Y-%m-%d %H:%M:%S'
    #     )
    #     # atexit.register(self._instance.close_log)






    def info(self, message) -> None:
        """
        :param message: Logs arg message.
        :return: None
        """
        logging.info(message)

    def warning(self, message) -> None:
        """
        :param message: Logs arg warning.
        :return: None
        """
        logging.warning(message)

    def error(self, message) -> None:
        """
        :param message: Logs arg error.
        :return: None
        """
        logging.error(message)

    def exception(self, message) -> None:
        """
        :param message: Logs arg exception.
        :return: None
        """
        logging.exception(message)

    def close_log(self) -> None:
        """
        Explicitly close the log file handler.
        :return: None
        """
        if logging.root.handlers:
            logging.shutdown()



# import logging
#
# class ProfessionalLogger:
#     def __init__(self, name=__name__, log_file='my_log.log', log_level=logging.INFO):
#         self.logger = logging.getLogger(name)
#         self.logger.setLevel(log_level)
#
#         self._setup_file_handler(log_file, log_level)
#         self._setup_console_handler(log_level)
#
#     def _setup_file_handler(self, log_file, log_level):
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler = logging.FileHandler(log_file)
#         file_handler.setLevel(log_level)
#         file_handler.setFormatter(formatter)
#         self.logger.addHandler(file_handler)
#
#     def _setup_console_handler(self, log_level):
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(log_level)
#         console_handler.setFormatter(formatter)
#         self.logger.addHandler(console_handler)
#
#     def log(self, level, message):
#         log_function = getattr(self.logger, level, None)
#         if log_function:
#             log_function(message)
#         else:
#             self.logger.info(f"Invalid log level '{level}'. Logging as info. {message}")
#
# # Example usage
# if __name__ == "__main__":
#     logger = ProfessionalLogger(name='MyAppLogger', log_file='my_app.log', log_level=logging.DEBUG)
#
#     logger.log('info', "This is an informational message.")
#     logger.log('warning', "This is a warning message.")
#     logger.log('error', "This is an error message.")
