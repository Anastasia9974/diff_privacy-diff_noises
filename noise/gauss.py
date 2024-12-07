from diffprivlib.mechanisms import Gaussian

class Gauss(Gaussian):
    def __init__(self, epsilon, delta, sensitivity):
        self.gaussian_mechanism = Gaussian(epsilon=epsilon, delta=delta, sensitivity=sensitivity)
    def masking_data(self, data):
        return self.gaussian_mechanism.randomise(data)
