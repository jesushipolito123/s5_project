import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')
st.header('Construir un histograma')
build_hist = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un grafico de dispersion')

if build_hist:
    st.write('Creear un histograma de anuncios de coches de EU')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir un grafico de dispersion de anuncion de coches en EU')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)
