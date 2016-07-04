# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def login():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':  'gzip, deflate, sdch',
        'Accept-Language':  'zh-CN,zh;q=0.8',
        'Cache-Control':  'max-age=0',
        'Connection':  'keep-alive',
        'User-Agent':  'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    session = requests.session()
    res = session.get('http://www.zhihu.com',headers = header).content
    _xsrf = BeautifulSoup(res, "html.parser").find('input', attrs={'name': '_xsrf'})['value']

    login_data = {
        '_xsrf':_xsrf,
        'password':'smy1384578',
        'remember_me':'true',
        'email':'13166217194'
    }
    session.post('https://www.zhihu.com/#signin',data = login_data,headers = header)
    res = session.get('http://www.zhihu.com')
    print(res.text)

if __name__ == '__main__':
    login()