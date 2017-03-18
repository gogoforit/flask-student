import pymongo

def get_col():
    client = pymongo.MongoClient('127.0.0.1',27017)
    db = client.web
    user = db.user_info
    return user

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save(self):
        user = {"username":self.username,"password":self.password,"num":0,"restnum":15}
        col = get_col()
        id = col.insert(user)
        print(id)

    @staticmethod
    def query_users():
        users = get_col().find()
        return users

    def confirm_user(self):
        info  = {"username":self.username,"password":self.password}
        findseq = get_col().find_one(info)
        return findseq
    @staticmethod
    def sign(st):
        info = {"username":st}
        findseq = get_col()
        j = findseq.find_one({"username": st})
        # j = info.update({"username":})?
        num1 = j["num"]
        restnum = j["restnum"]
        findseq.update({"username": st}, {'$set': {'num': num1 + 1, 'restnum': restnum - 1}})
        j = findseq.find_one({"username": st})
        print(j)