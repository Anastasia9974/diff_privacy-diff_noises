import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

class SettingParameters:
    def __init__(self, a, y):
        self.a = a
        self.y = y
        self.w = self.get_w()
    def get_w(self):
        first_parts = stats.norm.sf(self.a/self.y)*math.sqrt(2 * math.pi)+ 2*self.y/self.a* np.sinh(pow(self.a,2)/(2*pow(self.y,2)))
        if first_parts >0:
            return first_parts*2
        else:
            return 0
