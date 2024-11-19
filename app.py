import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Cargar css
with open('./style.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Titulo, subtitulo e imagen
st.markdown('<div class="centered_content"><p class="dashboard_title">Phones Dashboard</p></div>', unsafe_allow_html=True)
st.markdown('<div class="centered_content"><p class="dashboard_subtitle">Compare your phone options</p></div>', unsafe_allow_html=True)
st.markdown('<div class="centered_content"><img class="header_image" src="https://gosmartway.com/wp-content/uploads/2021/04/cell-phones.png" alt="Phones Image"></div>', unsafe_allow_html=True)

# Menu Horizontal
menu_selected = option_menu(
    None, ["Home", "EDA", "Insights"],
    icons=['house', 'bar-chart', 'lightbulb'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"background-color": "#437f9f"},
        "icon": {"color": "#FFD700", "font-size": "20px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#387db4"},
        "nav-link-selected": {"background-color": "#387db4"},
    }
)

# Cargar el dataset
df = pd.read_csv("smartphones.csv")

# Inicio
if menu_selected == "Home":
    st.markdown('<p class="page_heading">Welcome to the Smartphone Analysis App</p>', unsafe_allow_html=True)
    st.markdown('<p class="page_content">Explore trends and insights in smartphone data to make informed decisions</p>', unsafe_allow_html=True)

# EDA
elif menu_selected == "EDA":
    st.markdown('<p class="page_heading">Exploratory Data Analysis</p>', unsafe_allow_html=True)

    if st.checkbox("Show raw data"):

        st.dataframe(df)


    st.markdown('<p class="section_subheading">Summary Statistics</p>', unsafe_allow_html=True)

    st.write(df.describe())

    # Distribucion de precios
    st.markdown('<p class="section_subheading">Price Distribution</p>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.histplot(df['Final Price'], kde=True, ax=ax, color="#68b4ff")
    st.pyplot(fig)

    # Ram vs precio final
    st.markdown('<p class="section_subheading">RAM vs Final Price</p>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='Final Price', y='RAM', ax=ax, color="#FFD700")
    st.pyplot(fig)

# Insights
elif menu_selected == "Insights":
    st.markdown('<p class="page_heading">Insights</p>', unsafe_allow_html=True)

    # Distribucion de precios
    st.markdown('<p class="section_subheading">Price Distribution</p>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.histplot(df['Final Price'], kde=True, ax=ax, color="#68b4ff")
    st.pyplot(fig)

    # Ram vs Final Price
    st.markdown('<p class="section_subheading">RAM vs Final Price</p>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='Final Price', y='RAM', ax=ax, color="#FFD700")
    st.pyplot(fig)
    
    # Storage vs Final Price
    st.markdown('<p class="section_subheading">Storage vs Final Price</p>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='Final Price', y='Storage', ax=ax, color="#FF5733")
    st.pyplot(fig)
