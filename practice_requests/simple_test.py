import requests

# 发送各种请求

r = requests.get('https://github.com/timeline.json')
r = requests.post('http://httpbin.org/post')
r = requests.delete('http://httpbin.org/delete')
r = requests.put('http://httpbin.org/put')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# 为url传递参数

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)