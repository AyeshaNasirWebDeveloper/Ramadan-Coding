# Random Joke Generator (Streamlit + FastAPI)

Welcome to the **Random Joke Generator** project! This is a fun web app that provides a random joke in Roman Urdu every time you click a button. It is built using **Streamlit** for the frontend and **FastAPI** for the backend.

### Project Overview

- **Frontend:** Streamlit - A Python framework to create interactive web apps with minimal code.
- **Backend:** FastAPI - A modern, fast (high-performance) web framework for building APIs.
- **Jokes:** A list of funny jokes in Roman Urdu for the entertainment of users.

### Features

- Random jokes generation.
- Fun and simple user interface.
- The jokes are fetched from the FastAPI server, making it scalable and easy to extend.

### Prerequisites

Before running this project, you’ll need to install the following dependencies:

1. **Python** (>= 3.7)
2. **FastAPI**
3. **Uvicorn** (for running FastAPI)
4. **Streamlit** 
5. **Requests**

### Installation

#### 1. Clone the repository:

```bash
git clone https://github.com/AyeshaNasirWebDeveloper/joke-generator.git
cd random-joke-generator
```

#### 2. Install required packages:

You can install the required dependencies using `uv':

```bash
pip install -r requirements.txt
```

#### 3. Run the FastAPI backend:

To run the FastAPI backend, use Uvicorn:

```bash
uvicorn main:app --reload
```

By default, the FastAPI app will run on `http://127.0.0.1:8000`.

#### 4. Run the Streamlit frontend:

To run the Streamlit frontend, use the following command:

```bash
streamlit run random_joke_generator.py
```

This will open the app in your default web browser, usually on `http://localhost:8501`.

### Usage

Once the Streamlit app is running:

- The page will display a button "Generate Joke".
- Click the button to fetch a random joke.
- The joke will appear on the screen in Roman Urdu.

### Example Output

When you click the button, a joke like the following will appear:

```
Pehli baar, aik shakhs doctor ke paas gaya aur bola: 'Doctor sahab, mujein bhoolne ki bimari ho gayi hai!' Doctor ne kaha: 'Kab se?' Shakhs bola: 'Kab se kya?'
```

### How It Works

- **FastAPI** serves the backend by providing an endpoint that returns a random joke from a list of jokes stored in memory.
- **Streamlit** is used to create the frontend UI where users can interact with the API and fetch random jokes.
- The frontend communicates with the FastAPI backend via HTTP requests.

### Contributing

If you'd like to contribute to this project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.


### Contact

If you have any questions, feel free to open an issue in this repository or contact me via Linkedln.