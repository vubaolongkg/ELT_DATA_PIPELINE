import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. Cấu hình kết nối Database
db_user = 'airflow'
db_password = 'airflow'
db_host = 'postgres'
db_port = '5432'
db_name = 'airflow'

def ingest_data():
    print("--- Bắt đầu lấy dữ liệu từ API ---")
    
    # 2. Gọi API
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Đã lấy thành công {len(data)} dòng dữ liệu.")
        
        # 3. Chuyển đổi sang DataFrame (SỬA Ở ĐÂY)
        # pd.json_normalize giúp làm phẳng dữ liệu lồng nhau (nested json)
        # Cột 'rating' sẽ tách thành 'rating.rate' và 'rating.count'
        df = pd.json_normalize(data)
        
        # Đổi tên cột dấu chấm thành gạch dưới cho chuẩn SQL (rating.rate -> rating_rate)
        df.columns = [c.replace('.', '_') for c in df.columns]

        print("Các cột dữ liệu:", df.columns.tolist())
        
        # 4. Tạo kết nối tới Postgres
        conn_string = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(conn_string)
        
        # 5. Lưu vào Database
        df.to_sql('raw_products', engine, if_exists='replace', index=False)
        
        print("--- Đã nạp dữ liệu vào bảng 'raw_products' thành công! ---")
    else:
        print("Lỗi khi gọi API:", response.status_code)

if __name__ == "__main__":
    ingest_data()