import numpy as np


class SettingParameters():
    def __init__(self, epsilon, task_method = True):
        self.epsilon = epsilon
        self.task_method = task_method
        self.s = self.get_s()
        self.m = self.get_m()
        self.w = self.get_w()
        self.d = self.get_d()

    def get_m(self):
        return (1+np.exp(self.s)+ np.exp(self.epsilon)+np.exp(self.epsilon-self.s))/(np.exp(self.epsilon)-1)
        ...
    def get_w(self):

        ...
    def get_d(self):
        ...
    def get_s(self):
        ...