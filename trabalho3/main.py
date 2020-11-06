import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def encode_dataframe_values(dataframe):

    enc = OrdinalEncoder()
    columns = dataframe.columns.values
    object_columns = []

    for i in columns:
        df_datatypes = dataframe[i].dtypes
        if df_datatypes == 'object':
            object_columns.append(i)

    dataframe[object_columns] = enc.fit_transform(dataframe[object_columns])

    return dataframe


def fix_dataframe_values(dataframe):

    columns = dataframe.columns.values

    # for i in columns:
    #     df_datatypes = dataframe[i].dtypes
    #     if df_datatypes == 'object':

    #         # print(i)
    #         for j in dataframe[i]:
    #             if isinstance(j, str):
    #                 if j.find('<') != -1:
    #                     print(i, j)

    obj_columns = []
    for i in columns:
        if dataframe[i].isnull().values.any() :

            df_datatypes = dataframe[i].dtypes
            if df_datatypes != 'object':
                dataframe[i] = dataframe[i].replace(np.NaN, 0)
            else:
                obj_columns.append(i)
                    
    dataframe['Urine - Leukocytes'] = dataframe['Urine - Leukocytes'].replace(['<1000'], 500)
    dataframe['Urine - pH'] = dataframe['Urine - pH'].replace(['Não Realizado'], 0)
    dataframe = dataframe.replace(np.NaN, '')
    
    mix_columns = []
    for i in obj_columns:
        int_count = 0
        str_count = 0
        for j in dataframe[i]:
            if not isinstance(j, str):
                int_count += 1
            if isinstance(j, str):
                str_count += 1
            if not (int_count == 0 ):
                mix_columns.append(i)
                obj_columns.remove(i)
                break
    print(mix_columns)



    return dataframe

def fix_dataframe(dataframe):
    dataframe = fix_dataframe_values(dataframe)
    dataframe = dataframe.drop(["Patient ID"], axis = 1)
    # print(dataframe)
    # dataframe = encode_dataframe_values(dataframe)
    return dataframe



def main():

    dataframe = pd.read_excel("data/dataset.xlsx")
    dataframe = fix_dataframe(dataframe)

    X = dataframe.drop(["SARS-Cov-2 exam result"], axis=1)
    y = dataframe["SARS-Cov-2 exam result"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # print("X_train shape: ", X_train.shape)
    # print("=====================")
    # print("X_test shape: ", X_test.shape)
    # print("=====================")
    # print("y_train shape: ", y_train.shape)
    # print("=====================")
    # print("y_testshape: ", y_test.shape)
    # print("=====================")

    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.fit_transform(X_test)

    # print(X_train)
    # print("=====================")
    # print(X_test)
    # print("=====================")

    # classifier = RandomForestClassifier(n_estimators=20, random_state=0)
    # classifier.fit(X_train, y_train)
    # y_pred = classifier.predict(X_test)

    # print(confusion_matrix(y_test, y_pred))
    # print(classification_report(y_test, y_pred))
    # print(accuracy_score(y_test, y_pred))

main()