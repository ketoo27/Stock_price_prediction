import streamlit as st
from database import add_user, get_user

def login():
    st.title('Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        user = get_user(username, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful')
            st.rerun()
        else:
            st.error('Invalid username or password')

def register():
    st.title('Register')

    full_name = st.text_input('Full Name')
    email = st.text_input('Email')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Register'):
        add_user(username, password, full_name, email)
        st.success('Registration successful. Please log in.')

def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    st.success('Logged out successfully.')
    st.rerun()

def auth():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login_option = st.selectbox('Login/Register', ['Login', 'Register'])
        if login_option == 'Login':
            login()
        else:
            register()
    else:
        st.sidebar.success(f"Logged in as {st.session_state['username']}")
        if st.sidebar.button('Logout'):
            logout()
