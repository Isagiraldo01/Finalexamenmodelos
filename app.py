import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# 📌 Título de la aplicación
st.title("📊 Comparación de Tendencias en Departamentos Universitarios")

# 📌 Verificar si los archivos CSV existen
if os.path.exists("university_student_dashboard_data.csv"):
    df = pd.read_csv("university_student_dashboard_data.csv")

    # 📌 Mostrar los primeros datos
    st.subheader("🔍 Vista previa de los datos")
    st.dataframe(df.head())

    # 📌 Seleccionar columnas relevantes para el gráfico
    columnas_departamentos = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
    columnas_tasas = ["Retention Rate (%)", "Student Satisfaction (%)"]

    # 📌 Convertir la columna de años a índice (si es necesario)
    if "Year" in df.columns:
        df.set_index("Year", inplace=True)

    # 📌 Crear la figura para matplotlib
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 📌 Graficar las inscripciones por departamento
    for columna in columnas_departamentos:
        if columna in df.columns:
            ax1.plot(df.index, df[columna], marker="o", linestyle="-", label=columna)

    ax1.set_xlabel("Año")
    ax1.set_ylabel("Número de estudiantes inscritos")
    ax1.set_title("Comparación de Tendencias: Departamentos, Tasas de Retención y Satisfacción")
    ax1.legend(loc="upper left")
    ax1.grid(True)

    # 📌 Agregar un segundo eje para la tasa de retención y satisfacción
    ax2 = ax1.twinx()
    if all(col in df.columns for col in columnas_tasas):
        ax2.plot(df.index, df["Retention Rate (%)"], color="red", linestyle="--", label="Tasa de Retención (%)")
        ax2.plot(df.index, df["Student Satisfaction (%)"], color="green", linestyle="--", label="Satisfacción (%)")

    ax2.set_ylabel("Porcentaje")
    ax2.legend(loc="upper right")

    # 📌 Mostrar el gráfico en Streamlit
    st.pyplot(fig)

else:
    st.error("⚠️ Error: No se encontró `university_student_dashboard_data.csv`. Súbelo al repositorio.")
