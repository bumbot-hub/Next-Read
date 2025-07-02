from src.data_manager import DataManager
from src.preprocessor import Preprocessor
from src.recommender import Recomedner

import src.utils as utils


def main():
    data_manager = DataManager(
        books_path=utils.BOOKS_PATH,
        book_tags_path=utils.BOOK_TAGS_PATH,
        tags_path=utils.TAGS_PATH,
        user_data_path=utils.USER_DATA_PATH,
        dataset_path=utils.DATASET_PATH,
    )
    preprocessor = Preprocessor()

    b_dataset = data_manager.get_book_dataset()
    u_dataset = data_manager.get_user_dataset()

    preprocessor.fit(b_dataset)

    main_vectors = preprocessor.transform(b_dataset)
    user_vectors = preprocessor.transform(u_dataset)


if __name__ == "__main__":
    main()
