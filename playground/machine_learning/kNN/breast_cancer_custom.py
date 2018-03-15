from __future__ import division

import pandas as pd
import random

from custom_knn import k_nearest_neighbors

def test_custom_knn_cancer():
    # load data
    df = pd.read_csv("../test_data/breast-cancer-wisconsin.data")
    df.replace('?', -99999, inplace=True)
    df.drop(['id'], 1, inplace=True)
    full_data = df.astype(float).values.tolist() # make sure for sure that the data are floats

    # test/train split
    random.shuffle(full_data)
    test_size = 0.2
    train_set = {2: [], 4: []}
    test_set = {2: [], 4: []}
    train_data = full_data[:-int(test_size * len(full_data))] # everything up to the last 20% of the data
    test_data = full_data[-int(test_size * len(full_data)):]  # the last 20% of the data

    # build the training set - remove class column
    for train_item in train_data:
        train_set[train_item[-1]].append(train_item[:-1])

    # build the testing set - remove class column
    for test_item in test_data:
        test_set[test_item[-1]].append(test_item[:-1])

    # test it out!
    correct = 0
    total = 0

    for data_class in test_set:
        for features in test_set[data_class]:
            vote, confidence = k_nearest_neighbors(train_set, features, k=5)
            if data_class == vote:
                correct += 1
            #else: print(confidence)
            total += 1

    accuracy = correct / total
    #print("Accuracy:", accuracy)
    return accuracy
