# Simple Calculator App (Streamlit)

Welcome to the **Simple Calculator** project! This is a basic calculator built using **Streamlit**, which allows users to perform simple arithmetic operations like addition, subtraction, multiplication, and division. It features a clean, user-friendly interface where users can input numbers and select operations.

### Try Now: https://modernsimplecalculator.streamlit.app/

### Features

- Perform basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.
- Error handling for division by zero.
- Interactive user interface using **Streamlit**.
  
### Prerequisites

Before running this project, you’ll need to install the following dependencies:

- **Python 3.7+**
- **Streamlit**

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/AyeshaNasirWebDeveloper/simple-calculator.git
cd simple-calculator
```

#### 2. Install required dependencies

You can install Streamlit using the following:

```bash
uv add streamlit
```

#### 3. Run the app

Once the dependencies are installed, you can run the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will open the calculator app in your default web browser (usually on `http://localhost:8501`).

### Usage

1. **Enter two numbers** in the input fields for "First Number" and "Second Number".
2. **Select an operation** from the dropdown list: Addition (+), Subtraction (-), Multiplication (x), or Division (/).
3. Click the **"Calculate"** button to see the result.

### Example Output

- If you enter `10` for the first number, `5` for the second number, and choose **Addition (+)**, the result will be:

```
10 + 5 = 15
```

- If you choose **Division (/)** and enter `10` for the first number and `0` for the second number, the app will show an error: 

```
Error: Division by zero is not allowed
```

### How It Works

- **Streamlit** is used for the frontend, providing an interactive interface for inputting numbers and selecting operations.
- **Python** handles the logic for performing arithmetic operations.
- If division by zero is attempted, an error message is shown to the user.

### Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

### Contact

Feel free to open issues or contact me through Linkedln if you have any questions or suggestions!
