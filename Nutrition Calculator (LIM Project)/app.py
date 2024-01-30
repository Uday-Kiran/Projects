import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() #load all environmental varialbles
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    
    if uploaded_file is not None:
        
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
#initialize streamlit app
st.set_page_config(page_title='Calories Advisor App')
st.header('Calories Advisor App')
uploaded_file = st.file_uploader('Choose an image...', type=['jpeg','jpg','png'])
image = ''

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded Image.', use_column_width = True)
    
submit = st.button("Tell me about total calories")

input_prompt = '''
You are an expert in Nutrition where you need to see food items from an image and calculate 
the total calories, and also provide of every food items with calories intake in below format.

1. Item 1 - No. of. calories
2. Item 2 - No. of. calories

Finally you can also mention whether the food is healthy or not and also mention the 
percentage split of ratio of carbohydrates, protiens, fats, fibers and other things required in our diet. 
'''

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data)
    st.header('The Response is')
    st.write(response)