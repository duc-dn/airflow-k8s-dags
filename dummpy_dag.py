from airflow import DAG
from airflow.operators.empty import EmptyOperator  # Airflow 2.x thay thế DummyOperator bằng EmptyOperator
from datetime import datetime

# Định nghĩa DAG
with DAG(
    dag_id="my_dummy_dag",
    start_date=datetime(2024, 3, 14),
    schedule_interval="@daily",  # Chạy hàng ngày
    catchup=False,  # Không chạy lại các ngày trước đó
) as dag:

    # Định nghĩa EmptyOperator (trước đây là DummyOperator)
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    # Flow của DAG
    start >> end  # Chạy từ start đến end
