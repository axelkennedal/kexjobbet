import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd

def test_knn_cancer():
    df = pd.read_csv("../test_data/breast-cancer-wisconsin.data")

    # handle missing data in the dataset
    df.replace('?', -99999, inplace=True)

    # ignore ID column (comment this out when making predictions)
    df.drop(['id'], 1, inplace=True)

    # X is for features, Y for labels
    X = np.array(df.drop(['class'], 1))
    y = np.array(df['class'])

    # cross validation - separate the data into training and test chunks
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # define classifier
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)

    # test the classifier
    accuracy = clf.score(X_test, y_test)
    #print(accuracy)
    return accuracy

    # make an example to predict
    # example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1], [4, 2, 1, 2, 2, 2, 3, 2, 1]])
    # example_measures = example_measures.reshape(len(example_measures), -1)
    # prediction = clf.predict(example_measures)
    # print(prediction)
