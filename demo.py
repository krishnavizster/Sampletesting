from cmath import pi
import logging
from sklearn import pipeline
from storessale.pipeline.pipeline import pipeline
from storessales.exeception import StoressalesExeception


def main():
    try:
        pipeline = pipeline
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        

if __name__ == '__main__':
    main()
