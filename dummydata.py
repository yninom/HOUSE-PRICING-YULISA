import numpy as np
import pandas as pd 


precio = np.random.randint(20000, 1000000, 10000)
habitaciones = np.random.randint(1, 6, 10000)
piso = np.random.randint(1, 21, 10000)
barrio = np.random.randint(1, 51, 10000)

df = pd.DataFrame({'Precio (dolares)':precio, 'Número de Habitaciones':habitaciones, 'Piso':piso, 'Barrio':barrio})


df.to_csv('housesdata.csv', index=False)