from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'elt_pipeline_v1',
    default_args=default_args,
    description='A simple ELT pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'elt'],
) as dag:

    # Task 1: Chạy script Python để lấy dữ liệu (Extract & Load)
    t1_ingest_data = BashOperator(
        task_id='ingest_data_from_api',
        bash_command='python /opt/airflow/scripts/ingest_products.py'
    )

    # Task 2: Chạy dbt để làm sạch dữ liệu (Transform)
    # Lưu ý: Cần chỉ rõ đường dẫn project-dir và profiles-dir
    t2_dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --profiles-dir /opt/airflow/dbt_project --project-dir /opt/airflow/dbt_project'
    )

    # Quy định thứ tự chạy: t1 xong rồi mới đến t2
    t1_ingest_data >> t2_dbt_run