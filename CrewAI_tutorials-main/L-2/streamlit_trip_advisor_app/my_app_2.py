import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Trip Advisor", layout="centered")
st.title("AI Trip Advisor ✈️🌍")

# Inputs
location = st.text_input("Where do you want to go?", placeholder="e.g. Paris, France")
days = st.number_input("How many days?", min_value=1, max_value=30, value=3)
budget = st.text_input("Budget (optional)", placeholder="e.g. $500-1000 or 'moderate'")

# API key from Streamlit secrets or env
OPENAI_KEY = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
if not OPENAI_KEY:
    st.error("OpenAI key not found. Add OPENAI_API_KEY in Streamlit Secrets or set env var.")
else:
    openai.api_key = OPENAI_KEY

    if st.button("Generate Plan"):
        if not location:
            st.warning("Please enter a destination.")
        else:
            prompt = f"""Create a {days}-day travel plan for {location}.
Budget: {budget or 'not specified'}.
Give a short summary, day-by-day itinerary, 3 places to stay, 3 local foods, and safety tips."""
            with st.spinner("Generating plan..."):
                try:
                    resp = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=800,
                        temperature=0.7,
                    )
                    text = resp["choices"][0]["message"]["content"]
                    st.subheader("Your Travel Plan")
                    st.markdown(text)
                except openai.error.OpenAIError as e:
                    st.error(f"OpenAI API error: {e}")
                except Exception as e:
                    st.error(f"Request failed: {e}")
