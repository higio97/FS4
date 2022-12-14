import pymongo
import config

myclient = pymongo.MongoClient(config.MONGO_DB_URL)

mydb = myclient[config.MONGO_DB_NAME]
mycol = mydb["user"]


async def cek_user_didatabase(chat_id: int):
    found = mycol.find_one({'_id': chat_id})
    if found:
        return True
    else:
        return False

async def tambah_user(chat_id: int):
    mycol.insert_one({"_id": chat_id})

async def get_all_user():
    user_id = []
    for doc in mycol.find():
        user_id.append(doc['_id'])
    return user_id
