# _*_ coding:utf-8 _*_
import requests

r = requests.get('http://www.sebastianblade.com')
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.history)