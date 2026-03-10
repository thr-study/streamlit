import io
import streamlit as st
import pandas as pd

st.title("Min første Streamlit-app")
st.write("Velkommen til datavisualisering!")

uploaded_file = st.file_uploader("Upload et datasæt (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    st.write(df.tail())

    # df.info() returnerer None, fordi metoden skriver output direkte til en tekststream (stdout) 
    # i stedet for at returnere en streng eller et objekt. Når du gør st.write(df.info()), 
    # prøver Streamlit at vise returværdien – og den er None. Derfor ser du “None”.
    #
    # Såderfor skal vi bruge en tekstbuffer til at "opsnappe" tekstoutputtet, og så vise det som tekst i 
    # streamlit st.text i stedet for st.write.
    # PS '''  '''  er en streng literal og ikke en kommentar i python. Brug # eller
    # eller opret .streamlit/config.toml og tilføj 
    # 1.[runner]
    # 2.magicEnabled = false

    buf = io.StringIO()
    df.info(buf=buf)           # skriv info-teksten til buffer i stedet for stdout
    s = buf.getvalue()         # hent teksten ud
    st.text(s)                 # vis den i Streamlit