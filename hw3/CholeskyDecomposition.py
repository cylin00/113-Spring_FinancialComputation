import numpy as np
import math

def Decomposition(cov):
    A = np.zeros(cov.shape)
    A[0, 0] = np.sqrt(cov[0, 0])  # A[1, 1]

    for j in range(1, cov.shape[0]): # A[1, 2], A[1, 3], ...
        A[0, j] = cov[0, j] / A[0, 0]

    for i in range(1, cov.shape[0]-1): # next rows
        temp_sum = 0
        for k in range(i):
            temp_sum += A[k, i] ** 2
        A[i, i] = math.sqrt(cov[i, i] - temp_sum)

        for j in range(i + 1, cov.shape[0]):
            temp_sum = 0
            for k in range(i):
                temp_sum += A[k, i] * A[k, j]
            A[i, j] = (cov[i, j] - temp_sum) / A[i, i]
        
    temp_sum = 0
    for k in range(cov.shape[0]-1):
        temp_sum += A[k, cov.shape[0]-1] ** 2
    A[cov.shape[0]-1, cov.shape[0]-1] = math.sqrt(cov[cov.shape[0]-1, cov.shape[0]-1] - temp_sum)

    return A