import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def fix_dataframe(dataframe):

    columns = dataframe.columns.values

    for i in columns:
        if dataframe[i].isnull().values.any() :

            df_datatypes = dataframe[i].dtypes

            if df_datatypes != 'object':
                dataframe[i] = dataframe[i].replace(np.NaN, 0)

    dataframe = dataframe.replace(np.NaN, '')

    return dataframe

def main():

    enc = OrdinalEncoder()
    dataframe = pd.read_excel("data/test1.xlsx")
    dataframe = fix_dataframe(dataframe)   
    # print(dataframe)

    X = dataframe.drop(["SARS-Cov-2 exam result", "Patient ID"], axis=1)
    y = dataframe["SARS-Cov-2 exam result"]
    # print(X)
    # print("=====================")
    # print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    print("X_train shape: ", X_train.shape)
    print("=====================")
    print("X_test shape: ", X_test.shape)
    print("=====================")
    print("y_train shape: ", y_train.shape)
    print("=====================")
    print("y_testshape: ", y_test.shape)
    print("=====================")

    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.fit_transform(X_test)

    # # print(X_train)
    # # print("=====================")
    # # print(X_test)
    # # print("=====================")
    # classifier = RandomForestClassifier(n_estimators=10, random_state=0)
    # classifier.fit(X_train, y_train)
    # y_pred = classifier.predict(X_test)

    # print(confusion_matrix(y_test, y_pred))
    # print(classification_report(y_test, y_pred))
    # print(accuracy_score(y_test, y_pred))

main()