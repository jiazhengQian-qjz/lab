import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_csv('housing.csv')
st.title('California Housing Data (1990) by jiazhengQian')

median_house_price_filter = st.slider('Median House Price:', 0, 500001, 200000)  # min, max, default

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())

genre = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

#filter by median_house_price
df = df[df.median_house_value >= median_house_price_filter]
# filter by country
df = df[df.ocean_proximity.isin(location_filter)]
# filter by genre
if genre == 'Low':
    df = df[df.median_income <= 2.5]
if genre == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
if genre == 'High':
    df = df[df.median_income >= 4.5] 

# show on map
st.subheader('See more filters in the sidebar:')
st.map(df)
# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
df.median_house_value.hist(ax=ax,bins=30)
st.pyplot(fig)