import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import numpy as np

from  dataclasses import dataclass



@dataclass
class DataELTConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataETL:
    def __init__(self):
        self.data_transformation_config=DataELTConfig()


