'''
=================================================
Milestone 3

Name  : Maulana Yusuf Taufiqurrahman
Batch : FTDS-026-HCK

This program is designed to automate the ETL (Extract, Transform, Load) pipeline for a dataset on Mobile Device Usage and User Behavior, with the following specific goals:
1. Extract data from a PostgreSQL database table containing raw mobile device usage and user behavior records.

2. Transform the dataset by:
- Normalizing column names (lowercase, replacing spaces with underscores, and removing unnecessary characters).
- Handling missing values by dropping incomplete rows to ensure data quality.
- Removing duplicates.

3. Load the cleaned dataset into an ElasticSearch index to enable:
- Fast, scalable full-text search.
- Real-time analytics for user behavior trends.
- Advanced filtering, aggregation, and visualization via Kibana or similar tools.

The end-to-end workflow is scheduled and orchestrated using Apache Airflow, ensuring that the ETL process runs automatically, consistently, and can be monitored and scaled as needed.
=================================================
'''

import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
import time
import re
from elasticsearch import Elasticsearch

default_args= {
    'owner': 'Yusuf',
    'start_date': datetime(2024, 11, 1)
}

with DAG(
    'Stream_P2M3_Maulana_Yusuf',
    description = 'Milestone 3',
    schedule_interval = '10,20,30 9 * * 6',
    default_args = default_args, 
    catchup = False
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task() # Task 1
    def extract_to_airflow():
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()

        # Task 1
        df = pd.read_sql('SELECT * FROM table_m3', conn)
        df.to_csv('/opt/airflow/data/P2M3_Maulana_Yusuf_data_raw.csv', index=False)
        print("Success INSERT")

    @task() # Task 2
    def preprocess_data():
        '''This function used to clean the raw CSV file from postgresql'''
        df = pd.read_csv('/opt/airflow/data/P2M3_Maulana_Yusuf_data_raw.csv')

        # 1. Drop duplicates
        df.drop_duplicates(inplace = True)

        # 2. Handle missing values
        df.dropna(inplace=True)

        # 3. Normalization data
        def normalize_column(col):
            # Separate the contents in brackets
            match = re.search(r"\((.*?)\)", col)
            unit = f'({match.group(1)})' if match else ''

            # Remove the contents in brackets from the main string
            base = re.sub(r"\(.*?\)", "", col)
            # Remove white spaces and lowercasing
            base = base.strip().lower()
            # Deleting symbols 
            base = re.sub(r'[^\w\s]', '', base)
            # Convert spaces/tab into underscore
            base = re.sub(r'\s+', '_', base)


            return f"{base}_{unit}" if unit else base
        
        df.columns = [normalize_column(col) for col in df.columns]

        # Save the cleaned data
        print(f'Preprocessed data is Success')
        df.to_csv('/opt/airflow/data/P2M3_Maulana_Yusuf_data_clean.csv', index=False)

    @task() # Task 3
    def load_elastic():
        '''This function used to upload the cleaned data into ElasticSearch'''
        es = Elasticsearch("http://elasticsearch:9200")
        
        df = pd.read_csv('/opt/airflow/data/P2M3_Maulana_Yusuf_data_clean.csv')

        index_name = "p2m3_maulana_yusuf"

        # Insert each record
        for i, record in df.iterrows():
            doc = record.to_dict()
            es.index(index=index_name, body=doc)

        print(f"Data loaded to Elasticsearch index '{index_name}'")
    
    start >> extract_to_airflow() >> preprocess_data() >> load_elastic() >> end
