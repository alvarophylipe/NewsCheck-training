import os
import sys
sys.path.append(os.path.abspath('.'))
from src.pipeline.components.ingestion_component import DataIngestion
from src.pipeline.components.transformer_component import DataTransformation
from src.pipeline.components.trainer_component import ModelTrainer
from src.entities.config_entity import *
from src.entities.artifact_entity import *
from src.utils.tokenizer import encode

data_ingestion = DataIngestion(DataIngestionConfigs)
ingestion_artifacts = data_ingestion.run_data_ingestion()
transformation = DataTransformation(ingestion_artifacts, DataTransformationConfigs)
transformation_artifacts = transformation.run_transformation()
trainer = ModelTrainer(transformation_artifacts, ModelTrainerConfigs, encode)
trainer.run_trainer()