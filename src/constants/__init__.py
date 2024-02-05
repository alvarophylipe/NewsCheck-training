import os

from datetime import datetime
from typing import Dict, List

# Commun constants
TIMESTAMP: str = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
ARTIFACTS_DIR: str = os.path.join("artifacts_", TIMESTAMP)
LABEL: str = 'label'
TEXT: str = 'text'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.path.abspath('.'), 'data')
RAW_DATA_DIR: str = 'raw'
PROCESSED_DATA_DIR: str = 'processed'
RAW_DATA_FILE: str = 'raw_data.csv'
PROCESSED_DATA_FILE: str = 'processed_data.csv'

# Data transformation constants
INPLACE: bool = True
USECOLS: List[str] = ['label', 'text']

# Fake True Br Corpus constants
USECOLS_FAKETRUEBR: List[str] = ['fake', 'true']
MAP_LABEL_COL: Dict[str, int] = {'fake': 1, 'true': 0}
FAKE_TRUE_BR_URL: str = 'https://raw.githubusercontent.com/jpchav98/FakeTrue.Br/main/FakeTrueBr_corpus.csv'
RENAME_TRUE_COL: Dict[str, str] = {'true': TEXT}
RENAME_FAKE_COL: Dict[str, str] = {'fake': TEXT}
FAKE: str = 'fake'
TRUE: str = 'true'

# Splitting Constants
TEST_SIZE: float = 0.25
TEST_SIZE_2: float = 0.5
TRAIN_FILE: str = 'train.csv'
TEST_FILE: str = 'test.csv'
EVAL_FILE: str = 'eval.csv'
RANDOM_STATE: int = 42

# Tokenizer Constants 
TOKENIZER_FROM_PRETRAINED: str = 'neuralmind/bert-base-portuguese-cased'
DO_LOWER_CASE: bool = False

# Tokenization Parameters
MAX_LEN: int = 512
PADDING: str = 'max_length'
TRUNCATION: bool = True
TENSOR_TYPE: str = 'tf'
ADD_SPECIAL_TOKENS: bool = True
RETURN_TOKEN_TYPE_IDS: bool = True
RETURN_ATTENTION_MASK: bool = True


# Training Arguments Parameters
MODEL_CHECKPOINT_PATH: str = os.path.join(os.path.abspath('.'), 'serving', 'checkpoint')
EPOCH: int = 10
EVALUATION_STRATEGY: str = 'epoch'
EVAL_STEPS: int = 500
PER_DEVICE_TRAIN_BATCH_SIZE: int = 8
PER_DEVICE_EVAL_BATCH_SIZE: int = 8
LEARNING_RATE: float = 2.5e-5
WEIGHT_DECAY: float = 0.01
NUM_TRAIN_EPOCHS: float = 10.0
LOAD_THE_BEST_MODEL_AT_END: bool = True
METRICS_FOR_BEST_MODEL: str = 'accuracy'
SAVE_STEPS: int = 1000
SAVE_STRATEGY: str = 'epoch'
SAVE_TOTAL_LIMIT: int = 5
OVERWRITE_OUTPUT_DIR: bool = True


# Model Architecture constants
MODEL_FROM_PRETRAINED: str = 'neuralmind/bert-base-portuguese-cased'
NUM_LABELS: int = 2
OUTPUT_ATTENTIONS: bool = False
OUTPUT_HIDDEN_STATES: bool = False
MAX_POSITION_EMBEDDINGS: int = MAX_LEN
HIDDEN_DROPOUT_PROB: float = 0.5
ARGS: Dict[str, bool] = {
    'use_cached_eval_features': False,
    'no_cache': True,
    'reprocess_input_data': True
}
MODEL_SAVE_PATH = os.path.join(os.path.abspath('.'), 'serving', 'saved_model')
METRIC_SAVE_PATH = os.path.join(os.path.abspath('.'), 'metrics')