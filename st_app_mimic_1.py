import streamlit as st

st.title('Welcome to Python Programming!')

st.header('Why Learn Python?')

st.write('Python is a versatile language that you can use for web development, data analysis, artificial intelligence, and more. Its simplicity allows you to focus on solving problems rather than on syntax.')

st.caption("Python powers some of the world's most complex applications.")

st.code('print("Hello, World!")', language = 'python',line_numbers = True)

st.write('Did you know? Python was named after the British comedy group Monty Python.')

if st.button('Let it snow!'):
    st.snow()