import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numbers as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def main():

    dataset = pd.read_excel("data/teste_e13.xlsx")
    print(dataset)
    print("=====================")
    X = dataset.iloc[:,1:5]
    y = dataset.iloc[:, 5]
    # print(X)
    # print("=====================")
    # print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    print(X_train)
    print("=====================")
    print(X_test)
    print("=====================")
    print(y_train)
    print("=====================")
    print(y_test)
    print("=====================")

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    # print(X_train)
    # print("=====================")
    # print(X_test)
    # print("=====================")
    classifier = RandomForestClassifier(n_estimators=20, random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(y_pred)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

main()



    # for i in columns:
    #     df_datatypes = dataframe[i].dtypes
    #     if df_datatypes == 'object':

    #         # print(i)
    #         for j in dataframe[i]:
    #             if isinstance(j, str):
    #                 if j.find('<') != -1:
    #                     print(i, j)

    
    # for i in dataframe[mix_columns[0]]:
    #     if isinstance(i, int):
    #         print(i, type(i))
    # for i in dataframe[mix_columns[0]]:
    #     print(i, type(i))

    # print(dataframe[mix_columns].dtypes)
    # print(mix_columns)

    # print("X_train shape: ", X_train.shape)
    # print("=====================")
    # print("X_test shape: ", X_test.shape)
    # print("=====================")
    # print("y_train shape: ", y_train.shape)
    # print("=====================")
    # print("y_testshape: ", y_test.shape)
    # print("=====================")