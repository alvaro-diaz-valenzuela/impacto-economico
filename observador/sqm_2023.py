import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd


def vee():
    pais = pd.read_excel("data/sqm.xlsx", sheet_name="PAIS")
    agno = st.selectbox("Selecciona el año", options=["2022", "2023"])
    total = pais[f"Año {agno}"].sum()
    fig = px.bar(pais, x="Pagos", y=f"Año {agno}", title=f"VEE (en Chile) - USD {total:,.0f} millones")
    st.plotly_chart(fig)


def impacto_economico():
    agno2 = st.selectbox("Selecciona el año", key="agno2", options=["2022", "2023"])
    paisa = pd.read_excel("data/sqm.xlsx", sheet_name="PAISa")
    impacto = paisa.loc[paisa["Glosa"] == "IMPACTO ECON", f"A{agno2}"].iloc[0]
    fig = go.Figure(go.Waterfall(
        name="VED",
        orientation="v",
        measure=list(paisa["Measure"]),
        x=list(paisa["Glosa"]),
        y=list(paisa[f"A{agno2}"]),
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))

    fig.update_layout(
        title=f"Impacto Económico {agno2} - {impacto:,.0f} millones USD",
        showlegend=True
    )

    st.plotly_chart(fig)


def pagos_estado():
    no = pd.read_excel("data/sqm.xlsx", sheet_name="NO")
    no_ok = no[(no.Glosa == "Renta") | (no.Glosa == "IVA")]
    fig = px.bar(
        no_ok,
        x=["Año"],
        y="Valor",
        color="Glosa",
        title=f"Pagos al Estado (millones de USD"
    )
    st.plotly_chart(fig)


def impulso_empleo():
    no2 = pd.read_excel("data/sqm.xlsx", sheet_name="NO2")
    fig = px.bar(
        no2,
        x=["Año"],
        y="Valor",
        color="Glosa",
        title="Impulso al Empleo (2019 - 2023)"
    )
    st.plotly_chart(fig)


def empleo_local_importado():
    no2a = pd.read_excel("data/sqm.xlsx", sheet_name="NO2a")
    fig = px.bar(
        no2a,
        x="Glosa",
        y="Valor",
        color="Región",
        title="Empleo Local vs Importado - Año 2023 (Nº Personas)"
    )
    st.plotly_chart(fig)


def valor_irradiado():
    agno3 = st.selectbox("Selecciona el año", key="agno3", options=[2022, 2023])
    paisb = pd.read_excel("data/sqm.xlsx", sheet_name="PAISb")
    paisb_ok = paisb[paisb.Agno == agno3].copy()
    total = paisb_ok["Valor"].sum()
    fig = px.treemap(paisb_ok, path=[px.Constant("Todos"), 'Agno', 'Glosa'], values='Valor', hover_data="Valor")
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(
        title=f"Valor Irradiado {agno3}: {total:,.0f} millones USD",
        margin=dict(t=50, l=25, r=25, b=25)
    )
    st.plotly_chart(fig)


col1, col2 = st.columns(2, vertical_alignment="bottom", border=True)

with col1:
    impacto_economico()

with col2:
    pagos_estado()

col3, col4 = st.columns(2, vertical_alignment="bottom", border=True)
with col3:
    empleo_local_importado()

with col4:
    vee()

col5, col6 = st.columns(2, border=True, vertical_alignment="bottom")
with col5:
    valor_irradiado()

with col6:
    impulso_empleo()
