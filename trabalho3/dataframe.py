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

    obj_columns = []
    for i in columns:
        if dataframe[i].isnull().values.any() :

            df_datatypes = dataframe[i].dtypes
            if df_datatypes != 'object':
                dataframe[i] = dataframe[i].replace(np.NaN, 0)
            else:
                obj_columns.append(i)
                    
    dataframe = dataframe.replace(np.NaN, '')
    dataframe['Urine - Leukocytes'] = dataframe['Urine - Leukocytes'].replace(['<1000'], '500')
    dataframe['Urine - pH'] = dataframe['Urine - pH'].replace(['Não Realizado'], 0.0)
    dataframe['Urine - pH'] = dataframe['Urine - pH'].replace([''], 0.0)
    
    mix_columns = []
    for i in obj_columns:
        int_count = 0
        str_count = 0
        for j in dataframe[i]:
            if not isinstance(j, str):
                int_count += 1
            if not (int_count == 0 ):
                mix_columns.append(i)
                break

    for i in dataframe[mix_columns[0]]:
        if not isinstance(i, float):
            dataframe['Urine - pH'] = dataframe['Urine - pH'].replace([i], float(i))

    # for i in dataframe[mix_columns[0]]:
    #     if not isinstance(i, float):
    #         print(i, type(i))

    return dataframe

def fix_dataframe(dataframe):
    dataframe = fix_dataframe_values(dataframe)
    dataframe = dataframe.drop(["Patient ID"], axis = 1)
    dataframe = encode_dataframe_values(dataframe)
    return dataframe
