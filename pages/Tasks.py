import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import numpy as np

if not st.session_state["password_correct"]:
    st.stop()



st.markdown("# Tasks ❄️")
st.sidebar.markdown("# Tasks ❄️")

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="Tasks", ttl="10m").execute()

df = pd.DataFrame(rows.data)
# Print results.
st.table(df)