import os
import re
import sys
import string
import nltk
import pandas as pd
import numpy as np
import spacy
from src.entities.config_entity import DataTransformationConfigs
from src.entities.artifact_entity import DataIngestionArtifacts

nlp = spacy.load('pt_core_news_md')

