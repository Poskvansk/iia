import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from matplotlib import pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from dataframe import *
from quest2 import *
from quest22 import *

def main():

    dataframe = pd.read_excel("data/dataset.xlsx")
    dataframe = fix_dataframe(dataframe)

    # classif(dataframe, "SARS-Cov-2 exam result")
    quest22(dataframe)

main()