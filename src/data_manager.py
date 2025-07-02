import numpy as np
import os
import pandas as pd

from src.preprocessor import Preprocessor


class DataManager:
    def __init__(
        self, books_path, book_tags_path, tags_path, user_data_path, dataset_path
    ):
        self._books_path = books_path
        self._book_tags_path = book_tags_path
        self._tags_path = tags_path
        self._user_data_path = user_data_path
        self._dataset_path = dataset_path

        self._dataset = None
        self._user_dataset = None

        self._prepared_tags = self._prepare_tags()

        self._preprocessor = Preprocessor()

    def get_book_dataset(self):
        if self._dataset is None:
            if not os.path.exists(self._dataset_path):
                self._dataset = self._create_book_dataset()
            else:
                self._dataset = pd.read_csv(self._dataset_path)

        return self._dataset.copy()

    def get_user_dataset(self):
        if self._user_dataset is None:
            if not os.path.exists(self._user_data_path):
                return None
            else:
                self._user_dataset = self._create_user_dataset()

        return self._user_dataset.copy()

    def _create_book_dataset(self):
        data = pd.read_csv(self._books_path)
        columns = [
            "book_id",
            "title",
            "original_title",
            "authors",
            "isbn",
            "average_rating",
            "ratings_count",
            "work_ratings_count",
            "work_text_reviews_count",
        ]
        data = data.loc[:, columns]

        dataset = data.merge(self._prepared_tags, on="book_id", how="left")

        return dataset

    def _create_user_dataset(self):
        data = pd.read_csv(self._user_data_path)
        columns = [
            "Book Id",
            "Title",
            "Author",
            "Additional Authors",
            "ISBN",
            "My Rating",
            "Read Count",
        ]
        data = data.loc[:, columns]

        # Modifying to consistent dataset
        lower_cols = [col.lower().replace(" ", "_") for col in columns]
        mapping = dict(zip(columns, lower_cols))
        data.rename(columns=mapping, inplace=True)

        # Merge two author columns into one
        data["additional_authors"] = data["additional_authors"].fillna("")
        data["author"] = data["author"] + ", " + data["additional_authors"]
        data.drop(columns=["additional_authors"], inplace=True)

        dataset = data.merge(self._prepared_tags, on="book_id", how="left")

        return dataset

    def _prepare_tags(self):
        tags = pd.read_csv(self._tags_path)
        book_tags = pd.read_csv(self._book_tags_path)

        avg_popularity = np.mean(book_tags["count"])

        book_tags = (
            book_tags[book_tags["count"] > avg_popularity]
            .rename(columns={"goodreads_book_id": "book_id"})
            .drop(columns="count")
        )

        book_tags = book_tags.merge(tags, on="tag_id", how="left")
        merged_data = book_tags.groupby("book_id")["tag_name"].apply(list).reset_index()

        return merged_data
