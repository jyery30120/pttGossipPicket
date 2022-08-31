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
#   if(jf[i]['Title: '].startswith('[問卦]') and str_count2(remove_urls(jf['articles'][i]['content'])) < 30 ):
#     lst_word.append(jf['articles'][i]['author'])
    if(jf[i]['Title: '].startswith('[新聞]')):
      lst_news.append(jf[i]['Author: '])
    if(jf[i]['Title: '].startswith('[問卦]')):
      lst_ask.append(jf[i]['Author: '])
    lst_all.append(jf[i]['Author: '])  
  except:
    pass
#print('字數：')    

# filename =  'data_0613.json'
# with open( filename , 'r',encoding="utf-8") as reader:
#     jf = json.loads(reader.read())

# for i in range(0,len(jf)-1):
#   try:
# #   if(jf[i]['Title: '].startswith('[問卦]') and str_count2(remove_urls(jf['articles'][i]['content'])) < 30 ):
# #     lst_word.append(jf['articles'][i]['author'])
#     if(jf[i]['Title: '].startswith('[新聞]')):
#       lst_news.append(jf[i]['Author: '])
#     if(jf[i]['Title: '].startswith('[問卦]')):
#       lst_ask.append(jf[i]['Author: '])
#     lst_all.append(jf[i]['Author: '])  
#   except:
#     pass	

print('新聞超貼：')
print([(i,j) for i , j in Counter(lst_news).most_common()[0:10] if j > 1])
print('問卦超貼：')
print([(i,j) for i , j in Counter(lst_ask).most_common()[0:10] if j > 2])
print('本日超貼：')
print([(i,j) for i , j in Counter(lst_all).most_common()[0:10] if j > 5])