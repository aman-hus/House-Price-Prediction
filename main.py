from House_Price.components.data_ingestion import DataIngestion
from House_Price.components.data_validation import DataValidation
from House_Price.exception.exception import HousePricePredictionException
from House_Price.logging.logger import logging
from House_Price.entity.config_entity import DataIngestionConfig,DataValidationConfig
from House_Price.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestedartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiated completed")
        print(dataingestedartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestedartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validate()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        
        
    except Exception as e:
        raise HousePricePredictionException(e,sys)    