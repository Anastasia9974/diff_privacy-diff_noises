# This is a sample Python script.
from random import gauss
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time as tm

from fontTools.misc.bezierTools import epsilon
from sklearn.utils.extmath import density

from noise.tuber.tuber import Tuber
from noise.tuber.generate_param import SettingParameters as param_tuber

from noise.podium.podium import Podium
from noise.podium.generate_param import SettingParameters as param_podium
from evaluation.accuracy import Euclidean_distance
from noise.gauss import Gauss
from generate_data import GenerateData
from evaluation.density import Density

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''так что осталось реализовать:
    1) сделать печать данных и скрин в отчет
    2) реализовать вывод вида плотности обратного хьюберта и сделать скрин для различных комбинаций параметров
    3) реализовать вывод вида плотности подиума и сделать скрина два первый зависимость от данных и второй зависимость от параметров
    4) после реализовать ДК подиумом, хьюбертом и гаусом, ну и лапласам, замерить время выполнения
    5) расчитать точность и утечку информации
    '''
    #получение данных
    data = GenerateData(url = 'https://raw.githubusercontent.com/OpenMined/PyDP/dev/examples/Tutorial_4-Launch_demo/data/01.csv')
    data_all = data.get_data()
    data.print_data()
    #получение параметров
    parameters_podium = param_podium(data=data.get_data_sales_amount(), epsilon= 5.9, task_method=True)
    print("Параметры механизма Подиум:")
    print(f"Эпсилон: {parameters_podium.epsilon}")
    print(f"Чувствительность: {parameters_podium.delta}")
    print(f"s: {parameters_podium.s}")
    print(f"w: {parameters_podium.w}")
    print(f"d: {parameters_podium.d}")
    print(f"m: {parameters_podium.m}")
    parameters_tuber = param_tuber(a = 1, y = 1)
    print("Параметры перевернутого механизма Хьюбера:")
    print(f"a: {parameters_tuber.get_a()}")
    print(f"y: {parameters_tuber.get_y()}")
    print(f"w: {parameters_tuber.get_w()}")
    #внесение шума
    start_time = tm.time()
    metod_podium = Podium(parameters=parameters_podium)
    what_change = data.get_data_sales_amount()
    what_get_podium = []
    for x in what_change:
        metod_podium.change_x(x = x)
        result = abs(metod_podium.masking_data())
        what_get_podium.append(result)
    end_time = tm.time()
    elapsed_time = end_time - start_time  # Вычисляем разницу
    print(f"Время выполнения Подиума: {elapsed_time:.5f} секунд")
    print("Данные что получились при механизме Подиум:")
    data_all['sales_amount'] = what_get_podium
    data.correct_print()
    print(data_all)
    print(f"Евклидова расстояние для механизма Подиум:{Euclidean_distance(data_old=what_change, data_new=what_get_podium, size=len(what_get_podium))}")
    start_time = tm.time()
    metod_tuber = Tuber(parameters=parameters_tuber)
    what_get_tuber = []
    for x in what_change:
        result = metod_tuber.masking_data(x)
        what_get_tuber.append(result)
    end_time = tm.time()
    elapsed_time = end_time - start_time  # Вычисляем разницу
    print(f"Время выполнения Хьюбера: {elapsed_time:.5f} секунд")

    print("Данные что получились при перевернутом механизме Хьюбера:")
    data_all['sales_amount'] = what_get_tuber
    data.correct_print()
    print(data_all)
    print(f"Евклидова расстояние для перевернутого механизма Хьюбера:{Euclidean_distance(data_old=what_change, data_new=what_get_tuber, size=len(what_get_tuber))}")
    print("Параметры механизма Гаусса:")
    print("epsilon=1.0")
    print("delta=1.0")
    print("sensitivity=6.2")
    start_time = tm.time()
    gauss_metod = Gauss(epsilon=1.0,delta=1.0,sensitivity=6.2)
    data_gauss = []
    for x in what_change:
        result = gauss_metod.masking_data(x)
        data_gauss.append(result)
    end_time = tm.time()
    elapsed_time = end_time - start_time  # Вычисляем разницу
    print(f"Время выполнения Гаусса: {elapsed_time:.5f} секунд")

    print("Данные что получились при механизма Гаусса:")
    data_all['sales_amount'] = data_gauss
    data.correct_print()
    print(data_all)
    print(f"Евклидова расстояние для перевернутого механизма Гаусса:{Euclidean_distance(data_old=what_change, data_new=data_gauss, size=len(data_gauss))}")

    #вывод плотности графиков
    density_ = Density()
    density_.print_density_tuber(data_new=what_get_tuber,data_old=what_change, size=len(what_get_tuber), a=parameters_tuber.get_a(), y=parameters_tuber.get_y())
    #density_.print_density_gauss(data_new=data_gauss,data_old=what_change, size=len(what_get_tuber), epsilon=1.0,delta=1.0,sensitivity=6.2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
