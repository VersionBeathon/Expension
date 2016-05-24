# 阶段总结
这段时间主要接触了pyenv、Virtualenv、redis数据库、mongoDB、Cerberus模块以及函数式编程
## pyenv
[pyenv](https://github.com/yyuu/pyenv)是一个功能强大的python版本管理工具，可以指定路径下python的版本，并且每个版本对应的包管理工具都是不同的，例如：指定 A 路径为 python 2.7.10 那么对应的 pip则为 python 2.7.10，指定 B 路径为 python 3.5.1 那么对应的 pip则为 pyton 3.5.1。官方文档请点击上面的蓝色链接。
### 安装
* 安装方式点击链接--[pyenv install](https://github.com/yyuu/pyenv#homebrew-on-mac-os-x)
* 安装完修改bash
```unix
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```
* 如果是zsh则修改~/.zshrc
```unix
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
### 使用方法
* 修改全局版本
```unix 
pyenv global 3.5.1
```
* 修改局部版本
```unix
cd xxx
pyenv local 3.5.1
```
* 修改shell
```unix
pyenv shell 3.5.1
```
* shell >> local >> global
## Virtualenv
[Virtualenv](https://virtualenv.pypa.io/en/latest/)是一个可以虚拟化python环境的工具，指定路径产生虚拟环境，配合pyenv使用可很好的实现版本隔离，在同一台电脑上使用不同版本开发python。官方文档请点击上面的蓝色链接。
### 安装
* pip install virutalenv
### 使用
* 创建虚拟环境
```unix
virtualenv ENV
```
在当前路径下创建ENV文件夹，ENV就是所创建的虚拟环境。
* 激活环境
```unix
source bin/activate
```
* 退出环境
```unix
deactivate
```
* 可以指定创建环境的内容，请查看官方使用文档
## [redis](https://github.com/VersionBeathon/Expension/tree/master/practice_redis)
redis一种内存数据库，轻便小巧，redis有五种数据类型：string、hash、list、set、zset。
### 安装Python中对应的模块
* pip install redis
### 使用
* [simple_redis.py](https://github.com/VersionBeathon/Expension/blob/master/practice_redis/simple_redis.py)
* transaction Python的事务操作
## mongodb
monbgodb一种NoSql数据库。为key-value形式可以理解成Python中的字典。
### 安装python中对应的模块
* pip install Pymongo
### 使用
* [overview_monogo.py](https://github.com/VersionBeathon/Expension/blob/master/practice_mongo/overview_monogo.py)
### 注意
很多网上的资料链接数据库都是connection方法，但是在最新版本中此方法移除变为MongoClient
## [Cerberus](http://docs.python-cerberus.org/en/stable/index.html)
从单词意思来讲是：看门狗，具体使用方法也如此，指定规则允许指定的数据通过。此模块没有具体的中文文档，测试python文件中很多注释有可能翻译的不准确。
### 安装
* pip install cerberus
### 使用
* [practice_cerberus](https://github.com/VersionBeathon/Expension/tree/master/prcatice_cerberus)
每种方法都进行了注释。

