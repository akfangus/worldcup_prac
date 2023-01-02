from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://lee:sparta@Cluster0.nw7w0pd.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url_receive = 'https://fixturedownload.com/feed/json/fifa-world-cup-2022/'
data = requests.get(url_receive, headers=headers)
matches = data.json()
print(matches[0])

# print(data.json()[0])

group_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for item in group_list:
    print('절취선')
    for match in matches:
        if match['Group'] == f'Group {item}':
            user_home = db.teams.find_one({'name': match['HomeTeam']})
            user_away = db.teams.find_one({'name': match['AwayTeam']})
            home_img = user_home['img']
            away_img = user_away['img']
            # print(user['img'])

            doc = {
                'MatchNumber': match['MatchNumber'],
                'DateUtc': match['DateUtc'],
                'HomeTeam': match['HomeTeam'],
                'home_img': home_img,
                'AwayTeam': match['AwayTeam'],
                'away_img': away_img,
                'Group': match['Group'],
                'HomeTeamScore': match['HomeTeamScore'],
                'AwayTeamScore': match['AwayTeamScore']
            }
            db.matches.insert_one(doc)
            # print(item)

