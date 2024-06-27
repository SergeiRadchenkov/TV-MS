'''
Используя функцию stats.t.ppf найдите, расчетное значение Стьюдента
Определите табличное значение критерия Стьюдента
'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])

print(stats.t.ppf(1-0.936/2,38))

print(stats.ttest_ind(a, b, alternative='greater', equal_var=True))