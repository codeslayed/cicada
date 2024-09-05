import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image

API_KEY = 'AIzaSyB6rcCHX4bq4YEmTtSfXPBUCQQawUymgjM'

genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Cicada Ai: Algorithm Detector", page_icon="📸", layout="centered", initial_sidebar_state='collapsed')

st.header("Cicada Ai: Crypto Detector")

uploaded_file = st.file_uploader("Choose an File", accept_multiple_files=False, type=['jpg', 'png','txt', 'csv'])

if uploaded_file is not None:
    if uploaded_file.type in ['jpg', 'png']:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded file', use_column_width=True)
    else:
        st.write("Uploaded file is not an image.")
    
    bytes_data = uploaded_file.getvalue()
    question = st.text_area("Ask a question about the file:", height=100)
    submit_question = st.button("Submit Question")
    
    response = None  # Define response variable here
    
    if submit_question:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            glm.Content(parts=[
                glm.Part(text="you are a cryptographic algorithm expert ."
                         "You are a highly knowledgeable crypto expert."
                         "Your task is to examine the following file in detail. "
                         "Provide a comprehensive, factual, and scientifically accurate explanation of what the file depicts. "
                         "You task is to first detect the algorithm given accurately"
                         "After the algorithm is detected give the accurate decoding of the algorithm "
                         "If you cant detect show there is a unkknown cipher present."
                         "Scan the image for text and number for the algorithm and give the result accordingly"
                         ),
                glm.Part(inline_data=glm.Blob(mime_type='text/plain' if uploaded_file.type == 'txt' else 'text/csv', data=bytes_data)),
            ]),
            stream=True
        )
        response.resolve()  # Resolve the response here
        
    if response is not None:  # Check if response is not None before writing
        st.write(response.text)



        