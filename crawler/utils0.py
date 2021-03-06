# -*- coding: utf-8 -*-

#from crawler.models import Portfolio, Positions_change, Accumulated_position
from login import login
from datetime import datetime
from decimal import Decimal
#from django.db.models import F

import json
import requests
import re
from bs4 import BeautifulSoup
import time
import pandas

"""



import re

"""


telephone = '******'
password  = '******'

agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {
    'User-Agent': agent,
    'Host': "xueqiu.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.6",
    "Connection": "keep-alive"
}
session = requests.session()



def save_latest_change(url):
    headers = login(telephone, password)
    url0 = 'https://xueqiu.com/'+url
    data = session.get(url0, headers=headers).text
    soup = BeautifulSoup(data, "lxml")
    followers = soup.find('li', class_="gender_info" )
    followers = followers.find_next_siblings("li")[0]
    followers = followers.contents[0]
    print(followers)


"""
    if data["stocks"]:
        for item in data["stocks"]:
            if re.search('ZH\d{6}',str(item)):
                ZHs0[item["code"]]=item["stockName"]
        Positions_change.objects.filter(portfolio=Portfolio.objects.filter(title=url)[0]).delete()
        for ZH0 in ZHs0:
            prof(ZH0, ZHs0, headers, url)
        Accumulated_position.objects.filter(portfolio=Portfolio.objects.filter(title=url)[0]).delete()
        ZHs = re.findall('ZH\d{6}',data["portfolios"][0]["stocks"])
        for ZH in ZHs:
            get_xueqiu_hold("https://xueqiu.com/P/"+ZH, headers, url)


def prof(url_ap0, ZHs0, headers, portfilio):
    url = 'https://xueqiu.com/cubes/rebalancing/history.json?cube_symbol='+url_ap0+'&count=20&page=1'
    data = session.get(url, headers=headers).text
    data = json.loads(data)

    for i in range(len(data[u'list'])):
        for j in range(len(data[u'list'][i]['rebalancing_histories'])):
            if pandas.isnull(data[u'list'][i]['rebalancing_histories'][j]['prev_weight_adjusted']):
                data[u'list'][i]['rebalancing_histories'][j]['prev_weight_adjusted'] = str(0)
            else:
                data[u'list'][i]['rebalancing_histories'][j]['prev_weight_adjusted'] = str(data[u'list'][i]['rebalancing_histories'][j]['prev_weight_adjusted'])
            if pandas.isnull(data[u'list'][i]['rebalancing_histories'][j]['target_weight']):
                data[u'list'][i]['rebalancing_histories'][j]['target_weight'] = str(0)
            else:
                data[u'list'][i]['rebalancing_histories'][j]['target_weight'] = str(data[u'list'][i]['rebalancing_histories'][j]['target_weight'])
    try:
        for i in range(len(data[u'list'])):
            localtime = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(data[u'list'][i]['updated_at'] / 1000))
            print(localtime,ZHs0[url_ap0])
            if (time.time() - (data[u'list'][i]['updated_at'] / 1000)) < 86400*20:
                for j in range(len(data[u'list'][i]['rebalancing_histories'])):
                    detail = data[u'list'][i]['rebalancing_histories'][j]['stock_name'] + ': '+ data[u'list'][i]['rebalancing_histories'][j]['prev_weight_adjusted'] + '% ' + ("⬆" if float(data[u'list'][i]['rebalancing_histories'][j]['prev_weight_adjusted'])<float(data[u'list'][i]['rebalancing_histories'][j]['target_weight']) else "⇩") + ' '+ data[u'list'][i]['rebalancing_histories'][j]['target_weight'] + '%'
                    print(detail,ZHs0[url_ap0], )
                    if not Positions_change.objects.filter(detail=detail, portfolio=Portfolio.objects.filter(title=portfilio)[0], code=url_ap0).exists():
                        positions_change = Positions_change(
                            portfolio=Portfolio.objects.filter(title=portfilio)[0],
                            time= datetime.fromtimestamp(data[u'list'][i]['updated_at'] / 1000),
                            name=ZHs0[url_ap0],
                            code=url_ap0,
                            detail=detail
                        )
                        positions_change.save()
    except:
        print("exception occured")


def get_xueqiu_hold(url, headers, portfilio):
    soup = session.get(url, headers=headers).text
    soup = BeautifulSoup(soup, 'lxml')
    script = soup.find('script', text=re.compile('SNB\.cubeInfo'))
    json_text = re.search(r'^\s*SNB\.cubeInfo\s*=\s*({.*?})\s*;\s*$',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(1)
    data = json.loads(json_text)
    for d in data["view_rebalancing"]["holdings"]:
        if not Accumulated_position.objects.filter(stock=d['stock_name'], portfolio=Portfolio.objects.filter(title=portfilio)[0]).exists():
            accumulated_position = Accumulated_position(
                portfolio=Portfolio.objects.filter(title=portfilio)[0],
                stock=d['stock_name'],
                percent = d['weight'],
                people=1,
            )
            accumulated_position.save()
        else:
            accumulated_position = Accumulated_position.objects.filter(stock=d['stock_name'], portfolio=Portfolio.objects.filter(title=portfilio)[0])
            accumulated_position.update(percent=F('percent')+Decimal(d['weight']))
            accumulated_position.update(people=F('people')+1)
"""

if __name__ == "__main__":
    print("what is this")
    save_latest_change("1180102135")