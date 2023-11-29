import os

from datetime import datetime

# Commun constants
TIMESTAMP: str = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
LABEL: str = 'label'
CONTENT: str = 'content'
MODEL_NAME: str = 'model.h5'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR: str = 'data'
DATA_INGESTION_RAW_DATA: str = 'raw_data.csv'
DATA_INGESTION_PROCESSED_DATA: str = 'processed.csv'

# Data transformation constants
RAW_DATA_DIR: str = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'
INPLACE: bool = True
