import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import fitz
import pprint as pp
import numpy as np
#list of keys tied to widgets that you want to protect
import base64
from pdf2docx import Converter
import io
st.session_state
keeper_list = ['username', "user"]

for key in keeper_list:
    if key in st.session_state:
        st.session_state[key] = st.session_state[key]
if not st.session_state["password_correct"]:
    st.stop()   
def show(rows):
    # Perform query.
    df = pd.DataFrame(rows.data)
    # Print results.
    
    st.table(df)
st.markdown("# Tasks ❄️")
st.sidebar.markdown("# Tasks ❄️")

conn = st.connection("supabase",type=SupabaseConnection)
st.query_params.clear()

if st.session_state.user == 'mohsinsattar':
    rows = conn.query("*", table="Tasks").execute()
    st.query_params.clear()
    show(rows)
else:
    rows = conn.query("*", table="Tasks").eq(column="username",value=st.session_state.user).execute()
    st.query_params.clear()
    show(rows)
    





