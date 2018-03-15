import time

from breast_cancer_custom import test_custom_knn_cancer
from breast_cancer import test_knn_cancer

accuracies = []
number_of_runs = 25

print("Running custom kNN...")
custom_start = time.time()
for i in range(number_of_runs):
    accuracies.append(test_custom_knn_cancer())

print("Completed in " + str(time.time() - custom_start) + " seconds")
print("Average accuracy for " + str(number_of_runs) + " runs: " + str(sum(accuracies) / len(accuracies)))

print("Running sklearn kNN...")
sklearn_start = time.time()
for i in range(number_of_runs):
    accuracies.append(test_knn_cancer())

print("Completed in " + str(time.time() - sklearn_start) + " seconds")
print("Average accuracy for " + str(number_of_runs) + " runs: " + str(sum(accuracies) / len(accuracies)))
