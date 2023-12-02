import sys
sys.path.append('/inspector')
from src.pipeline.components.ingestion_component import DataIngestion
from src.pipeline.components.transformer_component import DataTransformation
from src.pipeline.components.trainer_component import ModelTrainer
from src.entities.config_entity import *
from src.entities.artifact_entity import *

data_ingestion = DataIngestion(DataIngestionConfigs)
ingestion_artifacts = data_ingestion.run_data_ingestion()
transformation = DataTransformation(ingestion_artifacts, DataTransformationConfigs)
transformation_artifacts = transformation.run_transformation()
trainer = ModelTrainer(transformation_artifacts, ModelTrainerConfigs)
trainer.run_trainer()