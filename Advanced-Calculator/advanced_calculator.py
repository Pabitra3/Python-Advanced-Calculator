
import streamlit as st
import math

def main():
    st.title("Advanced Calculator")
    menu = ["Basic Calculator", "Statistical Calculator", "Temperature Converter", "Derivative Calculator"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    if choice == "Basic Calculator":
        basic_calculator()
    elif choice == "Statistical Calculator":
        statistical_calculator()
    elif choice == "Temperature Converter":
        temperature_converter()
    elif choice == "Derivative Calculator":
        derivative_calculator()

def basic_calculator():
    st.subheader("Basic Calculator")
    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")
    operation = st.selectbox("Select an operation", ["+", "-", "*", "/", "%"])

    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed")
                return
        elif operation == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                st.error("Modulus by zero is not allowed")
                return

        st.success(f"Result: {result}")
        
def statistical_calculator():
    st.subheader("Statistical Calculator")
    numbers = st.text_input("Enter a list of numbers separated by commas")
    if st.button("Calculate Mean"):
        nums = [float(x) for x in numbers.split(",")]
        mean = sum(nums) / len(nums)
        st.success(f"Mean: {mean}")
    if st.button("Calculate Median"):
        nums = [float(x) for x in numbers.split(",")]
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            median = (nums[n//2-1] + nums[n//2]) / 2
        else:
            median = nums[n//2]
        st.success(f"Median: {median}")
      

def temperature_converter():
    st.subheader("Temperature Converter")
    option = st.selectbox("Select an option", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius")
        if st.button("Convert"):
            fahrenheit = (celsius * 9/5) + 32
            st.success(f"{celsius}°C is equal to {fahrenheit}°F")
    else:
        fahrenheit = st.number_input("Enter temperature in Fahrenheit")
        if st.button("Convert"):
            celsius = (fahrenheit - 32) * 5/9
            st.success(f"{fahrenheit}°F is equal to {celsius}°C")
def derivative_calculator():
    st.subheader("Derivative Calculator")
    function = st.text_input("Enter a function (e.g., x**2 + 2*x + 1)")
    x_value = st.number_input("Enter the value of x to calculate the derivative")
    if st.button("Calculate Derivative"):
        try:
            derivative = eval(f"lambda x: {function}", {"__builtins__": None}, {"math": math})
            derivative_value = derivative(x_value)
            st.success(f"The derivative of {function} at x={x_value} is {derivative_value}")
        except Exception as e:
            st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()