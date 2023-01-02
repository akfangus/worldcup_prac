from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://lee:sparta@Cluster0.nw7w0pd.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

url = "https://worldcupjson.net/teams"

data = requests.get('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup#Teams')
soup = BeautifulSoup(data.text, 'html.parser')
print(soup)
trs = soup.select(
    '#mw-content-text > div.mw-parser-output > div:nth-child(75) > table > tbody > tr > td > ul > li > span > span >img ')
trs2 = soup.select(
    '#mw-content-text > div.mw-parser-output > div:nth-child(75) > table > tbody > tr > td > ul > li > span > a')

list1 = []

for i, j in zip(trs, trs2):
    print(i,j)
    if j.text == 'South Korea':
        list1.append(list(['Korea Republic', i['src']]))
    else:
        list1.append(list([j.text, i['src']]))

response = requests.request("GET", url)
all_data = response.json()
# print(all_data['groups'][0]['letter'])
# print(all_data['groups'][0]['teams'])

group_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
list2 = []

for idx, value in enumerate(group_list):

    group_data = all_data['groups'][idx]['teams']
    for item in group_data:
        # print(item['name'], value)
        list2.append(list([item['name'], item['country'], value]))

#
# print(sorted((list1)))
# print(sorted((list2)))
# 최초 팀 그룹 데이터베이스 => 나라 이미지가 없어서 데이터베이스 만들어서 저장해놓으려고함.
# 나머지 팀 기록같은건 굳이 db 안쓰고 api로 불러와서 처리하면 될듯.
# 사실 db로 저장미리 해놓고 쿼리문 이쁘게짜서 원하는 데이터만 뽑아내는게 더 효율적이긴한데
# 쿼리문을 잘 짤지 몰름.
l1 = sorted((list1))
print(l1)
l2 = sorted((list2))
for idx in range(len(l2)):
    doc = {
        'group': l2[idx][2],
        'name': l1[idx][0],
        'country': l2[idx][1],
        'img': l1[idx][1]
    }
    # print(l2[idx][2], l1[idx][0], l2[idx][1], l1[idx][1])
    # print(l2[idx][1], l1[idx][0], l1[idx][1])

    # 여기가 데이터 저장 # 주석풀면 중복 데이터 저장됨.
    # db.teams.insert_one(doc)

    # print(l1[idx][0], l2[idx][0])

# print(response.json())


# 원하는 데이터가 없어? 시간이 없으니 그냥 크롤링해서 값을 넣어야하나?
##root > main > div > section:nth-child(4) > div > div.fdcp-tournament-groups-view_groupsContainer__w862T.row > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.ff-pl-8 > div > div.fdcp-standings-group_teamName__2TaPn.ff-pl-8


# 한글깨짐 해결하는 방법이라는데 오ㅑㅐ 안되는거지?
# 계속 안되다가 어느순간 됨?
# data2.content.decode('utf-8', 'replace')
