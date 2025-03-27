import streamlit as st
from fastapi import FastAPI
import random
import requests

app =FastAPI()

funny_joke = [
    "Pehli baar, aik shakhs doctor ke paas gaya aur bola: 'Doctor sahab, mujein bhoolne ki bimari ho gayi hai!' Doctor ne kaha: 'Kab se?' Shakhs bola: 'Kab se kya?'",
    "Aik shakhs apni biwi se: 'Tum kahan ja rahi ho?' Biwi: 'Main mandir ja rahi hoon.' Shakhs: 'Kyun?' Biwi: 'Dua karne!' Shakhs: 'Acha, to phir dua karna ke mujhe biwi kaam ke liye waqt de!'",
    "Teacher: 'Pappu! Tumhara homework kahan hai?' Pappu: 'Mam, kal ka din to holiday tha!'",
    "Babu: 'Jab main paise kamata tha, tab tum mujh se pyar karti thi!' Biwi: 'Main ab bhi tumse pyar karti hoon, lekin ab paise ki bhi talash hai!'",
    "Aik shakhs apni wife se: 'Mujhe lagta hai tum mujh se pyar karti ho!' Wife: 'Haan, aur agar tum ne aik aur ghalat kaam kiya to tumhe pyar karte hue maar dungi!'",
    "Banda: 'Yaar, aaj kal log itni jaldi shaadi karte hain!' Dost: 'Haan, kyun ke shadi ke baad apne haq mein sab kuch karte hain!'",
    "Dost: 'Tumne shaadi ke baad apne zindagi ka sab se acha kaam kya kiya?' Shakhs: 'Shaadi!'",
    "Shakhs: 'Mujhe chai mein adrak dalwana hai!' Chaiwala: 'Kyun?' Shakhs: 'Kyun ke chai peenay ke baad bhi thodi si taazgi chahiye!'",
    "Aik shakhs apni friend se: 'Mujhe tumhara fashion sense bohot pasand hai!' Friend: 'Aap ko kis cheez ka fashion pasand hai?' Shakhs: 'Woh jo tumne kuch nahi pehna!'",
    "Teacher: 'Ali, tumhare jawab galat hain!' Ali: 'Mam, koi baat nahi, mein aap se shaadi karunga to jawab theek ho jayenge!'",
    "Mamu: 'Beta, zindagi mein kis cheez ka khayal rakhna chahiye?' Bachcha: 'Mamu, paisay ka!' Mamu: 'Kyun?' Bachcha: 'Jab paisay hon to har cheez milti hai!'",
    "Biwi: 'Mujhe tum se kuch baat karni hai.' Shakhs: 'Haan, batao.' Biwi: 'Tumhare liye kuch bhi nahi badla!' Shakhs: 'To kya badalna tha? Shaadi ke baad thodi aur pehchan milti hai!'",
    "Aik shakhs: 'Tum kaise raat bhar khayal rakhti ho?' Biwi: 'Jab tum so rahe hote ho, main khayal rakhti hoon ke kab tum uth ke chakma doge!'",
    "Sardarji ka phone aya: 'Jee bhai, main job ke liye interview dena chahta hoon.' Interviewer: 'Aap kahan se hain?' Sardarji: 'Main phir bhi yahan se hoon!'",
    "Aik shakhs apni dost se: 'Mujhe laga tum mere dil mein ho!' Dost: 'Tumhare dil mein hon, ya tumhare paise mein, yeh hum dono hi jaante hain!'",
    "Jeevan: 'Tumhara favourite color kya hai?' Dost: 'Main bhi soch raha tha, aaj tum kya padhoge!'",
    "Aik shakhs: 'Mujhe jaldi se pyar chahiye!' Dost: 'Kyun?' Shakhs: 'Kyun ke shaadi ke baad mujhe aap se love milne ka intezaar karna padega!'",
    "Bapu: 'Beta, tumhare school ka homework kahan hai?' Beta: 'Bapu, sab kuch internet par milta hai, homework bhi!'",
    "Aik shakhs: 'Main apne ghar ki safai kar raha tha!' Dost: 'Toh phir ghar ka system kaise kaam kar raha hai?' Shakhs: 'Ab toh wo bhi chutti par gaya hai!'",
    "Bachay ka dhanda: 'Mujhe pata nahi tha ke bachpan mein aap ke paas paise the!' Dost: 'Agar paise nahi hote to aaj mujhe job bhi nahi milti!'",
    "Aik shakhs: 'Mujhe soojh raha tha ke kahan jaana chahiye!' Dost: 'Kahaan?' Shakhs: 'Jaise shaadi ke baad hum dono milke chalenge!'",
    "Biwi: 'Main aaj raat aap ke saath dinner karna chahti hoon!' Shakhs: 'Kyun?' Biwi: 'Taake mujhe aap ki dosti ka ehsaas ho!'",
    "Aik shakhs apne dost se: 'Mujhe samajh nahi aata ke yeh pichlay dafa ka maqsad kya tha!' Dost: 'Agar tum bhi samajh jaate, to yeh joke nahi chalne ka tha!'",
    "Doctor: 'Aap ko rest ki zarurat hai!' Shakhs: 'Doctor, kis zindagi ka rest?' Doctor: 'Apni purani zindagi ka!'",
    "Aik shakhs apni biwi se: 'Tum toh mujh se ziada smart ho!' Biwi: 'Aap toh sab samajhte ho, lekin aap ke paas koi plans nahi!'",
    "Bachay ka sawal: 'Mum, mujhe jhoot bolna seekhna hai!' Mum: 'Kyun beta?' Bachay: 'Kyun ke jab aap ke gussa aata hai, to mujh se pyar karne ka bahana karte ho!'",
    "Teacher: 'Raza, tumhare jawab galat hain!' Raza: 'Mam, galat jawab dena bhi toh aik skill hai!'",
    "Aik shakhs: 'Mujhe pyar ki talaash thi!' Dost: 'To phir tum aaj kis se mil rahe ho?' Shakhs: 'Main apni salary se pyar kar raha hoon!'",
    "Babu: 'Tumhe har waqt cooking karni aati hai!' Biwi: 'Nahi, bas apni life ka kuch plan hai!'",
    "Pappu: 'Mujhe lagta hai tum mujhe bachpan se yaad karte ho!' Dost: 'Main tumhe yaad karne ka waqt nahi nikalta!'",
    "Sardarji: 'Mujhe sab se zaruri kaam karna hai!' Dost: 'Kya?' Sardarji: 'Mobile ka balance check karna!'",
    "Aik shakhs apni dost se: 'Tumhe pata hai, main tum se pyar karta hoon!' Dost: 'Main tum se shaadi nahi karne wali!' Shakhs: 'Main toh sirf pyar ka matlab bata raha tha!'",
    "Aik shakhs apni wife se: 'Agar tum gussa karogi to main kya karun ga?' Wife: 'Tumhe kya laga tha, yeh toh tumhi kaam karoge!'",
    "Teacher: 'Ali, tumhare kaam kaise chal rahe hain?' Ali: 'Aap ko yaad hai mam, jab aap ne pucha tha, to main ne kaha tha, 'kal!'",
    "Jeevan: 'Tum kahan ke job ke liye apply kar rahe ho?' Dost: 'Tumhare ghar ki doston mein!'",
    "Bachay ka jawab: 'Aap ko pata hai main ne paise ke liye kaam kiya!' Dost: 'Aap se puchna tha ke kis cheez ke liye kaam kiya!'"
]

@app.get("/joke")
async def joke():
    return {"joke": random.choice(funny_joke)}

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("http://127.0.0.1:8000/joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['joke']}"
        else:
            return "Failed to fetch joke. Please try again later!"
        
    except:
        return "Why did the two Java methods get a divorce? \nBecause they had constant arguments."
    
def main():
    st.title("😆 Welcome to the Random Joke Generator!😆") 
    st.write("### 👇 Click the button below to generate the funny Joke! ")
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)



if __name__ == "__main__":
    main()