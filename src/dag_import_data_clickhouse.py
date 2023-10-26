import os
from datetime import datetime, timedelta
import os
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
import psycopg2
import pandas as pd
import pandahouse as ph
from airflow.utils.edgemodifier import Label


dag_id = f"prod_dbt_loader_dag_table_different_format"
dag = DAG(
    dag_id,
    start_date=datetime(2021, 1, 1),
    description="A dbt wrapper for Airflow.",
    schedule_interval="0 * * * *", # run every hour
    catchup=False,
    doc_md=__doc__,
    # max_active_runs=3,
    max_active_tasks=4,
)

def read_data_from_postgres():
    connect_portgreSQL = psycopg2.connect(host="localhost",
                                    database="postgres",
                                    user="postgres",
                                    password="huutinh123@.com",
                                    port = 5432)
    
    query = 'SELECT * FROM data_iris'
    dataFrame = pd.read_sql(query, connect_portgreSQL)
    print(dataFrame)
    return dataFrame
def load_data_into_clickhouse(dataFrame):
    connection = dict(database='data',
                  host='https://cnkm9cv2o3.eu-west-1.aws.clickhouse.cloud:8443',
                  user='default',
                  password='')
    
    ph.to_clickhouse(dataFrame, 'data_iris', index=False, chunksize=100000, connection=connection)

task1 = PythonOperator(task_id='read_data_from_kafka', python_callable=read_data_from_postgres, dag=dag)
task2 = PythonOperator(task_id='transform_data_kafka', python_callable=load_data_into_clickhouse, dag=dag)

task1 >> Label("Load_data") >> task2 
if __name__ == "__main__":
    dag.cli()

