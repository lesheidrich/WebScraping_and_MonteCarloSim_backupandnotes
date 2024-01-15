# # import re
# # import requests
# # import csv
# # import multiprocessing
# #
# #
# # def handler(proxy_address):
# #     link = "http://icanhazip.com/"
# #
# #     l = []
# #
# #     proxies = {
# #         'http': f"http://{proxy_address}",
# #         'https': f"https://{proxy_address}"
# #     }
# #
# #     try:
# #         #add proxy to sauce
# #         response = requests.get(link, proxies=proxies, timeout=1).text
# #         if 22 > len(response) > 0:
# #             print(f"IP: {proxy_address}\nResponse: {response}")
# #             l.append(proxy_address)
# #     except:
# #         pass
# #
# #     return l
# #
# #
# # if __name__ == '__main__':
# #     #make proxy list from csv
# #     proxies = []
# #     with open("./proxy.csv", "r") as proxy_table:
# #         content = csv.reader(proxy_table)
# #         next(content)  # skip header row
# #
# #         for row in content:
# #             proxy_add = f"{row[0]}:{row[1]}"
# #             proxies.append(proxy_add)
# #
# #     #run handler to read proxies with multiprocessing
# #     multiprocessing.freeze_support()
# #     with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
# #         process.map(handler, proxies)
#
#
# import requests
# import csv
# import multiprocessing
#
#
# def handler(proxy_address):
#     link = "http://icanhazip.com/"
#
#     l = []
#
#     proxies = {
#         'http': f"http://{proxy_address}",
#         'https': f"https://{proxy_address}"
#     }
#
#     try:
#         response = requests.get(link, proxies=proxies, timeout=1).text
#         if 22 > len(response) > 0:
#             print(f"IP: {proxy_address}\nResponse: {response}")
#             l.append(proxy_address)
#     except:
#         pass
#
#     return l
#
#
# if __name__ == '__main__':
#     #make proxy list from csv
#     proxies = []
#     with open("./proxy.csv", "r") as proxy_table:
#         content = csv.reader(proxy_table)
#         next(content)  # skip header row
#
#         for row in content:
#             proxy_add = f"{row[0]}:{row[1]}"
#             proxies.append(proxy_add)
#
#     #run handler to read proxies with multiprocessing
#     multiprocessing.freeze_support()
#     with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
#         process.map(handler, proxies)

import requests
import csv
import multiprocessing


class ProxyHandler:
    def __init__(self, proxies_file: str = "./proxy.csv"):
        self.proof_link = "http://icanhazip.com/"
        self.proxies = self.load_proxies(proxies_file)

    def load_proxies(self, proxies_csv: str) -> [str]:
        with open(proxies_csv, "r") as file:
            return [f"{row[0]}:{row[1]}" for row in csv.reader(file)][1:]

    def handle_proxy(self, proxy_address: str) -> str:
        proxies = {
            'http': f"http://{proxy_address}",
            'https': f"https://{proxy_address}"
        }

        try:
            res = requests.get(self.proof_link, proxies=proxies, timeout=1)
            response = res.text

            if res.status_code == 200 and 0 < len(response) < 22:
                print(f"Proxy check succeeded\nIP: {proxy_address}\nStatus Code: {res.status_code}\nResponse: {response}")
                return proxy_address

        except requests.RequestException as e:
            # print(f"Proxy check failed for {proxy_address}: {e}")
            pass

    def process_proxies(self) -> [str]:
        with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
            return list(filter(None, process.map(self.handle_proxy, self.proxies)))


if __name__ == '__main__':
    try:
        ph = ProxyHandler()
        valid_proxies = ph.process_proxies()

        print(f"Valid proxies: {valid_proxies}")
    except Exception as e:
        print(f"An error occurred: {e}")
