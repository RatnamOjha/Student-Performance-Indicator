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

    def get_data_transformer_object(self):
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
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehotencoder', OneHotEncoder(handle_unknown='ignore'))
                ]
            )
        
        except:
            pass




