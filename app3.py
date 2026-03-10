import streamlit as st
import pandas as pd

st.title("Min anden Streamlit-app")
st.write("Velkommen til datavisualisering!")

df = pd.read_csv("Titanic.csv")

st.write(df.head(10))
st.write(df.describe())
st.write(df.info())

df['Survived'].value_counts()

antal_1 = (df['Survived'] == 1).sum()
antal_0 = (df['Survived'] == 0).sum()

st.markdown(f"<p><span style='color:red; font-weight:bold;'>Der er {antal_0} døde</span>,<span style='color:green;'> og {antal_1} overlevende</span></p>", unsafe_allow_html=True)

st.write(df['Survived'].value_counts(normalize=True))