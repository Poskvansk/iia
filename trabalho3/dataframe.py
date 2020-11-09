import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Transforma as colunas com valores nao numericos em colunas com valores numericos
# ex: negative, postive tornam-se 0 e 1.
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

# Função criada para tratar a tabela com dados que possam ser utilizados pela lib scikit-learn
# A tabela continha diversas células com strings, NaN, e colunas que continham tanto strings quanto números
# Esses problemas sao corrigidos nessa funcao
def fix_dataframe_values(dataframe):

    # columns é uma lista com o nome de todas as colunas (todas as features dos objetos)
    columns = dataframe.columns.values

    obj_columns = []
    for i in columns:
        if dataframe[i].isnull().values.any() :

            df_datatypes = dataframe[i].dtypes

            # se coluna não é object (é completamente numerica)
            if df_datatypes != 'object':
                # replace NaN por 0
                dataframe[i] = dataframe[i].replace(np.NaN, 0)
            else:
                obj_columns.append(i)
    
    # replace os NaN restantes por ' ' (string vazia) 
    dataframe = dataframe.replace(np.NaN, '')

    # replaces específicos para alguns elementos problematicos dessas colunas
    dataframe['SARS-Cov-2 exam result'] = dataframe['SARS-Cov-2 exam result'].replace(['negative'], '0')
    dataframe['SARS-Cov-2 exam result'] = dataframe['SARS-Cov-2 exam result'].replace(['positive'], '1')
    dataframe['Urine - Leukocytes'] = dataframe['Urine - Leukocytes'].replace(['<1000'], '900')
    dataframe['Urine - pH'] = dataframe['Urine - pH'].replace(['Não Realizado'], 0.0)
    dataframe['Urine - pH'] = dataframe['Urine - pH'].replace([''], 0.0)

    # alguns numeros na coluna [Urine - pH] estao como strings (??)
    for i in dataframe['Urine - pH']:
        if not isinstance(i, float):
            dataframe['Urine - pH'] = dataframe['Urine - pH'].replace([i], float(i))
            
    return dataframe

# conserta o dataframe
# dá encode nos valores
# descarta a coluna de ID (não necessaria)
def fix_dataframe(dataframe):
    dataframe = fix_dataframe_values(dataframe)
    dataframe = dataframe.drop(["Patient ID"], axis = 1)
    dataframe = encode_dataframe_values(dataframe)
    return dataframe
