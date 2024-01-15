import datetime
import unittest
import os
from unittest.mock import patch
from log.logger import Logger


class TestLogger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = "../log/application_test_log.log"

    def setUp(self):
        self.logger = Logger(log_file=self.file_path)

    def tearDown(self):
        """
        Truncates log file and closes log.
        :return: None
        """
        with open(self.file_path, "a") as file:
            file.truncate(0)
        self.logger.close_log()

    def test_log_file_creation(self):
        """
        Ensures existence of test log file.
        :return: None
        """
        self.assertTrue(os.path.exists(self.file_path))

    def test_logging_methods(self):
        """
        Ensures info, warning and error logging through content and timestamp check.
        :return: None
        """
        self.logger.info("This is an informational message.")
        self.logger.warning("This is a warning message.")
        self.logger.error("This is an error message.")

        log_messages = [
            "This is an informational message.",
            "This is a warning message.",
            "This is an error message."
        ]
        current_datetime = datetime.datetime.now()
        current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M")

        with open(self.file_path, "r") as file:
            content = file.read()
            for message in log_messages:
                self.assertIn(message, content)
                self.assertIn(current_datetime_str, content)

    def test_info_bool(self):
        """
        Test boolean input for log. Ensure info function logs properly.
        :return: None
        """
        self.logger.info(True)
        with open(self.file_path, 'r') as log_file:
            content = log_file.read()
        self.assertIn("True", content)
        self.assertIn("[INFO]", content)

    def test_warning_string(self):
        """
        Tests logging for string input. Ensures warning logs properly.
        :return: None
        """
        self.logger.warning("Test string message.")
        with open(self.file_path, 'r') as log_file:
            content = log_file.read()
        self.assertIn("Test string message.", content)
        self.assertIn("[WARNING]", content)

    def test_error_int(self):
        """
        Tests int logging. Ensures error logs properly.
        :return: None
        """
        self.logger.error(42)
        with open(self.file_path, 'r') as log_file:
            content = log_file.read()
        self.assertIn("42", content)
        self.assertIn("[ERROR]", content)

    def test_exception_logging(self):
        """
        Ensures exception log handling.
        :return: None
        """
        with self.assertRaises(ValueError):
            with patch.object(self.logger, 'exception') as mock_exception:
                mock_exception.side_effect = ValueError("Mock value error exception")
                self.logger.exception("An exception occurred.")
