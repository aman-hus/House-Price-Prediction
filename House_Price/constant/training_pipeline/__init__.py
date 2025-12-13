import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""

TARGET_COLUMN="price"
PIPELINE_NAME: str = "House_Price"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "house_price.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
"""
Data Ingested related constant start with DATA_INGESTED VAR NAME
"""

DATA_INGESTED_COLLECTION_NAME: str ="Housepricedata"
DATA_INGESTED_DATABASE_NAME: str = "AMANAI"
DATA_INGESTED_DIR_NAME: str = "data_ingested"
DATA_INGESTED_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTED_INGESTED_DIR: str ="ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATION: float = 0.2