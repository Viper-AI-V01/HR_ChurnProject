import os
import sys

from src.exception import HRmodel_Exception
from src.logger import logging
from src.utils import save_obj

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder

from dataclasses import dataclass


@dataclass
class DataTransformerConfig:
    preprocessing_path = os.path.join('Artifacts','preprocessing.pkl')

class DataTransformer:
    def __init__(self):
        self.data_preprocessing_path = DataTransformerConfig()
    
    def preprocess_data(self,test_dat,train_dat):

        try:
            test_data = test_dat
            train_data = train_dat
            num = [item for item in train_data.columns if train_data[item].dtype != 'str' and item!='left']
            cat = [item for item in train_data.columns if train_data[item].dtype =='str']
            logging.info('num and cat columns splitted')
            
            Ord_cat = ['low','medium','high']

            pipeline_ohe = Pipeline(steps=[
                ('Ordinal_Encoder',OrdinalEncoder(categories=[Ord_cat],handle_unknown='use_encoded_value',unknown_value=-1)),
                ('MixMaxScaler',MinMaxScaler())
                ])
            pipeline_cat = ColumnTransformer(transformers=[
                ('Salary',pipeline_ohe,['salary']),
                ('Department_cols',OneHotEncoder(drop='first',sparse_output=False),['Departments '])
            ],remainder='passthrough')
            preprocesser = ColumnTransformer(transformers=[
                        ('Category',pipeline_cat,cat),('Numeric',MinMaxScaler(),num)],
                        remainder='passthrough')           
            logging.info('Preprocessor_Created........')

            y = train_data['left']
            train_data  = train_data.drop('left',axis =1)
            y_test = test_data['left']
            test_data = test_data.drop('left',axis =1)

            preprocesser.set_output(transform='pandas')

            train_data = preprocesser.fit_transform(train_data)
            logging.info('Training Data Fit & Transformed')
            test_data = preprocesser.transform(test_data)
            logging.info('Testing Data Transformed')

            save_obj(path=self.data_preprocessing_path.preprocessing_path,object=preprocesser)
            logging.info('Preprocessor Saved')
            logging.info('DataPreprocessed')
            return train_data,test_data,y,y_test

        except Exception as e:
            raise HRmodel_Exception(e,sys)



