import streamlit as st

st.title('My Streamlit Web App on Windows')

user_input = st.text_input("What's your name?", 'Type Here...')
st.write(f'Hello, {user_input}!')

if st.button('Click Me'):
    st.write('Button clicked!')
