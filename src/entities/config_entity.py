import os
from src.constants import *
from dataclasses import dataclass

@dataclass
class DataIngestionConfigs:
    DATA_INGESTION_ARTIFACTS_DIR: str = DATA_INGESTION_ARTIFACTS_DIR
    DATA_ARTIFACTS_DIR: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, ARTIFACTS_DIR)
    RAW_DATA_DIR: str = os.path.join(DATA_ARTIFACTS_DIR, RAW_DATA_DIR)
    PROCESSED_DATA_DIR: str = os.path.join(DATA_ARTIFACTS_DIR, PROCESSED_DATA_DIR)
    

@dataclass
class DataTransformationConfigs:
    LABEL: str = LABEL
    INPLACE: bool =  INPLACE
    CONTENT: str = CONTENT
    USECOLS_FAKEBR = USECOLS_FAKEBR
    MAP_LABEL_COL = MAP_LABEL_COL
    USECOLS = USECOLS
    RENAME_COL = RENAME_COL