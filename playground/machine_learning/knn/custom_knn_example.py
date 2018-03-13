import matplotlib
matplotlib.use('TKAgg') # so the plotting window can be closed manually when running
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

from custom_knn import k_nearest_neighbors

# define two classes with three features each
dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
new_features = [5, 7]

result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)

# plot the data
for data_class in dataset:
    for feature_set in dataset[data_class]:
        plt.scatter(feature_set[0], feature_set[1], s=100, color=data_class)

plt.scatter(new_features[0], new_features[1], s=100, color=result, marker='*')
plt.show()
