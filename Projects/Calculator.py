#Creating an Python operator for calculator using Streamlit Library
import streamlit

streamlit.title("🧮 Simple Calculator")

num1 = streamlit.number_input("Enter first number", 0)
num2 = streamlit.number_input("Enter second number", 0)

operation = streamlit.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

if streamlit.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2

    streamlit.success(f"The result is: {result}")
