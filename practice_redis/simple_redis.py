import redis
r = redis.Redis(host='localhost', port=6379, db=0)
# get set 操作
r.set('foo', 'bar')
r.get('foo')
r.delete('foo')
r['age'] = 20
print(r.get('age'))
r.append('email', 's87576683@hotmail.com')
print(r.get('email'))
# 判断是否有key
r.exists('email')
# 查看库里有多少key,多少数据
print(r.dbsize())
# 删除当前数据库里所有的数据
r.flushdb()

# string
r.set('name', 'Kira')
r.set('age', 20)
r.getset('name', 'Kira')
r.getset('age', 20)
# incr自增
r.incr('age')
print(r.get('age'))
# decr自减
r.decr('age')
print(r.get('age'))
# 同时取一批数据
print(r.mget('name', 'age'))
# 查看所有的key
print(r.keys())
for i in r.keys():
    print(r.get(i))
# 随机key
print(r.randomkey())
# 修改key的值
r.rename('name', 'uname')
# 让数据在多少秒后过期
r.expire('uname', 1000)
# 查看剩余过期时间
r.ttl('uname')

# hash
# 创建一个hash
r.hset('test', 'foo', 'bar')
# 获取一个hash所有的值
print(r.hgetall('test'))
# 获取一个hash所有的key
print(r.hkeys('test'))

# sets
r.sadd('a', 'hello')
r.sadd('a', 'world')
r.sadd('a', '!')
r.sadd('b', 'nihao')
r.sadd('b', 'world')
r.sadd('b', '!')
# 获取集合元素个数
print(r.scard('a'))
# 判断set中是否有元素
print(r.sismember('a', 'hello'))
print(r.sismember('a', 'nihao'))
# 求交集
print(r.sinter('a', 'b'))
# 求交集并将结果赋值
print(r.sinterstore('c', 'a', 'b'))
print(r.smembers('c'))
# 求并集
print(r.sunion('a', 'b'))
# 求并集并将结果赋值
print(r.sunionstore('e', 'a', 'b'))
print(r.smembers('e'))
# 求集合的不同
print(r.sdiff('a', 'b'))
print(r.sdiffstore('f', 'a', 'b'))
print(r.smembers('f'))
# 取随机数
print(r.srandmember('a'))
# 从集合中删除
print(r.srem('a', 'hello'))
# 打印list by key
print(r.smembers('a'))
r.flushdb()

# lists
# left 左
r.lpush('a', 'hello')
r.lpush('a', 'world')
test = r.lrange('a', 0, 2)
print(test)
# right 右
r.rpush('a', 'right')
r.rpush('a', 'rightright')
test = r.lrange('a', 0, '5')
print(test)
# 获取指定位置的值
print(r.lindex('a', 0))
print(r.lindex('a', '-1'))
# 排序
for i in range(10):
    r.lpush('b', i)
test = r.lrange('b', 0, 9)
print(test)
print(r.sort('b'))
# 删除列表元素
r.lrem('b', 1)
print(r.sort('b'))
r.flushdb()

# zset
r.zadd('age','age1', 10 ,'age2', 11, age3=13, age4=14)
# 获取数量
print(r.zcard('age'))
# 获取数据
print(r.zrange('age', 0, -1))