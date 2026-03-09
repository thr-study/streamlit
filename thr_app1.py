import streamlit as st
import pandas as pd

st.title("Min første Streamlit-app")
st.write("Velkommen til datavisualisering!")

uploaded_file = st.file_uploader("Upload et datasæt (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    st.write(df.tail())

