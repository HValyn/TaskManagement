import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import numpy as np
st.session_state
#list of keys tied to widgets that you want to protect
keeper_list = ['username', "user"]

for key in keeper_list:
    if key in st.session_state:
        st.session_state[key] = st.session_state[key]
st.markdown("# Officers ❄️")
st.sidebar.markdown("# Officers ❄️")



    # Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

    # Perform query.
    #rows = conn.query("Name", table="Officers", ttl= "10m").ilike(column="Name" , pattern="Muhammad Abu Bakar").execute()

st.query_params.clear()
rows = conn.query("*", table="Officers", ttl="10m").execute()

df = pd.DataFrame(rows.data)
    # Print results.
st.dataframe(df)

   

