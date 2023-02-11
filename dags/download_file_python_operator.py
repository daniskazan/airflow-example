import pandas as pd
import requests
from zipfile import ZipFile
from io import BytesIO
import datetime
import logging
from airflow.utils.dates import  days_ago
from airflow.decorators import dag, task

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

EVERY_WEEK = "0 0 * * 0"
default_args = {
    'owner': 'danis',
    'depends_on_past': False,
    'email': ['danis.sharafiev@bk.ru'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}


@dag(dag_id="extract",
     start_date=days_ago(0, 0, 0, 0, 0),
     schedule=EVERY_WEEK,
     default_args=default_args,
     catchup=False,
     tags=["extract"])
def extract_data():

    @task(task_id="download_zip_and_create_csv_file")
    def download_extract_zip(link: str = "https://www.reformagkh.ru/opendata/export/131"):
        r = requests.get(link, stream=True)
        zip_file = ZipFile(BytesIO(r.content))
        df = pd.read_csv(BytesIO(zip_file.read(zip_file.namelist()[0])), sep=";")
        df.to_csv("companies.csv", index=False)
        logger.info("FINISHED UPLOADING")
    download_extract_zip()

extract_data()


