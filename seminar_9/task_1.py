'''
Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
линейной регрессии.
'''
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x1= np.array([30,30,40, 40])
y1= np.array([37, 47, 50, 60])

x2= np.array([30,30,40, 40, 20, 20, 50, 50])
y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])

x3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84]) 

def estimate_coef(x, y):
# number of observations/points
    n = np.size(x)
# mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
# calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
# calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    return (b_0, b_1)

def plot_regression_line(x, y, b):
# plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
    marker = "o", s = 30)
# predicted response vector
    y_pred = b[0] + b[1]*x
# plotting the regression line
    plt.plot(x, y_pred, color = "g")
# putting labels
    plt.xlabel('x')
    plt.ylabel('y')
# function to show plot
    plt.show()

def main(x,y):
# observations / data
#x = X3#np.array([30,30,40, 40])
#y = Y3#np.array([37, 47, 50, 60])
# estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {} \
    \nb_1 = {}".format(b[0], b[1]))
# plotting regression line
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main(x1,y1)
    main(x2,y2)
    main(x3,y3)
    plt.scatter(x1,y1)
    plt.title('r=вписать значение коэффициента')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Given data points
x0 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60]).reshape(-1, 1)
y0 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

# Creating and fitting the linear regression model
model = LinearRegression()
model.fit(x0, y0)

# Making predictions using the model
y_pred = model.predict(x0)

# Plotting the data points and the regression line
plt.scatter(x0, y0, color='blue', label='Data points')
plt.plot(x0, y_pred, color='red', label='Regression line')
plt.xlabel('x0')
plt.ylabel('y0')
plt.title('Linear Regression')
plt.legend()
plt.show()

# Printing the coefficients of the regression line
print(f"Coefficient (slope): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")