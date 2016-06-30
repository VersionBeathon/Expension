# _*_ coding:utf-8 _*_
import requests

r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

# 禁用重定向

r = requests.get('http://github.com', allow_redirects=False)
print(r.history)

# 定义超时时间(请求的时间)

requests.get('http://github.com', timeout=0.001)