from storessales.pipeline.pipeline import Pipeline
from storessales.exeception import StoressalesExeception
from storessales.logger import logging
from storessales.config.configuration import Configuartion
from storessales.component.data_transformation import DataTransformation
from storessales.exeception import HousingException
import os



def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")  


    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == '__main__':
    main()
