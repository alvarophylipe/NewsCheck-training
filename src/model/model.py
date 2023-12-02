from src.constants import *
from src.entities.config_entity import ModelTrainerConfigs
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, SpatialDropout1D, \
GlobalMaxPooling1D, Embedding, Conv1D, BatchNormalization, Dropout

class ModelArchitecture:
    def __init__(self) -> None:
        pass


    def get_model() -> Sequential:
        model = Sequential()
        model.add(Embedding(MAX_WORDS, EMBEDDING_DIM, input_length=MAX_LEN))
        model.add(Conv1D(filters=64, kernel_size=3, padding='same', activation='relu'))
        model.add(SpatialDropout1D(0.2))
        model.add(Bidirectional(LSTM(100, return_sequences=True)))
        model.add(SpatialDropout1D(0.2))
        model.add(Bidirectional(LSTM(100, return_sequences=True)))
        model.add(GlobalMaxPooling1D())
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(BatchNormalization())
        model.add(Dense(1, activation=ACTIVATION))

        model.summary()
        model.compile(optimizer='adam', loss=LOSS, metrics=METRICS)

        return model
    