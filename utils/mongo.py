import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

def insert_many_documents(documents):
    if not documents:
        print("❗ 문서 없음. 삽입 생략.")
        return
    result = collection.insert_many(documents)
    print(f"✅ 총 {len(result.inserted_ids)}개 문서 삽입 완료.")