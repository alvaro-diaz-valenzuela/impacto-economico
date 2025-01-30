import streamlit as st
import pandas as pd
from datetime import datetime
import json

from models import models

st.header("Datos de la Empresa", divider="gray")
today = datetime.today()
agno = st.number_input(
    "Año de la Data",
    min_value=2010,
    max_value=today.year,
    value=today.year
)
rut_empresa = st.session_state.user["rut_empresa"]

try:
    with open(f'./data/data_anual_{agno}_{rut_empresa}.json', 'r') as file:
        data = json.load(file)
        empresa = models.DataAnual(**data)
except Exception as e:
    st.error(f"No se encuentran los datos de la empresa {rut_empresa} para el año {agno}")
fx = 1000
df = pd.DataFrame([empresa.flat_numeric_dump()])
df.set_index("agno", inplace=True)
st.write("Tabla de Datos")
st.dataframe(df)
bar_df = df[["ventas", "importaciones", "exportaciones"]]
bar_df["importaciones"] *= fx
bar_df["exportaciones"] *= fx
total_impuestos = df.iloc[0]["primera_cat"] + df.iloc[0]["iva"] + df.iloc[0]["otros_impuestos"]
bar_df["total_impuestos"] = total_impuestos
tax_df = df[["primera_cat", "iva", "otros_impuestos"]]

st.header("Gráficos", divider="gray")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Ventas e Impuestos")
    st.bar_chart(bar_df, stack=False)
with col2:
    st.markdown("#### Composición Impuestos")
    st.bar_chart(tax_df)
