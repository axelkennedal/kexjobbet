from math import sqrt
import numpy as np
import matplotlib
matplotlib.use('TKAgg') # so the plotting window can be closed manually when running
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

# define two classes with three features each
dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
new_features = [5, 7]

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less than total voting groups!")

    # calculate all distances
    distances = []
    for data_class in data:
        for features in data[data_class]:
            euclidian_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidian_distance, data_class])

    # get the classes of the k nearest neighbors
    votes = [distance_data[1] for distance_data in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result


result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)

# plot the data
for data_class in dataset:
    for feature_set in dataset[data_class]:
        plt.scatter(feature_set[0], feature_set[1], s=100, color=data_class)

plt.scatter(new_features[0], new_features[1], s=100, color=result, marker='*')
plt.show()
