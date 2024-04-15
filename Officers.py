import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import numpy as np

st.markdown("# Officers ❄️")
st.sidebar.markdown("# Officers ❄️")



# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="Officers", ttl="10m").execute()

df = pd.DataFrame(rows.data)
# Print results.
st.table(df)
