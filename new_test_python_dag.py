from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Hàm Python sẽ được thực thi trong DAG
def add_numbers(a: int, b: int):
    result = a + b
    print(f"Tổng của {a} và {b} là: {result}")
    return result  # Giá trị này có thể được sử dụng trong XCom

# Định nghĩa DAG
with DAG(
    dag_id="my_python_addition_dag",
    start_date=datetime(2024, 3, 14),
    schedule_interval="@daily",  # Chạy hàng ngày
    catchup=False,  # Không chạy lại các ngày trước đó
) as dag:

    # Định nghĩa PythonOperator
    add_task = PythonOperator(
        task_id="add_numbers_task",
        python_callable=add_numbers,  # Gọi hàm Python
        op_kwargs={"a": 5, "b": 10},  # Truyền tham số vào hàm
    )

    add_task  # Chạy task
