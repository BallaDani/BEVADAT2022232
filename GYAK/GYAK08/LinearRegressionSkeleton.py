import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt



class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = -1e-3):
        self.m=0
        self.c=0
        self.epochs=epochs
        self.lr=lr




    def fit(self, X: np.array, y: np.array):
        
        
        n = float(len(X))

        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*self.X + self.c  # The current predicted value of Y

            residuals = y - y_pred
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m - self.lr * D_m  # Update m
            self.c = self.c - self.lr * D_c  # Update c
        
        

         

    def predict(self, X):
               
        pred = []
        for x in X:
                y_pred = self.m*x + self.c
                pred.append(y_pred)
        return pred
        
        
       
