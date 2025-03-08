import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Verificar si el archivo existe antes de cargarlo
if os.path.exists("university_student_dashboard_data.csv"):
    df = pd.read_csv("university_student_dashboard_data.csv")
    st.success("📂 Archivo cargado correctamente.")
else:
    st.error("⚠️ Error: No se encontró `university_student_dashboard_data.csv`. Por favor, súbelo al repositorio.")

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
