from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    raw_data_path: str
    processed_data_path: str


@dataclass
class TransformationArtifacts:
    transformed_data_file_path: str