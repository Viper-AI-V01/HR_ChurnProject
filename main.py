from src.components import data_ingestion
from src.components import data_transformation
from src.components import model_trainer

def main():
    print("Hello from hr-project!")


if __name__ == "__main__":
   data_inges = data_ingestion.DataIngestion()
   train_data,test_data = data_inges.start_data_ingestion()
   data_pre = data_transformation.DataTransformer()
   train_data,test_data,y_train,y_testt = data_pre.preprocess_data(train_dat=train_data,test_dat=test_data)
   model_trainer.ModelTrainer().model_trainer(train_data,test_data,y_train=y_train,y_test=y_testt)
