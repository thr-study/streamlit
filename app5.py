import plotly.express as px
import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'lat': [41.72556],
    'lon': [49.94694]
})

st.map(df)

df = px.data.gapminder().query("country == 'Denmark'")

fig = px.line(df, x="year", y="lifeExp",
              title="Forventet levealder i Danmark")
st.plotly_chart(fig, use_container_width=True)


col1, col2, col3 = st.columns(3)

col1.metric("Temperatur", "21°C", "+1.2°C")
col2.metric("Fugtighed", "56%", "-3%")
col3.metric("Vind", "4.2 m/s", "+0.4")


df = pd.DataFrame({"Navn": ["Anna", "Bent"], "Point": [12, 8]})
st.data_editor(df)

text = "data streamlit python data visualisering htx undervisning"
wc = WordCloud(width=500, height=300).generate(text)

fig, ax = plt.subplots()
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)


valg = st.selectbox(
    "Vælg en mulighed:",
    ["Titanic", "Overlevet", "Død", "Mand", "Kvinde"]
)

st.write("Du valgte:", valg)

