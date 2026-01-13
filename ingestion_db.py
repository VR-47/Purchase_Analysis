import pandas as pd
from sqlalchemy import create_engine
import os
import logging
import time

logging.basicConfig(
    filename="logs/.log",
    level=logging.DEBUG,
    format="%((asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# create SQLAlchemy engine (what pandas expects)
engine = create_engine(
    "mysql+pymysql://root:---------@localhost/purchase_analysis_data"
)
'''------------------------------------this part ingest the new uploaded data-----------------------------------------'''
def ingest_db(df,table_name,engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name,con=engine, if_exists='replace',index=False)
    
def load_raw_data():
    '''this function will load the CSVs as dataframe and ingest into db'''
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time=(end-start)/60
    logging.info('-----------------Ingestion Complete-----------------')
    logging.info(f'\nTotal Time Taken: {total_time} minutes')
'''------------------------------------------------------------------------------------------------------'''

'''since we have already uploaded the data into the db and there is no other data right now we can perform operations'''
print("Connected to MySQL successfully")

# show all tables
tables_df = pd.read_sql("SHOW TABLES;", engine)
tables_df

vendor_df = pd.read_sql("SELECT * FROM vendor_master", engine)
material_df = pd.read_sql("SELECT * FROM material_master", engine)
section_df = pd.read_sql("SELECT * FROM section_master", engine)
order_df = pd.read_sql("SELECT * FROM purchase_orders", engine)
payment_df = pd.read_sql("SELECT * FROM purchase_payments", engine)
department_df = pd.read_sql("SELECT * FROM department_master", engine)
division_df = pd.read_sql("SELECT * FROM division_master", engine)
plant_df = pd.read_sql("SELECT * FROM plant_master", engine)
