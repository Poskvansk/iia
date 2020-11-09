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

# Função que printa as 10 caracterisitcas mais importantes para a Floresta.
def important_features(classifier, X):
    
    important_features = classifier.feature_importances_
    indexes = np.argsort(important_features)[::-1]
    top10 = []
    aux = 1

    for i in range(10):
        top10.append(X.columns.tolist()[indexes[i]])

    print("================================")
    print("Most important features:")
    for i in top10:
        print(aux, " - ", i)
        aux += 1
    print("================================")

# Esta funcao cria uma Random Forest
# dataframe = conjunto de dados utilizados para a floresta (tabela)
# column = coluna que a Floresta pretende prever (o resultado)
def classif(dataframe, column):

    print("Random forest var: ", column)

    X = dataframe.drop([column], axis=1)
    y = dataframe[column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    classifier = RandomForestClassifier(n_estimators=300, random_state=0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(classification_report(y_test, y_pred))
    # print(accuracy_score(y_test, y_pred))

    important_features(classifier, X)

# Esta função cria uma nova coluna ["Patient destination"], especifica para poder tentar prever o local de acompanhamento de um paciente
def create_new_column(dataframe):
  
    dataframe["Patient addmited to regular ward (1=yes, 0=no)"] = dataframe["Patient addmited to regular ward (1=yes, 0=no)"].replace(1, 1)

    dataframe["Patient addmited to semi-intensive unit (1=yes, 0=no)"] = dataframe["Patient addmited to semi-intensive unit (1=yes, 0=no)"].replace(1, 2)

    dataframe["Patient addmited to intensive care unit (1=yes, 0=no)"] = dataframe["Patient addmited to intensive care unit (1=yes, 0=no)"].replace(1, 3)
    
    dataframe["Patient destination"] = dataframe["Patient addmited to regular ward (1=yes, 0=no)"] + dataframe["Patient addmited to semi-intensive unit (1=yes, 0=no)"] + dataframe["Patient addmited to intensive care unit (1=yes, 0=no)"]

    return dataframe

# Apenas para separar a questão 1 da questão 2 do trabalho
def quest2(dataframe):

    dat2 = create_new_column(dataframe)

    dat2 = dat2.drop(["Patient addmited to regular ward (1=yes, 0=no)"], axis=1)
    dat2 = dat2.drop(["Patient addmited to semi-intensive unit (1=yes, 0=no)"], axis=1)
    dat2 = dat2.drop(["Patient addmited to intensive care unit (1=yes, 0=no)"], axis=1)

    classif(dat2, "Patient destination")