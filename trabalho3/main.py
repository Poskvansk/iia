import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from dataframe import *

def main():

    dataframe = pd.read_excel("data/dataset.xlsx")
    dataframe = fix_dataframe(dataframe)

    X = dataframe.drop(["SARS-Cov-2 exam result"], axis=1)
    y = dataframe["SARS-Cov-2 exam result"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    print("X_train shape: ", X_train.shape)
    print("=====================")
    print("X_test shape: ", X_test.shape)
    print("=====================")
    print("y_train shape: ", y_train.shape)
    print("=====================")
    print("y_testshape: ", y_test.shape)
    print("=====================")

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    classifier = RandomForestClassifier(n_estimators=20, random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

main()