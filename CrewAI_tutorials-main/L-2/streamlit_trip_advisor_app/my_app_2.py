import streamlit as st
import google.generativeai as genai

st.title("AI Trip Advisor ✈️🌍")

location = st.text_input("Where do you want to go?")
days = st.number_input("How many days?", 1, 30, 3)
budget = st.text_input("Budget (optional)")

if st.button("Generate Plan"):
    if not location:
        st.error("Please enter a destination.")
    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

        prompt = f"""
        Create a {days}-day travel plan for {location}.
        Include:
        - places to visit
        - hotel suggestions
        - food recommendations
        - travel tips
        - consider budget: {budget}
        """

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        st.subheader("Your Travel Plan")
        st.markdown(response.text)
