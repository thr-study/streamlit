import streamlit as st
import pandas as pd
import altair as alt

st.title("Min anden Streamlit-app")
st.write("Velkommen til datavisualisering!")

df = pd.read_csv("Titanic.csv")

st.write(df.head(10))
st.write(df.describe())
st.write(df.info())

df['Survived'].value_counts()

antal_1 = (df['Survived'] == 1).sum()
antal_0 = (df['Survived'] == 0).sum()

st.error(f"Der er {antal_0} døde, og {antal_1} overlevende")

st.write(df['Survived'].value_counts(normalize=True))

# Gør alder numerisk
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

mask = df["Age"].between(20, 30, inclusive="both") & (df["Survived"] == 1)
df_20_30_surv = df[mask]

antal = df_20_30_surv.shape[0]

mask2 = df["Age"].between(20, 30, inclusive="both") & (df["Survived"] == 0)
df_20_30_dead = df[mask2]

antal2 = df_20_30_dead.shape[0]

st.warning(f"Antal der var mellem 20 og 30 og overlevede er {antal}")

# Kvider mellem 20 og 30, der overlevede og døde

mask = df["Age"].between(20, 30, inclusive="both") & (df["Survived"] == 1) & (df["Sex"].str.lower().isin(["female", "f"]))
df_kvinder_20_30_surv = df[mask]
femal_surv = df_kvinder_20_30_surv.shape[0]

mask = df["Age"].between(20, 30, inclusive="both") & (df["Survived"] == 0) & (df["Sex"].str.lower().isin(["female", "f"]))
df_kvinder_20_30_dead = df[mask]
femal_dead = df_kvinder_20_30_dead.shape[0]

# mænd mellem 20 og 30 der overlevede og døde

mask = df["Age"].between(20, 30, inclusive="both") & (df["Survived"] == 1) & (df["Sex"].str.lower().isin(["male", "m"]))
df_maend_20_30_surv = df[mask]
mal_surv = df_maend_20_30_surv.shape[0]

mask = df["Age"].between(20, 30, inclusive="both") & (df["Survived"] == 0) & (df["Sex"].str.lower().isin(["male", "m"]))
df_maend_20_30_dead = df[mask]
mal_dead = df_maend_20_30_dead.shape[0]

st.success(f"Antal Kvinder der var mellem 20 og 30 og overlevede er {femal_surv}")


df2 = pd.DataFrame({
    'Status': ['Død', 'Død', 'Overlevet', 'Overlevet'],
    'Køn': ['Mand - 20 til 30', 'Kvinde - 20 til 30', 'Mand - 20 til 30', 'Kvinde - 20 til 30'],
    'Antal': [mal_dead, femal_dead , mal_surv, femal_surv]
})

chart = alt.Chart(df2).mark_bar().encode(
    x='Status',
    y='Antal',
    color='Køn',
    tooltip=['Status', 'Køn', 'Antal']
)

st.altair_chart(chart, use_container_width=True)

df = pd.DataFrame({
    'lat': [41.72556],
    'lon': [49.94694]
})

st.map(df)

df = pd.DataFrame({
    'lat': [55.71068],
    'lon': [9.53946]
})

st.map(df)