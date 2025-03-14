from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from datetime import datetime

# Hàm Python chạy trong virtualenv
def my_virtualenv_task():
    import numpy as np  # Cài đặt thư viện này trong môi trường ảo
    data = np.array([1, 2, 3, 4, 5])
    print(f"Trung bình của mảng là: {np.mean(data)}")

# Định nghĩa DAG
with DAG(
    dag_id="my_virtualenv_dag",
    start_date=datetime(2024, 3, 14),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    # Định nghĩa PythonVirtualenvOperator
    virtualenv_task = PythonVirtualenvOperator(
        task_id="my_virtualenv_task",
        python_callable=my_virtualenv_task,  # Hàm sẽ chạy trong virtualenv
        requirements=["numpy"],  # Cài đặt numpy trong môi trường ảo
        system_site_packages=False,  # Không kế thừa package từ hệ thống
    )

    virtualenv_task  # Chạy task
