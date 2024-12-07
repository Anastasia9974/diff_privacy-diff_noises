import numpy as np
from scipy import stats


# Algorithms
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB


from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

import matplotlib.pyplot as plt
import random
import math
from generate_param import SettingParameters
from scipy import stats
class Tuber:
    def __init__(self, parameters: SettingParameters):
        self.parameters = parameters
        ...
    def get_t(self):
        u = random.uniform(0, 1)
        if min(u, 1-u) >= math.sqrt(2 * math.pi)/self.parameters.w*stats.norm.sf(self.parameters.a/self.parameters.y):
            return -1* (pow(self.parameters.y,2)/self.parameters.a)*np.sign(2*u-1)*np.log2(1-self.parameters.a*self.parameters.w/(self.parameters.y*2)*abs(2*u-1)*np.exp(-1*pow(self.parameters.a,2)/(2*pow(self.parameters.y,2))))
        else:
            return self.parameters.y*np.sign(2*u-1)* stats.norm.isf(self.parameters.w*(1-abs(2*u-1))/(2*math.sqrt(2 * math.pi)))
    def masking_data(self, data):
        return data+self.get_t()