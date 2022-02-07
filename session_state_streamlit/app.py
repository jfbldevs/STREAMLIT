#Modules
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Fruits List")

#Create a diccionary and DataFrame

_dic = {
    "Name": ["Apple", "Orange", "Banana", "Pear"],
    "Quantity": [10, 20, 30, 40]
}

_df = pd.DataFrame(_dic)
#Create a button
#load = st.checkbox("Load Data")
load = st.button("Load Data")


#Initiate session state
if "load_state" not in st.session_state:
    st.session_state.load_state=False


if load or st.session_state.load_state:
    st.session_state.load_state=True
    st.write(_df)
    #User option
    opt = st.radio("Plot type", ("Bar", "Pie"))
    if opt == "Bar":
        fig = px.bar(_df, x="Name", y="Quantity", title="Bar Chart")
        st.plotly_chart(fig)
    else:
        fig = px.pie(_df, names="Name", values="Quantity", title="Pie Chart")
        st.plotly_chart(fig)
