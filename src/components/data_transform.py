import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exceptions import CustomException 
from src.logger import logging
import os

@dataclass
class DataTransformConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransform:
    def __init__(self):
        self.data_transform_config = DataTransformConfig()

    def get_data_transformer_object(self): #this is reponsible for data transformation
        try: 
            numerical_columns = ['writing score', 'reading score']
            categorical_columns = [
                'gender', 
                'race/ethnicity', 
                'parental level of education', 
                'lunch', 
                'test preparation course'
            ]
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')), ##deals with missing values and replaces them with median
                ('scaler', StandardScaler())   # standardize the data
            ])
            
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),  # deals with missing values and replaces them with mode
                    ('onehotencoder', OneHotEncoder(handle_unknown='ignore')), # one-hot encoding
                    ('scaler', StandardScaler())
                ]
            )
            logging.info(f'Numerical columns:{numerical_columns}')
            logging.info(f'Categorical columns:{categorical_columns}')

            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns)

                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
            

def initiate_data_transformation(self,train_path,test_path):
    
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        logging.info('Read train and test data completed')
        logging.info('Obtaining Preprocessing object')


        preprocessing_obj = self.get_data_transformer_object()

        target_column_name = 'math score'
        numerical_columns = ['writing score', 'reading score']

    except:
        pass


