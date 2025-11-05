import streamlit as st
st.title('Creating a Button')
st.markdown("**Kelompok 23**")
st.markdown("""
1. Amru Abdurrahman Azzam - 0110122322
2. Hayatunnisa - 0110222118
3. Nurul Maedatul - Awaliah 0110122222
            """)

("========================================================================================")

#defining a button
button = st.button('Click Here')
if button:
    st.write('You Have Clicked the Button')
else:
    st.write('You Have Not Clicked the Button')

("========================================================================================")
import streamlit as st
st.title('Creating Radio Buttons')

#defining radio button
gender = st.radio(
"Select Your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You Havae Selected Male.')
elif gender == 'Female':
    st.write("You Have Selected Female.")
else:
    st.write("You Have Selected Others.")

("========================================================================================")

import streamlit as st
st.title('Creating Checkboxes')
st.write('Select Your Hobbies:')

#defining checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

("========================================================================================")

import streamlit as st
st.title("Creating Dropdown")

#creating dropdown
hobby = st.selectbox('Choose Your Hobbby: ', ('Books', 'Movies', 'Sports'))

("========================================================================================")

import streamlit as st
st.title('Multi-Select')

#defining multi_select with pre-selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)

("========================================================================================")

import streamlit as st
st.title("Download Button")

#creating download button
down_btn = st.download_button(
    label="Download Image",
    data = open("assets/burung.jpg", "rb"),
    file_name="burung.jpg",
    mime="image/jpg"
)
st.download_button(
    label="Download CSV",
    data=open("assets/burung.jpg", "rb"),
    file_name='data.csv',
    mime='csv'
)

("========================================================================================")

import streamlit as st
import time
st.title('Progress Bar')

#defining progress bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

("========================================================================================")

import streamlit as st
import time
st.title('Spinner')

#defininf spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')