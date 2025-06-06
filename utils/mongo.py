import os
from pymongo import MongoClient
from dotenv import load_dotenv
from tqdm import tqdm  # ✅ 추가

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]


def upsert_many_documents(documents, unique_key='name'):
    if not documents:
        print("❗ 문서 없음. 삽입 생략.")
        return

    updated = 0
    inserted = 0

    print(f"🔄 {len(documents)}개의 문서 업서트 중...")

    for doc in tqdm(documents, desc="📥 업서트 진행중", unit="doc"):
        # certification_name + grade 로 name 생성
        if "certification_name" in doc and "grade" in doc:
            doc["name"] = f"{doc['certification_name']} ({doc['grade']})"
        elif "certification_name" in doc:
            doc["name"] = doc["certification_name"]

        if unique_key not in doc:
            print(f"⚠️ 문서에 '{unique_key}' 필드가 없음. 스킵: {doc}")
            continue

        filter_query = {unique_key: doc[unique_key]}
        update_query = {"$set": doc}
        result = collection.update_one(filter_query, update_query, upsert=True)

        if result.matched_count > 0:
            updated += 1
        elif result.upserted_id is not None:
            inserted += 1

    print(f"\n✅ 삽입: {inserted}개 / 업데이트: {updated}개 완료")