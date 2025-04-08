import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Visualizer")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Pick a numeric column", numeric_cols)
        st.line_chart(df[selected_col])
    else:
        st.warning("No numeric columns found.")
