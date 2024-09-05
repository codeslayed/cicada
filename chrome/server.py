from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import os
import google.generativeai as genai
import google.ai.generativelanguage as glm

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Replace with your actual API key
API_KEY = 'AIzaSyB6rcCHX4bq4YEmTtSfXPBUCQQawUymgjM'
genai.configure(api_key=API_KEY)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    question = request.form.get('question', '')

    # Save the uploaded file temporarily
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Analyze the file based on its type
    if file.filename.endswith(('.jpg', '.jpeg', '.png')):
        response_text = process_image(file_path)
    elif file.filename.endswith(('.txt', '.csv')):
        response_text = process_text(file_path)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    # Clean up the uploaded file
    os.remove(file_path)

    # Send back the response
    return jsonify({"result": response_text})

def process_image(file_path: str) -> str:
    with open(file_path, 'rb') as image_file:
        image_data = image_file.read()

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        glm.Content(parts=[
            glm.Part(text="You are a cryptographic algorithm expert. "
                          "Your task is to analyze the following image. "
                          "Provide a comprehensive explanation of what the image depicts and any cryptographic algorithms present."),
            glm.Part(inline_data=glm.Blob(mime_type='image/jpeg', data=image_data)),
        ]),
        stream=True
    )
    response.resolve()
    return response.text

def process_text(file_path: str) -> str:
    with open(file_path, 'rb') as text_file:
        text_data = text_file.read()

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        glm.Content(parts=[
            glm.Part(text="You are a cryptographic algorithm expert. "
                          "Your task is to analyze the following text. "
                          "Provide a comprehensive explanation of any cryptographic algorithms present. "
                          "Please provide a simple and short but detailed analysis of the file. "
                          "Ensure that the response is clean and does not include any asterisks or emojis."),
            glm.Part(inline_data=glm.Blob(mime_type='text/plain', data=text_data)),
        ]),
        stream=True
    )
    response.resolve()
    response_text = response.text.replace('*', '').strip()
    return response_text

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    app.run(host='0.0.0.0', port=8000)