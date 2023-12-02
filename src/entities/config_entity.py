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


@dataclass
class ModelTrainerConfigs:
    X_TRAIN_FILE: str = X_TRAIN_FILE
    Y_TRAIN_FILE: str = Y_TRAIN_FILE
    X_TEST_FILE: str = X_TEST_FILE
    Y_TEST_FILE: str = Y_TEST_FILE
    NUM_WORDS: int = MAX_WORDS
    MAX_LEN: int = MAX_LEN
    MODEL_SAVE_PATH: str = MODEL_SAVE_PATH
    RANDOM_STATE: str = RANDOM_STATE
    EPOCH: str = EPOCH
    BATCH_SIZE: str = BATCH_SIZE
    VALIDATION_SPLIT: str = VALIDATION_SPLIT
