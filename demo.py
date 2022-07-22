from cmath import pi
import logging
#from sklearn import pipeline
from storessales.pipeline import pipeline
from storessales.exeception import StoressalesExeception
from storessales.logger import logging
from storessales.config.configuration import Configuartion
import os

def main():
    try:
        pipeline1 = pipeline.pipeline()
        pipeline1.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == '__main__':
    main()
