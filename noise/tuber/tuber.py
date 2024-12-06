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

from generate_param import SettingParameters

class Tuber:
    def __init__(self, parameters: SettingParameters):
        self.parameters = parameters
        ...
    def get_t(self):
        ...
    def masking_data(self):
        ...