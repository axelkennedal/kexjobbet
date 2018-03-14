import time

from breast_cancer import test_SVM_cancer

accuracies = []
number_of_runs = 25

print("Running SVM...")
start = time.time()
for i in range(number_of_runs):
    accuracies.append(test_SVM_cancer())

print("Completed in " + str(time.time() - start) + " seconds")
print("Average accuracy for " + str(number_of_runs) + " runs: " + str(sum(accuracies) / len(accuracies)))
