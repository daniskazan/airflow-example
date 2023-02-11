from airflow.models.dag import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator, SQLExecuteQueryOperator
import pandas as pd
import requests
from zipfile import ZipFile
from io import BytesIO
import datetime

DAG_ID = "postgres_conn"

