import os
import sys
import shutil
import pandas as pd
from typing import Optional, Tuple
from src.exception import exception
from src.entities.artifact_entity import DataIngestionArtifacts
from src.entities.config_entity import DataIngestionConfigs

class DataIngestion:
    def __init__(self, data_ingestion_configs: DataIngestionConfigs) -> None:
        self.data_ingestion_configs = data_ingestion_configs
    

    @exception
    def _move_data(self) -> Tuple[str, str]:

        os.makedirs(self.data_ingestion_configs.PROCESSED_DATA_DIR, exist_ok=True)
        os.makedirs(self.data_ingestion_configs.RAW_DATA_DIR, exist_ok=True)
        
        dataframe = pd.read_csv(self.data_ingestion_configs.DATA_URL)
        dataframe.to_csv(self.data_ingestion_configs.RAW_DATA_FILE)
        
        return self.data_ingestion_configs.RAW_DATA_FILE, self.data_ingestion_configs.PROCESSED_DATA_DIR



    @exception
    def run_data_ingestion(self) -> DataIngestionArtifacts:
        
        raw_data_file, processed_data_dir = self._move_data()

        return DataIngestionArtifacts(
            raw_data_file=raw_data_file,
            processed_data_path=processed_data_dir)
