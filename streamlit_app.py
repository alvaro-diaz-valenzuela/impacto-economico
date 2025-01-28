import streamlit as st

# st.set_page_config(layout="wide")


if "user" not in st.session_state:
    st.session_state.user = None
    st.session_state.role = None

ROLES = [None, "Informador", "Observador", "Admin"]

usuarios = [
    {
        "rut": "10000000-1",
        "nombre_empresa": "ACME",
        "rut_empresa": "44111777-R",
        "rol": ROLES[1],
        "password": "password",
    },
    {
        "rut": "10000000-2",
        "nombre_empresa": "ACME",
        "rut_empresa": "44111777-R",
        "rol": ROLES[2],
        "password": "password",
    },
    {
        "rut": "10000000-3",
        "nombre_empresa": "MAX",
        "rut_empresa": "90000000-L",
        "rol": ROLES[2],
        "password": "password",
    }
]


def login():
    st.header("Ingreso")
    empresa = st.selectbox("RUT Empresa", set([r["rut_empresa"] for r in usuarios]))
    usuario = st.selectbox("RUT Usuario", [r["rut"] for r in usuarios if r["rut_empresa"] == empresa])
    rol = [u["rol"] for u in usuarios if u["rut"] == usuario ][0]
    rol_display = st.text_input(
        "Rol Usuario",
        value=rol,
        disabled=True
    )
    password = st.text_input("Password", type="password")
    if st.button("Aceptar"):
        if password != "password":
            st.error("Passwords do not match")
        else:
            st.session_state.user = [u for u in usuarios if u["rut"] == usuario][0]
            st.session_state.role = st.session_state.user["rol"]
            st.rerun()


role = st.session_state.role


def logout():
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()


logout_page = st.Page(
    logout,
    title="Salir",
    icon=":material/logout:"
)

settings = st.Page(
    "settings.py",
    title="Configuración",
    icon=":material/settings:"
)

request_1 = st.Page(
    "informador/informador_1.py",
    title="Datos Básicos",
    icon=":material/help:",
    default=(role == "Informador"),
)

request_2 = st.Page(
    "informador/informador_2.py",
    title="Ingresos y Gastos",
    icon=":material/bug_report:"
)

respond_1 = st.Page(
    "observador/observador_1.py",
    title="Dashboard 1",
    icon=":material/healing:",
    default=(role == "Observador"),
)
respond_2 = st.Page(
    "observador/observador_2.py",
    title="Dashboard 2",
    icon=":material/handyman:"
)

admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)

admin_2 = st.Page(
    "admin/admin_2.py",
    title="Admin 2",
    icon=":material/security:"
)

account_pages = [logout_page, settings]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]
admin_pages = [admin_1, admin_2]

st.title("Cálculo de Impacto Económico")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")
page_dict = {}
if role in ["Informador", "Admin"]:
    page_dict["Carga Data"] = request_pages
    page_dict["Dashboards"] = respond_pages
if role in ["Observador", "Admin"]:
    page_dict["Dashboards"] = respond_pages
if role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
