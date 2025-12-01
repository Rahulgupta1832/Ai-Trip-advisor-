import streamlit as st
from openai import OpenAI
import os

st.title("AI Trip Advisor ✈️🌍")

# INPUTS — always created (outside try/except)
location = st.text_input("Where do you want to go?")
days = st.number_input("How many days?", 1, 30, 3)

# Ensure key availability
key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
if not key:
    st.error("OpenAI API key missing. Add OPENAI_API_KEY to Streamlit Secrets.")
else:
    client = OpenAI(api_key=key)

# Button and safe call
if st.button("Generate Plan"):
    if not location:
        st.warning("Please enter a destination.")
    else:
        if not key:
            st.error("No API key — can't call OpenAI.")
        else:
            prompt = f"Create a {days}-day travel plan for {location}..."
            with st.spinner("Generating plan..."):
                try:
                    res = client.chat.completions.create(
                        model="gpt-3.5-turbo",   # use a model you have quota for
                        messages=[{"role":"user","content":prompt}],
                        max_tokens=600,
                        temperature=0.7
                    )
                    text = res.choices[0].message["content"]
                    st.subheader("Your Travel Plan")
                    st.markdown(text)
                except Exception as e:
                    st.error(f"OpenAI API error: {e}")
                    # Optionally show a fallback example:
                    st.info("Example fallback plan:\n\n- Day 1: ...")
