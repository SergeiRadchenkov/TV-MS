'''
Постройте модель линейной регрессии для подходящих данных
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.stats import shapiro, kstest

# Given data points
x0 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60]).reshape(-1, 1)
y0 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

# Creating and fitting the linear regression model
model = LinearRegression()
model.fit(x0, y0)

# Making predictions using the model
y_pred = model.predict(x0)

# Calculating residuals
residuals = y0 - y_pred

# Plotting residuals vs fitted values to check for homoscedasticity and linearity
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted values')

# Plotting residuals distribution to check for normality
plt.subplot(1, 2, 2)
sns.histplot(residuals, kde=True)
plt.title('Residuals distribution')

plt.tight_layout()
plt.show()

# Normality test (Shapiro-Wilk Test)
shapiro_test = shapiro(residuals)
print(f'Shapiro-Wilk Test: W={shapiro_test[0]:.4f}, p-value={shapiro_test[1]:.4f}')

# Independence test (using K-S test on residuals)
ks_test = kstest(residuals, 'norm', args=(np.mean(residuals), np.std(residuals)))
print(f'K-S Test: D={ks_test[0]:.4f}, p-value={ks_test[1]:.4f}')