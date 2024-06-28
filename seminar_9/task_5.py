'''
Оценить статистическую значимость полученной модели линейной регрессии
Какой должна быть численность групп, чтобы с вероятностью 90%
обнаруживать снижение летальности с 90 до 30%. Уровень
значимости α = 0,05. При решении вам пригодятся табличные
значения стандартного нормального распределения
'''
import numpy as np
import statsmodels.api as sm

# Given data points
x0 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
y0 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

# Adding a constant (intercept) to the independent variable
x0_with_intercept = sm.add_constant(x0)

# Creating and fitting the linear regression model using statsmodels
model = sm.OLS(y0, x0_with_intercept)
results = model.fit()

# Printing the summary of the regression results
print(results.summary())