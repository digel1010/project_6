import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de venta de vehículos')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram = st.checkbox('Construir histograma') # crear una casilla de verificacion
        
if build_histogram: # al hacer clic en el botón
     # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
     # crear un histograma
     fig = px.histogram(car_data, x="odometer")
        
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión') # creamos una casilla de verificacion

if build_scatter:
    # escribir mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    #crear grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
