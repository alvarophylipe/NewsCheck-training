import os
import sys
import shutil
from typing import Optional, Tuple
from src.entities.decorator import exception
from src.entities.artifact_entity import DataIngestionArtifacts
from src.entities.config_entity import DataIngestionConfigs

class DataIngestion:
    def __init__(self, data_ingestion_configs: DataIngestionConfigs) -> None:
        self.data_ingestion_configs = data_ingestion_configs
    

    @exception
    def move_data(self) -> Tuple[str, str]:

        os.makedirs(self.data_ingestion_configs.PROCESSED_DATA_DIR, exist_ok=True)
        os.makedirs(self.data_ingestion_configs.RAW_DATA_DIR, exist_ok=True)
        
        raw_data_path = 'D:\\Inspector\\raw_data'

        if os.path.exists(raw_data_path):

            for file in os.listdir(raw_data_path):
                file_path = os.path.join(raw_data_path, file)
                target_path = os.path.join(self.data_ingestion_configs.RAW_DATA_DIR, file)
                shutil.copy(file_path, target_path)
            
            shutil.rmtree(raw_data_path)
        
        return self.data_ingestion_configs.RAW_DATA_DIR, self.data_ingestion_configs.PROCESSED_DATA_DIR



    @exception
    def run_data_ingestion(self) -> DataIngestionArtifacts:
        
        raw_data_dir, processed_data_dir = self.move_data()

        return DataIngestionArtifacts(
            raw_data_path=raw_data_dir,
            processed_data_path=processed_data_dir)
