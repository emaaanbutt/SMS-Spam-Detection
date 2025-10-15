import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("SMS Spam Detection")
st.write("Enter a message below to find out if it's spam or not!")

user_input = st.text_area("Type your message here...")

if st.button("Check Spam"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        if prediction == 1:
            st.error(f"Spam Detected")
        else:
            st.success(f"Not Spam")

