import streamlit as st
import pandas as pd
import numpy as np
import fitz
import pprint as pp
from st_supabase_connection import SupabaseConnection
import base64
# Import the required modules
from pdf2docx import Converter
import io

if not st.session_state["password_correct"]:
    st.stop()


def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download Pdf</a>'

def create_download_link_office(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.docx">Download Docx</a>'


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
    currentDateO = st.date_input('Current Date')
    
    assignmentDescription = st.text_area('Assignment Description')
    EDCO = st.date_input('EDC')
    EDC = EDCO.strftime("%m/%d/%Y")
    difficulty = st.text_input('Difficulty')
    assignedTo = st.selectbox('Assigned To', Names)
    assignedby = st.selectbox('Assigned By', Names)
    approvedBy = st.selectbox('Approved By', Names)
    taskCompleted = st.checkbox('Task Completed')
    CompletionDateO = st.date_input('Completion Date')
    CompletionDate = CompletionDateO.strftime("%m/%d/%Y")
    currentDate = currentDateO.strftime("%m/%d/%Y")
    duration = ''
    submit = st.form_submit_button('Generate Document')
    if submit:
         InsertResult = conn.table("Tasks").insert(
            {"ProjectID": project, "Dated": currentDate, "AssignmentDescription": assignmentDescription,"EDC": EDC,"Difficulty": difficulty,"Completed": taskCompleted,"Completion Date": CompletionDate,"Assigned To": assignedTo,"Assigned by": assignedby,"Approved By": approvedBy,"username": st.session_state.user,}, count="None").execute()
    
         st.write(InsertResult)

         fields_to_update = {
            'Project': str(project),
            'Date': str(currentDate),
            'Description': str(assignmentDescription),
            'Duration': str(duration),
            'ExtraPages': '0',
            'Difficulty': difficulty,
            'EDC': EDC,
            'ExtensionReason': '',
            'AssignedTo': assignedTo,
            'Lab': 'DS',
            'WorkDetail': '',
            'TabDuration': '',
            'ToAssisst': '',
            'AssignedBy': assignedby,
            'ApprovedBy': approvedBy,
            'AsignDesign': 'GM (Tech)',
            'ApprovedDesign': 'GM (Tech)',
            'Completed': str(taskCompleted),
            'CompletionDate': CompletionDate,
        }
         
         def update_pdf_widgets(pdf_path, field_values):
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    widgets = page.widgets()
                    for widget in widgets:
                        field_name = widget.field_name
                        if field_name in field_values:
                            widget.field_value = field_values[field_name]
                            widget.update()
                    doc.saveIncr()
         update_pdf_widgets('pages/TaskAssignmentFieldsNew.pdf', fields_to_update)

         doc = fitz.open('pages/TaskAssignmentFieldsNew.pdf')

         pdf_bytes = doc.write()
         
         doc.close()

         html = create_download_link(pdf_bytes, "TaskAssignment")
         cv = Converter('pages/TaskAssignmentFieldsNew.pdf')
         out_stream = io.BytesIO()
         cv.convert(out_stream)
         cv.close()



         html_office = create_download_link_office(out_stream.getvalue(), "TaskAssignmentO")
         st.markdown(html, unsafe_allow_html=True)
         st.markdown(html_office, unsafe_allow_html=True)