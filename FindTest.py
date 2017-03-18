import pymongo

client = pymongo.MongoClient()
db = client.web
user = db.user_info

info = user.find_one({"username" : "wfwesx",
    "password" : "vvwvw"})

if info==None:
    print("没有这个人")
else:
    print(info)
