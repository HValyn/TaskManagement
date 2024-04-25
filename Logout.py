# streamlit_app.py

import hmac
import streamlit as st

# set sidebar collapsed before login
#list of keys tied to widgets that you want to protect
keeper_list = ['username', "user"]

for key in keeper_list:
    if key in st.session_state:
        st.session_state[key] = st.session_state[key]
def collapse():
    st.markdown("""
        <style>
            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }
        </style>
        """, unsafe_allow_html=True)
# set sidebar expanded after login
collapse()
if 'user' not in st.session_state:
    st.session_state.user = ""
def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.session_state
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            st.session_state.user = st.session_state["username"]
            #del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
            st.session_state["login_status"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


def clickedLogout():
    st.session_state["password_correct"] = False
    st.session_state.user = ""
    st.session_state["username"] = ""
    collapse()
    if not check_password():
        st.stop()


if not check_password():
    st.stop()

st.session_state
st.button("Logout" , on_click=clickedLogout)
    



st.write("Hello and Welcome To Task Mangement")

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: initial;
        }
    </style>
    """, unsafe_allow_html=True)





