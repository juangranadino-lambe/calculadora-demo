import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Presupuestador LAMBE", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DEFINITIVO (Flexbox para igualar alturas)
st.markdown("""
<style>
    /* Reducimos el espacio inútil arriba */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
        max-width: 95%;
    }
    
    /* 1. Hacemos que las columnas sean flexibles */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
    }
    
    /* 2. LA MAGIA: Obligamos a nuestras cajas a crecer hasta abajo (flex-grow: 1) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 4px solid #22c55e !important;
        background-color: #ebfef0 !important;
        border-radius: 15px !important;
        flex-grow: 1 !important; 
    }
    
    /* 3. Hacemos transparente el fondo nativo de Streamlit para que se vea nuestro color */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        background-color: transparent !important;
    }
    
    h3, h4 {
        padding-bottom: 0rem;
        margin-bottom: 0rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 📊 Calculadora de Presupuestos LAMBE")
st.write("") 

# 3. DIVISIÓN PRINCIPAL
col_izq, col_der = st.columns([2.2, 1], gap="large")

# ==========================================
# COLUMNA IZQUIERDA: TODOS LOS INPUTS
# ==========================================
with col_izq:
    with st.container(border=True):
        st.markdown("### ⚙️ Datos a introducir")
        st.write("")
        
        c1, c2, c3, c4 = st.columns(4)
        tirada = c1.number_input("📦 Tirada (uds)", min_value=1, value=15000, step=100)
        paginas_interior = c2.number_input("📄 Págs Interior", min_value=1, value=192, step=1)
        paginas_cubierta = c3.number_input("📘 Págs Cubierta", min_value=1, value=4, step=1)
        pliegos_interior = c4.number_input("📑 Pliegos", min_value=1, value=12, step=1)

        st.divider()
        
        col_int, col_cub = st.columns(2)
        
        with col_int:
            st.markdown("#### 📄 INTERIOR")
            ci1, ci2 = st.columns(2)
            with ci1:
                ancho_int = st.number_input("Ancho (cm)", value=80.0, step=1.0)
                largo_int = st.number_input("Largo (cm)", value=63.0, step=1.0)
                gramaje_int = st.number_input("Gramaje (g/m2)", value=150.0, step=1.0)
                precio_papel_int = st.number_input("Papel (€/kg)", value=1.02, step=0.01, format="%.3f")
                encuadernacion_int = st.number_input("Encuadernación (€)", value=129.6, step=1.0)
            with ci2:
                fijos_imp_int = st.number_input("Fijos Imp. (plancha)", value=250.0, step=1.0)
                sucesivos_imp_int = st.number_input("Suc. Imp. (€/1k)", value=10.0, step=1.0)
                merma_fija_int = st.number_input("Merma Fija (hojas)", value=2350.0, step=1.0)
                merma_suc_int = st.number_input("Merma Sucesiva", value=1.08, step=0.01)

        with col_cub:
            st.markdown("#### 📘 CUBIERTA")
            cc1, cc2 = st.columns(2)
            with cc1:
                ancho_cub = st.number_input("Ancho (cm) C.", value=70.0, step=1.0)
                largo_cub = st.number_input("Largo (cm) C.", value=100.0, step=1.0)
                gramaje_cub = st.number_input("Gramaje (g/m2) C.", value=350.0, step=1.0)
                precio_papel_cub = st.number_input("Papel (€/kg) C.", value=1.20, step=0.01, format="%.3f")
                encuadernacion_cub = st.number_input("Encuadernación (€) C.", value=27.5, step=1.0)
            with cc2:
                fijos_imp_cub = st.number_input("Fijos Imp. (€) C.", value=250.0, step=1.0)
                sucesivos_imp_cub = st.number_input("Suc. Imp. (€/1k) C.", value=110.0, step=1.0)
                merma_fija_cub = st.number_input("Merma Fija (hojas) C.", value=500.0, step=1.0)
                merma_suc_cub = st.number_input("Merma Sucesiva C.", value=1.10, step=0.01)

# 4. CÁLCULOS MATEMÁTICOS OCULTOS
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
    with st.container(border=True):
        st.markdown("<h3 style='margin-top:0;'>💰 Resultados</h3>", unsafe_allow_html=True)
        
        # HTML Seguro y limpio
        html_resultados = f"""
        <div style="text-align: center;">
            <p style="color: #166534; font-size: 1.2rem; font-weight: bold; margin: 15px 0 0 0;">💶 COSTE UNITARIO</p>
            <h1 style="color: #16a34a; font-size: 4rem; font-weight: 900; margin: 0; line-height: 1.1;">{coste_unitario:,.3f} €</h1>
            <hr style="border-color: #22c55e; margin: 25px 0;">
            <p style="color: #166534; font-size: 1.2rem; font-weight: bold; margin: 0;">📚 TOTAL EDICIÓN</p>
            <h2 style="color: #15803d; font-size: 2.5rem; font-weight: 800; margin: 0;">{total_edicion:,.2f} €</h2>
            <div style="margin-top: 30px; text-align: left; background-color: #ffffff; padding: 15px; border-radius: 10px; border: 2px solid #22c55e;">
                <p style="margin: 8px 0; font-size: 1.1rem; color: #374151;">🏭 <b>Total Producción:</b> {total_produccion:,.2f} €</p>
                <p style="margin: 8px 0; font-size: 1.1rem; color: #374151;">🌲 <b>Total Papel:</b> {total_papel:,.2f} €</p>
                <hr style="border-color: #bbf7d0; margin: 10px 0;">
                <p style="margin: 8px 0; font-size: 1rem; color: #6b7280;">📝 Subtotal Interior: {(total_prod_int_calc + total_papel_int_calc):,.2f} €</p>
                <p style="margin: 8px 0; font-size: 1rem; color: #6b7280;">📗 Subtotal Cubierta: {(total_prod_cub_calc + total_papel_cub_calc):,.2f} €</p>
            </div>
        </div>
        """
        st.markdown(html_resultados, unsafe_allow_html=True)
