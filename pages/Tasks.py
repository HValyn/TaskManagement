import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import numpy as np
st.write(st.session_state.user)
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
if st.session_state.user == 'mohsinsattar':
    rows = conn.query("*", table="Tasks", ttl="10m").execute()
    show(rows)
else:
    rows = conn.query("*", table="Tasks", ttl="10m").eq(column="username",value=st.session_state.user).execute()
    show(rows)





