import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data.csv")
x=df['HoursStudied']
y=df['ExamScore']
x_train,x_test,y_train,y_test
st.title("My First Streamlit App")
st.write("Hello! Creating a simple web application using Streamlit.")
name=st.text_input("Enter your name:")
#Displaying a message when a button is clicked
if st.button("Submit"):
  st.write(f"Hello, {name}! Welcome to Streamlit.")
