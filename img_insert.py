import requests
from bs4 import BeautifulSoup

data = requests.get('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup#Teams')

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select(
    '#mw-content-text > div.mw-parser-output > div:nth-child(75) > table > tbody > tr > td > ul > li > span > span >img ')
trs2 = soup.select(
    '#mw-content-text > div.mw-parser-output > div:nth-child(75) > table > tbody > tr > td > ul > li > span > a')

list1 = []

for i, j in zip(trs, trs2):
    if j.text == 'South Korea':
        list1.append(list(['Korea Republic', i['src']]))
    else:
        list1.append(list([j.text, i['src']]))


