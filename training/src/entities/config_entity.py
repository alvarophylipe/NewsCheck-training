import os
from src.constants import *
from dataclasses import dataclass

@dataclass
class DataIngestionConfigs:
    DATA_URL: str = FAKE_TRUE_BR_URL
    DATA_INGESTION_ARTIFACTS_DIR: str = DATA_INGESTION_ARTIFACTS_DIR
    DATA_ARTIFACTS_DIR: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, ARTIFACTS_DIR)
    RAW_DATA_DIR: str = os.path.join(DATA_ARTIFACTS_DIR, RAW_DATA_DIR)
    PROCESSED_DATA_DIR: str = os.path.join(DATA_ARTIFACTS_DIR, PROCESSED_DATA_DIR)
    RAW_DATA_FILE: str = os.path.join(RAW_DATA_DIR, RAW_DATA_FILE)

@dataclass
class DataTransformationConfigs:
    LABEL: str = LABEL
    TEXT: str = TEXT
    INPLACE: bool = INPLACE
    TEST_SIZE: float = TEST_SIZE
    TEST_SIZE_2: float = TEST_SIZE_2
    TRAIN_FILE: str = TRAIN_FILE
    TEST_FILE: str = TEST_FILE
    EVAL_FILE: str = EVAL_FILE
    RANDOM_STATE: int = RANDOM_STATE
    RENAME_FAKE_COL: str = RENAME_FAKE_COL
    RENAME_TRUE_COL: str = RENAME_TRUE_COL
    FAKE: str = FAKE   
    TRUE: str = TRUE

@dataclass
class TokenizerConfigs:
    TOKENIZER_FROM_PRETRAINED: str = TOKENIZER_FROM_PRETRAINED
    DO_LOWER_CASE: str = DO_LOWER_CASE
    MAX_LEN: str = MAX_LEN
    PADDING: str = PADDING
    TRUNCATION: str = TRUNCATION
    TENSOR_TYPE: str = TENSOR_TYPE


@dataclass
class ModelTrainerConfigs:
    LABEL: str = LABEL
    TEXT: str = TEXT
    MODEL_SAVE_PATH: str = MODEL_SAVE_PATH
    MODEL_CHECKPOINT_PATH: str = MODEL_CHECKPOINT_PATH
    EPOCH: int = EPOCH
    EVALUATION_STRATEGY: str = EVALUATION_STRATEGY
    EVAL_STEPS: int = EVAL_STEPS
    PER_DEVICE_TRAIN_BATCH_SIZE: int = PER_DEVICE_TRAIN_BATCH_SIZE
    PER_DEVICE_EVAL_BATCH_SIZE: int = PER_DEVICE_EVAL_BATCH_SIZE
    LEARNING_RATE: float = LEARNING_RATE
    WEIGHT_DECAY: float = WEIGHT_DECAY
    NUM_TRAIN_EPOCHS: float = NUM_TRAIN_EPOCHS
    LOAD_THE_BEST_MODEL_AT_END: bool = LOAD_THE_BEST_MODEL_AT_END
    METRICS_FOR_BEST_MODEL: str = METRICS_FOR_BEST_MODEL
    SAVE_STEPS: int = SAVE_STEPS
    SAVE_STRATEGY: str = SAVE_STRATEGY
    SAVE_TOTAL_LIMIT: int = SAVE_TOTAL_LIMIT
    OVERWRITE_OUTPUT_DIR: bool = OVERWRITE_OUTPUT_DIR
    MODEL_FROM_PRETRAINED: str = MODEL_FROM_PRETRAINED
    NUM_LABELS: int = NUM_LABELS
    OUTPUT_ATTENTIONS: bool = OUTPUT_ATTENTIONS
    OUTPUT_HIDDEN_STATES: bool = OUTPUT_HIDDEN_STATES
    MAX_POSITION_EMBEDDINGS: int = MAX_POSITION_EMBEDDINGS
    HIDDEN_DROPOUT_PROB: float = HIDDEN_DROPOUT_PROB
    ARGS = ARGS
    MODEL_SAVE_PATH: str = MODEL_SAVE_PATH
    METRIC_SAVE_PATH: str = METRIC_SAVE_PATH
