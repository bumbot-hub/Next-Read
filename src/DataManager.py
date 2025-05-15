import numpy as np
import pandas as pd

import src.utils as utils


class DataManager:
    def __init__(self):
        self._tags = self.organize_tags(utils.ASSOCATION_PATH, utils.TAGS_PATH)
        self._dataset = self.organize_dataset(utils.DATASET_PATH)
        self._user_data = self.organize_userset(utils.USER_DATA_PATH)

    def organize_tags(self, tag_names, user_tags):
        data = pd.read_csv(user_tags)
        merge_table = pd.read_csv(tag_names)

        avg_popularity = np.mean(merge_table['count'])

        merge_table = (
            merge_table[merge_table['count'] > avg_popularity]
            .rename(columns={'goodreads_book_id': 'book_id'})
            .drop(columns='count')
        )

        merge_table = merge_table.merge(data, on='tag_id', how='left')
        merged_tags = merge_table.groupby('book_id')['tag_name'].apply(list).reset_index()

        return merged_tags

    def organize_dataset(self, dataset_paths):
        data = pd.read_csv(dataset_paths)
        columns = ["book_id", "title", "original_title", "authors", "isbn", "average_rating",
                   "ratings_count", "work_ratings_count", "work_text_reviews_count"]
        data = data.loc[:, columns]

        dataset = data.merge(self._tags, on='book_id', how='left')
        return dataset

    def organize_userset(self, user_path):
        data = pd.read_csv(user_path)
        columns = ["Book Id", "Title", "Author", "Additional Authors", "ISBN", "My Rating", "Read Count"]
        data = data.loc[:, columns]

        # Clear dataset
        lower_cols = [col.lower().replace(' ', '_') for col in columns]
        mapping = dict(zip(columns, lower_cols))
        data.rename(columns=mapping, inplace=True)
        data['isbn'] = data['isbn'].str.replace(r'["=]', '', regex=True)
        data['additional_authors'] = data['additional_authors'].fillna('')
        data['author'] = data['author'] + ', ' + data['additional_authors']
        data.drop(columns=['additional_authors'], inplace=True)

        user_dataset = data.merge(self._tags, on='book_id', how='left')
        user_dataset['tag_name'] = user_dataset['tag_name'].fillna('')
        print(user_dataset)

        return user_dataset
