import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.exception import exception
from src.entities.config_entity import DataTransformationConfigs
from src.entities.artifact_entity import DataIngestionArtifacts, TransformationArtifacts


class DataTransformation:
    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts, 
                 transformation_configs: DataTransformationConfigs) -> None:
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.transformation_configs = transformation_configs
    
    
    @staticmethod
    def run_text_cleaning(text: str) -> str:
        doc = text.lower() # normalize text
        doc = ' '.join([word for word in doc.split() if word != ' '])

        return doc


    @exception
    def _process_train_data(self) -> str:

        raw_data_file = self.data_ingestion_artifacts.raw_data_file
        processed_data_dir = self.data_ingestion_artifacts.processed_data_path

        dataframe = pd.read_csv(raw_data_file)

        dataframe[self.transformation_configs.FAKE] = dataframe[self.transformation_configs.FAKE] \
            .apply(lambda x: DataTransformation.run_text_cleaning(x))
        dataframe[self.transformation_configs.TRUE] = dataframe[self.transformation_configs.TRUE] \
            .apply(lambda x: DataTransformation.run_text_cleaning(x))

        df_true = dataframe[[self.transformation_configs.TRUE]]
        df_fake = dataframe[[self.transformation_configs.FAKE]]
        df_true.rename(columns=self.transformation_configs.RENAME_TRUE_COL, inplace=self.transformation_configs.INPLACE)
        df_fake.rename(columns=self.transformation_configs.RENAME_FAKE_COL, inplace=self.transformation_configs.INPLACE)
        df_true[self.transformation_configs.LABEL] = [0 for _ in range(df_true.shape[0])]
        df_fake[self.transformation_configs.LABEL] = [1 for _ in range(df_fake.shape[0])]
        
        concat_dataframe = pd.concat([df_true, df_fake])

        train_file = os.path.join(processed_data_dir, self.transformation_configs.TRAIN_FILE)
        test_file = os.path.join(processed_data_dir, self.transformation_configs.TEST_FILE)
        eval_file = os.path.join(processed_data_dir, self.transformation_configs.EVAL_FILE)

        df_train, df_temp = train_test_split(concat_dataframe, 
            stratify=concat_dataframe[self.transformation_configs.LABEL],
            test_size=self.transformation_configs.TEST_SIZE,
            random_state=self.transformation_configs.RANDOM_STATE,
            shuffle=True)
        
        df_test, df_eval = train_test_split(
            df_temp,
            stratify=df_temp[self.transformation_configs.TEXT],
            test_size=self.transformation_configs.TEST_SIZE_2,
            random_state=self.transformation_configs.RANDOM_STATE
        )

        df_train.to_csv(train_file, index=False)
        df_test.to_csv(test_file, index=False)
        df_eval.to_csv(eval_file, index=False)
    

        return train_file, test_file, eval_file


    @exception
    def run_transformation(self) -> TransformationArtifacts:

        train_file, test_file, eval_file = self._process_train_data()
        
        transformation_artifacts = TransformationArtifacts(
            train_file=train_file,
            test_file=test_file,
            eval_file=eval_file
        )

        return transformation_artifacts




