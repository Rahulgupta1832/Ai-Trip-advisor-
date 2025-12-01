import streamlit as st
import openai
import os

st.title("AI Trip Advisor ✈️🌍")

# set API key from Streamlit Secrets (preferred) or environment
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")

location = st.text_input("Where do you want to go?")
days = st.number_input("How many days?", 1, 30, 3)

if st.button("Generate Plan"):
    if not location:
        st.error("Please enter a destination.")
    else:
        prompt = f"Create a {days}-day travel plan for {location}. Include places to visit, food, hotels, and tips."

        try:
            resp = openai.ChatCompletion.create(
                model="gpt-4o-mini",                 # change if your account doesn't have access
                messages=[{"role": "user", "content": prompt}],
                max_tokens=700,
                temperature=0.7,
            )
            # Safely extract text
            text = resp["choices"][0]["message"]["content"]
            st.subheader("Your Travel Plan")
            st.markdown(text)
        except Exception as e:
            st.error(f"OpenAI request failed: {e}")
