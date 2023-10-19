import pandas as pd 
import plotly.express as px
import streamlit as st

st.title("Taal Volcano SO2 Readings")


df = pd.read_csv("Taal Updated.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Year'] = df['Date'].dt.year
years =df['Year'].unique()


selected_years = st.multiselect('Select year(s)', options = years, default=years)

filter = df[df['Year'].isin(selected_years)]

fig = px.line(filter, x='Date', y='SO2', title="Chart of the Data",)

st.plotly_chart(fig, use_container_width=True)
