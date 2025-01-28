import streamlit as st

st.header("Datos Anuales")
st.divider()

agno = st.number_input("Datos para el Año", min_value=2010, max_value=2025, step=1)
with st.expander("### Ventas e Impuestos", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        ventas = st.number_input("Ventas (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
        exportaciones = st.number_input("Exportaciones (MM USD)", min_value=0, max_value=1_000_000_000, step=1)
        importaciones = st.number_input("Importaciones (MM USD)", min_value=0, max_value=1_000_000_000, step=1)
    with col2:
        primera_cat = st.number_input("Pago 1ra Categoría (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
        iva = st.number_input("Pago IVA (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
        otros_impuestos = st.number_input("Pago Otros Impuestos (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)

with (st.expander("### Proveedores de Bienes", expanded=True)):
    col1, col2, col3 = st.columns(3)
    with col1:
        num_proveedores_bienes = st.number_input(
            "Número Proveedores Bienes en Chile", min_value=0, max_value=1_000, step=1)
        insumos = st.multiselect("Insumos", options=["Químicos", "Explosivos", "Repuestos"])
        gasto_total_bienes = st.number_input("Gasto Bienes (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
    with col2:
        num_local_bienes = st.number_input("Número Proveedores Locales Bienes", min_value=0, max_value=1_000, step=1)
        gasto_local_bienes = st.number_input(
            "Gasto Proveedores Locales Bienes (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
    with col3:
        num_proveedores_internacional_bienes = st.number_input(
            "Número Proveedores Internacionales Bienes", min_value=0, max_value=1_000, step=1)
        gasto_internacional_bienes = st.number_input(
            "Gasto Proveedores Internacionales Bienes (MM USD)", min_value=0, max_value=1_000_000_000, step=1)

with ((st.expander("### Proveedores de Servicios", expanded=True))):
    col1, col2, col3 = st.columns(3)
    with col1:
        num_proveedores_servicios = st.number_input(
            "Número Proveedores Servicios en Chile", min_value=0, max_value=1_000, step=1)
        servicios = st.multiselect("Servicios", options=["Financieros", "Legales", "RRHH"])
        gasto_total_servicios = st.number_input(
            "Gasto Servicios (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
    with col2:
        num_local_servicios = st.number_input(
            "Número Proveedores Locales Servicios", min_value=0, max_value=1_000, step=1)
        gasto_local = st.number_input(
            "Gasto Proveedores Locales Servicios (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
    with col3:
        num_internacional = st.number_input(
            "Número Proveedores Internacionales Servicios", min_value=0, max_value=1_000, step=1)
        gasto_internacional = st.number_input(
            "Gasto Proveedores Internacionales Servicios (MM USD)", min_value=0, max_value=1_000_000_000, step=1)
