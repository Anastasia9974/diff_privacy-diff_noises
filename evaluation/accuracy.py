import numpy as np
import math
from scipy.spatial.distance import cdist
def Euclidean_distance(data_old, data_new, size):
    sum = 0
    for i in range(size):
        sum += pow(data_old[i] - data_new[i],2)
    return math.sqrt(sum)