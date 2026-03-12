import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Presupuestador LAMBE", layout="wide")

st.markdown("## 📊 Calculadora de Presupuestos LAMBE")

# 2. Creamos un "contenedor" vacío arriba del todo para inyectar los resultados luego
resultados_superiores = st.container()

st.divider()

# 3. ZONA DE INTRODUCCIÓN DE DATOS (Abajo)
st.markdown("### ⚙️ Parámetros del Presupuesto")

# Datos Generales
c1, c2, c3, c4 = st.columns(4)
tirada = c1.number_input("📦 Tirada (unidades)", min_value=1, value=15000, step=100)
paginas_interior = c2.number_input("📄 Páginas Interior", min_value=1, value=192, step=1)
paginas_cubierta = c3.number_input("📘 Páginas Cubierta", min_value=1, value=4, step=1)
pliegos_interior = c4.number_input("📑 Pliegos Interior", min_value=1, value=12, step=1)

st.write("") # Espaciador

# Columnas de Interior y Cubierta
col_int, col_cub = st.columns(2)

with col_int:
    st.markdown("#### 📄 INTERIOR")
    ci1, ci2 = st.columns(2)
    with ci1:
        ancho_int = st.number_input("Ancho (cm) Int.", value=80.0, step=1.0)
        largo_int = st.number_input("Largo (cm) Int.", value=63.0, step=1.0)
        gramaje_int = st.number_input("Gramaje (g/m2) Int.", value=150.0, step=1.0)
        precio_papel_int = st.number_input("Papel (€/kg) Int.", value=1.02, step=0.01, format="%.3f")
        encuadernacion_int = st.number_input("Encuadernación (€) Int.", value=129.6, step=1.0)
    with ci2:
        fijos_imp_int = st.number_input("Fijos Imp. (plancha) Int.", value=250.0, step=1.0)
        sucesivos_imp_int = st.number_input("Suc. Imp. (€/1k) Int.", value=10.0, step=1.0)
        merma_fija_int = st
