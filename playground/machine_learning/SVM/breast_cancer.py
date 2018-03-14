from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def test_SVM_cancer():
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
    clf = SVC()
    clf.fit(X_train, y_train)

    # test the classifier
    accuracy = clf.score(X_test, y_test)
    #print(accuracy)
    return accuracy
