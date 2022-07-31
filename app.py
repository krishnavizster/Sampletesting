
from flask import Flask
import sys
import pip
from storessales.logger import logging
from storessales.exeception import StoressalesExeception
from matplotlib.style import context
from storessales.util.util import read_yaml_file, write_yaml_file
import os, sys
import json
from storessales.config.configuration import Configuartion
from storessales.constants import CONFIG_DIR, get_current_time_stamp
from storessales.pipeline.pipeline import Pipeline
from storessales.entity.storessales_predictor import HousingPredictor, HousingData
from flask import send_file, abort, render_template


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:

        storessales=StoressalesExeception(e,sys)


        logging.info(storessales.error_message)

        logging.info("first version storessales loggging message")
    return "CI CD pipeline has been established for store sales predection"

if __name__ == "__main__":
    app.run(debug=True)
