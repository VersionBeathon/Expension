# _*_ coding:utf-8 _*_
import requests

# 响应内容

r = requests.get('https://github.com/timeline.json')
print(r.text)
print(r.encoding)

# 二进制响应内容

print(r.content)

# json响应内容

r = requests.get('https://github.com/timeline.json')
print(r.json())

# 原始响应内容

r = requests.get('https://github.com/timeline.json', stream=True)
print(r.raw)