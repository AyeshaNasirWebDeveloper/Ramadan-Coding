import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"]) #for configuration

model = genai.GenerativeModel(model_name="gemini-2.0-flash") #it works like an object

while True:
    # Getting user input
    user_input = input("Hello There!\nEnter your Query or write 'quit' for exit:\n")

    if user_input.lower() == 'quit':
        print("Thank you for chatting with me! Allah Hafiz")
        break

    # giving response
    try:
        response = model.generate_content(user_input)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")