#librerías necesarias
import numpy as np
import pandas as pd 

#generación aleatoria de los datos, low es incluyente y high es excluyente
precio = np.random.randint(20000, 1000001, 10000)
habitaciones = np.random.randint(1, 6, 10000)
piso = np.random.randint(1, 21, 10000)
barrio = np.random.randint(1, 51, 10000)

#dataframe con los datos generados
df = pd.DataFrame({'Precio (dolares)':precio, 'Número de Habitaciones':habitaciones, 'Piso':piso, 'Barrio':barrio})

#exportar los datos generados en un archivo .csv
df.to_csv('housesdata.csv', index=False)