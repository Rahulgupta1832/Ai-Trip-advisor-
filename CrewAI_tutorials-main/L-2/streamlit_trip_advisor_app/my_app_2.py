import streamlit as st
import os
from openai import OpenAI  # modern client

st.set_page_config(page_title="AI Trip Advisor", layout="centered")
st.title("AI Trip Advisor ✈️🌍")

# ---- UI inputs (restored) ----
col1, col2 = st.columns(2)
with col1:
    origin = st.text_input("From (optional)", placeholder="e.g. New Delhi")
with col2:
    destination = st.text_input("To (destination)", placeholder="e.g. Paris")

days = st.number_input("Number of days", min_value=1, max_value=30, value=3)
start_date = st.date_input("Start date (optional)", help="Optional start date")
budget = st.text_input("Budget (optional)", placeholder="e.g. $500 or moderate")

if st.button("Generate Plan"):
    if not destination:
        st.error("Please enter a destination (To).")
    else:
        # get key from secrets or env
        key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
        if not key:
            st.error("OpenAI key not found. Add OPENAI_API_KEY to Streamlit Secrets.")
        else:
            client = OpenAI(api_key=key)

            prompt = f"""
You are a helpful travel planner.
From: {origin or 'N/A'}
To: {destination}
Days: {days}
Start date: {start_date if start_date else 'N/A'}
Budget: {budget or 'N/A'}

Give:
- Short summary
- Day-by-day itinerary
- 3 recommended hotels/areas to stay
- 3 local foods to try
- Safety tips
Keep it concise and practical.
"""

            with st.spinner("Asking the model..."):
                try:
                    resp = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=800,
                        temperature=0.7,
                    )
                    # modern response shape
                    text = resp.choices[0].message["content"]
                    st.success("Trip plan generated ✅")
                    st.markdown(text)
                except Exception as e:
                    # If quota / billing or other OpenAI error -> show friendly message
                    msg = str(e)
                    st.error(f"OpenAI API error: {msg}")
                    # fallback demo so page still shows something useful
                    st.info("Showing a demo plan while the API error is resolved.")
                    demo = f"""
**Demo plan for {destination} ({days} days)**

**Summary:** Quick demo itinerary.

**Day 1:** Arrive, check-in, local walk.
**Day 2:** Major sightseeing.
**Day 3:** Local food & depart.

**Hotels:** Demo Hotel A, Demo Hotel B, Demo Hotel C.
**Foods:** Demo Dish 1, Demo Dish 2, Demo Dish 3.

*Resolve your OpenAI billing/quotas to get real model output.*"""
                    st.markdown(demo)
