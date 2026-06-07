import pickle
from src.exception import HRmodel_Exception
from src.logger import logging
import sys
import os

from sklearn.metrics import accuracy_score,precision_score,recall_score


def save_obj(path:str,object):
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path,exist_ok=True)
        with open(path,'wb') as file:
            pickle.dump(object,file=file)
    except Exception as e:
        raise HRmodel_Exception(e, sys)

def evaluate_model(models:dict,X_test,y_test):
    try:
        accu,prec,reca = {}, {}, {}
        model_accu = {}
        for i,j in models.items():
            y_pred = j.predict(X_test)
            accuracy = accuracy_score(y_test,y_pred)
            accu[i] = float(accuracy)
            model_accu[i] = j
            precision = precision_score(y_test,y_pred)
            prec[i] = float(precision)
            recall  = recall_score(y_test,y_pred)
            reca[i] = float(recall)
        logging.info('Model Evaluation Done -----------')
        acc_max  =max(accu, key =accu.get,default=None)#type: ignore
        prec_max =max(prec,key = prec.get,default=None)#type: ignore
        reca_max =max(reca,key = reca.get,default=None)#type: ignore
        logging.info(f'model_accu:{accu}\nmodel_prec:{prec}\nmodel_reca:{reca}')

        logging.info(f'max_acc_model:{acc_max}:{accu[acc_max]}\nmax_prec_model:{prec_max}:{prec[prec_max]}\nmax_reca_model:{reca_max}:{reca[reca_max]}')
        return (model_accu[acc_max])
    except Exception as e:
        raise HRmodel_Exception(e, sys)
    
def load_obj(path:str):
    try:
        with open(path,'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise HRmodel_Exception(e, sys)

        

    
