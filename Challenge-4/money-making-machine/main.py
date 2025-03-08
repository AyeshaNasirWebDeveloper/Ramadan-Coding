import streamlit as st # UI
import random #For getting random things
import time # Time related functionalities
import requests # For API calls 

st.title("Money making machine")

def generate_money():
    return random.randint(1, 1000) # random integers

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your Money......")
    time.sleep(5) # sleep method is used to delay in seconds
    amount = generate_money()
    st.success(f"You made ${amount}!") 

def fetch_motivational_quotes():
    try:
        response = requests.get('http://127.0.0.1:8000/motivation')
        if response.status_code == 200:
            motivation = response.json()
            return motivation["motivational_quotes"]
        else:
            return ("Don't give up until you succeed!")

    except:
        return("Something went wrong!")
    
st.subheader("Motivate your self")
if st.button("Generate Quote!"):
    idea = fetch_motivational_quotes()
    st.warning(idea)

def fetch_business_ideas():
    try:
        response = requests.get('http://127.0.0.1:8000/business')
        if response.status_code == 200:
            business = response.json()
            return business["business idea"]
        else:
            return("Develop a mobile app for language learning.")
    
    except:
        return("Something went wrong!")
    
st.subheader("Business Ideas")
if st.button("Get your Idea"):
    quote = fetch_business_ideas()
    st.info(quote)

def fetch_funny_jokes():
    try:
        response = requests.get('http://127.0.0.1:8000/jokes')
        if response.status_code == 200:
            jokes = response.json()
            return jokes["funny jokes"]
        else:
            return("Do you want to hear a pizza joke?????     Nah! Its too cheesy!!")
    
    except:
        return("Something went wrong!")
    
st.subheader("Funny Jokes")
if st.button("Tell me a joke"):
    joke = fetch_funny_jokes()
    st.success(joke)