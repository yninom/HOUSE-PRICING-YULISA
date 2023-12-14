# Predicción del precio de casas
En este repositorio encontrará los siguientes modulos:
- dummydata.py: Genera un conjunto de datos aleatorio de 10000 filas, cuyas variables son Precio, Número de Habitaciones, Piso y Barrio, y lo exporta en un archivo .csv.
- linearregression.py: Realiza una regresión lineal sobre los datos generados por dummydata.py para realizar predicciones sobre el precio de las casas. Además, almacena este modelo en un archivo .pkl.
- interfaz.py: Despliega una interfaz usando Streamlit, donde el usuario podrá ingresar valores para el Número de Habitaciones, Piso y Barrio y obtener un precio estimado para una casa con estas características.
