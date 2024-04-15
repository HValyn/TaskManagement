import streamlit as st
import pandas as pd
import numpy as np
from st_supabase_connection import SupabaseConnection

st.markdown("# Add New Task🎈")
st.sidebar.markdown("# Add New Task 🎈")
conn = st.connection("supabase",type=SupabaseConnection)
rows = conn.query("*", table="Officers", ttl="10m").execute()
# Print results.
IDs = []
Names = []
for row in rows.data:
    IDs.append(row['id'])
    Names.append(row['Name'])
Officers = ['Dr. Mohsin Sattar', 'Asad Ullah Farid' , 'Muhammad Umair Aslam' , 'Muhammad Abu Bakar']
with st.form("Task Form"):
    project = st.number_input('Project Number' ,min_value=1, step=1)
    currentDate = st.date_input('Current Date')
    currentDate = currentDate.strftime("%m/%d/%Y")
    assignmentDescription = st.text_area('Assignment Description')
    EDC = st.date_input('EDC')
    EDC = EDC.strftime("%m/%d/%Y")
    difficulty = st.text_input('Difficulty')
    assignedby = st.selectbox('Assigned To', Names)
    assignedTo = st.selectbox('Assigned By', Names)
    approvedBy = st.selectbox('Approved By', Names)
    taskCompleted = st.checkbox('Task Completed')
    CompletionDate = st.date_input('Completion Date')
    CompletionDate = CompletionDate.strftime("%m/%d/%Y")
    submit = st.form_submit_button('Generate Document')
    if submit:
         InsertResult = conn.table("Tasks").insert(
            {"ProjectID": project, "Dated": currentDate, "AssignmentDescription": assignmentDescription,"EDC": EDC,"Difficulty": difficulty,"Completed": taskCompleted,"Completion Date": CompletionDate,"Assigned To": assignedTo,"Assigned by": assignedby,"Approved By": approvedBy,}, count="None").execute()

