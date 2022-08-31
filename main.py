import sys
from PyPtt import PTT
import json
from datetime import date

print('start = ')
S = int(input())
# S = 778623
print('end = ')
E = int(input())
# E = 779929

ptt_id, password = '',''
ptt_bot = PTT.API()
try:
    ptt_bot.login(ptt_id, password)
except PTT.exceptions.LoginError:
    ptt_bot.log('登入失敗')
    sys.exit()
except PTT.exceptions.WrongIDorPassword:
    ptt_bot.log('帳號密碼錯誤')
    sys.exit()
except PTT.exceptions.LoginTooOften:
    ptt_bot.log('請稍等一下再登入')
    sys.exit()
ptt_bot.log('登入成功')

if ptt_bot.unregistered_user:
    print('未註冊使用者')

    if ptt_bot.process_picks != 0:
        print(f'註冊單處理順位 {ptt_bot.process_picks}')

if ptt_bot.registered_user:
    print('已註冊使用者')


def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

# call ptt_bot other api
result = []


for i in range( S , E + 1):
	post_info = ptt_bot.get_post(
		'Gossiping',
		post_index = i )
		
#	try:	
#		if not post_info.title.startswith('[新聞]'):
#			continue
#	except:
#		print('except',i)
#		continue
		

	data = {
		'Board' : post_info.board,
		'index:': str(post_info.index),
		'Author: ' : post_info.author,
		'Date: ' : post_info.date,
		'Title: ' : post_info.title,
		'URL: ' : post_info.web_url,
		'List Date: ' : post_info.list_date
	}

	result.append(data)
	progressBar( i - S , E-S )
	#print(i, end='\r')

today = date.today()
d1 = today.strftime("%m%d")
filename =  'data_' + str(d1) + '.json'
with open(filename, 'w', encoding='utf8') as f:
    json.dump(result, f, ensure_ascii=False)

ptt_bot.logout()