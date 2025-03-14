from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Định nghĩa DAG
with DAG(
    dag_id="my_bash_dag",
    start_date=datetime(2024, 3, 14),
    schedule_interval="@daily",  # Chạy hàng ngày
    catchup=False,  # Không chạy lại các ngày trước đó
) as dag:

    # Định nghĩa BashOperator
    task = BashOperator(
        task_id="my_bash_task",
        bash_command="echo 'Hello from Airflow BashOperator!'",  # Lệnh bash sẽ được chạy
    )

    task  # Chạy task
