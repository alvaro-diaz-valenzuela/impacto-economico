import streamlit as st

st.header("Datos Básicos de la Empresa")
st.divider()

regiones = [
    "AP", "TA", "AN", "AT", "CO",
    "VA", "RM", "OH", "MA", "ÑU",
    "BB", "LA","LL", "AY", "MA"
]
col1, col2 = st.columns(2)
with col1:
    nombre_empresa = st.text_input("Nombre de la Empresa", st.session_state.user["nombre_empresa"], disabled=True)
    region_matriz = st.selectbox("Región Casa Matriz", regiones)
with col2:
    rut_empresa = st.text_input("Rut Empresa", st.session_state.user["rut_empresa"], disabled=True)
    regiones_opera = st.multiselect("Regiones Donde Opera", regiones)

