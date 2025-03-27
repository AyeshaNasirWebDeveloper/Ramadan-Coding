import os #for enviroment varibale
import chainlit as cl #for chatbot interface
import google.generativeai as genai #for google genai api
from dotenv import load_dotenv #for loading file and environment varibales

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key = gemini_api_key )

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.on_chat_start
async def chat_start():
    await cl.Message(content="Welcome to the Ayesha's AI chatbot! How can I help you?").send()

@cl.on_message
async def chat(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response, "text") else ""
    await cl.Message(content=response_text).send()