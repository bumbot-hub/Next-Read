import pandas as pd

from src.DataManager import DataManager

if __name__ == "__main__":
    datasets = DataManager()
    print(datasets._dataset)
    print(datasets._user_data)
