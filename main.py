# Streamlit
import streamlit as st
import warnings

from streamlit_extras.add_vertical_space import add_vertical_space

# Main Library
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit Web Configuration
st.set_page_config(
    page_title="My Dashboard - Iris",
    page_icon="",
    layout="wide",
    initial_sidebar_state="auto"
)

# Load Dataset
dataset = sns.load_dataset("iris")

# Container - Header
with st.container(border=False):
    st.markdown('<h1 style=text-align:center>My Iris Dashboard - Created by M Reza A P</h1>', unsafe_allow_html=True)
    add_vertical_space(3)

# Container - Content
col1, col2 = st.columns([0.5, 0.5])

with col1:
    
    st.dataframe(data=dataset, width=1200, use_container_width=False, hide_index=True)

with col2:
    
    sns.countplot(data=dataset)
    fig, ax = plt.subplots(figsize= (8,4))
    sns.countplot(data=dataset, x="species", hue="species")

    ax.set_title("", fontsize=14)
    ax.set_xlabel("", fontsize=14)
    ax.set_ylabel("", fontsize=14)
    ax.grid(True)

    plt.tight_layout()
    st.pyplot(fig)
    # plt.show()


col1, col2 = st.columns([0.5, 0.5])

with col1:
    species_count = dataset['species'].value_counts()

    width = st.sidebar.slider("plot width", 1, 5, 3)
    height = st.sidebar.slider("plot height", 1, 5, 3)

    fig, ax = plt.subplots(figsize=(width, height))
    species_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#619CFF', '#F8766D', '#00BA38'], textprops={'fontsize': 4})
    ax.set_title("", fontsize=7)
    ax.set_xlabel("", fontsize=7)
    ax.set_ylabel("", fontsize=7)

    plt.tight_layout()
    st.pyplot(fig)
    # plt.show()

with col2:
    largest_values = dataset.groupby('species')[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].max()

    largest_values = largest_values.reset_index()
    melted_df = largest_values.melt(id_vars="species", var_name="Measurement", value_name="Size")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=melted_df, x="species", y="Size", hue="Measurement", palette="inferno", ax=ax)

    ax.set_title("", fontsize=14)
    ax.set_xlabel("", fontsize=14)
    ax.set_ylabel("", fontsize=14)
    plt.legend(title="Measurement")
    
    plt.tight_layout()
    st.pyplot(fig)
    # plt.show()