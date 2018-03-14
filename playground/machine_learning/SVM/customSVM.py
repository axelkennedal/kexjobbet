import numpy as np
import warnings

class SupportVectorMachine:
    def __init__(self):
        self.data = None
        pass

    ## Trains the SVM
    ## Input:
    ##     data = { 1: [[]], -1: [[]] }
    def fit(self, data):
        # We want to maximize the distance between the two hyperplanes
        # Consider x+, x- to be two points on each respective hyperplane.
        # The distance between the two points is x+ - x-.
        #
        # Suppose we have a vector w orthogonal to the hyperplanes, the
        # distance between the two planes can be calculated with
        #
        # width = dot((x+ - x-), w / ||w||) = (dot(x+, w) - dot(x-, w)) / ||w||
        #
        # We substitute the bounderies of the hyperplanes into the width equation
        # dot(x+, w) - b >= y, y = 1     => y * (dot(x+, w) - b) >= 1, y = 1
        # dot(x-, w) - b <= y, y = -1    => y * (dot(x-, w) - b) >= 1, y = -1
        #
        # dot(x+, w) = 1 + b
        # dot(x-, w) = 1 - b
        #
        # width = (1 - b - (1 - b)) = 2 / ||w||
        #
        # We want to minimize ||w|| in order to maximize the distance between the
        # hyperplanes, with respect to the boundery condition y * (dot(x, w) - b) - 1 >= 0.
        #
        ###############################
        ## Method 1: Lagrange multiples
        ###############################
        #
        # NOTE: min(2 / ||w||) => min(||w||^2 / 2) 
        #
        # L(w, b, t...) = ||w||^2 / 2 - sum(t_i * y *(dot(x_i, w) - b) - 1)
        # dL_w = w - sum(
        self.data = data

        # The category a certain feature belongs to
        for yi in self.data:
            # The features belonging to said category
            for xi in self.data[yi]:

        

    def predict(self, feature):
        if len(feature) != len(self.data[0]):
            warnings.warn("Dimension of feature vector does not match the dimension of the data used to train model")
        elif self.data=None:
            warnings.warn("Model not yet trained")

        # Classifies the model into two categories (-1, 1) based on
        # the sign of the result of dot(w, x) - b
        classification = np.sign(np.dot(self.w, np.array(feature)) - self.b)

        return classification
        
        
