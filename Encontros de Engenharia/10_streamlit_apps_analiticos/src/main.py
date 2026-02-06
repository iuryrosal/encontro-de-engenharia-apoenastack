import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
import time

# print("Oi")

# answer = {}

# with st.form("formulario"):

#     answer["name"] = st.text_input("Seu Nome Completo")

#     answer["feedback"] = st.text_area("seu feedback")

#     submit_form = st.form_submit_button("Submit")
#     if submit_form:
#         if not all(answer.values()):
#             st.warning("Precisa preencher todos os campos!")
#         else:
#             st.balloons()

# st.write(answer)


# print("Ola")

# ==========================================================
# Problema da recarga de código após click no botão
# ==========================================================

# if "contador" not in st.session_state:
#     st.session_state.contador = 0

# st.write("Contador aqui (1): ", st.session_state.contador)

# button_click = st.button("Esse é um contador!")
# if button_click:
#     st.session_state.contador += 1

# st.write("Contador aqui (2): ", st.session_state.contador)

# ==========================================
# GRÁFICOS

# data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["A", "B", "C"]
# )

# st.write(data)

# # Gráfico de Área
# st.area_chart(data)

# # Gráfico de Barra
# st.bar_chart(data)

# # Gráfico de Linha
# st.line_chart(data)

# ==========================================
# MATPLOTLIB
# fig, ax = plt.subplots()
# ax.plot(data["A"], label="A")
# ax.plot(data["B"], label="B")
# ax.plot(data["C"], label="C")
# ax.set_title("Pyplot Line Chart")
# ax.legend()

# st.pyplot(fig)

# ==========================================
# SEABORN

# flights = sb.load_dataset("flights")
# st.write(flights.head())

# fig, ax = plt.subplots()
# may_flights = flights.query("month == 'May'")
# ax = sb.lineplot(data=may_flights, x="year", y="passengers")
# ax.set_title("Titulo Teste")
# st.pyplot(fig)

# ==========================================
# PLOTLY
# df = px.data.iris()
# fig = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     size="petal_length",
#     hover_data=["petal_width"],
# )

# event = st.plotly_chart(fig, key="iris", on_select="rerun")

# event.selection


# ==========================================
# ELEMENT ID STREAMLIT
# st.button("OK", key="btn1")
# st.button("OK", key="btn2")

# ==============================================
# CACHE DATA
# @st.cache_data
# def load_data():
#     print("carregando dados...")
#     time.sleep(3)
#     flights = sb.load_dataset("flights")
#     return flights

# st.write(load_data())

# st.button("OK")

@st.cache_resource
def load_file(file="example.txt"):
    print("carrega arquivo")
    file = open(file, "+a")
    return file

file = load_file()

if st.button("Incrementar"):
    file.write("Ola \n")
    file.flush()
    st.write("Incrementou..")

if st.button("Ler"):
    file.seek(0)
    st.write(file.read())

if st.button("Fechar"):
    file.close()