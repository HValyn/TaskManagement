import streamlit as st
from st_supabase_connection import SupabaseConnection
st.session_state
#list of keys tied to widgets that you want to protect
keeper_list = ['username', "user"]

for key in keeper_list:
    if key in st.session_state:
        st.session_state[key] = st.session_state[key]
if not st.session_state["password_correct"]:
    st.stop()

if st.session_state.user != "mohsinsattar" or st.session_state.user == "":
    st.write(st.session_state.user)
    st.write("You Do Not Have the Authority")
    st.stop()
else:
    st.markdown("# Add New Officer❄️")
    st.sidebar.markdown("# Add New Officer ❄️")
    conn = st.connection("supabase",type=SupabaseConnection)

    with st.form("Add New Officer"):
        name = st.text_input('Officer Name')
        designation = st.text_input('Officer Designation')
        submit = st.form_submit_button('Add New Officer')
        if submit:
            

            InsertResult = conn.table("Officers").insert(
                {"Name": name, "Designation": designation,}, count="None").execute()
            
            st.write(InsertResult)

