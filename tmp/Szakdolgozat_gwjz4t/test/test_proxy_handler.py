import os
import unittest
from unittest.mock import patch, MagicMock
from proxy.proxy_handler import ProxyHandler

class TestProxyHandler(unittest.TestCase):
    def setUp(self):
        self.mocked_proxies_csv = "mocked_proxy_list.csv"
        self.mocked_proxy = "proxy1:8080"
        self.mocked_working_proxies = [self.mocked_proxy]

    # @patch("proxy.proxy_handler.requests.get")
    # def test_handle_proxy_success(self, mock_get):
    #     # Set up the mock to simulate a successful response
    #     mock_response = MagicMock()
    #     mock_response.status_code = 200
    #     mock_response.text = "127.0.0.1"
    #     mock_get.return_value = mock_response
    #
    #     # Create an instance of ProxyHandler with mocked data
    #     proxy_handler = ProxyHandler(proxies_file=self.mocked_proxies_csv)
    #
    #     # Call the handle_proxy method with a mocked proxy
    #     result = proxy_handler.handle_proxy(self.mocked_proxy)
    #
    #     # Print the log directory for debugging
    #     log_directory = os.path.dirname(proxy_handler.log.log_file)
    #     print(f"Log Directory from ProxyHandler: {log_directory}")
    #
    #     # Assert that the result is the expected proxy
    #     self.assertEqual(result, self.mocked_proxy)

if __name__ == "__main__":
    unittest.main()
