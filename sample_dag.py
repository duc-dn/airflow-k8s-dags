from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from Airflow!")

# Định nghĩa DAG
with DAG(
    dag_id="test_hello_dag",
    default_args={"start_date": datetime(2024, 3, 10)},
    schedule_interval="@daily",
    catchup=False,
    tags=["test"]
) as dag:
    
    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello
    )

    hello_task
