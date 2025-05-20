📊 Dashboard de Pronóstico de Producción Hidroeléctrica
Este proyecto es un dashboard interactivo creado con Streamlit y Plotly, que utiliza un modelo estadístico ARIMA para pronosticar la producción diaria de energía (MWh) en una planta hidroeléctrica durante los próximos 30 días, basado en datos históricos.

🧠 ¿Qué hace esta app?
📈 Simula 2 años de producción energética diaria (con ruido y estacionalidad)

🧮 Ajusta un modelo ARIMA para detectar tendencias y estacionalidades

🔮 Realiza un pronóstico de 30 días con intervalos de confianza

📊 Visualiza los resultados con una gráfica interactiva de Plotly

🌐 Se despliega como aplicación web con Streamlit

🛠 Tecnologías utilizadas
Streamlit – para crear la aplicación web

Plotly – para gráficos interactivos

Pandas – para manipulación de datos

NumPy – para simulaciones y cálculos

Statsmodels – para el modelo ARIMA

📦 Requisitos de instalación
Primero, asegúrate de tener Python 3.8 o superior. Luego instala los paquetes necesarios con:

bash
Copiar
Editar
pip install -r requirements.txt
🚀 Cómo ejecutar la app localmente
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
streamlit run app.py
Se abrirá automáticamente en tu navegador en http://localhost:8501.

🌐 Cómo desplegar en Streamlit Cloud
Sube este repositorio a tu cuenta de GitHub

Ve a Streamlit Cloud

Haz clic en "Deploy an app"

Conecta tu cuenta de GitHub y selecciona este repositorio

Especifica:

Branch: main

Main file path: app.py

Haz clic en Deploy

¡Listo! Tendrás una URL pública para compartir tu app

📸 Vista previa del dashboard
(Agrega una captura de pantalla aquí si gustas)

✨ Ideas para mejorar
Subir archivos CSV reales en lugar de simular datos

Ajustar parámetros ARIMA dinámicamente desde la interfaz

Exportar resultados del pronóstico como archivo CSV o Excel

Integrar alertas si la producción baja de cierto umbral

🧑‍💻 Autor
Este proyecto fue creado como parte de un ejercicio de ciencia de datos aplicada a la energía y el pronóstico de series temporales. Ideal para presentaciones profesionales o académicas.

