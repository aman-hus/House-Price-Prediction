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

SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")
"""
Data Ingested related constant start with DATA_INGESTED VAR NAME
"""

DATA_INGESTED_COLLECTION_NAME: str ="Housepricedata"
DATA_INGESTED_DATABASE_NAME: str = "AMANAI"
DATA_INGESTED_DIR_NAME: str = "data_ingested"
DATA_INGESTED_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTED_INGESTED_DIR: str ="ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATION: float = 0.2

"""
Data validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yml"