
# -*- coding: utf-8 -*-
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

#import urllib2
import urllib
#import  cookielib
try:
    import cookielib
except:
    import http.cookiejar
    cookielib = http.cookiejar
import requests
import json
from emoji import emojize


bot_token = 'XXXXXXXXXXXXXXXXXXXo' #inserir aqui TOKEN do Telegram
bot_chatID = 'XXXXXXXXXXXXXXXXXX' #inserir aqui chatid do Telegram
url_worten = "https://encomendas.worten.pt/api/order/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" #inserir aqui URL com guid da encomenda

cookies = {
}


headers = {
'Host' : 'encomendas.worten.pt',
'Connection' : 'keep-alive',
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'Content-Type': 'application/json'
}

#headers = urllib.urlencode(headers)
def bot_sendtext(bot_message):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        requests.get(send_text)


state_worten_web = requests.get(url_worten, headers=headers, cookies=cookies)
state_worten_web_json =  json.loads(state_worten_web.text)
estado_online = state_worten_web_json['Items'][0]['ActiveStep']
product_name = state_worten_web_json['Items'][0]['ProductName']
f=open("file.txt","r")
file_status=f.read()
f.close()

if str(estado_online) != file_status:
        bot_sendtext(emojize(":v: Novo estado item "+str(product_name) +": "+str(estado_online), use_aliases=True))
        f=open("file.txt","w+")
        f.write(str(estado_online))
        f.close()
