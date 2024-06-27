'''
Используя функцию stats.ttest_ind, проведите односторонний
тест. Проверить ,что мю 1 > мю 2
'''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])

res = stats.ttest_ind(a, b,alternative='greater', equal_var = True)
print(res)

print(str(np.mean(a)) + ' ' + str(np.mean(b)))

tstat, pvalue = res
alpha = 0.05
if pvalue < alpha:
    print('Нулевую гипотезу отвергаем. Средние значания выборок различаются')
else:
    print('Нулевую гипотезу принимаем. Существенных различий значания выборок нет')