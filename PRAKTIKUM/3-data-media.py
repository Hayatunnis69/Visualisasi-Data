import streamlit as st


st.title("Data and Media Elements")
st.markdown("**Kelompok 23**")
st.markdown("""
1. Amru Abdurrahman Azzam - 0110122322
2. Hayatunnisa - 0110222118
3. Nurul Maedatul - Awaliah 0110122222
            """)

("========================================================================================")

st.subheader ("Images")

st.write("Display an Images")

#display image by specifying path

st.image("assets\leebit.jpg")


st.write("Image Courtesy: unplash.com") #image courtesy by unplash

("========================================================================================")

#image courtesy
st.write("Display Multiple Images")

#listing out animal images
animal_images = [
    
    'assets/burung.jpg',
    'assets/ikan.jpg',
    'assets/jerapah.jpg',
    'assets/capung.jpg',
    
]

#display multiple images with width 150
st.image(animal_images, width=150)

#image courtesy
st.write("Image Courtesy: Unplash")

("========================================================================================")


import streamlit as st
import base64

#function to set image as background
def add_local_background_image(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.write("Image Courtesy: unplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("data:image/jpg; base64, {encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        }}
        </style>
        """,
    unsafe_allow_html=True
    )

st.write("Background Image")

#calling Image in Function
add_local_background_image("assets//bg.jpg")

("========================================================================================")

import streamlit as st
from PIL import Image

original_image = Image.open("assets/strawberry.jpg")
#display original image

st.subheader("Original Image")
st.image(original_image)

#resizing image to 600*400
resized_image = original_image.resize((600, 400))

#display resized image
st.title("Resized Image")
st.image(resized_image)