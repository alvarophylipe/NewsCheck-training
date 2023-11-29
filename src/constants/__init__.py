import os

from datetime import datetime

# Commun constants
TIMESTAMP: str = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
ARTIFACTS_DIR: str = os.path.join("artifacts_", TIMESTAMP)
LABEL: str = 'label'
CONTENT: str = 'content'
MODEL_NAME: str = 'model.h5'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR: str = 'data'
RAW_DATA_DIR: str = 'raw'
PROCESSED_DATA_DIR: str = 'processed'
DATA_INGESTION_PROCESSED_DATA_FILE: str = 'processed_data.csv'

# Data transformation constants
INPLACE: bool = True

# Fake Br Corpus constants
USECOLS_FAKEBR: str = ['label', 'preprocessed_news']
RENAME_LABEL_COL: dict = {'fake': 1, 'true': 0}
FAKE_BR_CORPUS_URL: str = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/preprocessed/pre-processed.csv'
