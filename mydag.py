from airflow import  DAG
from datetime import datetime , timedelta
from airflow.operators.bash import BashOperator


# this is the DAG class we use to initialize the dags
with DAG (
    dag_id="BASH_DAG",
    description='This is bash operator dag',
    default_args={
    'owner':'Rhon',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
    },
    start_date=datetime(2024,1,11,22),
    schedule_interval='@daily'

) as dag: 
    task1 = BashOperator (
        task_id='first_dag',
        bash_command='echo Hey Senyonjo we made it out first airflow dag',
    )

    task2 = BashOperator (
        task_id='second_dag',
        bash_command='echo Hey Senyonjo 2',
    )

    task1 >> [task2]