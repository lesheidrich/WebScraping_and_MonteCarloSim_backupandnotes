import unittest
from test.test_logger import TestLogger


class TestRegression(unittest.TestCase):
    def run_test_logger(self):
        logger = TestLogger()
        logger.run()

