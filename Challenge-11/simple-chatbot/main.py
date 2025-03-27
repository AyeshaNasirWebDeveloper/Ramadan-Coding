import chainlit as cl

@cl.on_message
async def handle_message(message: cl.Message):
    response = f"You said: {message.content}"
    await cl.Message(content=response).send()
