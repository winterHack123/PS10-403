import streamlit as st
from streamlit_lottie import st_lottie


# ---- LOAD ASSETS ----
lottie_coding1 = "https://lottie.host/0cb996b4-4a94-480a-b0f3-4cb6508b4b94/dddajgyDoz.json"
lottie_coding2 = "https://lottie.host/1240fabd-1a2f-4c8b-baa3-18dc4dca7079/b3qCPSC1SU.json"

st.set_page_config(page_title="FinnCut", page_icon="🎬", layout="wide")



with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("🎬 FinnCut")
        st.subheader("LLM powered YT Short generator")
    with right_column:
        st_lottie(lottie_coding2, height=300, key="browsing")

