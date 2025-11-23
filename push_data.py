import os
import sys
from dotenv import load_dotenv
load_dotenv()

import json

MONGO_DB_URL=os.getenv("MONGO_DB_url")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from House_Price.exception.exception import HousePricePredictionException
from House_Price.logging.logger import logging

class HousePriceExtraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise HousePricePredictionException(e,sys)
        
    def csv_to_json_convert(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise HousePricePredictionException(e,sys)   

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)    
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise HousePricePredictionException(e,sys)
        

if __name__=='__main__':
    FILE_PATH="House_Price_Data\house_price.csv"
    DATABASE="AMANAI"
    Collection="Housepricedata"
    housepriceobj=HousePriceExtraction()
    records=housepriceobj.csv_to_json_convert(file_path=FILE_PATH)
    print(records)
    no_of_records=housepriceobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)