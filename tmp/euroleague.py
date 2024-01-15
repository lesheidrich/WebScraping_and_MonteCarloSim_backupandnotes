import requests
from bs4 import BeautifulSoup
# from fake_user_agent import user_agent
import pandas as pd
import pymysql


name = []
team = []
gp = []
min = []
efg = []
ts = []
oreb = []
dreb = []
reb = []
astto = []
astr = []
tor = []
pta2r = []
pta3r = []
ftrt = []

url = "C:/Users/dblin/Downloads/freeformatter-out.html"

with open(url) as html:
    soup = BeautifulSoup(html, 'html.parser')

player_name = soup.find_all("span", class_="complex-stat-table_longValue__3xUTT")
player_team = soup.find_all("span", class_="complex-stat-table_advancedTeamText__25NEW")
block = soup.find_all("div", class_="complex-stat-table_cell__1lxC7 complex-stat-table__w600__FRIuO")

indexer = 0
while indexer < len(block):
    player_no = int(block[indexer].text)-1

    name.append(player_name[player_no].text)
    team.append(player_team[player_no].text)
    gp.append(int(block[indexer+2].text))
    min.append(block[indexer+3].text.replace(block[indexer+3].text, f"00:{block[indexer+3].text}")) #text
    efg.append(float(block[indexer+4].text.replace("%", ""))/100)
    ts.append(float(block[indexer+5].text.replace("%", ""))/100)
    oreb.append(float(block[indexer+6].text.replace("%", ""))/100)
    dreb.append(float(block[indexer+7].text.replace("%", ""))/100)
    reb.append(float(block[indexer+8].text.replace("%", ""))/100)
    astto.append(float(block[indexer+9].text))
    astr.append(float(block[indexer+10].text.replace("%", ""))/100)
    tor.append(float(block[indexer+11].text.replace("%", ""))/100)
    pta2r.append(float(block[indexer+12].text.replace("%", ""))/100)
    pta3r.append(float(block[indexer+13].text.replace("%", ""))/100)
    ftrt.append(float(block[indexer+14].text.replace("%", ""))/100)

    indexer += 15

data = {
    'Player': name,
    'Team': team,
    'Games_Played': gp,
    'Min_Played': min,
    'Effective_FG': efg,
    'True_Shooting': ts,
    'OREB': oreb,
    'DREB': dreb,
    'REB': reb,
    'ASTTO': astto,
    'ASTR': astr,
    'TOR': tor,
    'PTA2R': pta2r,
    'PTA3R': pta3r,
    'FTRT': ftrt
}
df = pd.DataFrame(data)
print(df)

print(df['Min_Played'])


conn = pymysql.connect(
    host='localhost',
    user='sport',
    password='rLm/XlaTTHe5ofi-',
    database='bball')

cursor = conn.cursor()

truncate = "truncate table euroleague_player;"
cursor.execute(truncate)

#create table script is buggy, probably because of comma at end,
#just run this and copy text into phpmyadmin
# query = f"CREATE TABLE IF NOT EXISTS euroleague_player (\n"
# for col in df.columns:
#     query += col + " "
#     if df[col].dtype == 'object':
#         item_type = 'VARCHAR(255)'
#     elif df[col].dtype == 'int64':
#         item_type = 'INT'
#     elif df[col].dtype == 'float64':
#         item_type = 'FLOAT'
#     query += item_type
#     if col != 'FT-RT':
#         query += ",\n"
#     else:
#         query += "\n"
# query += ");"
# query.replace("Min_Played VARCHAR(255),", "Min_Played TIME,")
# print(query)
#
# cursor.execute(query)

# insert data into the table
for row in df.itertuples(index=False):
    placeholders = ','.join(['%s'] * len(row))
    sql = f"INSERT INTO euroleague_player ({','.join(df.columns)}) VALUES ({placeholders})"
    cursor.execute(sql, row)

# commit the changes to the database
conn.commit()

# close the database connection
conn.close()



# df.to_excel('euroleague_player.xlsx', index=False)


