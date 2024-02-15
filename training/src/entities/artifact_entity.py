from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    raw_data_file: str
    processed_data_dir: str


@dataclass
class TransformationArtifacts:
    train_file: str
    test_file: str
    eval_file: str


@dataclass
class ModelTrainerArtifacts:
    model_saved_path: str