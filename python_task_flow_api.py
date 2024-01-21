from airflow.decorators import task , dag
from datetime import datetime,timedelta

@dag(   dag_id="Python_dag_api",
    default_args={
        'owner':'Rhon',
        'retries':5,
        'retry_delay':timedelta(minutes=2)
    },
    description="this is my first python dag",
    start_date=datetime(2024,1,21),
    schedule_interval='@daily')
def etl():
    @task
    def get_name():
        return 'Akello Babra'
    
    @task
    def get_age():
        return 17
    
    @task
    def greet(name, age):
        print(f'Hi {name} , am {age} years  old')

    name=get_name()
    age=get_age()

    greet(name=name,age=age)

greet=etl()
