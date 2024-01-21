from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.python import PythonOperator

def greet(ti,time_):
    name=ti.xcom_pull(task_ids='get_name')
    print(f'Good morning {name}, its {time_} already')

def get_name():
    return 'Akello'


with DAG(
    dag_id="Python_dag",
    default_args={
        'owner':'Rhon',
        'retries':5,
        'retry_delay':timedelta(minutes=2)
    },
    description="this is my first python dag",
    start_date=datetime(2024,1,21),
    schedule_interval='@daily'
) as dag:
    task1= PythonOperator(
        task_id='run_python',
        python_callable=greet,
        op_kwargs={'time_':9}
    )

    task2=PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task2 >> task1