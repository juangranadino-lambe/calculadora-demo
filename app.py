import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Presupuestador LAMBE", layout="wide", initial_sidebar_state="collapsed")

# CSS para reducir los márgenes y evitar scrolls innecesarios
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 95%;
        }
        h3, h4 {
            padding-bottom: 0rem;
            margin-bottom: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 📊 Calculadora de Presupuestos LAMBE")
st.divider()

# 2. DIVISIÓN PRINCIPAL: Izquierda (Inputs) y Derecha (Resultados)
# Usamos [2.2, 1] para que la izquierda sea el doble de ancha que la derecha
col_izq, col_der = st.columns([2.2, 1], gap="large")

# ==========================================
# COLUMNA IZQUIERDA: TODOS LOS INPUTS
# ==========================================
with col_izq:
    st.markdown("### ⚙️ Datos a introducir")
    st.write("")
    
    # Datos Generales (en 1 fila)
    c1, c2, c3, c4 = st.columns(4)
    tirada = c1.number_input("📦 Tirada (uds)", min_value=1, value=15000, step=100)
    paginas_interior = c2.number_input("📄 Págs Interior", min_value=1, value=192, step=1)
    paginas_cubierta = c3.number_input("📘 Págs Cubierta", min_value=1, value=4, step=1)
    pliegos_interior = c4.number_input("📑 Pliegos", min_value=1, value=12, step=1)

    st.write("")
    st.write("")
    
    # Subdivisión para Interior y Cubierta
    col_int, col_cub = st.columns(2)
    
    with col_int:
        st.markdown("#### 📄 INTERIOR")
        ci1, ci2 = st.columns(2)
        with ci1:
            ancho_int = st.number_input("Ancho (cm)", value=80.0, step=1.0, key="ai")
            largo_int = st.number_input("Largo (cm)", value=63.0, step=1.0, key="li")
            gramaje_int = st.number_input("Gramaje (g/m2)", value=150.0, step=1.0, key="gi")
            precio_papel_int = st.number_input("Papel (€/kg)", value=1.02, step=0.01, format="%.3f", key="pi")
            encuadernacion_int = st.number_input("Encuadernación (€)", value=129.6, step=1.0, key="ei")
        with ci2:
            fijos_imp_int = st.number_input("Fijos Imp. (plancha)", value=250.0, step=1.0, key="fii")
            sucesivos_imp_int = st.number_input("Suc. Imp. (€/1k)", value=10.0, step=1.0, key
