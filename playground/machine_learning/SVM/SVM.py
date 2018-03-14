import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

## Support Vector Machine (SVM) classifier
class SVM:
    def __init__(self, visualization = True):
        self.visualization = visualization
        self.colors = {1: 'r', -1: 'b'}

        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    ## Train SVM
    def fit(self, data):
        self.data = data

        # { ||w||: [w, b] }
        optDict = {}

        transforms = [[1, 1],
                      [-1, 1],
                      [-1, -1],
                      [1, -1]]

        allData = []
        for yi in self.data:
            for featureSet in self.data[yi]:
                for feature in featureSet:
                    allData.append(feature)

        self.maxFeatureValue = max(allData)
        self.minFeatureValue = min(allData)

        allData = None

        # Dyrt att köra mindre steg än stepSize[-1]
        stepSizes = [ self.maxFeatureValue * 0.1,
                      self.maxFeatureValue * 0.01,
                      self.maxFeatureValue * 0.001 ]

        # Extremely expensive
        bRangeMult = 5

        # We don't ned to take as small steps with b as we do with w
        bMult = 5
        latestOpt = self.maxFeatureValue * 10

        for step in stepSizes:
            w = np.array([latestOpt, latestOpt])

            # We can do this because convex
            optimized = False
            while not optimized:
                for b in np.arange(-1 * self.maxFeatureValue * bRangeMult,
                                   self.maxFeatureValue * bRangeMult,
                                   step * bMult):
                    for transformation in transforms:
                        w_t = w * transformation
                        foundOption = True

                        # Weakest link in SVM
                        # SMO attempts to fix this
                        # self.data is a dictionary
                        #
                        # yi(dot(xi, w) + b) >= 1
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i

                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    foundOption = False
                                    break

                        if foundOption:
                            optDict[np.linalg.norm(w_t)] = [w_t, b]

                if w[0] < 0:
                    optimized = True
                    print('Optimized a step')
                else:
                    w = w - step

            norms = sorted([n for n in optDict])
            # optDict = { ||w||: [w, b] }
            optChoice = optDict[norms[0]]

            self.w = optChoice[0]
            self.b = optChoice[1]
            latestOpt = optChoice[0][0] + step*2
                                

    def predict(self, features):
        # Lös dot(w, u) + b = r
        # om r <= 0, klass-
        # om r >= 0, klass+
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)
        if classification != 0 and self.visualization:
            self.ax.scatter(features[0], features[1], s=200, marker='*', c=self.colors[classification])

        return classification

    def visualize(self):
        [[self.ax.scatter(x[0], x[1], s=100, color=self.colors[i]) for x in self.data[i]] for i in self.data]

        # hyperplane = dot(x, w) + b
        # v = dot(x, w) + b
        # psv = 1
        # nsv = -1
        # dec = 0
        def hyperplane(x, w, b, v):
            return (-w[0] * x - b + v) / w[1]


        dataRange = (self.minFeatureValue * 0.9, self.maxFeatureValue * 1.1)
        hypXMin = dataRange[0]
        hypXMax = dataRange[1]

        # (dow(w, x) + b = 1
        # positive support vector hyperplane
        psv1 = hyperplane(hypXMin, self.w, self.b, 1)
        psv2 = hyperplane(hypXMax, self.w, self.b, 1)

        self.ax.plot([hypXMin, hypXMax], [psv1, psv2])

        # (dow(w, x) + b = -1
        # negative support vector hyperplane
        nsv1 = hyperplane(hypXMin, self.w, self.b, -1)
        nsv2 = hyperplane(hypXMax, self.w, self.b, -1)

        self.ax.plot([hypXMin, hypXMax], [nsv1, nsv2])

        # (dow(w, x) + b = 0
        # positive support vector hyperplane
        db1 = hyperplane(hypXMin, self.w, self.b, 0)
        db2 = hyperplane(hypXMax, self.w, self.b, 0)

        self.ax.plot([hypXMin, hypXMax], [db1, db2])

        plt.show()


