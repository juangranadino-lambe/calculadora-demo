import streamlit as st
import pandas as pd

# 1. Configuración de página
st.set_page_config(page_title="Presupuestador LAMBE", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS Personalizado para un diseño moderno
st.markdown("""
    <style>
        /* Reducir márgenes superiores */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        /* Estilo para el título principal */
        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #1e3c72, #2a5298);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        /* Ajuste de espaciado en subtítulos */
        h4 {
            color: #555;
            padding-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Título moderno
st.markdown("<div class='main-title'>✨ Calculadora de Presupuestos LAMBE</div>", unsafe_allow_html=True)

# --- SECCIÓN 1: DATOS DE ENTRADA (En una tarjeta destacada) ---
with st.container(border=True):
    st.markdown("### ⚙️ Datos Generales del Proyecto")
    c1, c2, c3, c4 = st.columns(4)
    tirada = c1.number_input("📦 Tirada (unidades)", min_value=1, value=15000, step=100)
    paginas_interior = c2.number_input("📄 Páginas Interior", min_value=1, value=192, step=1)
    paginas_cubierta = c3.number_input("📘 Páginas Cubierta", min_value=1, value=4, step=1)
    pliegos_interior = c4.number_input("📑 Pliegos Interior", min_value=1, value=12, step=1)

st.write("") # Pequeño espacio

# --- SECCIÓN 2: PANELES PRINCIPALES ---
col_int, col_cub, col_tot = st.columns([1.4, 1.4, 1.2])

# --- PANEL IZQUIERDO: INTERIOR ---
with col_int:
    with st.container(border=True):
        st.markdown("#### 📄 Parámetros INTERIOR")
        ci1, ci2 = st.columns(2)
        with ci1:
            ancho_int = st.number_input("Ancho (cm)", value=80.0, step=1.0, key="a_i")
            largo_int = st.number_input("Largo (cm)", value=63.0, step=1.0, key="l_i")
            gramaje_int = st.number_input("Gramaje (g/m2)", value=150.0, step=1.0, key="g_i")
            precio_papel_int = st.number_input("Papel (€/kg)", value=1.02, step=0.01, format="%.3f", key="p_i")
            encuadernacion_int = st.number_input
