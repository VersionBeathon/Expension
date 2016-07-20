from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urljoin
url = urlparse('http://www.baidu.com/index.php?username=guo1')
print(url)
print(url.netloc)

u = urlunparse(url)
print(u)

url=urlsplit('http://www.baidu.com/index.php?username=guo1')
print(url)

print(urljoin('http://www.oschina.com', 'index.php'))