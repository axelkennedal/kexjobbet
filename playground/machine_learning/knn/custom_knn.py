from __future__ import division

from math import sqrt
import numpy as np
import warnings
from collections import Counter

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
    confidence = Counter(votes).most_common(1)[0][1] / k

    return vote_result, confidence
