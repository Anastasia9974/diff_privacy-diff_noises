import matplotlib.pyplot as plt
import numpy as np

class Density:
    def __init__(self):
        ...
    def print_density_gauss(self, data_new, data_old, size,  epsilon, delta, sensitivity ):
        all_t = []
        for i in range(size):
            all_t.append(data_new[i] - data_old[i])

        # Построить гистограмму и оценку плотности
        plt.figure(figsize=(10, 6))
        plt.hist(all_t, bins=9, density=True, alpha=0.6, color='blue', label='Гистограмма выборок')

        # Оценка плотности ядром
        from scipy.stats import gaussian_kde
        density = gaussian_kde(all_t)
        x_vals = np.linspace(min(all_t), max(all_t), 1000)
        plt.plot(x_vals, density(x_vals), color='red', label='Плотность')

        # Настройка графика
        plt.title(f"Плотность шума из перевернутого механизма Гаусса при epsilon={epsilon}, delta={epsilon}, чуствительности={sensitivity}")
        plt.xlabel("Шум")
        plt.ylabel("Плотность")
        plt.legend()
        plt.grid()
        plt.show()
    def print_density_tuber(self, data_new, data_old,size, a , y):
        all_t = []
        for i in range(size):
            all_t.append(data_new[i]-data_old[i])

        # Построить гистограмму и оценку плотности
        plt.figure(figsize=(10, 6))
        plt.hist(all_t, bins=9, density=True, alpha=0.6, color='blue', label='Гистограмма выборок')

        # Оценка плотности ядром
        from scipy.stats import gaussian_kde
        density = gaussian_kde(all_t)
        x_vals = np.linspace(min(all_t), max(all_t), 1000)
        plt.plot(x_vals, density(x_vals), color='red', label='Плотность')

        # Настройка графика
        plt.title(f"Плотность шума из перевернутого механизма Хьюбера при a ={a}, y = {y}")
        plt.xlabel("Шум")
        plt.ylabel("Плотность")
        plt.legend()
        plt.grid()
        plt.show()
