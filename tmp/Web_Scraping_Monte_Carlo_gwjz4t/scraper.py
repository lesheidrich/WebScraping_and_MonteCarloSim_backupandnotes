import requests
from bs4 import BeautifulSoup
from fake_user_agent import user_agent
import pandas as pd
from io import StringIO
import time
import random
from pprint import pprint


def random_header() -> dict:
    user = user_agent()
    return {'user-agent': user}


def start_session():
    return requests.Session()


def close_session(session) -> None:
    session.close()


def request_sauce_text(url: str, session=None, http=None, https=None) -> str:
    proxies = {
        'http': http,
        'https': https
    }

    if session:
        response = session.get(url, headers=random_header(), proxies=proxies)
    else:
        response = requests.get(url, headers=random_header(), proxies=proxies)

    return response.text


def random_delay(min_sec: float = 1.0, max_sec: float = 5.0) -> None:
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)


def table_2_df(url, session=None, http=None, https=None):
    response_text = request_sauce_text(url, session, http, https)
    soup = BeautifulSoup(response_text, 'html.parser')
    table_html = soup.find('table', class_='tablesaw')
    table_str = str(table_html)
    mock_html = StringIO(table_str)

    return pd.read_html(mock_html)


if __name__ == '__main__':
    url1 = 'https://basketball.realgm.com/nba/teams/Boston-Celtics/2/individual-games/2006/points/Regular_Season/desc/5'
    url2 = 'https://basketball.realgm.com/nba/teams/Boston-Celtics/2/Stats/2006/Averages/All/points/All/desc/1/Away'
    url3 = 'https://basketball.realgm.com/nba/team-stats/2007/Advanced_Stats/Team_Totals/Regular_Season'

    # url = 'https://basketball.realgm.com/nba/teams/Boston-Celtics/2/Depth_Charts'

    # BS4 + Pandas -> straight to df
    # response = requests.get(url, headers=random_header())
    # sauce = response.text
    # soup = BeautifulSoup(request_sauce_text(url), 'html.parser')
    # table = soup.find('table', class_='tablesaw')
    #
    # html_string = str(table)
    # html_file_like = StringIO(html_string)  # this is some bullshit
    #
    # package = pd.read_html(html_file_like)

    pp = '37.19.205.194'

    s = start_session()

    try:
        print(table_2_df(url3, s, http=pp, https=pp))
        random_delay()
        print(table_2_df(url3, s, http=pp, https=pp))
    # except requests.exceptions.RequestException as e:
    #     print(f"An error occurred during the request: {e}")
    # except OSError as e:
    #     print(f"An error occurred during the request: {e}")
    #

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        pp = ''
        print(table_2_df(url3, s, http=pp, https=pp))
        random_delay()
        print(table_2_df(url3, s, http=pp, https=pp))



    close_session(s)
