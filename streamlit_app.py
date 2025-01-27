import streamlit as st

# st.set_page_config(layout="wide")


if "user" not in st.session_state:
    st.session_state.user = None
    st.session_state.role = None

ROLES = [None, "Informador", "Observador", "Admin"]

usuarios = [{
    "rut": "10000000-1",
    "rut_empresa": "90000000-K",
    "rol": ROLES[1],
},
{
    "rut": "10000000-2",
    "rut_empresa": "90000000-K",
    "rol": ROLES[2],
},
    {
        "rut": "10000000-3",
        "rut_empresa": "90000000-L",
        "rol": ROLES[2],
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
    if st.button("Aceptar"):
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
    title="Log out",
    icon=":material/logout:"
)

settings = st.Page(
    "settings.py",
    title="Settings",
    icon=":material/settings:"
)

request_1 = st.Page(
    "request/request_1.py",
    title="Request 1",
    icon=":material/help:",
    default=(role == "Informador"),
)

request_2 = st.Page(
    "request/request_2.py",
    title="Request 2",
    icon=":material/bug_report:"
)

respond_1 = st.Page(
    "respond/respond_1.py",
    title="Respond 1",
    icon=":material/healing:",
    default=(role == "Observador"),
)
respond_2 = st.Page(
    "respond/respond_2.py",
    title="Respond 2",
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
    page_dict["Request"] = request_pages
    page_dict["Respond"] = respond_pages
if role in ["Observador", "Admin"]:
    page_dict["Respond"] = respond_pages
if role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
