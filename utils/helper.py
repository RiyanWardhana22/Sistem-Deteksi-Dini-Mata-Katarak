import pandas as pd
import altair as alt
import streamlit as st

def plot_probability_chart(probabilities):
    df = pd.DataFrame({
        "Kelas": list(probabilities.keys()),
        "Probabilitas": list(probabilities.values())
    })

    chart = alt.Chart(df).mark_bar(
        color="#408a71", 
        cornerRadiusEnd=4, 
        height=25
    ).encode(
        x=alt.X('Probabilitas:Q', scale=alt.Scale(domain=[0, 100]), title='Probabilitas (%)'),
        y=alt.Y('Kelas:N', sort='-x', title=None), 
        tooltip=['Kelas', 'Probabilitas']
    ).properties(height=200)
    st.altair_chart(chart, use_container_width=True)