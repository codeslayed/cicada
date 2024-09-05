import os
import telebot
import google.generativeai as genai
import google.ai.generativelanguage as glm

# Replace with your actual API keys
TELEGRAM_API_TOKEN = '7205868210:AAHMtpjQoOq-MHawvmsO-eYDzGNk97OKpPo'
API_KEY = 'AIzaSyB6rcCHX4bq4YEmTtSfXPBUCQQawUymgjM'

genai.configure(api_key=API_KEY)

# Initialize the bot
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Send me a file to analyze.")

@bot.message_handler(content_types=['document'])
def handle_file(message):
    global uploaded_file_path
    
    # Download the file
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Save the file temporarily
    with open('uploaded_file', 'wb') as new_file:
        new_file.write(downloaded_file)

    # Store the uploaded file path
    uploaded_file_path = 'uploaded_file'

    # Determine file type
    mime_type = message.document.mime_type
    if mime_type in ['image/jpeg', 'image/png']:
        response_text = process_image(uploaded_file_path)
    elif mime_type in ['text/plain', 'text/csv']:
        response_text = process_text(uploaded_file_path)
    else:
        response_text = "Unsupported file type."

    # Send response back to user
    bot.reply_to(message, response_text)

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

@bot.message_handler(func=lambda message: True)
def handle_question(message):
    global uploaded_file_path
    
    # Check if a file has been uploaded
    if uploaded_file_path:
        response_text = process_question(message.text)
        bot.reply_to(message, response_text)
    else:
        bot.reply_to(message, "Please upload a file first before asking a question.")

def process_question(question: str) -> str:
    global uploaded_file_path
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    with open(uploaded_file_path, 'rb') as file:
        file_data = file.read()

    response = model.generate_content(
        glm.Content(parts=[
            glm.Part(text=f"You are a cryptographic algorithm expert. Analyze the uploaded file and provide a detailed response to the following question: {question}"),
            glm.Part(inline_data=glm.Blob(mime_type='text/plain', data=file_data)),
        ]),
        stream=True
    )
    response.resolve()
    response_text = response.text.replace('*', '').strip()
    return response_text

if __name__ == '__main__':
    bot.polling()