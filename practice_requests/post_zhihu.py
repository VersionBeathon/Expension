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
html = s.get('http://www.zhihu.com', headers=headers)
print(html.text)
print('\n')
soup = BeautifulSoup(html.text, 'lxml')
_xsrf = soup.findAll(type='hidden')[0]['value']
print(_xsrf)
captcha_url = 'http://www.zhihu.com/captcha.gif'
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
    'password': '',
    'remember_me': 'true',
    'phone_num': '',
    'captcha': captcha_str
}
r = s.post('https://www.zhihu.com/#sigin', data=login_data, headers=headers)
print(r.json())
r = s.get('http://www.zhihu.com')
print(r.text)

# 具体思路是正确的抓取不到正确的验证码 会有图片验证码跟文本验证码混编出现