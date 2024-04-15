import streamlit as st
from st_supabase_connection import SupabaseConnection

st.markdown("# Add New Officer❄️")
st.sidebar.markdown("# Add New Officer ❄️")
conn = st.connection("supabase",type=SupabaseConnection)
rows = conn.query("*", table="Officers", ttl="10m").execute()

with st.form("Add New Officer"):
    name = st.text_input('Officer Name')
    designation = st.text_input('Officer Designation')
    submit = st.form_submit_button('Add New Officer')
    if submit:
        

        InsertResult = conn.table("Officers").insert(
            {"id": (len(rows.data) + 1) , "Name": name, "Designation": designation,}, count="None").execute()

