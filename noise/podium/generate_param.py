import numpy as np


class SettingParameters:
    def __init__(self, epsilon, data, task_method = True):
        self.epsilon = epsilon
        self.task_method = task_method
        self.s = self.get_s()
        self.m = self.get_m()
        self.delta = self.get_delta(data)
        self.w = self.get_w()
        self.d = self.get_d()

    def get_m(self):
        return (1+np.exp(self.s)+ np.exp(self.epsilon)+np.exp(self.epsilon-self.s))/(np.exp(self.epsilon)-1)

    def get_delta(self, data):
        if len(data) < 2:
            return 1  # Если в массиве меньше двух элементов, разность невозможна
        max_value = max(data)  # Находим максимальное значение в массиве
        min_value = min(data)  # Находим минимальное значение в массиве
        return abs(max_value - min_value)  # Возвращаем абсолютную разность

    def get_w(self):
        return (self.delta*self.m)/(1+np.exp(self.s))

    def get_d(self):
        return ((1+np.exp(self.s))*(1+np.exp(-1*self.s)))/(self.delta*self.m*(1+np.exp(self.s)+np.exp(self.epsilon)+np.exp(self.epsilon-self.s)))

    def get_s(self):
        if self.task_method:
            return self.epsilon/3
        else:
            # для эпсилана = 1.0
            # данные из таблицы, если точное значение нужно
            return 0.25367785386777708112