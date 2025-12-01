import streamlit as st
import openai

st.title("AI Trip Advisor ✈️🌍")

location = st.text_input("Where do you want to go?")
days = st.number_input("How many days?", 1, 30, 3)

if st.button("Generate Plan"):
    if not location:
        st.error("Please enter a destination.")
    else:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        prompt = f"Create a {days}-day travel plan for {location}. Include places to visit, food, hotels, and tips."

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("Your Travel Plan")
        st.write(res.choices[0].message["content"])
