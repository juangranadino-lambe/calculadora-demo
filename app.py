import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Presupuestador LAMBE", layout="wide", initial_sidebar_state="collapsed")

# CSS REFORZADO: Obligamos a Streamlit a pintar el fondo con "!important"
st.markdown("""
<style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 1rem;
        max-width: 95%;
    }
    h3, h4 {
        padding-bottom: 0rem;
        margin-bottom: 0rem;
    }
    /* Magia obligatoria para la caja de la izquierda */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f0fdf4 !important;
        border: 3px solid #22c55e !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 📊 Calculadora de Presupuestos LAMBE")
st.write("") 

# 2. DIVISIÓN PRINCIPAL: Izquierda (Inputs) y Derecha (Resultados)
col_izq, col_der = st.columns([2.2, 1], gap="large")

# ==========================================
# COLUMNA IZQUIERDA: TODOS LOS INPUTS
# ==========================================
with col_izq:
    with st.container(border=True):
        st.markdown("### ⚙️ Datos a introducir")
        st.write("")
        
        # Datos Generales
        c1, c2, c3, c4 = st.columns(4)
        tirada = c1.number_input("📦 Tirada (uds)", min_value=1, value=15000, step=100)
        paginas_interior = c2.number_input("📄 Págs Interior", min_value=1, value=192, step=1)
        paginas_cubierta = c3.number_input("📘 Págs Cubierta", min_value=1, value=4, step=1)
        pliegos_interior = c4.number_input("📑 Pliegos", min_value=1, value=12, step=1)

        st.divider() 
        
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
                sucesivos_imp_int = st.number_input("Suc. Imp. (€/1k)", value=10.0, step=1.0, key="sii")
                merma_fija_int = st.number_input("Merma Fija (hojas)", value=2350.0, step=1.0, key="mfi")
                merma_suc_int = st.number_input("Merma Sucesiva", value=1.08, step=0.01, key="msi")

        with col_cub:
            st.markdown("#### 📘 CUBIERTA")
            cc1, cc2 = st.columns(2)
            with cc1:
                ancho_cub = st.number_input("Ancho (cm)", value=70.0, step=1.0, key="ac")
                largo_cub = st.number_input("Largo (cm)", value=100.0, step=1.0, key="lc")
                gramaje_cub = st.number_input("Gramaje (g/m2)", value=350.0, step=1.0, key="gc")
                precio_papel_cub = st.number_input("Papel (€/kg)", value=1.20, step=0.01, format="%.3f", key="pc")
                encuadernacion_cub = st.number_input("Encuadernación (€)", value=27.5, step=1.0, key="ec")
            with cc2:
                fijos_imp_cub = st.number_input("Fijos Imp. (€)", value=250.0, step=1.0, key="fic")
                sucesivos_imp_cub = st.number_input("Suc. Imp. (€/1k)", value=110.0, step=1.0, key="sic")
                merma_fija_cub = st.number_input("Merma Fija (hojas)", value=500.0, step=1.0, key="mfc")
                merma_suc_cub = st.number_input("Merma Sucesiva", value=1.10, step=0.01, key="msc")

# 3. CÁLCULOS MATEMÁTICOS OCULTOS
peso_hoja_int = (ancho_int * largo_int * gramaje_int) / 10000000
precio_hoja_int = peso_hoja_int * precio_papel_int
prod_fijos_int = fijos_imp_int * pliegos_interior
prod_suc_int = (sucesivos_imp_int * pliegos_interior) + encuadernacion_int
papel_fijos_int = merma_fija_int * pliegos_interior * precio_hoja_int
papel_suc_int = pliegos_interior * merma_suc_int * precio_hoja_int * 1000
total_prod_int_calc = prod_fijos_int + (prod_suc_int * (tirada / 1000))
total_papel_int_calc = papel_fijos_int + (papel_suc_int * (tirada / 1000))

peso_hoja_cub = (ancho_cub * largo_cub * gramaje_cub) / 10000000
precio_hoja_cub = peso_hoja_cub * precio_papel_cub
prod_fijos_cub = fijos_imp_cub
prod_suc_cub = sucesivos_imp_cub + encuadernacion_cub
papel_fijos_cub = merma_fija_cub * precio_hoja_cub
papel_suc_cub = merma_suc_cub * precio_hoja_cub * 250 
total_prod_cub_calc = prod_fijos_cub + (prod_suc_cub * (tirada / 1000))
total_papel_cub_calc = papel_fijos_cub + (papel_suc_cub * (tirada / 1000))

total_produccion = total_prod_int_calc + total_prod_cub_calc
total_papel = total_papel_int_calc + total_papel_cub_calc
total_edicion = total_produccion + total_papel
coste_unitario = total_edicion / tirada

# ==========================================
# COLUMNA DERECHA: RESULTADOS GRANDES
# ==========================================
with col_der:
    html_resultados = f"""
<div style="background-color: #f0fdf4; border: 3px solid #22c55e; border-radius: 15px; padding: 25px 20px; text-align: center; height: 100%; box-shadow: 2px 4px 10px rgba(0,0,0,0.1);">
    <p style="color: #166534; font-size: 1.2rem; font-weight: bold; margin: 0;">💶 COSTE UNITARIO</p>
    <h1 style="color: #16a34a; font-size: 4rem; font-weight: 900; margin: 0; line-height: 1.1;">{coste_unitario:,.3f} €</h1>
    <hr style="border-color: #bbf7d0; margin: 25px 0;">
    <p style="color: #166534; font-size: 1.2rem; font-weight: bold; margin: 0;">📚 TOTAL EDICIÓN</p>
    <h2 style="color: #15803d; font-size: 2.5rem; font-weight: 800; margin: 0;">{total_edicion:,.2f} €</h2>
    <div style="margin-top: 30px; text-align: left; background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #bbf7d0;">
        <p style="margin: 8px 0; font-size: 1.1rem; color: #374151;">🏭 <b>Total Producción:</b> {total_produccion:,.2f} €</p>
        <p style="margin: 8px 0; font-size: 1.1rem; color: #374151;">🌲 <b>Total Papel:</b> {total_papel:,.2f} €</p>
        <hr style="border-color: #e5e7eb; margin: 10px 0;">
        <p style="margin: 8px 0; font-size: 1rem; color: #6b7280;">📝 Subtotal Interior: {(total_prod_int_calc + total_papel_int_calc):,.2f} €</p>
        <p style="margin: 8px 0; font-size: 1rem; color: #6b7280;">📗 Subtotal Cubierta: {(total_prod_cub_calc + total_papel_cub_calc):,.2f} €</p>
    </div>
</div>
"""
    st.markdown(html_resultados, unsafe_allow_html=True)
