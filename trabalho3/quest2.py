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

def classif(dataframe, column):

    print("Random forest var: ", column)

    X = dataframe.drop([column], axis=1)
    y = dataframe[column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    classifier = RandomForestClassifier(n_estimators=100, random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    important_features = classifier.feature_importances_
    indexes = np.argsort(important_features)[::-1]
    top10 = []

    for i in range(10):
        top10.append(X.columns.tolist()[indexes[i]])
    for i in top10:
        print(i)
    print("================================")

def quest2(dataframe):

    classif(dataframe, "Patient addmited to regular ward (1=yes, 0=no)")
    classif(dataframe, "Patient addmited to semi-intensive unit (1=yes, 0=no)")
    classif(dataframe, "Patient addmited to intensive care unit (1=yes, 0=no)")
