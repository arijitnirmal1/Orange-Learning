import streamlit as st
st.title("My First Streamlit App")
st.write("Hello! Creating a simple web application using Streamlit.")
name=st.text_input("Enter your name:")
#Displaying a message when a button is clicked
if st.button("Submit"):
  st.write(f"Hello, {name}! Welcome to Streamlit.")
