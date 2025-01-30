import streamlit as st
import json

from models import models


st.header("Datos Básicos de la Empresa", divider="gray")

regiones = [
    "AP", "TA", "AN", "AT", "CO",
    "VA", "RM", "OH", "MA", "ÑU",
    "BB", "LA", "LL", "AY", "MA"
]


col1, col2 = st.columns(2)
with col1:
    nombre_empresa = st.text_input("Nombre de la Empresa", st.session_state.user["nombre_empresa"], disabled=True)
    region_matriz = st.selectbox("Región Casa Matriz", regiones)
with col2:
    rut_empresa = st.text_input("Rut Empresa", st.session_state.user["rut_empresa"], disabled=True)
    regiones_opera = st.multiselect("Regiones Donde Opera", regiones)

if st.button("Aceptar"):
    empresa = models.Empresa(
        nombre_empresa=nombre_empresa,
        region_matriz=region_matriz,
        rut_empresa=rut_empresa,
        regiones_opera=regiones_opera if len(regiones_opera) > 0 else None
    )

    try:
        empresa_json = empresa.model_dump()
        with open(f'./data/{rut_empresa}.json', 'w', encoding='utf-8') as f:
            json.dump(empresa_json, f, ensure_ascii=False, indent=4)
        st.success("Data grabada correctamente")
    except Exception as e:
        st.error("Sucedió un error al grabar la data: {str(e)}")
