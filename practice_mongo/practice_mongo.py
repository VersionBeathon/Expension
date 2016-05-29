# _*_ coding:utf-8 _*_
import pymongo
import datetime
import json
client = pymongo.MongoClient("localhost", 27017)
db = client.practice
print(db.collection_names())
posts = db.posts
posts.remove()
n1 = {"title":"c", "age":10, "user":100, "author":"Mike"}
n2 = {"title":"c++", "age":20, "user":10, "author":"John"}
n3 = {"title":"java", "age":30, "user": 50, "author":"Ammy"}
n4 = {"title":"lisp", "age":40, "user": 70, "author": "Jim"}
n = [n1, n2 ,n3, n4]
posts.insert(n)
for i in posts.find():
    print(i)

print("\n查询数据库中 age = 10")
for i in posts.find({"age":10}):
    print(i)

print("\n查询数据库中 age = 10 and user = 100")
for i in posts.find({"age":10, "user":100}):
    print(i)
for i in posts.find({"$and":[{"age":100},{"user":100}]}):
    print(i)

print("\n查询数据库中 age = 10 or user = 50")
for i in posts.find({"$or":[{"age":10},{"user":50}]}):
    print(i)

print("\n数据库中 age>20")
for i in posts.find({"age":{"$gt":20}}):
    print(i)

print("\n数据库中 age>=20")
for i in posts.find({"age":{"$gte":20}}):
    print(i)

print("\n数据库中 age<20")
for i in posts.find({"age":{"$lt":20}}):
    print(i)

print("\n数据库中 age<=20")
for i in posts.find({"age":{"$lte":20}}):
    print(i)

print("\n数据库中 10<age<30 ")
for i in posts.find({"$and":[{"age":{"$gt":10}},{"age":{"$lt":30}}]}):
    print(i)

print("\n数据库中 10<=age<=30")
for i in posts.find({"$and":[{"age":{"$gte":10}},{"age":{"$lte":30}}]}):
    print(i)

print("\n数据库中 age<20, age>30")
for i in posts.find({"$or":[{"age":{"$gt":30}},{"age":{"$lt":20}}]}):
    print(i)

print("\n更新数据库中 age>10 ,author:julia")
# 批量更新 multi = True
posts.update({"age":{"$gt":10}},{"$set":{"author":"julia"}},multi=True)
for i in posts.find():
    print(i)
print("\n")
# 创建索引
posts.create_index([("age", pymongo.DESCENDING), ("user", pymongo.ASCENDING)])

# 查看索引

for index in posts.list_indexes():
    print(index)
print("\n")
result = json.dumps(posts.find({"age":{"$gte":20}}).sort("user").explain(), indent=1)
print(result)
