# _*_ coding :utf-8 _*_
import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.status_code == requests.codes.ok)
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# bad_r.raise_for_status()
print(r.raise_for_status())
print(r.headers)
print(r.headers['connection'])
print(r.headers['COnnection'])