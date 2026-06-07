import sys
import os
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.logger import logging 
from src.exception import HRmodel_Exception


@dataclass
class DataIngestionConfig:
    raw_data_path:str =os.path.join('Artifacts','raw_data.csv')
    train_data_path:str = os.path.join('Artifacts','train_data.csv')
    test_data_path:str = os.path.join('Artifacts','test_data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_path = DataIngestionConfig()
    def start_data_ingestion(self):
        try:
            logging.info('Data ingestion stareted....')
            
            os.makedirs(os.path.dirname(self.data_ingestion_path.train_data_path),exist_ok=True)
            df = pd.read_csv(os.path.join(os.getcwd(),'notebook','datasetV2','HR_Dataset.csv'))
            logging.info('Dataset loaded successfully')
            
            df.to_csv(path_or_buf=self.data_ingestion_path.raw_data_path,index=False,header=True)
            logging.info('Raw Data Send successfully')

            train_data,test_data = train_test_split(df,test_size=0.25,random_state=42)
            logging.info('Data Successfully Splitted into Train_set and Test_set')

            train_data.to_csv(path_or_buf= self.data_ingestion_path.train_data_path,index = False,header = True)
            test_data.to_csv(path_or_buf= self.data_ingestion_path.test_data_path,index = False,header = True)
            logging.info('Train Data and Test Data Successfully Splitted.....')

            return train_data,test_data

        except Exception as e:
            raise HRmodel_Exception(e,sys)

    

