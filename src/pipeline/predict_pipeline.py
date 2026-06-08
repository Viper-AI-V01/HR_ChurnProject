from src.utils import load_obj
from src.exception import HRmodel_Exception
from src.logger import logging
import os
import sys
import pandas as pd

class Predicted:
    def __init__(self) -> None:
        pass 
    def predict(self,data):
        try:
            model = load_obj(path=os.path.join('Artifacts','model.pkl'))
            preprocessor_obj = load_obj(path=os.path.join('Artifacts','preprocessing.pkl'))
            data_scaled = preprocessor_obj.transform(data)
            predicted_= model.predict(data_scaled)
            return predicted_
        except Exception as e:
            raise HRmodel_Exception(e, sys)

class GetData:
    def __init__(self,satisfaction_level,last_evaluation,number_project,average_montly_hours,
                 time_spend_company,Work_accident,promotion_last_5years,Departments,salary) -> None:
        self.Satisfaction_level:float = satisfaction_level
        self.last_evaluation:float = last_evaluation
        self.number_project:int = number_project
        self.average_montly_hours:int = average_montly_hours
        self.time_spend_company:int = time_spend_company
        self.Work_accident:int = Work_accident
        self.promotion:int = promotion_last_5years
        self.Departments:str = Departments
        self.salary:str = salary
    def get_dataFrame(self):
        try:
            predicted_dataFrame = {'satisfaction_level':self.Satisfaction_level,
                                'last_evaluation':self.last_evaluation,
                                'number_project':self.number_project,
                                'average_montly_hours':self.average_montly_hours,
                                'time_spend_company':self.time_spend_company,
                                'Work_accident':self.Work_accident,
                                'promotion_last_5years':self.promotion,
                                'Departments ':self.Departments,
                                'salary':self.salary
                                }
            logging.info('Data coverted to Pd DataFrame')
            return pd.DataFrame(predicted_dataFrame,index=[0])
        except Exception as e:
            raise HRmodel_Exception(e, sys)

    
    
    
        