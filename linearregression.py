import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics 
import pickle

df = pd.read_csv('housesdata.csv')

X = df[['Número de Habitaciones', 'Piso', 'Barrio']]
y = df[['Precio (dolares)']]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, train_size=0.7, shuffle=True) 

regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeficientes = pd.DataFrame(regressor.coef_, index=['Coeficientes']).transpose()
variables = pd.DataFrame(X.columns, columns=['Variables'])
coeff_df = pd.concat([variables, coeficientes], axis=1, join='inner')

y_pred = regressor.predict(X_test)
y_pred = pd.DataFrame(y_pred, columns=['Precio Predicho'])

from sklearn import metrics 
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
r2 = metrics.r2_score(y_test, y_pred)

# save
with open('linearregression.pkl','wb') as f:
    pickle.dump(regressor,f)