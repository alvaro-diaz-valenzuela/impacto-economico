import streamlit as st
import json

from models import models


insumos = ["Químicos", "Explosivos", "Repuestos"]


st.header("Datos Anuales", divider="gray")

agno = st.number_input("Datos para el Año", min_value=2010, max_value=2025, step=1)

with st.expander("### Ventas e Impuestos", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        ventas = st.number_input("Ventas (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
        exportaciones = st.number_input("Exportaciones (MM USD)", min_value=0, max_value=1_000_000_000, step=1)
        importaciones = st.number_input("Importaciones (MM USD)", min_value=0, max_value=1_000_000_000, step=1)
    with col2:
        primera_cat = st.number_input("Pago 1ra Categoría (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
        iva = st.number_input("Pago IVA (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
        otros_impuestos = st.number_input("Pago Otros Impuestos (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)

with (st.expander("### Proveedores de Bienes", expanded=False)):
    col1, col2, col3 = st.columns(3)
    with col1:
        num_proveedores_bienes = st.number_input(
            "Número Proveedores Bienes en Chile", min_value=0, max_value=1_000, step=1)
        insumos = st.multiselect("Insumos", options=insumos)
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

with ((st.expander("### Proveedores de Servicios", expanded=False))):
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
        gasto_local_servicios = st.number_input(
            "Gasto Proveedores Locales Servicios (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)
    with col3:
        num_proveedores_internacional_servicios = st.number_input(
            "Número Proveedores Internacionales Servicios", min_value=0, max_value=1_000, step=1)
        gasto_internacional_servicios = st.number_input(
            "Gasto Proveedores Internacionales Servicios (MM USD)", min_value=0, max_value=1_000_000_000, step=1)

with ((st.expander("### Gasto e Inversión en Personas", expanded=False))):
    col1, col2 = st.columns(2)
    with col1:
        remuneraciones_brutas = st.number_input(
            "Remuneraciones Brutas (MM CLP)", min_value=0, max_value=1_000, step=1)
        num_empleados_permanentes = st.number_input(
            "Número de Empleados Permanentes", min_value=0, max_value=1_000_000_000, step=1)
        num_empleados_esporadicos = st.number_input(
            "Número de Empleados Esporádicos (Promedio Anual)", min_value=0, max_value=1_000_000_000, step=1)
    with col2:
        inversion_comunidades = st.number_input(
            "Inversión en Comunidades (MM CLP)", min_value=0, max_value=1_000, step=1)
        inversion_ambiental = st.number_input(
            "Inversión Ambiental (MM CLP)", min_value=0, max_value=1_000_000_000, step=1)

if st.button("Aceptar"):
    rut_empresa = st.session_state.user["rut_empresa"]
    try:
        with open(f'./data/{rut_empresa}.json', 'r') as file:
            data = json.load(file)
            empresa = models.Empresa(**data)
    except Exception as e:
        st.error(f"No se encuentran los datos de la empresa {rut_empresa}")

    ventas_impuestos = models.VentasImpuestos(
        ventas=ventas,
        exportaciones=exportaciones,
        importaciones=importaciones,
        primera_cat=primera_cat,
        iva=iva,
        otros_impuestos=otros_impuestos,
    )

    proveedores_bienes = models.ProveedoresBienes(
        num_proveedores_bienes=num_proveedores_bienes,
        insumos=insumos if len(insumos) > 0 else None,
        gasto_total_bienes=gasto_total_bienes,
        num_local_bienes=num_local_bienes,
        gasto_local_bienes=gasto_local_bienes,
        num_proveedores_internacional_bienes=num_proveedores_internacional_bienes,
        gasto_internacional_bienes=gasto_internacional_bienes,
    )

    proveedores_servicios = models.ProveedoresServicios(
        num_proveedores_servicios=num_proveedores_servicios,
        servicios=servicios if len(servicios) > 0 else None,
        gasto_total_servicios=gasto_total_servicios,
        num_local_servicios=num_local_servicios,
        gasto_local_servicios=gasto_local_servicios,
        num_proveedores_internacional_servicios=num_proveedores_internacional_servicios,
        gasto_internacional_servicios=gasto_internacional_servicios,
    )

    gasto_inversion_personas = models.GastoInversionPersonas(
        remuneraciones_brutas=remuneraciones_brutas,
        num_empleados_permanentes=num_empleados_permanentes,
        num_empleados_esporadicos=num_empleados_esporadicos,
        inversion_comunidades=inversion_comunidades,
        inversion_ambiental=inversion_ambiental,
    )

    data_anual = models.DataAnual(
        agno=agno,
        empresa=empresa,
        ventas_impuestos=ventas_impuestos,
        proveedores_bienes=proveedores_bienes,
        proveedores_servicios=proveedores_servicios,
        gasto_inversion_personas=gasto_inversion_personas,
    )

    try:
        data_anual_json = data_anual.model_dump()
        with open(f'./data/data_anual_{agno}_{rut_empresa}.json', 'w', encoding='utf-8') as f:
            json.dump(data_anual_json, f, ensure_ascii=False, indent=4)
        st.success("Data grabada correctamente")
    except Exception as e:
        st.error("Sucedió un error al grabar la data: {str(e)}")
