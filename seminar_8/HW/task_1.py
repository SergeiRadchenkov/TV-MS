'''
Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy Полученные значения должны быть равны. Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.
'''
import numpy as np
import pandas as pd

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

mean_zp = np.mean(zp)
mean_ks = np.mean(ks)

cov_manual = np.sum((np.array(zp) - mean_zp) * (np.array(ks) - mean_ks)) / len(zp)
print(f'Ковариация вручную: {cov_manual}')

cov_np = np.cov(zp, ks, ddof=0)[0, 1]
print(f'Ковариация с помощью numpy: {cov_np}')

std_zp = np.std(zp)
std_ks = np.std(ks)

pearson_manual = cov_manual / (std_zp * std_ks)
print(f'Коэффициент корреляции Пирсона вручную: {pearson_manual}')

df = pd.DataFrame({'zp': zp, 'ks': ks})
pearson_np = np.corrcoef(zp, ks)[0, 1]
pearson_pd = df.corr().loc['zp', 'ks']

print(f'Коэффициент корреляции Пирсона с помощью numpy: {pearson_np}')
print(f'Коэффициент корреляции Пирсона с помощью pandas: {pearson_pd}')