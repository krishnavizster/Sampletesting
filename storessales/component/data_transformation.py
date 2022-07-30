from cgi import test
from sklearn import preprocessing
from storessales.exeception import HousingException
from storessales.logger import logging
from storessales.entity.config_entity import DataTransformationConfig 
from storessales.entity.artifact_entity import DataIngestionArtifact,\
DataValidationArtifact,DataTransformationArtifact
import sys,os
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
from storessales.constants import *
from storessales.util.util import read_yaml_file,save_object,save_numpy_array_data,load_data

#columns:

  #Item_Weight:float64
  #Item_Visibility:float64
  #Item_MRP:float64
  
#numerical_columns:

#Outlet_Establishment_Year:int64 

#categorical_columns:

#Item_Identifier:object 
#Item_Fat_Content:object
#Item_Type:object
#Item_Outlet_Sales
#Outlet_Identifier:object
#Outlet_Size:object 
#Outlet_Location_Type:object 
#Outlet_Type:object 
#stores:Category 

#target_column:   Item_Outlet_Sales:float64


class FeatureGenerator(BaseEstimator, TransformerMixin):

    def __init__(self, add_years_established=True, 
                 Item_Fat_Content=3,
                 Item_Type=5,
                 Outlet_Location_Type=6,
                 Outlet_Size =4, 
                 Outlet_Establishment_Year=1, 
                 Item_Visibility=1, 
                 Item_MRP=1,
                 Item_Outlet_Sales=1,
                 Outlet_Type=1,
                 columns=None):
        """
        FeatureGenerator Initialization
        
        """
        try:
            self.columns = columns
            if self.columns is not None:
                Item_Fat_Content = self.columns.index(COLUMN_ITEM_FAT_CONTENT)
                Item_Type= self.columns.index(COLUMN_ITEM_TYPE)
                Outlet_Location_Type = self.columns.index(COLUMN_OUTLETLOCATION_TYPE)
                Outlet_Size = self.columns.index(COLUMN_OUTLET_SIZE)
                Outlet_Establishment_Year=self.columns(COLUMN_ESTABLISHED_YEAR)
                Item_Visibility=self.columns(COLUMN_ITEM_VISIBILITY )
                Item_MRP=self.columns(COLUMN_ITEM_MRP)
                Item_Outlet_Sales=self.columns(COLUMN_ITEMOUTLET_SALES)
                Outlet_Type=self.columns(COLUMN_OUTLET_TYPE)


            self.add_years_established = add_years_established
            self.Item_Fat_Content  = Item_Fat_Content 
            self.Item_Type = Item_Type
            self.Outlet_Location_Type =  Outlet_Location_Type
            self. Outlet_Size = Outlet_Size
            self.Outlet_Establishment_Year=Outlet_Establishment_Year
            self.Item_Visibility=Item_Visibility
            self.Item_MRP= Item_MRP
            self.Item_Outlet_Sales=Item_Outlet_Sales
            self.Outlet_Type=Outlet_Type

        except Exception as e:
            raise StoressalesExeception(e, sys) from e

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        try:
           Item_Outlet_Sales= X[:, self. Item_Outlet_Sales] / \
                                 X[:, self.Item_Fat_Content
           Outlet_Location_Type= X[:, self.Outlet_Location_Type] / \
                                       X[:, self.Item_Type]
            if self.add_years_established:
                years_established = X[:, self.Item_Outlet_Sale] / \
                                    X[:, self.Outlet_Establishment_Year]
                generated_feature = np.c_[
                    X,Item_Outlet_Sales,Outlet_Location_Type,  years_established]
            else:
                generated_feature = np.c_[
                    X, Item_Outlet_Sales,  Outlet_Location_Type]

            return generated_feature
        except Exception as e:
            raise StoressalesExeception(e, sys) from e





class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact
                 ):
        try:
            logging.info(f"{'>>' * 30}Data Transformation log started.{'<<' * 30} ")
            self.data_transformation_config= data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact

        except Exception as e:
            raise StoressalesExeception(e,sys) from e

    

    def get_data_transformer_object(self)->ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path

            dataset_schema = read_yaml_file(file_path=schema_file_path)

            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]
            categorical_columns = dataset_schema[CATEGORICAL_COLUMN_KEY]


            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="median")),
                ('feature_generator', FeatureGenerator(
                    add_years_established=self.data_transformation_config.add_years_established,
                    columns=numerical_columns
                )),
                ('scaler', StandardScaler())
            ]
            )

            cat_pipeline = Pipeline(steps=[
                 ('impute', SimpleImputer(strategy="most_frequent")),
                 ('one_hot_encoder', OneHotEncoder()),
                 ('scaler', StandardScaler(with_mean=False))
            ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")


            preprocessing = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns),
            ])
            return preprocessing

        except Exception as e:
            raise StoressalesExeception(e,sys) from e   


    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info(f"Obtaining preprocessing object.")
            preprocessing_obj = self.get_data_transformer_object()


            logging.info(f"Obtaining training and test file path.")
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            

            schema_file_path = self.data_validation_artifact.schema_file_path
            
            logging.info(f"Loading training and test data as pandas dataframe.")
            train_df = load_data(file_path=train_file_path, schema_file_path=schema_file_path)
            
            test_df = load_data(file_path=test_file_path, schema_file_path=schema_file_path)

            schema = read_yaml_file(file_path=schema_file_path)

            target_column_name = schema[TARGET_COLUMN_KEY]


            logging.info(f"Splitting input and target feature from training and testing dataframe.")
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)


            train_arr = np.c_[ input_feature_train_arr, np.array(target_feature_train_df)]

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            transformed_train_dir = self.data_transformation_config.transformed_train_dir
            transformed_test_dir = self.data_transformation_config.transformed_test_dir

            train_file_name = os.path.basename(train_file_path).replace(".csv",".npz")
            test_file_name = os.path.basename(test_file_path).replace(".csv",".npz")

            transformed_train_file_path = os.path.join(transformed_train_dir, train_file_name)
            transformed_test_file_path = os.path.join(transformed_test_dir, test_file_name)

            logging.info(f"Saving transformed training and testing array.")
            
            save_numpy_array_data(file_path=transformed_train_file_path,array=train_arr)
            save_numpy_array_data(file_path=transformed_test_file_path,array=test_arr)

            preprocessing_obj_file_path = self.data_transformation_config.preprocessed_object_file_path

            logging.info(f"Saving preprocessing object.")
            save_object(file_path=preprocessing_obj_file_path,obj=preprocessing_obj)

            data_transformation_artifact = DataTransformationArtifact(is_transformed=True,
            message="Data transformation successfull.",
            transformed_train_file_path=transformed_train_file_path,
            transformed_test_file_path=transformed_test_file_path,
            preprocessed_object_file_path=preprocessing_obj_file_path

            )
            logging.info(f"Data transformationa artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise StoressalesExeception(e,sys) from e

    def __del__(self):
        logging.info(f"{'>>'*30}Data Transformation log completed.{'<<'*30} \n\n")