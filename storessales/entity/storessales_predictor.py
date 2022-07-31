import os
import sys

from numpy import int64

from storessales.exeception import StoressalesExeception
from storessales.util.util import load_object

import pandas as pd


class StoressalesData:

    def __init__(self,
                 Item_Identifier : str,
                 Item_Weight : float,
                 Item_Fat_Content  : str,
                 Item_Visibility: float,
                 Item_Type : str,
                 Item_MRP: float,
                 Outlet_Identifier: str,
                 Outlet_Establishment_Year : int64,
                 Outlet_Size : str,
                 Outlet_Location_Type: str = None
                 Outlet_Type : str,
                 Item_Outlet_Sales :float,


                 ):
        try:
            self.Item_Identifier = Item_Identifier
            self.Item_Weight  = Item_Weight 
            self.Item_Fat_Content   = Item_Fat_Content  
            self.Item_Visibility = Item_Visibility
            self.Item_Type  = Item_Type 
            self.Item_MRP = Item_MRP
            self.Outlet_Identifier = Outlet_Identifier
            self.Outlet_Establishment_Year  = Outlet_Establishment_Year 
            self.Outlet_Size  = Outlet_Size 
            self.Outlet_Location_Type = Outlet_Location_Type
            self.Outlet_Type = OuOutlet_Type
            self.Item_Outlet_Sales = Item_Outlet_Sales


        except Exception as e:
            raise StoressalesExeception(e, sys) from e

#.......
#Item_Identifier               object
#Item_Weight                  float64
#Item_Fat_Content              object
#Item_Visibility              float64
#Item_Type                     object
#Item_MRP                     float64
#Outlet_Identifier             object
#Outlet_Establishment_Year      int64
#Outlet_Size                   object
#Outlet_Location_Type          object
#Outlet_Type                   object
#Item_Outlet_Sales            float64
#......


#..........
#columns:

  #Item_Weight:float64
  #Item_Visibility:float64
  #Item_MRP:float64
  
#numerical_columns:

#Outlet_Establishment_Year:int64 

#categorical_columns:

#Item_Identifier:object 
##Item_Fat_Content:object
#Item_Type:object
#Outlet_Identifier:object
#Outlet_Size:object 
#Outlet_Location_Type:object 
#Outlet_Type:object 
#stores:Category 

#target_column:   Item_Outlet_Sales:float64
#..........

    def get_storessales_input_data_frame(self):

        try:
            storessales_input_dict = self.get_storessales_data_as_dict()
            return pd.DataFrame(storessales_input_dict)
        except Exception as e:
            raise StoressalesExeception(e, sys) from e

    def get_storessales_data_as_dict(self):
        try:
            input_data = {
                "Item_Identifier": [self.Item_Identifier],
                "Item_Weight": [self.Item_Weight],
                "Item_Fat_Content": [self.Item_Fat_Content],
                "Item_Visibility": [self.Item_Visibility],
                "Item_Type": [self.Item_Type],
                "Item_MRP": [self.Item_MRP],
                "Outlet_Identifier": [self.Outlet_Identifier],
                "Outlet_Establishment_Year ": [self.Outlet_Establishment_Year ],
                "Outlet_Size": [self.Outlet_Size]
                "Outlet_Location_Type": [self.Outlet_Location_Type],
                "Outlet_Type": [self.Outlet_Type],
                "Item_Outlet_Sales": [self.Item_Outlet_Sales],



                
                }
            return input_data
        except Exception as e:
            raise StoressalesExeception(e, sys)


class  StoressalesPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise StoressalesExeception(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise StoressalesExeception(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_sales_value = model.predict(X)
            return   median_sales_value
        except Exception as e:
            raise StoressalesExeception(e, sys) from e