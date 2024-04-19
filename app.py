import streamlit as st
from PIL import Image

# set wide mode
st.set_page_config(layout="wide")

# Title
st.title('Object Detection Workshop')

# Subheader
st.subheader('Upload a photo of your skin to detect acne')


# 3 columns
col1, col2, col3 = st.columns([3, 1, 3],gap='large')

with col1:
    # button to upload image
    upload_button = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'], key='upload_button')
    if upload_button is not None:
        image = Image.open(upload_button)
        st.image(image, caption='Uploaded Image', use_column_width=True)

with col2:
    st.write('')
    inference_button = st.button('Inference')

with col3:
    # display image
    if inference_button:
        st.write('Inference button clicked')
        st.write('Displaying the image')
        if 'image' in locals():
            st.image(image, caption='Uploaded Image', use_column_width=True)