import requests
import re
from bs4 import BeautifulSoup
s = requests.Session()
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Referer": "https://www.zhihu.com/"
}
html = requests.get('http://www.zhihu.com/#sigin', headers=headers)
print(html.cookies._now)
picture_id = str(html.cookies._now)
soup = BeautifulSoup(html.text, 'lxml')
_xsrf = soup.findAll(type='hidden')[0]['value']
print(_xsrf)
captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + picture_id + '&type=login'
print(captcha_url)
captcha = s.get(captcha_url, stream=True, headers=headers)
with open('captcha.gif', 'wb') as f:
    for line in captcha.iter_content(10):
        f.write(line)
    f.close()
print('验证码:', end = '')
captcha_str = input()
print(captcha_str)
login_data = {
    '_xsrf': _xsrf,
    'password': 'smy1384578',
    'remember_me': 'true',
    'phone_num': '13166217194',
    'captcha': captcha_str
}
r = s.post('https://www.zhihu.com/login/phone_num', data=login_data, headers=headers)
print(r.json())
r = s.get('https://www.zhihu.com', headers=headers)
print(r.text)


