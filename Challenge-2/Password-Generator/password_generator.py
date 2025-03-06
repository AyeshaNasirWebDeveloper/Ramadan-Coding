import streamlit as st # importing streamlit
import random #create random characters
import string #string module for getting special characters, number and alphabetical letters a-z A-Z 
import pyperclip  # For copying to clipboard

def generate_password(Length, use_digits, use_special, exclude_similar):
    letters = string.ascii_letters # ascii letters provide the lower and uppercase letters

    if use_digits:
        letters += string.digits #provide (0-9)

    if use_special:
        letters += string.punctuation # Add Special Characters (!, @, #, $, %, ^, &, *)

    if exclude_similar:
        similar_chars = "il1Lo0O"
        letters = ''.join([char for char in letters if char not in similar_chars])
    
    
    return ''.join(random.choice(letters) for _ in range(Length)) # _ sign yeh batata hai loop ki koi length nhi hai 

# Streamlit
st.title( "Password Generator") 
st.write("Generate strong and secure passwords with custom options.")

# Slider is a streamlit function and it takes built in parameters of min_value and max_value and as a agruments of value
length = st.slider("Select Password Length", min_value = 8, max_value = 32, value = 12) #password length

# select the checkbox if the user want the digits
use_digits = st.checkbox("Include Digits")

# select the checkbox if the user want the special characters
use_special = st.checkbox("Include Special Characters")

exclude_similar = st.checkbox("Exclude Similar Characters (e.g., i, l, 1, L, o, 0, O)")

# Generate Password
if st.button("Generate Passeord"):
    password = generate_password(length, use_digits, use_special, exclude_similar)
    st.success("Generated Password: " + password)  # success is a streamlit function of alert with the background color of green

# Copy to Clipboard
    if st.button("Copy to Clipboard"):
        pyperclip.copy(password)
        st.success("Password copied to clipboard!")

# Password Strength Indicator (Basic Example)
if 'password' in locals():
    strength = "Weak"
    if length >= 12 and use_digits and use_special:
        strength = "Strong"
    elif length >= 10 and (use_digits or use_special):
        strength = "Medium"
    st.write(f"Password Strength: **{strength}**")

# Generate Multiple Passwords
if st.checkbox("Generate Multiple Passwords"):
    num_passwords = st.number_input("Number of Passwords", min_value=1, max_value=10, value=3)
    if st.button("Generate Multiple"):
        passwords = [generate_password(length, use_digits, use_special, exclude_similar) for _ in range(num_passwords)]
        st.write("Generated Passwords:")
        for pwd in passwords:
            st.code(pwd)