import streamlit as st
from PIL import Image  # Needed for some image stuff


#make title with name of page
st.title('About Me')

#make header with information
st.header('Information')
st.write('Name: Jeffrey George')
st.write('Date of Birth: November 2, 2001')
st.write('Hometown: Fredericksburg, Virginia')

#divider
st.divider()

#make header with interests
st.header('Interests')
st.write('Hobbies: Cars and Video Games')
st.write('Career Goals: Live comfortably at a job that I enjoy')

#make image of me
image = Image.open('gigachad.png')
st.image(image)


