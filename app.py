import streamlit as st
import pandas as pd

st.set_page_config(page_title="Presupuestador LAMBE EDICIONES", layout="wide")

st.title("Calculadora de Presupuestos - LAMBE EDICIONES")

# --- SECCIÓN 1: DATOS DE ENTRADA ---
st.header("1. Datos de Entrada")
col1, col2, col3, col4 = st.columns(4)
with col1:
    tirada = st.number_input("Tirada (unidades)", min_value=1, value=15000, step=100)
with col2:
    paginas_interior = st.number_input("Páginas Interior", min_value=1, value=192)
with col3:
    paginas_cubierta = st.number_input("Páginas Cubierta", min_value=1, value=4)
with col4:
    pliegos_interior = st.number_input("Pliegos Interior (Nº)", min_value=1, value=12)

st.markdown("---")

# --- SECCIÓN 2: PARÁMETROS TÉCNICOS ---
st.header("2. Parámetros Técnicos")

col_int, col_cub = st.columns(2)

# PARÁMETROS INTERIOR
with col_int:
    st.subheader("INTERIOR")
    ancho_int = st.number_input("Ancho Interior (cm)", value=80.0)
    largo_int = st.number_input("Largo Interior (cm)", value=63.0)
    gramaje_int = st.number_input("Gramaje Interior (g/m2)", value=150.0)
    precio_papel_int = st.number_input("Precio Papel Interior (€/kg)", value=1.02, format="%.3f")
    fijos_imp_int = st.number_input("Fijos Impresión Interior (plancha)", value=250.0)
    sucesivos_imp_int = st.number_input("Sucesivos Impresión Interior (€/1k)", value=10.0)
    merma_fija_int = st.number_input("Merma Papel Fija Interior", value=2350.0)
    merma_suc_int = st.number_input("Merma Papel Sucesivo Interior", value=1.08)
    encuadernacion_int = st.number_input("Encuadernación Interior", value=129.6)

# PARÁMETROS CUBIERTA
with col_cub:
    st.subheader("CUBIERTA")
    ancho_cub = st.number_input("Ancho Cubierta (cm)", value=70.0)
    largo_cub = st.number_input("Largo Cubierta (cm)", value=100.0)
    gramaje_cub = st.number_input("Gramaje Cubierta (g/m2)", value=350.0)
    precio_papel_cub = st.number_input("Precio Papel Cubierta (€/kg)", value=1.20, format="%.3f")
    fijos_imp_cub = st.number_input("Fijos Impresión Cubierta (€)", value=250.0)
    sucesivos_imp_cub = st.number_input("Sucesivos Impresión Cubierta (€/1k)", value=110.0)
    merma_fija_cub = st.number_input("Merma Papel Fija Cubierta", value=500.0)
    merma_suc_cub = st.number_input("Merma Papel Sucesivo Cubierta", value=1.10)
    encuadernacion_cub = st.number_input("Encuadernación Cubierta", value=27.5)

# --- CÁLCULOS INTERMEDIOS ---
# Peso de la hoja (kg) = (ancho * largo * gramaje) / 10,000,000
peso_hoja_int = (ancho_int * largo_int * gramaje_int) / 10000000
precio_hoja_int = peso_hoja_int * precio_papel_int

peso_hoja_cub = (ancho_cub * largo_cub * gramaje_cub) / 10000000
precio_hoja_cub = peso_hoja_cub * precio_papel_cub

# Costes Interior
prod_fijos_int = fijos_imp_int * pliegos_interior
prod_suc_int = (sucesivos_imp_int * pliegos_interior) + encuadernacion_int
papel_fijos_int = merma_fija_int * pliegos_interior * precio_hoja_int
papel_suc_int = pliegos_interior * merma_suc_int * precio_hoja_int * 1000

total_prod_int_calc = prod_fijos_int + (prod_suc_int * (tirada / 1000))
total_papel_int_calc = papel_fijos_int + (papel_suc_int * (tirada / 1000))

# Costes Cubierta
prod_fijos_cub = fijos_imp_cub
prod_suc_cub = sucesivos_imp_cub + encuadernacion_cub
papel_fijos_cub = merma_fija_cub * precio_hoja_cub
# Nota: La constante 250 que se observa en tu Excel original para la cubierta equivale a 1000 / 4 (portadas por pliego)
papel_suc_cub = merma_suc_cub * precio_hoja_cub * 250 

total_prod_cub_calc = prod_fijos_cub + (prod_suc_cub * (tirada / 1000))
total_papel_cub_calc = papel_fijos_cub + (papel_suc_cub * (tirada / 1000))

st.markdown("---")

# --- SECCIÓN 3: RESUMEN DE COSTES ---
st.header("3. Resumen de Costes")

col_res1, col_res2 = st.columns(2)

with col_res1:
    st.subheader("INTERIOR")
    st.write(f"**PRODUCCIÓN - Fijos:** {prod_fijos_int:,.2f} €")
    st.write(f"**PRODUCCIÓN - Sucesivos:** {prod_suc_int:,.2f} €")
    st.write(f"**Subtotal Producción:** {total_prod_int_calc:,.2f} €")
    st.write(f"**PAPEL - Fijos:** {papel_fijos_int:,.2f} €")
    st.write(f"**PAPEL - Sucesivos:** {papel_suc_int:,.2f} €")
    st.write(f"**Subtotal Papel:** {total_papel_int_calc:,.2f} €")

with col_res2:
    st.subheader("CUBIERTA")
    st.write(f"**PRODUCCIÓN - Fijos:** {prod_fijos_cub:,.2f} €")
    st.write(f"**PRODUCCIÓN - Sucesivos:** {prod_suc_cub:,.2f} €")
    st.write(f"**Subtotal Producción:** {total_prod_cub_calc:,.2f} €")
    st.write(f"**PAPEL - Fijos:** {papel_fijos_cub:,.2f} €")
    st.write(f"**PAPEL - Sucesivos:** {papel_suc_cub:,.2f} €")
    st.write(f"**Subtotal Papel:** {total_papel_cub_calc:,.2f} €")

st.markdown("---")

# --- SECCIÓN 4: TOTALES ---
st.header("4. Totales del Proyecto")

total_fijos = prod_fijos_int + prod_fijos_cub + papel_fijos_int + papel_fijos_cub
total_sucesivos = prod_suc_int + prod_suc_cub + papel_suc_int + papel_suc_cub

total_produccion = total_prod_int_calc + total_prod_cub_calc
total_papel = total_papel_int_calc + total_papel_cub_calc
total_edicion = total_produccion + total_papel
coste_unitario = total_edicion / tirada

col_tot1, col_tot2, col_tot3 = st.columns(3)
col_tot1.metric("TOTAL PRODUCCIÓN", f"{total_produccion:,.2f} €")
col_tot2.metric("TOTAL PAPEL", f"{total_papel:,.2f} €")
col_tot3.metric("TOTAL EDICIÓN", f"{total_edicion:,.2f} €")

st.success(f"### COSTE UNITARIO: {coste_unitario:,.3f} € / unidad")
