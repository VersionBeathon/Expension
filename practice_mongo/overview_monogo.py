# _*_ coding:utf-8 _*_
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.practice
print(db.collection_names())
practice = db.practice
print(practice.find_one())
posts = db.posts
print(posts.find_one())
posts1 = {"title": "physics", "author": "Newton", "lang": "english"}
posts.insert(posts1)
print(posts.find().count())
for i in posts.find():
    print(i)
n1 = {"title": "java", "name": "Bush"}
n2 = {"title": "fortran", "name": "John Warner Backus"}
n3 = {"title": "lisp", "name": "John McCarthy"}
n = [n1, n2, n3]
# 插入
posts.insert(n)
for i in posts.find():
    print(i)
print(posts.find_one({"title": "java"}))
# 升序排序
for i in posts.find().sort("title", pymongo.ASCENDING):
    print(i)
print("\n")
# 降序排序
for i in posts.find().sort("title", pymongo.DESCENDING):
    print(i)
print("\n")
# 更改
posts.update({"title": "java"}, {"$set": {"title": "python", "name": "kira"}})
for i in posts.find({"title": "python"}):
    print(i)
print("\n")
# 删除
posts.remove({"title": "physics"})
for i in posts.find():
    print(i)
