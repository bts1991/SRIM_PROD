from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://btsy7331:dmadkr753!@cluster0.dw6olvv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



# db = client.test_database
db = client['SRIM'] # test-db라는 이름의 데이터베이스에 접속
main = db.main

## document에 show_yn이라는 필드가 존재하지 않는 경우, show_yn 필드를 add 함(값은 Y)
# main.update_many({"nation": {"$exists": False}}, {"$set": {"nation": 'kor'}})
# main.update_one({"baseDate":"2023/09", "CoID":"SK가스"},{"$set" : {"show_yn": show_yn
#     }})

## baseDate가 2023/09이고 CoID가 SK가스인 경우의 show_yn을 추출
# result = main.find_one({"baseDate":"2023/09", "CoID":"SK가스"}, {"show_yn"})
# print(result)

## CoID를 기준으로 중복을 제거하여 CoID 값을 추출함
# result1 = main.distinct("CoID",{})
# for i in result1:
#     print(i)

## 조건 없이 모든 nation 값을 추출함
# result = main.find({}, {"nation"})
# for i in result:
#     print(i)


