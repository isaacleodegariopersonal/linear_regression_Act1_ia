# linear_regression_Act1_IA
García Estrada Isaac Leodegario

Predicción de presión arterial

##Proceso

Para realizar este algoritmo de prediccion se baso en tres componentes basicos
- Funcion de ecuacion lineal:

    <a href="https://www.codecogs.com/eqnedit.php?latex=y=mx&plus;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=mx&plus;b" title="y=mx+b" /></a>
- Ajuste de error cuadratico medio (costo):

     <a href="https://www.codecogs.com/eqnedit.php?latex=MSE&space;=&space;\frac{1}{n}\sum_{i=1}^{n}(y_{i}-\tilde{y_{i}})^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?MSE&space;=&space;\frac{1}{n}\sum_{i=1}^{n}(y_{i}-\tilde{y_{i}})^{2}" title="MSE = \frac{1}{n}\sum_{i=1}^{n}(y_{i}-\tilde{y_{i}})^{2}" /></a>

- Algoritmo de gradiante decendente:

    <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial}{\partial&space;m}=\frac{2}{n}\sum_{i=1}^{n}-x^{_{i}}(y_{i}-(mx_{i}&plus;b))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial&space;m}=\frac{2}{n}\sum_{i=1}^{n}-x^{_{i}}(y_{i}-(mx_{i}&plus;b))" title="\frac{\partial}{\partial m}=\frac{2}{n}\sum_{i=1}^{n}-x^{_{i}}(y_{i}-(mx_{i}+b))" /></a>

    y
    
    <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial}{\partial&space;m}=\frac{2}{n}\sum_{i=1}^{n}-(y_{i}-(mx_{i}&plus;b))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial}{\partial&space;m}=\frac{2}{n}\sum_{i=1}^{n}-(y_{i}-(mx_{i}&plus;b))" title="\frac{\partial}{\partial m}=\frac{2}{n}\sum_{i=1}^{n}-(y_{i}-(mx_{i}+b))" /></a>


##Referencias

Dataset from:

https://people.sc.fsu.edu/~jburkardt/datasets/regression/x03.txt

Información matemática:

https://towardsdatascience.com/linear-regression-using-gradient-descent-in-10-lines-of-code-642f995339c0
