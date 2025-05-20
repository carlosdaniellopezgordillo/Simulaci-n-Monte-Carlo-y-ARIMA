# 📊 Pronóstico de Producción Hidroeléctrica con ARIMA

Este proyecto es un **dashboard interactivo profesional** creado con [Streamlit](https://streamlit.io/) y [Plotly](https://plotly.com/), que utiliza un modelo estadístico **ARIMA** para predecir la producción diaria de energía (en MWh) en una planta hidroeléctrica durante los próximos 30 días, con base en datos históricos.

---

## 📸 Vista previa del dashboard

<img src="preview.png" alt="Vista previa del dashboard" width="100%">

<!-- 
👉 Alternativamente, puedes usar un GIF animado:
<img src="demo.gif" alt="Demo del dashboard en acción" width="100%">
-->

---

## 🧠 ¿Qué hace esta app?

- Simula 2 años de producción energética diaria
- Ajusta un modelo ARIMA (2,1,2) automáticamente
- Genera un pronóstico de 30 días con intervalo de confianza
- Visualiza todo con una gráfica interactiva
- Se puede desplegar como una app web sin servidores

---

## 🚀 Cómo ejecutar localmente

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

## 2. Instala las dependencias
pip install -r requirements.txt

3. Ejecuta la aplicación
streamlit run app.py
La app se abrirá en tu navegador por defecto (http://localhost:8501)

🌐 Cómo desplegar en Streamlit Cloud
Sube este repositorio a GitHub

Ve a Streamlit Cloud

Haz clic en "Deploy an app"

Selecciona el repositorio

Configura:

Branch: main

Main file path: app.py

Haz clic en Deploy

Tu app estará disponible en una URL como:

arduino
Copiar
Editar
https://nombre-app.streamlit.app
📦 Requisitos (requirements.txt)
txt
Copiar
Editar
streamlit
plotly
pandas
numpy
statsmodels
✨ Posibles mejoras
Permitir carga de archivos CSV reales

Ajuste dinámico de parámetros del modelo ARIMA

Exportar pronóstico como Excel o CSV

Mostrar métricas de precisión (RMSE, MAE)

Integración con bases de datos externas

🧑‍💻 Autor
Este proyecto fue creado como ejercicio académico para demostrar el uso de modelos de series temporales en un entorno visual e interactivo. Ideal para presentaciones o implementaciones en el sector energético.


