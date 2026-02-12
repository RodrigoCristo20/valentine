import streamlit as st
import random

st.set_page_config(page_title="Pergunta Important", page_icon="🦖")


st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    h1 {
        color: #c9184a;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Oi Ticha")
st.write("### Tenho uma pergunta muito importante para te fazer...")

st.image("fototicha.jpeg", caption="ganda testa", use_container_width=True)

st.write("## Will you be my Valentine? (dia 21) (e sempre)")

col1, col2 = st.columns(2)

with col1:
    if st.button("SIM! 😍"):
        st.balloons()
        st.success("Boa resposta!")
        st.write("perioooddd")

with col2:
    if st.button("Não... 😢"):
        respostas_engracadas = [
            "Resposta de merda. Tenta de novo.",
            "Tás maluca",
            "Erro 404: Opção 'Não' indisponível.",
            "Carrega no sim parva"
        ]
        st.error(random.choice(respostas_engracadas))