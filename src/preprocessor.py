import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack, csr_matrix


class Preprocessor:
    def __init__(self):
        # self.vectorizer = TfidfVectorizer()
        self.scaler = StandardScaler()
        self.numeric_cols = ["average_rating", "rating_counts"]

    def fit(self, data):
        numeric_data = data.copy()
        numeric_data = numeric_data[self.numeric_cols].fillna(0)
        self.scaler.fit(numeric_data)

        return self

    def transform(self, data):
        cleaned_data = self._clean_data(data.copy())
        normalized = self._normalize_data(cleaned_data)
        combined_features = hstack([csr_matrix(normalized)])

        return combined_features

    def _clean_data(self, data):
        data["isbn"] = data["isbn"].astype(str).str.replace(r'["=]', "", regex=True)
        data["tag_name"] = data["tag_name"].fillna("")

        for col in self.numeric_cols:
            if col not in data:
                data[col] = 0

            data[col] = data[col].fillna(0)

        return data

    def _normalize_data(self, data):
        numeric_data = data[self.numeric_cols].fillna(0)
        return self.scaler.transform(numeric_data)
