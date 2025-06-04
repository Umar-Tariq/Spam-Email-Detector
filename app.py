import streamlit as st
import joblib

# Load the trained model
model = joblib.load('spam_detector_model.joblib')

# App title
st.title("📧 Spam Email Detector")

# Input field
user_input = st.text_area("Enter the message:", height=150)

# Predict button
if st.button("Check for Spam"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([user_input])[0]
        prob = model.predict_proba([user_input]).max()

        if prediction == "spam":
            st.error(f"❌ This message is SPAM! (Confidence: {prob:.2%})")
        else:
            st.success(f"✅ This message is HAM (Not Spam). (Confidence: {prob:.2%})")
