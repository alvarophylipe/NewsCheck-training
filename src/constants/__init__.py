import os

from datetime import datetime

# Commun constants
TIMESTAMP: str = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
ARTIFACTS_DIR: str = os.path.join("artifacts_", TIMESTAMP)
LABEL: str = 'label'
CONTENT: str = 'content'
MODEL_NAME: str = 'model.h5'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.path.abspath('.'), 'data')
RAW_DATA_DIR: str = 'raw'
PROCESSED_DATA_DIR: str = 'processed'
DATA_INGESTION_PROCESSED_DATA_FILE: str = 'processed_data.csv'

# Data transformation constants
INPLACE: bool = True
USECOLS: list = ['label', 'content']

# Fake Br Corpus constants
USECOLS_FAKEBR: list = ['label', 'preprocessed_news']
MAP_LABEL_COL: dict = {'fake': 1, 'true': 0}
FAKE_BR_CORPUS_URL: str = 'https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/preprocessed/pre-processed.csv'
RENAME_COL = {'preprocessed_news': 'content'}

# Model Trainer Constants
X_TRAIN_FILE: str = 'x_train.csv'
Y_TRAIN_FILE: str = 'y_train.csv'
X_TEST_FILE: str = 'x_test.csv'
Y_TEST_FILE: str = 'y_test.csv'
MODEL_SAVE_PATH: str = os.path.join(os.path.abspath('.'), 'serving', 'saved_model')
RANDOM_STATE: int = 42
EPOCH: int = 5
BATCH_SIZE: int = 64
VALIDATION_SPLIT: float = 0.2

# Model Architecture constants
MAX_WORDS: int = 60000
MAX_LEN: int = 1500
LOSS: str = 'binary_crossentropy'
METRICS: list = ['accuracy']
ACTIVATION: str = 'sigmoid'
EMBEDDING_DIM: int = 100