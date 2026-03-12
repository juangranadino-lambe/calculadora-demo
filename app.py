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
            encuadernacion_int = st.number_input("Encuadernación (€)", value=129.6, step=1.0, key="e_i")
        with ci2:
            fijos_imp_int = st.number_input("Fijos Imp. (plancha)", value=250.0, step=1.0, key="fi_i")
            sucesivos_imp_int = st.number_input("Suc. Imp. (€/1k)", value=10.0, step=1.0, key="si_i")
            merma_fija_int = st.number_input("Merma Fija (hojas)", value=2350.0, step=1.0, key="mf_i")
            merma_suc_int = st.number_input("Merma Sucesiva", value=1.08, step=0.01, key="ms_i")
            
        # Cálculos Interior
        peso_hoja_int = (ancho_int * largo_int * gramaje_int) / 10000000
        precio_hoja_int = peso_hoja_int * precio_papel_int
        prod_fijos_int = fijos_imp_int * pliegos_interior
        prod_suc_int = (sucesivos_imp_int * pliegos_interior) + encuadernacion_int
        papel_fijos_int = merma_fija_int * pliegos_interior * precio_hoja_int
        papel_suc_int = pliegos_interior * merma_suc_int * precio_hoja_int * 1000
        total_prod_int_calc = prod_fijos_int + (prod_suc_int * (tirada / 1000))
        total_papel_int_calc = papel_fijos_int + (papel_suc_int * (tirada / 1000))
        
        st.divider()
        st.caption("📊 **SUBTOTALES INTERIOR**")
        st.write(f"🏭 Producción: **{total_prod_int_calc:,.2f} €** &nbsp;&nbsp;|&nbsp;&nbsp; 🌲 Papel: **{total_papel_int_calc:,.2f} €**")

# --- PANEL CENTRAL: CUBIERTA ---
with col_cub:
    with st.container(border=True):
        st.markdown("#### 📘 Parámetros CUBIERTA")
        cc1, cc2 = st.columns(2)
        with cc1:
            ancho_cub = st.number_input("Ancho (cm)", value=70.0, step=1.0, key="a_c")
            largo_cub = st.number_input("Largo (cm)", value=100.0, step=1.0, key="l_c")
            gramaje_cub = st.number_input("Gramaje (g/m2)", value=350.0, step=1.0, key="g_c")
            precio_papel_cub = st.number_input("Papel (€/kg)", value=1.20, step=0.01, format="%.3f", key="p_c")
            encuadernacion_cub = st.number_input("Encuadernación (€)", value=27.5, step=1.0, key="e_c")
        with cc2:
            fijos_imp_cub = st.number_input("Fijos Imp. (€)", value=250.0, step=1.0, key="fi_c")
            sucesivos_imp_cub = st.number_input("Suc. Imp. (€/1k)", value=110.0, step=1.0, key="si_c")
            merma_fija_cub = st.number_input("Merma Fija (hojas)", value=500.0, step=1.0, key="mf_c")
            merma_suc_cub = st.number_input("Merma Sucesiva", value=1.10, step=0.01, key="ms_c")
            
        # Cálculos Cubierta
        peso_hoja_cub = (ancho_cub * largo_cub * gramaje_cub) / 10000000
        precio_hoja_cub = peso_hoja_cub * precio_papel_cub
        prod_fijos_cub = fijos_imp_cub
        prod_suc_cub = sucesivos_imp_cub + encuadernacion_cub
        papel_fijos_cub = merma_fija_cub * precio_hoja_cub
        papel_suc_cub = merma_suc_cub * precio_hoja_cub * 250 
        total_prod_cub_calc = prod_fijos_cub + (prod_suc_cub * (tirada / 1000))
        total_papel_cub_calc = papel_fijos_cub + (papel_suc_cub * (tirada / 1000))

        st.divider()
        st.caption("📊 **SUBTOTALES CUBIERTA**")
        st.write(f"🏭 Producción: **{total_prod_cub_calc:,.2f} €** &nbsp;&nbsp;|&nbsp;&nbsp; 🌲 Papel: **{total_papel_cub_calc:,.2f} €**")

# --- PANEL DERECHO: TOTALES ---
with col_tot:
    with st.container(border=True):
        st.markdown("#### 💰 TOTALES PROYECTO")
        st.write("") # Espaciador
        
        total_produccion = total_prod_int_calc + total_prod_cub_calc
        total_papel = total_papel_int_calc + total_papel_cub_calc
        total_edicion = total_produccion + total_papel
        coste_unitario = total_edicion / tirada

        # Mostramos los totales parciales usando las métricas nativas de Streamlit
        st.metric(label="🏭 Total Producción", value=f"{total_produccion:,.2f} €")
        st.metric(label="🌲 Total Papel", value=f"{total_papel:,.2f} €")
        st.metric(label="📚 TOTAL EDICIÓN", value=f"{total_edicion:,.2f} €")
        
        st.divider()
        
        # Caja final súper destacada
        st.success(f"""
        <div style='text-align: center'>
            <p style='margin-bottom: 0px; font-size: 1.1rem;'>COSTE UNITARIO</p>
            <h1 style='margin-top: 0px; font-size: 2.8rem;'>{coste_unitario:,.3f} €</h1>
        </div>
        """, icon="✅")
