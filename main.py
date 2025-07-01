from src.data_manager import DataManager
import src.utils as utils

def main():
    dm = DataManager(
        books_path=utils.BOOKS_PATH,
        book_tags_path=utils.BOOK_TAGS_PATH,
        tags_path=utils.TAGS_PATH,
        user_data_path=utils.USER_DATA_PATH,
        dataset_path=utils.DATASET_PATH
    )

    dm.get_book_dataset()
    dm.get_user_dataset()

if __name__ == "__main__":
    main()
