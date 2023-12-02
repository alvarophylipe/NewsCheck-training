from src.constants import *
from src.entities.config_entity import ModelTrainerConfigs
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, SpatialDropout1D, AveragePooling1D, Embedding

class ModelArchitecture:
    def __init__(self) -> None:
        pass


    def get_model() -> Sequential:
        model = Sequential()
        model.add(Embedding(MAX_WORDS, EMBEDDING_DIM, input_length=MAX_LEN))
        model.add(SpatialDropout1D(0.2))
        model.add(Bidirectional(LSTM(100, return_sequences=True)))
        model.add(SpatialDropout1D(0.2))
        model.add(AveragePooling1D(pool_size=2))
        model.add(Dense(1, activation=ACTIVATION))

        model.summary()
        model.compile(optimizer='adam', loss=LOSS, metrics=METRICS)

        return model