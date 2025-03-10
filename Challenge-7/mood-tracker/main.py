# # Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

import streamlit as st # For creating the UI
import pandas as pd # For data manipulation
import datetime # for handling dates
import csv # For reading & writing the CSV files
import os # For file operations

# Storing Mood Data
# Its capital because it is constant this file is not changed
MOOD_FILE = "mood_log.csv"

# For Read the file 
def read_mood_data():

    # check if he file exist
    if not os.path.exists(MOOD_FILE): # os is a functio which creates a path from mood_log.csv file to main.py

        # if no file, create empty dataframes with columns
        return pd.DataFrame(columns=["Date", "Mood"]) # dataframe is used for storing the data in a particular format

    # used pandas method read_csv for reading the data
    return pd.read_csv(MOOD_FILE) 

# Save the new Data on the csv file
def save_mood_data(date,mood):

# open file in append mode
    with open(MOOD_FILE, "a", encoding="utf-8", newline="") as file: # with function is used to create a resource between files like append, read, write etc and "a" stands for append

        # create a csv writer
        writer = csv.writer(file)

        # write new entry to file
        writer.writerow([date,mood]) # writerow method is used for creating the rows in our file

# Streamlit app

# streamlit title
st.title("Mood Tracker 🥰")

# streamlit content
# st.write("This is a mood tracker application.")

# Get today's date
today = datetime.date.today()

# create subheader for mood input
st.subheader("How are your feeling today? 🤔")

# create dropdown for mood selection
mood = st.selectbox("Select your mood 👇", ["Happy 😄", "Sad 😓", "Angry 😠", "Neutral 😐", "Stressed 😲", "Shocked 😱"])

# button to save mood
if st.button("Log Mood :angel:"):

    # save mood when button is clicked
    save_mood_data(today,mood)

# show success message
    st.success("Mood Logged Successfully! 😝")

st.write("Your mood for today is: ", mood)

# load or read existing data to display
data = read_mood_data()

# if there is not data to display
if not data.empty:

    # section for visualization
    st.subheader("Mood Trends Over Time! 😋")

    # convert date string to datetime object 
    data["Date"] = pd.to_datetime(data["Date"])

    # count frequency of each mood
    mood_counts = data.groupby(["Mood"]).count()["Date"]

    # display bar chart for mood frequencies or bar chart for showing the mood counts 
    st.bar_chart(mood_counts)