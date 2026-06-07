from src.exception  import HRmodel_Exception
from src.logger import logging
from src.utils import evaluate_model
from src.utils import save_obj

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier

from sklearn.model_selection import GridSearchCV
from dataclasses import dataclass

import sys
import os

@dataclass
class ModelTrainerConfig:
    model_path:str = os.path.join('Artifacts','model.pkl')

class ModelTrainer:
    def __init__(self) -> None:
        self.model_pathC = ModelTrainerConfig()
    
    def model_trainer(self,x_train,x_test,y_train,y_test):
        try:    
            models = {'Random_forest':RandomForestClassifier(),'XGB_classifier':XGBClassifier(),'CatBoost':CatBoostClassifier(),}

            params = {'Random_forest':{'n_estimators':[100,10,50,200],'criterion':['gini','entropy','log_loss'],'max_depth':[1,5,10],'min_samples_split':[2,4,8],'min_samples_leaf':[4,2,1,5]},
                    'XGB_classifier':{'learning_rate':[0.1,1,0.001,0.5],'max_depth':[1,2,3,4,6],'booster':['gbtree','gblinear','dart']},
                    'CatBoost':{}}
            trained_models = {}
            for model_name,model in models.items():
                gr_ = GridSearchCV(model,param_grid=params[model_name],scoring='accuracy',verbose=4)
                gr_.fit(x_train,y_train)
                trained_models[model_name] = model.set_params(**gr_.best_params_)
                trained_models[model_name].fit(x_train,y_train)
            logging.info('Model Training Done.............')   
            accu_model_hypertrained = evaluate_model(models=trained_models,X_test=x_test,y_test=y_test)
            save_obj(path=self.model_pathC.model_path,object=accu_model_hypertrained)
            logging.info('model_eval done')
            
        except Exception as e:
            raise HRmodel_Exception(e, sys)
        
