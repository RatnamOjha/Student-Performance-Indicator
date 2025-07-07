import logging
import os
import pandas as pd
import logging
# from src.logger import logging
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join("artifacts", "train.csv")
    test_data_path: str= os.path.join("artifacts","test.csv")
    raw_data_path: str= os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Load the dataset
            df = pd.read_csv('/Users/ratnamb.ojha/Downloads/StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")
            

        
        except:
            pass