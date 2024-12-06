from generate_param import SettingParameters
import random
import numpy as np
class Podium:
    def __init__(self, parameters: SettingParameters):
        self.x = 0 # это как раз данные что маскировать надо
        self.parameters = parameters
    def change_x(self, x):
        self.x = x # это как раз данные что маскировать надо
    def get_t(self):
        return ((2*self.x-self.parameters.w*self.parameters.w*self.parameters.d*(np.exp(self.parameters.epsilon)-1))/
                (self.parameters.w*self.parameters.d*(np.exp(self.parameters.epsilon)-1)))
    def first_component_p1(self):
        return self.parameters.d*(self.get_t()+(self.parameters.delta*self.parameters.m)/2)
    def second_component_p2(self):
        return self.parameters.d * np.exp(self.parameters.epsilon) * self.parameters.w
    def masking_data(self):
        Y = random.random()
        p1 = self.first_component_p1()
        p2 = self.second_component_p2()
        t = self.get_t()
        if Y< p1:
            left = (-1*self.parameters.delta*self.parameters.m)/2
            return random.uniform(left, t)
        elif Y< p2+p1:
            return random.uniform(t, t + self.parameters.w)
        else:
            left = (self.parameters.delta * self.parameters.m)/2
            return random.uniform(t + self.parameters.w, left)
