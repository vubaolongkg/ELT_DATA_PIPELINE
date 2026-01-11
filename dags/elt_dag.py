from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# 1. Cấu hình mặc định cho DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 2. Định nghĩa DAG
with DAG(
    'elt_pipeline_v1',              # Tên DAG (sẽ hiện trên web)
    default_args=default_args,
    description='A simple ELT pipeline',
    schedule_interval='@daily',     # Chạy hàng ngày
    start_date=datetime(2024, 1, 1),
    catchup=False,                  # False: Không chạy bù những ngày quá khứ
    tags=['example', 'elt'],
) as dag:

    # 3. Định nghĩa các Task (Công việc)
    
    # Task 1: Chạy script Python để lấy dữ liệu
    # Chúng ta dùng BashOperator vì nó đơn giản: giống hệt việc bạn gõ lệnh trong terminal
    t1_ingest_data = BashOperator(
        task_id='ingest_data_from_api',
        bash_command='python /opt/airflow/scripts/ingest_products.py' 
        # Lưu ý: /opt/airflow/scripts là đường dẫn bên trong Docker (đã map volume)
    )

    # Sau này sẽ có Task 2: Chạy dbt transform
    # t2_transform_data = ...

    # 4. Luồng chạy (Flow)
    # Hiện tại chỉ có 1 task nên không cần mũi tên, nhưng sau này sẽ là:
    # t1_ingest_data >> t2_transform_data
    
    t1_ingest_data