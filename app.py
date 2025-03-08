import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos (Asegúrate de subir un archivo CSV con los datos o reemplazar esto con tu código de carga)
df_dept = pd.read_csv("departments_data.csv", index_col=0)
df_tasas = pd.read_csv("retention_satisfaction.csv", index_col=0)

st.title("📊 Comparación de Tendencias en Departamentos")

# Crear gráficos
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(df_dept.index, df_dept["Engineering Enrolled"], label="Inscritos Ingeniería")
ax1.plot(df_dept.index, df_dept["Business Enrolled"], label="Inscritos Negocios")
ax1.plot(df_dept.index, df_dept["Arts Enrolled"], label="Inscritos Artes")
ax1.plot(df_dept.index, df_dept["Science Enrolled"], label="Inscritos Ciencias")

ax1.set_xlabel("Año")
ax1.set_ylabel("Número de estudiantes inscritos")
ax1.set_title("Comparación de tendencias entre departamentos, tasas de retención y satisfacción")
ax1.legend()
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(df_tasas.index, df_tasas["Retention Rate (%)"], color='red', linestyle='--', label="Tasa de Retención (%)")
ax2.plot(df_tasas.index, df_tasas["Student Satisfaction (%)"], color='green', linestyle='--', label="Satisfacción (%)")
ax2.set_ylabel("Porcentaje")

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

st.pyplot(fig)
