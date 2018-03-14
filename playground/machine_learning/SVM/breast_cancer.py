import pandas as pd
import SVM
import numpy as np

# df = pd.read_csv('../data/breast_cancer.data')
# df.replace('?', -9999, inplace=True)
# df.drop(['id'], 1, inplace=True)
# fullData = df.astype(float).values.tolist()

dataDict = { -1: np.array([[1, 7],
                           [2, 8],
                           [3, 8],]),
             1: np.array([[5, 1],
                          [6, -1],
                          [7, 3],])}



svm = SVM.SVM()
svm.fit(dataDict)

svm.predict([2, 5])
svm.predict([8, 5])

svm.visualize()



