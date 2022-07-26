from storessales.config.configuration import Configuartion
from storessales.entity.config_entity import DataIngestionConfig

from storessales.component.data_injection import DataIngestion
import os, sys

from storessales.exeception import StoressalesExeception

from collections import namedtuple
from datetime import datetime
import uuid

from storessales.logger import logging
from storessales.exeception import  StoressalesExeception
from threading import Thread
from typing import List

from multiprocessing import Process
from storessales.entity.artifact_entity import DataIngestionArtifact

from storessales.entity.config_entity import DataIngestionConfig
from storessales.component.data_injection import DataIngestion
import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd






class pipeline:
    def __init__(self, config:Configuartion=Configuartion())-> None:
        try:
            self.config = config
        except Exception as e:
            raise StoressalesExeception(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:


        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:

            raise StoressalesExeception(e,sys) from e





    def start_data_validation(self):
        pass 

    def data_transformations(self):
        pass
    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass



    def run_pipeline(self):
        try:
            #data_ingestion
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            
            raise StoressalesExeception(e,sys) from e