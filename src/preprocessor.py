import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

class Preprocessor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.scaler = StandardScaler()
        self.numeric_cols = ['average_rating', 'rating_counts']

    def fit(self, data):

        return None

    def transform_data(self, data):
        cleaned_data = self._clean_data(data.copy())

        return cleaned_data

    def _clean_data(self, data):
        data["isbn"] = data["isbn"].astype(str).str.replace(r'["=]', "", regex=True)
        data["tag_name"] = data["tag_name"].fillna('')

        return data