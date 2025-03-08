# Required Liabraries
import streamlit as st # Liabrary
from datetime import datetime #Module
from zoneinfo import ZoneInfo #Module All type of date and time data 

# Constant List of Time Zone
time_zones = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Asia/Tokyo",
    "Asia/Dubai",
    "Asia/Bangkok",
    "Asia/Jakarta",
    "Asia/Kolkata",
    "America/Los_Angeles",
    "America/Chicago",
    "Europe/Berlin",
]

# Title for the app
st.title("Time Zone App")

# Select Box for Time Zone
selected_timezone = st.multiselect("Select Timezones", time_zones, default=["UTC", "Asia/Karachi"])

# Display the selected timezones
st.subheader("Selected Timezones")

# Secrching tz in selected_timezones
for tz in selected_timezone:

    # Get & Format current time for each selected timezone with am & pm
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p") #modifiers 
    # Display the current timezone
    st.write(f"**{tz}** - {current_time}") #modifiers

# converting time betwween timezones
st.subheader("Convert Time Between Timezeons")

# time input widget for current time
current_time = st.time_input("Current Time", value=datetime.now().time())

# selectbox convert from
from_tz = st.selectbox("From Timezone", time_zones, index=0)

# selectbox convert to
to_tz = st.selectbox("To Timezone", time_zones, index=1)

# convert time
if st.button("Convert Time"):
    # combine the cuurect time with the selected timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    # convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    # disply the converted time
    st.success(f"Converted Time in {to_tz}: {converted_time}")