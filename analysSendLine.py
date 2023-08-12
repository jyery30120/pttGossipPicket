import requests
import json
import re
from collections import Counter
from datetime import date

today = date.today()
d1 = today.strftime("%m%d")
filename =  'data_' + str(d1) + '.json'
with open( filename , 'r',encoding="utf-8") as reader:
    jf = json.loads(reader.read())

lst_word=[]
lst_news=[]
lst_ask =[]
lst_all =[] 	

for i in range(0,len(jf)-1):
  try:
    if(jf[i]['Title: '].startswith('[新聞]')):
      lst_news.append(jf[i]['Author: '])
    if(jf[i]['Title: '].startswith('[問卦]')):
      lst_ask.append(jf[i]['Author: '])
    lst_all.append(jf[i]['Author: '])  
  except:
    pass


news = [(i,j) for i , j in Counter(lst_news).most_common()[0:10] if j > 1]
ask = [(i,j) for i , j in Counter(lst_ask).most_common()[0:10] if j > 2]
over = [(i,j) for i , j in Counter(lst_all).most_common()[0:10] if j > 5]

bearer_token = ""

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json" 
}

url = "https://notify-api.line.me/api/notify?message="

if len(news) > 0:
    print(requests.post(url + str(news)[:1000], headers=headers).text)
if len(ask) > 0:
    print(requests.post(url + str(ask)[:1000], headers=headers).text)
if len(over) > 0:
    print(requests.post(url + str(over)[:1000], headers=headers).text)