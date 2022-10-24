import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('World cities')

# ls in mac/ 

# create a select bar
df = pd.read_csv('worldcities.csv')
pop_filter = st.sidebar.slider('Minimal pop', 0.0, 40.0, 10.0)

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique()[0])  # defaults

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

# filter by population
df = df[df.population >= pop_filter]

# filter by capital
df = df[df.capital.isin(capital_filter)]

# filter by country
if country_filter != 'ALL':
    df = df[df.country == country_filter]

st.map(df)
st.write(df)

pop_sum = df.groupby('country')['population'].sum()
fig, ax = plt.subplots()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)

