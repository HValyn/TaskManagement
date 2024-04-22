import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import numpy as np


if not st.session_state["password_correct"]:
    st.stop()

if st.session_state.user != "mohsinsattar" or st.session_state.user == "":
    st.write(st.session_state.user)
    st.write("You Do Not Have the Authority")
    st.stop()
else:
    st.markdown("# Officers ❄️")
    st.sidebar.markdown("# Officers ❄️")



    # Initialize connection.
    conn = st.connection("supabase",type=SupabaseConnection)

    # Perform query.
    #rows = conn.query("Name", table="Officers", ttl= "10m").ilike(column="Name" , pattern="Muhammad Abu Bakar").execute()


    rows = conn.query("*", table="Officers", ttl="10m").execute()

    df = pd.DataFrame(rows.data)
    # Print results.
    st.dataframe(df)

   

