import os
import pandas as pd
import numpy as np
import json
from typing import Dict, List, Callable
import tensorflow as tf
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score
from src.utils.tokenizer import encode
from src.exception import exception
from src.entities.artifact_entity import TransformationArtifacts, ModelTrainerArtifacts
from src.entities.config_entity import ModelTrainerConfigs
from transformers import TFBertForSequenceClassification, \
TFTrainingArguments, TFTrainer, BertConfig

class ModelTrainer:
    def __init__(self, transformation_artifacts: TransformationArtifacts,
                 model_trainer_configs: ModelTrainerConfigs,
                 tokenizer: Callable[[List[str]], Dict[str, tf.Tensor]]) -> None:
        
        self.transformation_artifacts = transformation_artifacts
        self.model_trainer_configs = model_trainer_configs
        self.tokenizer = tokenizer
        self.model = None


    @exception
    def _load_data_and_create_datasets(self):

        train_ds = pd.read_csv(self.transformation_artifacts.train_file)
        test_ds = pd.read_csv(self.transformation_artifacts.test_file)
        eval_ds = pd.read_csv(self.transformation_artifacts.eval_file)

        train_text = train_ds[self.model_trainer_configs.TEXT].tolist()
        test_text = test_ds[self.model_trainer_configs.TEXT].tolist()
        eval_text = eval_ds[self.model_trainer_configs.TEXT].tolist()

        train_text = encode(train_text)
        test_text = encode(test_text)
        eval_text = encode(eval_text)

        train_label = train_ds[self.model_trainer_configs.LABEL].tolist()
        test_label = test_ds[self.model_trainer_configs.LABEL].tolist()
        eval_label = eval_ds[self.model_trainer_configs.LABEL].tolist()

        train = tf.data.Dataset.from_tensor_slices((train_text, train_label))
        test = tf.data.Dataset.from_tensor_slices((test_text, test_label))
        eval = tf.data.Dataset.from_tensor_slices((eval_text, eval_label))

        return train, test, eval


    def _compute_metrics(self, preds):
        predictions, labels = preds
        predictions = np.argmax(predictions, axis=-1)
        return {
            'accuracy': accuracy_score(labels, predictions),
            'f1_score': f1_score(labels, predictions, average='weighted'),
            'roc_auc_score': roc_auc_score(labels, predictions)
        }

    @exception
    def _load_training_args(self) -> TFTrainingArguments:
        return TFTrainingArguments(
            output_dir=self.model_trainer_configs.MODEL_CHECKPOINT_PATH,
            overwrite_output_dir=self.model_trainer_configs.OVERWRITE_OUTPUT_DIR,
            evaluation_strategy=self.model_trainer_configs.EVALUATION_STRATEGY,
            eval_steps=self.model_trainer_configs.EVAL_STEPS,
            per_device_train_batch_size=self.model_trainer_configs.PER_DEVICE_TRAIN_BATCH_SIZE,
            per_device_eval_batch_size=self.model_trainer_configs.PER_DEVICE_EVAL_BATCH_SIZE,
            learning_rate=self.model_trainer_configs.LEARNING_RATE,
            weight_decay=self.model_trainer_configs.WEIGHT_DECAY,
            num_train_epochs=self.model_trainer_configs.NUM_TRAIN_EPOCHS,
            load_best_model_at_end=self.model_trainer_configs.LOAD_THE_BEST_MODEL_AT_END,
            metric_for_best_model=self.model_trainer_configs.METRICS_FOR_BEST_MODEL,
            save_strategy=self.model_trainer_configs.SAVE_STRATEGY,
            save_steps=self.model_trainer_configs.SAVE_STEPS,
            save_total_limit=self.model_trainer_configs.SAVE_TOTAL_LIMIT
        )
    
    @exception
    def _load_tftrainer(self, train, eval) -> TFTrainer:

        training_args = self._load_training_args()

        with training_args.strategy.scope():
            config = BertConfig.from_pretrained(
                self.model_trainer_configs.MODEL_FROM_PRETRAINED,
                num_labels=self.model_trainer_configs.NUM_LABELS,
                output_attentions=self.model_trainer_configs.OUTPUT_ATTENTIONS,
                output_hidden_states=self.model_trainer_configs.OUTPUT_HIDDEN_STATES,
                max_position_embeddings=self.model_trainer_configs.MAX_POSITION_EMBEDDINGS,
                hidden_dropout_prob=self.model_trainer_configs.HIDDEN_DROPOUT_PROB,
                args=self.model_trainer_configs.ARGS
            )

            self.model = TFBertForSequenceClassification.from_config(config)

        return TFTrainer(
            model=self.model,
            args=training_args,
            train_dataset=train,
            eval_dataset=eval,
            compute_metrics=self._compute_metrics)
    
    @exception
    def _save_model(self):
        self.model.save_pretrained(self.model_trainer_configs.MODEL_SAVE_PATH)
    
    @exception
    def run_trainer(self) -> ModelTrainerArtifacts:

        if 'tf_model.h5' in os.listdir(self.model_trainer_configs.MODEL_SAVE_PATH):
            return ModelTrainerArtifacts(
                model_saved_path=self.model_trainer_configs.MODEL_SAVE_PATH
                )

        train, test, eval = self._load_data_and_create_datasets()

        trainer = self._load_tftrainer(train, eval)

        trainer.train()

        self._save_model()

        train_metrics = trainer.evaluate(train)
        test_metrics = trainer.evaluate(test)
        eval_metrics = trainer.evaluate(eval)

        metrics = {
            'train': train_metrics,
            'test': test_metrics,
            'eval': eval_metrics
        }

        with open(
            self.model_trainer_configs.METRIC_SAVE_PATH + '/metrics.json'
            ) as file:
            json.dump(metrics, file)
        
        return ModelTrainerArtifacts(
            model_saved_path=self.model_trainer_configs.MODEL_SAVE_PATH
        )






        



    

