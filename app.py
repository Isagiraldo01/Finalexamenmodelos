import streamlit as st
import pandas as pd
import os  # 👈 Agregar esta línea para evitar el NameError

# Verificar si el archivo existe antes de cargarlo
if os.path.exists("university_student_dashboard_data.csv"):
    df = pd.read_csv("university_student_dashboard_data.csv")
    st.success("📂 Archivo cargado correctamente.")
else:
    st.error("⚠️ Error: No se encontró `university_student_dashboard_data.csv`. Por favor, súbelo al repositorio.")
