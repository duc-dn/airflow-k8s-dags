from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Hàm Python sẽ được thực thi trong DAG
def my_python_task():
    print("Hello from Airflow PythonOperator!")

# Định nghĩa DAG
with DAG(
    dag_id="my_python_dag",
    start_date=datetime(2024, 3, 14),
    schedule_interval="@daily",  # Chạy hàng ngày
    catchup=False,  # Không chạy lại các ngày trước đó
) as dag:

    # Định nghĩa PythonOperator
    task = PythonOperator(
        task_id="my_python_task",
        python_callable=my_python_task,  # Hàm sẽ được gọi khi task chạy
    )

    task  # Chạy task
