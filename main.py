import pandas as pd
from utils.mongo import insert_many_documents

def load_csv_to_dicts(csv_path: str) -> list[dict]:
    df = pd.read_csv(csv_path)
    print(f"📦 CSV 로드 완료: {df.shape[0]}행, {df.shape[1]}열")
    return df.to_dict(orient="records")

if __name__ == "__main__":
    csv_file = "data.csv"  # 너의 CSV 파일명
    docs = load_csv_to_dicts(csv_file)
    insert_many_documents(docs)