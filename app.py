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
        merma_fija_int = st.number_input("Merma Fija (hojas) Int.", value=2350.0, step=1.0)
        merma_suc_int = st.number_input("Merma Sucesiva Int.", value=1.08, step=0.01)

with col_cub:
    st.markdown("#### 📘 CUBIERTA")
    cc1, cc2 = st.columns(2)
    with cc1:
        ancho_cub = st.number_input("Ancho (cm) Cub.", value=70.0, step=1.0)
        largo_cub = st.number_input("Largo (cm) Cub.", value=100.0, step=1.0)
        gramaje_cub = st.number_input("Gramaje (g/m2) Cub.", value=350.0, step=1.0)
        precio_papel_cub = st.number_input("Papel (€/kg) Cub.", value=1.20, step=0.01, format="%.3f")
        encuadernacion_cub = st.number_input("Encuadernación (€) Cub.", value=27.5, step=1.0)
    with cc2:
        fijos_imp_cub = st.number_input("Fijos Imp. (€) Cub.", value=250.0, step=1.0)
        sucesivos_imp_cub = st.number_input("Suc. Imp. (€/1k) Cub.", value=110.0, step=1.0)
        merma_fija_cub = st.number_input("Merma Fija (hojas) Cub.", value=500.0, step=1.0)
        merma_suc_cub = st.number_input("Merma Sucesiva Cub.", value=1.10, step=0.01)

# 4. CÁLCULOS MATEMÁTICOS
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

# 5. MOSTRAR RESULTADOS GIGANTES ARRIBA DEL TODO
with resultados_superiores:
    # Banner HTML gigante
    st.markdown(f"""
        <div style="background-color: #f0fdf4; border: 3px solid #22c55e; border-radius: 15px; padding: 30px; display: flex; justify-content: space-around; align-items: center; margin-bottom: 10px;">
            <div style="text-align: center;">
                <h3 style="color: #166534; margin: 0; padding-bottom: 10px; font-size: 1.5rem;">📚 TOTAL EDICIÓN</h3>
                <h1 style="color: #15803d; margin: 0; font-size: 3rem;">{total_edicion:,.2f} €</h1>
            </div>
            <div style="width: 2px; background-color: #22c55e; height: 80px;"></div>
            <div style="text-align: center;">
                <h3 style="color: #166534; margin: 0; padding-bottom: 10px; font-size: 1.5rem;">💶 COSTE UNITARIO</h3>
                <h1 style="color: #16a34a; margin: 0; font-size: 4.5rem; font-weight: 900;">{coste_unitario:,.3f} €</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Desglose secundario debajo del banner grande
    c_desglose1, c_desglose2, c_desglose3, c_desglose4 = st.columns(4)
    c_desglose1.metric("🏭 Total Producción", f"{total_produccion:,.2f} €")
    c_desglose2.metric("🌲 Total Papel", f"{total_papel:,.2f} €")
    c_desglose3.metric("📝 Subtotal Interior", f"{(total_prod_int_calc + total_papel_int_calc):,.2f} €")
    c_desglose4.metric("📗 Subtotal Cubierta", f"{(total_prod_cub_calc + total_papel_cub_calc):,.2f} €")
