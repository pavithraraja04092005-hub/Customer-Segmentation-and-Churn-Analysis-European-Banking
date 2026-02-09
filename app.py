import streamlit as st
import pandas as pd

st.title("Customer Segmentation & Churn Analysis")
st.write("Unified Mentor Internship – Applied Project")

data = pd.read_excel("bank_churn_data.xlsx")

st.write("Customer Dataset")
st.dataframe(data)

st.write("Churn Summary")
st.write(data["Exited"].value_counts())
