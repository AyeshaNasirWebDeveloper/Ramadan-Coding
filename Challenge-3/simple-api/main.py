from fastapi import FastAPI
import random

# app name is recommmennted and FastAPI is holding all the stuff of fastapi
app = FastAPI() 

# We will create two simple get endpoints
# endpoint is a url that we can call to get some data
# sMotivational Quotes & Empowering Women & Funny Jokes

# Data Arrays
motivational_quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
]

business_ideas = [
    "Start a subscription box service for eco-friendly products.",
    "Create an online course platform for niche skills.",
    "Launch a mobile app for mental health and mindfulness.",
    "Open a coworking space for freelancers and remote workers.",
    "Start a digital marketing agency specializing in small businesses.",
    "Develop a meal prep and delivery service for busy professionals.",
    "Create a platform for peer-to-peer equipment rental.",
    "Start a blog and monetize it through affiliate marketing.",
    "Launch a dropshipping store for trending products.",
    "Develop a SaaS (Software as a Service) tool for productivity.",
    "Start a pet grooming and daycare service.",
    "Create a platform for virtual events and conferences.",
    "Launch a niche e-commerce store (e.g., sustainable fashion).",
    "Start a YouTube channel focused on educational content.",
    "Develop a mobile app for language learning.",
]

funny_jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
]
# @app is a decorator who stores data from FastAPI
# creating get request
@app.get("/motivation")
def get_motivational_quotes():
# (apikey : str):
    """Returns a random motivational quote """
    # if apikey != "1234567890" :
    #     return {"error": "Invalid API key"}
    return {"motivational_quotes": random.choice(motivational_quotes)}

@app.get("/business")
def get_business_ideas():
# (apikey : str):
    """Returns a random business idea"""
    # if apikey != "1234567890" :
    #     return {"error": "Invalid API key"}
    return {"business idea": random.choice(business_ideas)}

@app.get("/jokes")
def get_funny_jokes():
    # (apikey : str):
    """Returns a random funny joke """
    # if apikey != "1234567890" :
    #     return {"error": "Invalid API key"}
    return {"funny jokes": random.choice(funny_jokes)}