
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Student Score Prediction App")
st.write("Predict an exam score based on study hours.")

# Training data
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Scores": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Study_Hours"]]
y = df["Scores"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Get user input
hours = st.number_input(
    "Enter daily study hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

# Predict when button is clicked
if st.button("Predict Score"):
    prediction = model.predict(
        pd.DataFrame({"Study_Hours": [hours]})
    )
    st.success(f"Predicted score: {prediction[0]:.2f}")
