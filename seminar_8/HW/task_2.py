'''
Измерены значения IQ выборки студентов, обучающихся в местных технических вузах: 131, 125, 115, 122, 131, 115, 107, 99, 125, 111. Известно, что в генеральной совокупности IQ распределен нормально. Найдите доверительный интервал для математического ожидания с надежностью 0.95.
'''
import numpy as np
from scipy import stats

iq = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
mean_iq = np.mean(iq)
std_iq = np.std(iq, ddof=1)
n = len(iq)
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)

margin_of_error = t_critical * (std_iq / np.sqrt(n))
confidence_interval = (mean_iq - margin_of_error, mean_iq + margin_of_error)

print(f'Доверительный интервал для среднего IQ: {confidence_interval}')

# Доверительный интервал для среднего IQ: (110.55608365158724, 125.64391634841274)