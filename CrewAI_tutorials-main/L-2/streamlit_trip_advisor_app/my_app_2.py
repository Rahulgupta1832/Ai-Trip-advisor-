# my_app_2.py — minimal, works WITHOUT the openai package (uses requests)
import streamlit as st
import os
import requests

st.title("AI Trip Advisor ✈️🌍")

location = st.text_input("Where do you want to go?")
days = st.number_input("How many days?", 1, 30, 3)

# Ensure secret is set in Streamlit Cloud
if "OPENAI_API_KEY" not in st.secrets and "OPENAI_API_KEY" not in os.environ:
    st.error("Add OPENAI_API_KEY to Streamlit Secrets.")
else:
    api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")

    if st.button("Generate Plan"):
        if not location:
            st.error("Please enter a destination.")
        else:
            prompt = f"Create a {days}-day travel plan for {location}. Include places to visit, food, hotels, and tips."

            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 800,
                "temperature": 0.7,
            }

            with st.spinner("Generating plan..."):
                r = requests.post(url, headers=headers, json=payload, timeout=60)
                if r.status_code != 200:
                    st.error(f"OpenAI API error: {r.status_code} {r.text}")
                else:
                    data = r.json()
                    # robust access
                    try:
                        content = data["choices"][0]["message"]["content"]
                    except Exception:
                        content = data.get("choices", [{}])[0].get("text", str(data))
                    st.subheader("Your Travel Plan")
                    st.markdown(content)
