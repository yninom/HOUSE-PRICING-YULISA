#librerías necesarias
import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

#título de la página 
st.title('Predice el precio de tu futuro hogar')

#wigdet para ingresar el número de habitaciones
rooms = st.number_input("Por favor ingresa el número de habitaciones (entre 1 y 5):",
                            min_value=1,
                            max_value=5,
                            step=1)
st.write('El número de habitaciones seleccionado es:', rooms)

#widget para ingresar el piso
floor = st.number_input("Por favor ingresa el piso (entre 1 y 20):",
                            min_value=1,
                            max_value=20,
                            step=1)
st.write('El piso seleccionado es:', floor)

#widget para ingresar el barrio
neighborhood = st.number_input("Por favor ingresa el barrio (entre 1 y 50):",
                            min_value=1,
                            max_value=50,
                            step=1)
st.write('El barrio seleccionado es:', neighborhood)

#dataframe con los datos ingresados por el usuario
data = pd.DataFrame({'Número de Habitaciones':[rooms], 'Piso':[floor], 'Barrio':[neighborhood]})

#carga del modelo de regresión lineal
with open('linearregression.pkl', 'rb') as f:
    model = pickle.load(f)

#predicción del precio de la casa    
value = model.predict(data)

#botón para realizar la predicción y mostrar el resultado
if st.button('Predecir'):
    st.write('El precio estimado de la casa es:',round(value[0][0]),'dólares')

#ejecutar en la terminal: streamlit run interfaz.py



