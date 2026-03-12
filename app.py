import streamlit as st
import pandas as pd

# 1. Configuración de página ancha
st.set_page_config(page_title="Presupuestador LAMBE", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS para reducir márgenes y evitar el scroll
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 0rem;
        }
        h4 {
            padding-top: 0rem;
            margin-bottom: -1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("### 📊 Calculadora de Presupuestos - LAMBE EDICIONES")

# --- FILA 1: DATOS DE ENTRADA (Una sola línea horizontal) ---
c1, c2, c3, c4 = st.columns(4)
tirada = c1.number_input("Tirada (unidades)", min_value=1, value=15000, step=100)
paginas_interior = c2.number_input("Páginas Interior", min_value=1, value=192)
paginas_cubierta = c3.number_input("Páginas Cubierta", min_value=1, value=4)
pliegos_interior = c4.number_input("Pliegos Interior", min_value=1, value=12)

st.divider()

# --- FILA 2: PANELES PRINCIPALES (Dividido en 3 grandes columnas) ---
# Damos proporción 1.5 al interior y cubierta, y 1 a los totales
col_int, col_cub, col_tot = st.columns([1.5, 1.5, 1])

# --- PANEL IZQUIERDO: INTERIOR ---
with col_int:
    st.markdown("#### 📄 PARÁMETROS INTERIOR")
    st.write("") # Espaciador
    # Subdividimos en 2 columnas para que los campos no ocupen tanto a lo alto
    ci1, ci2 = st.columns(2)
    with ci1:
        ancho_int = st.number_input("Ancho (cm)", value=80.0, key="a_i")
        largo_int = st.number_input("Largo (cm)", value=63.0, key="l_i")
        gramaje_int = st.number_input("Gramaje (g/m2)", value=150.0, key="g_i")
        precio_papel_int = st.number_input("Papel (€/kg)", value=1.02, format="%.3f", key="p_i")
        encuadernacion_int = st.number_input("Encuadernación (€)", value=129.6, key="e_i")
    with ci2:
        fijos_imp_int = st.number_input("Fijos Imp. (plancha)", value=250.0, key="fi_i")
        sucesivos_imp_int = st.number_input("Suc. Imp. (€/1k)", value=10.0, key="si_i")
        merma_fija_int = st.number_input("Merma Fija (hojas)", value=2350.0, key="mf_i")
        merma_suc_int = st.number_input("Merma Sucesiva", value=1.08, key="ms_i")
        
    # Cálculos ocultos Interior
    peso_hoja_int = (ancho_int * largo_int * gramaje_int) / 10000000
    precio_hoja_int = peso_hoja_int * precio_papel_int
    prod_fijos_int = fijos_imp_int * pliegos_interior
    prod_suc_int = (sucesivos_imp_int * pliegos_interior) + encuadernacion_int
    papel_fijos_int = merma_fija_int * pliegos_interior * precio_hoja_int
    papel_suc_int = pliegos_interior * merma_suc_int * precio_hoja_int * 1000
    total_prod_int_calc = prod_fijos_int + (prod_suc_int * (tirada / 1000))
    total_papel_int_calc = papel_fijos_int + (papel_suc_int * (tirada / 1000))
    
    # Resumen visual pequeño
    st.info(f"**Subtotales Interior:** Producción: {total_prod_int_calc:,.2f} € | Papel: {total_papel_int_calc:,.2f} €")

# --- PANEL CENTRAL: CUBIERTA ---
with col_cub:
    st.markdown("#### 📘 PARÁMETROS CUBIERTA")
    st.write("") # Espaciador
    cc1, cc2 = st.columns(2)
    with cc1:
        ancho_cub = st.number_input("Ancho (cm)", value=70.0, key="a_c")
        largo_cub = st.number_input("Largo (cm)", value=100.0, key="l_c")
        gramaje_cub = st.number_input("Gramaje (g/m2)", value=350.0, key="g_c")
        precio_papel_cub = st.number_input("Papel (€/kg)", value=1.20, format="%.3f", key="p_c")
        encuadernacion_cub = st.number_input("Encuadernación (€)", value=27.5, key="e_c")
    with cc2:
        fijos_imp_cub = st.number_input("Fijos Imp. (€)", value=250.0, key="fi_c")
        sucesivos_imp_cub = st.number_input("Suc. Imp. (€/1k)", value=110.0, key="si_c")
        merma_fija_cub = st.number_input("Merma Fija (hojas)", value=500.0, key="mf_c")
        merma_suc_cub = st.number_input("Merma Sucesiva", value=1.10, key="ms_c")
        
    # Cálculos ocultos Cubierta
    peso_hoja_cub = (ancho_cub * largo_cub * gramaje_cub) / 10000000
    precio_hoja_cub = peso_hoja_cub * precio_papel_cub
    prod_fijos_cub = fijos_imp_cub
    prod_suc_cub = sucesivos_imp_cub + encuadernacion_cub
    papel_fijos_cub = merma_fija_cub * precio_hoja_cub
    papel_suc_cub = merma_suc_cub * precio_hoja_cub * 250 
    total_prod_cub_calc = prod_fijos_cub + (prod_suc_cub * (tirada / 1000))
    total_papel_cub_calc = papel_fijos_cub + (papel_suc_cub * (tirada / 1000))

    # Resumen visual pequeño
    st.info(f"**Subtotales Cubierta:** Producción: {total_prod_cub_calc:,.2f} € | Papel: {total_papel_cub_calc:,.2f} €")

# --- PANEL DERECHO: TOTALES GLOBALES ---
with col_tot:
    st.markdown("#### 💰 TOTALES PROYECTO")
    st.write("") # Espaciador
    
    total_produccion = total_prod_int_calc + total_prod_cub_calc
    total_papel = total_papel_int_calc + total_papel_cub_calc
    total_edicion = total_produccion + total_papel
    coste_unitario = total_edicion / tirada

    # Cajas de métricas compactas
    st.metric("Total Producción", f"{total_produccion:,.2f} €")
    st.metric("Total Papel", f"{total_papel:,.2f} €")
    st.metric("TOTAL EDICIÓN", f"{total_edicion:,.2f} €")
    
    # Caja verde destacada para el coste final
    st.success(f"## COSTE UNITARIO\n# {coste_unitario:,.3f} €")
