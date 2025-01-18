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
