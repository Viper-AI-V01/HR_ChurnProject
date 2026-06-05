from src.components import data_ingestion
def main():
    print("Hello from hr-project!")


if __name__ == "__main__":
   data_inges = data_ingestion.DataIngestion()
   train_data,test_data = data_inges.start_data_ingestion()
