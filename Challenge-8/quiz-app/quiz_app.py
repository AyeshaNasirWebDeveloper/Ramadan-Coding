import streamlit as st  # for the UI
import random  # for randomizing the questions

# Define the quiz question, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Muhammad Ali", "Quaid-e-Azam", "Allama Iqbal", "Sir Syed Ahmed Khan"],
        "answer": "Quaid-e-Azam"
    },
    {
        "question": "What is the largest city of Pakistan?",
        "options": ["Lahore", "Islamabad", "Karachi", "Faisalabad"],
        "answer": "Karachi"
    },
    {
        "question": "Who is the first Governor-General of Pakistan?",
        "options": ["Sir Syed Ahmed Khan", "Quaid-e-Azam", "Sir Muhammad Zafrulla Khan", "Muhammad Ali"],
        "answer": "Quaid-e-Azam"
    },
    {
        "question": "What is the official language of Pakistan?",
        "options": ["English", "Punjabi", "Urdu", "Sindhi"],
        "answer": "Urdu"
    },
    {
        "question": "Which city of Pakistan is the city of lights?",
        "options": ["Lahore", "Islamabad", "Karachi", "Faisalabad"],
        "answer": "Karachi"
    },
    {
        "question": "Why is Karachi famous?",
        "options": ["For its beautiful beaches", "For its beautiful mountains", "For its beautiful deserts", "For its beautiful ports"],
        "answer": "For its beautiful ports"
    },
    {
        "question": "Which currency is used in Pakistan?",
        "options": ["USD", "EUR", "GBP", "PKR"],
        "answer": "PKR"
    }
]

# Define the quiz title
st.title("📝 Welcome to the Quiz Application")

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button for checking the answer
if st.button(":abacus: Submit Answer"):
    # Store the selected option in session state
    st.session_state.selected_option = selected_option
    st.session_state.show_result = True

# Show result if the user has submitted an answer
if st.session_state.show_result:
    # Check if the selected option is correct (case-insensitive comparison)
    if st.session_state.selected_option.lower() == question["answer"].lower():
        st.success("✔️ Correct answer! 🎈") 
        st.balloons()
    else: 
        st.error(f"❎ Incorrect answer! :anguished: The correct answer is {question['answer']}")

    # Add a delay before moving to the next question
    if st.button("Next Question"):
        # Reset the result display
        st.session_state.show_result = False
        # Randomly select a new question
        st.session_state.current_question = random.choice(questions)
        # Clear the selected option
        st.session_state.selected_option = None
        # Rerun the app to display the next question
        st.rerun() 