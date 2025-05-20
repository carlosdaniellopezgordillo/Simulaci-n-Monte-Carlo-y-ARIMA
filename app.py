import numpy as np
import pandas as pd
from datetime import timedelta
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objs as go
import streamlit as st

# Título del dashboard
st.set_page_config(page_title="Pronóstico de Producción de Energía", layout="wide")
st.title("🔮 Dashboard de Pronóstico de Producción Hidroeléctrica")

# Simulación de datos históricos
np.random.seed(42)
fechas = pd.date_range(start="2023-01-01", periods=730)
produccion = 500 + 20 * np.sin(np.linspace(0, 10*np.pi, 730)) + np.random.normal(0, 10, 730)
df = pd.DataFrame({'Fecha': fechas, 'Produccion_MWh': produccion})
df.set_index('Fecha', inplace=True)

# Mostrar tabla opcional
with st.expander("🔍 Ver datos históricos"):
    st.dataframe(df.tail(10))

# Ajustar modelo ARIMA
modelo = ARIMA(df['Produccion_MWh'], order=(2, 1, 2))
resultado = modelo.fit()

# Pronóstico de 30 días
forecast = resultado.get_forecast(steps=30)
predicciones = forecast.predicted_mean
conf_int = forecast.conf_int()
fechas_futuras = [df.index[-1] + timedelta(days=i) for i in range(1, 31)]

# Crear gráfico interactivo
fig = go.Figure()

# Línea histórica
fig.add_trace(go.Scatter(
    x=df.index,
    y=df['Produccion_MWh'],
    mode='lines',
    name='Histórico',
    line=dict(color='blue')
))

# Línea de pronóstico
fig.add_trace(go.Scatter(
    x=fechas_futuras,
    y=predicciones,
    mode='lines+markers',
    name='Pronóstico',
    line=dict(color='red', dash='dash')
))

# Banda de confianza
fig.add_trace(go.Scatter(
    x=fechas_futuras + fechas_futuras[::-1],
    y=list(conf_int.iloc[:, 0]) + list(conf_int.iloc[:, 1][::-1]),
    fill='toself',
    fillcolor='rgba(255, 182, 193, 0.4)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Intervalo de Confianza'
))

# Layout profesional
fig.update_layout(
    title='Pronóstico de Producción de Energía (30 días)',
    xaxis_title='Fecha',
    yaxis_title='Producción (MWh)',
    template='plotly_white',
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)

# Mostrar gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)
