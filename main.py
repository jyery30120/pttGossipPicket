import sys
from PyPtt import PTT, PostField, NewIndex
import json
from datetime import date, timedelta

ptt_id, password = '',''
ptt_bot = PTT.API()

def login():
    try:
        ptt_bot.login(ptt_id, password)
    except PTT.exceptions.LoginError:
        print('登入失敗')
        sys.exit()
    except PTT.exceptions.WrongIDorPassword:
        print('帳號密碼錯誤')
        sys.exit()
    except PTT.exceptions.LoginTooOften:
        print('請稍等一下再登入')
        sys.exit()
    print('登入成功')

    return ptt_bot

if __name__ == '__main__':
    login()
    result = []
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    list_today = today.strftime("%#m/%d")
    list_yesterday = yesterday.strftime("%#m/%d")
    newest_index = ptt_bot.get_newest_index(NewIndex.BOARD, 'Gossiping')
    tmp = newest_index
    print('end = ', newest_index)

    for i in range(newest_index , 0 , -1 ):
        post_info = ptt_bot.get_post(
            'Gossiping',
            index = i )
        
        data = {
            'Author: ' : post_info[PostField.author],
            'Title: ' : post_info[PostField.title]
        }
        if post_info[PostField.list_date] == list_today:
            continue
        elif post_info[PostField.list_date] != list_yesterday:
            break

        result.append(data)
        if (tmp - i == 100):
            print('now = ' , i)
            tmp = i

    filename =  'data_' + str(today.strftime("%m%d")) + '.json'
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False)

    ptt_bot.logout()