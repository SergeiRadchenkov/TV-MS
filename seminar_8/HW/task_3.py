'''
Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. Найдите доверительный интервал для математического ожидания с надежностью 0.95.
'''
import numpy as np
from scipy import stats

mean_height = 174.2
std_height = np.sqrt(25)
n_height = 27
alpha = 0.05
z_critical = stats.norm.ppf(1 - alpha/2)

margin_of_error = z_critical * (std_height / np.sqrt(n_height))
confidence_interval_height = (mean_height - margin_of_error, mean_height + margin_of_error)

print(f'Доверительный интервал для среднего роста: {confidence_interval_height}')
