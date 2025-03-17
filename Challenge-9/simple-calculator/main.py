import streamlit as st

def main():
    st.title("🥇 Simple Calculator") 
    st.write("Enter two numbers and choose an operation") 

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter your First Number", value = 0.0)

    with col2:
        num2 = st.number_input("Enter your Second Number", value =0.0)

    operation = st.selectbox("Choose an Operation", ["Addition (+)", "Subtraction (-)", "Multiplication (x)", "Diviision (/)"])
    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (x)":
                result = num1 * num2
                symbol = "x"
            else:
                if num2 == 0:
                    st.error( "Error: Division by zero is not allowed")
                    return
                result = num1 / num2
                symbol = "/"

            st.success(f"{num1} {symbol} {num2} = {result}")

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()