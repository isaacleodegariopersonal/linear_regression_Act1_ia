"""
Isaac Ledegario García Estrada
Aplicaciones de inteligencia artificial
Algoritmo de regresion lineal
"""
# Se importan las librerias a usar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Se importan los datos a user del dataset
# Se definen las variables ( x = edad, y = presion arterial)
df_data = pd.read_csv('dataset.csv')
x_data = df_data['Age']
y_data = df_data['Systolic blood pressure']
n = len(x_data)


# se define y retorna la funcion del modelo
def regression_model(m, x, b):
    y = m * x + b
    return y


# Se define funcion de error cuadratico medio para ajuste del error
def calculate_rme(y, y_current):
    error = (1/n)*np.sum((y-y_current)**2)
    return error


# Se define funcion de algoritmo decendente para encontrar el valor minimo de la funcion
# Se realizan los gradiantes de las funciones
# Se ajustan los valores de la funcion de prediccion
def descending_gradient(w_current, b_current, alpha, x, y):
    gradient_w = -(2/n)*np.sum(x*(y-(w_current*x+b_current)))
    gradient_b = -(2/n)*np.sum(y-(w_current*x+b_current))
    w = w_current-alpha*gradient_w
    b = b_current-alpha*gradient_b
    return w, b


# Se eligen valores al azar para comenzar con el entrenamiento
w = np.random.randn(1)
b = np.random.randn(1)

# Se elige valor de alga y numero de iteraciones
alpha = 0.0004
iterations = 40000
error = np.zeros((iterations, 1))

#Se realiza el entrenamiento de la funcion de prediccion
for i in range(iterations):
    [w, b] = descending_gradient(w, b, alpha, x_data, y_data)
    y_current = regression_model(w, x_data, b)
    error[i] = calculate_rme(y_data, y_current)

# variable de salida con ajusto de entrenamiento y datos para las predicciones
regression_y = regression_model(w, b, x_data)

# Prediccion de cuanto tendra una persona de presion cuando tenga 10 años
years = 10
pressure = regression_model(w, b, years)
print("when you have ", years, "you might have ", pressure, "of pressure")