from airflow.models import DAG 
from airflow.utlis.dates import days_ago 
from airflow.operators.empty import EmptyOperator 
from airflow.operators.bash_operator import BashOperator 

with DAG(
    "primeiroDag",
    startDate = days_ago(1),
    schedule_interval="@daily",

) as dag:

    tarefa1 = EmptyOperator(task_id = "tarefa1")
    tarefa2 = EmptyOperator(task_id = "tarefa2")
    tarefa3 = EmptyOperator(task_id = "tarefa3")
    tarefa4 = BashOperator(
        task_id = "cria_pasta",
        bash_comand = "mkdir - /home/millenagena/Documents/airflowalura/pasta1"
    )

    tarefa1 >> [tarefa2, tarefa3]

    # Dependência em paralelo { tarefa não depende uma da outra }
   
    tarefa3 >> tarefa4 

    # Dependência em série { tarefa que depende uma da outra }
    


    



















