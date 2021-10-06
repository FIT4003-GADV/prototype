"""
Consists of the "Predict" stage to make predictions about the chart type of the input SVG vis.
"""
import os
import sys
from importlib import import_module  # Used to import from Beagle; hyphen not allowed in imports.
from typing import Any
from symbol_dict import symbol_dict

import joblib
from absl import logging
from bs4 import BeautifulSoup
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler

from stages.stage import Stage
from supported_chart_types import SupportedType

# Append the Beagle repo into sys.path to resolve internal imports.
if 'LAMBDA_TASK_ROOT' in os.environ:
    sys.path.append(f"{os.environ['LAMBDA_TASK_ROOT']}/beagle-annotator/svg_classifier")
else:
    sys.path.append('../beagle-annotator/svg_classifier')

d3_feature_extractor = import_module('beagle-annotator.svg_classifier.d3_feature_extractor')


class Predict(Stage):
    def __init__(self, svg: BeautifulSoup):
        super().__init__()
        if not svg:
            raise ValueError('No SVG provided to Predict stage.')
        self.svg = svg
        # Load the trained models and objects.
        self.std_scaler: StandardScaler = Predict.load_object(os.path.abspath('models/scaler_d3.pkl'))
        self.dict_vectorizer: DictVectorizer = Predict.load_object(os.path.abspath('models/vectorizer_d3.pkl'))
        self.clf: RandomForestClassifier = Predict.load_object(os.path.abspath('models/model_d3.pkl'))

    def do_stage(self, *args, **kwargs) -> SupportedType:
        """Runs the Beagle Annotator pre-trained model to make predictions about chart type."""
        logging.info('Predicting...')
        feature_dict = d3_feature_extractor.extract(None, self.svg)
        logging.debug(feature_dict)

        feature_array = self.std_scaler.transform(self.dict_vectorizer.transform(feature_dict))[0]
        logging.debug(feature_array)

        prediction = symbol_dict[self.clf.predict(feature_array.reshape(1, -1))[0]]
        logging.info(prediction)

        # Return a canned answer for now.
        return SupportedType.LINE

    @staticmethod
    def load_object(file_path: str) -> Any:
        """Reconstructs saved Python objects in pickles."""
        return joblib.load(file_path)
