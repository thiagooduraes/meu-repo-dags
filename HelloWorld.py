from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_world",
    schedule=None,  # Execução manual
    start_date=pendulum.datetime(2023, 11, 20, tz="UTC"),
    catchup=False,
    tags=["exemplo", "simples"],
) as dag:
    imprimir_hello = BashOperator(
        task_id="imprimir_hello",
        bash_command="echo 'Hello, World!'",
    )