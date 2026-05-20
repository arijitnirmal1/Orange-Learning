import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data.csv")
X=df['HoursStudied']
y=df['ExamScore']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
st.title("chr(128217)Exam Score Predictor")
st.write("Enter hours studied to predict the exam score.")
hours=st.number_input("Hours Studied:",min_value=0.0,step=0.1)
#Displaying a message when a button is clicked
if st.button("Predict Score"):
  predicted_score=model.predict([[hours]])[0]
  st.success(f"chr(9745) Predicted Score: {predicted_score:.2f}")
st.write("###chr(128202) Sample Training Data")
st.dataframe(df)
