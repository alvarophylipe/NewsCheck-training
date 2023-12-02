import os
import pandas as pd
import numpy as np
import joblib
import pickle
from typing import Tuple
from src.constants import *
from src.exception import exception
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from src.entities.artifact_entity import TransformationArtifacts, ModelTrainerArtifacts
from src.entities.config_entity import ModelTrainerConfigs
from src.model.model import ModelArchitecture

class ModelTrainer:
    def __init__(self, transformation_artifacts: TransformationArtifacts,
                 model_trainer_configs: ModelTrainerConfigs) -> None:
        
        self.transformation_artifacts = transformation_artifacts
        self.model_trainer_configs = model_trainer_configs

    @exception
    def split_data(self) -> Tuple:
        dataframe = pd.read_csv(self.transformation_artifacts.transformed_data_file_path, index_col=False)

        dataframe = dataframe.dropna()

        X = dataframe[CONTENT]
        Y = dataframe[LABEL]

        x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify=Y, test_size=0.25, 
                                                            random_state=RANDOM_STATE)
        
        print(x_train.shape, x_test.shape)
        print(y_train.shape, y_test.shape)

        return x_train, x_test, y_train, y_test

    
    @exception
    def data_tokenizer(self, x_train: np.ndarray | list) -> None:
        tokenizer = Tokenizer(num_words=self.model_trainer_configs.NUM_WORDS)
        tokenizer.fit_on_texts(x_train)
        sequences = tokenizer.texts_to_sequences(x_train)
        pad_seqs = pad_sequences(sequences, maxlen=self.model_trainer_configs.MAX_LEN)

        os.makedirs(self.model_trainer_configs.MODEL_SAVE_PATH, exist_ok=True)
        tokenizer_path = os.path.join(self.model_trainer_configs.MODEL_SAVE_PATH, 'tokenizer.pkl')
        
        joblib.dump(tokenizer, tokenizer_path, protocol=pickle.HIGHEST_PROTOCOL)

        return pad_seqs

    
    
    @exception
    def run_trainer(self) -> ModelTrainerArtifacts:
        
        x_train, x_test, y_train, y_test = self.split_data()
        model_architecture = ModelArchitecture

        model = model_architecture.get_model()

        sequences = self.data_tokenizer(x_train=x_train)

        model.fit(
            sequences, y_train,
            batch_size=self.model_trainer_configs.BATCH_SIZE,
            epochs=self.model_trainer_configs.EPOCH,
            validation_split=self.model_trainer_configs.VALIDATION_SPLIT
        )

        model.save(self.model_trainer_configs.MODEL_SAVE_PATH)

        dir_path_name = os.path.dirname(self.transformation_artifacts.transformed_data_file_path)

        x_train_path = os.path.join(dir_path_name, self.model_trainer_configs.X_TRAIN_FILE)
        y_train_path = os.path.join(dir_path_name, self.model_trainer_configs.Y_TRAIN_FILE)
        x_train.to_csv(x_train_path)
        y_train.to_csv(y_train_path)
        
        x_test_path = os.path.join(dir_path_name, self.model_trainer_configs.X_TEST_FILE)
        y_test_path = os.path.join(dir_path_name, self.model_trainer_configs.Y_TEST_FILE)
        x_test.to_csv(x_test_path)
        y_test.to_csv(y_test_path)

        model_trainer_artifacts = ModelTrainerArtifacts(
            model_saved_path=self.model_trainer_configs.MODEL_SAVE_PATH,
            x_test_file_path=x_test_path,
            y_test_file_path=y_test_path
        )

        return model_trainer_artifacts
        



    

