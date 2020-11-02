import pandas as pd
import numpy as np


class PrepareDataset:
    def __init__(self):
        self.dataset = pd.read_csv('./dataset.csv')


def main():
    dataset = PrepareDataset()
    print(dataset.dataset)


main()
