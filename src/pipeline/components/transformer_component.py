import os
import re
import sys
import string
import pandas as pd
import numpy as np
import spacy
from unidecode import unidecode
from src.exception import exception
from src.entities.config_entity import DataTransformationConfigs
from src.entities.artifact_entity import DataIngestionArtifacts, TransformationArtifacts

nlp = spacy.load('pt_core_news_md')

class DataTransformation:
    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts, 
                 transformation_configs: DataTransformationConfigs) -> None:
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.transformation_configs = transformation_configs
    
    
    def run_text_cleaning(self, text: str) -> str:
        doc = text.lower() # normalize text 
        doc = unidecode(doc) # remove accentuation
        doc = [word for word in doc if len(word) < 19 and len(word) > 1] # remove word more than 19 chars
        doc = ' '.join(doc)
        doc = re.sub(r'[^\w\s]', '', doc) # remove punctuation
        doc = nlp(doc) # tokenization
        doc = [token.text for token in doc if not token.is_stop] # remove stopwords
        doc = ' '.join(doc)
        doc = nlp(doc) # tokenization
        doc = [token.lemma_ for token in doc] # transforming in lemma format
        doc = ' '.join(doc) # normalize text

        return doc


    @exception
    def _read_csv_data(self, filepath: str, filename: str) -> pd.DataFrame:
        if filename == 'fake_br_corpus.csv':
            data = pd.read_csv(filepath, usecols=self.transformation_configs.USECOLS_FAKEBR)
            data.rename(columns=self.transformation_configs.RENAME_COL, 
                        inplace=self.transformation_configs.INPLACE)
            data['label'] = data['label'].map(self.transformation_configs.MAP_LABEL_COL)
            data['content'] = data['content'].apply(lambda x: self.run_text_cleaning(x))
            return data
        
        data = pd.read_csv(filepath, usecols=self.transformation_configs.USECOLS)
        data['content'].apply(lambda x: self.run_text_cleaning(x))
        return data


    @exception
    def _process_train_data(self) -> str:

        raw_data_dir = self.data_ingestion_artifacts.raw_data_path
        processed_data_dir = self.data_ingestion_artifacts.processed_data_path

        raw_data_file_paths = [
            (os.path.join(raw_data_dir, filename), filename) 
            for filename in os.listdir(raw_data_dir)
        ]

        dataframes = []

        for file, name in raw_data_file_paths:
            dataframes.append(self._read_csv_data(file, name))
        
        processed_data_file = os.path.join(processed_data_dir, 'processed.csv')

        concat_dataframe = pd.concat(dataframes)
        concat_dataframe.to_csv(processed_data_file, index=False)

        return processed_data_file


    @exception
    def run_transformation(self) -> TransformationArtifacts:

        processed_data_file = self._process_train_data()
        
        transformation_artifacts = TransformationArtifacts(
            transformed_data_file_path= processed_data_file
        )

        return transformation_artifacts




