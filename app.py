# app.py
# AI Smart Tour Recommender – Simple Demo for Oman Travel Agencies

import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Smart Tour Recommender | Oman",
    page_icon="🌍",
    layout="centered"
)

st.title("AI-Powered Tour Recommendation – Oman")
st.write("This demo shows how Artificial Intelligence can increase sales through personalized tour suggestions.")

st.divider()

# -----------------------------
# Step 1: Traveler Input
# -----------------------------
st.header("1️⃣ Traveler Information")

nationality = st.selectbox(
    "Traveler Nationality",
    ["European", "GCC", "Asian", "Other"]
)

days = st.slider("Trip Duration (days)", 3, 14, 7)

budget = st.selectbox(
    "Budget Level",
    ["Low", "Medium", "High"]
)

interests = st.multiselect(
    "Travel Interests",
    ["Nature", "Luxury", "Cultural", "Adventure"]
)

st.divider()

# -----------------------------
# Step 2: AI Recommendation Logic (Simple & Explainable)
# -----------------------------
def recommend_tour(nationality, days, budget, interests):
    # Default values
    tour_name = "Classic Muscat Experience"
    base_price = 400
    explanation = []

    # Interest-based logic
    if "Luxury" in interests:
        tour_name = "Luxury Muscat & Coast Escape"
        base_price += 250
        explanation.append("Luxury experience selected")

    if "Adventure" in interests or "Nature" in interests:
        tour_name = "Adventure Oman: Mountains & Desert"
        base_price += 150
        explanation.append("Nature / Adventure preference detected")

    # Nationality-based adjustment
    if nationality == "European":
        base_price += 70
        explanation.append("European travelers prefer longer experiential tours")

    if nationality == "GCC":
        base_price += 120
        explanation.append("GCC travelers prefer premium comfort")

    # Budget adjustment
    if budget == "High":
        base_price += 200
        explanation.append("High budget selected")
    elif budget == "Low":
        base_price -= 80
        explanation.append("Low budget optimization applied")

    # Duration adjustment
    if days > 7:
        base_price += 100
        explanation.append("Extended trip duration")

    return tour_name, max(base_price, 300), explanation

# -----------------------------
# Step 3: Generate Recommendation
# -----------------------------
st.header("2️⃣ AI Recommendation")

if st.button("Generate Smart Tour Recommendation"):
    tour, price, reasons = recommend_tour(nationality, days, budget, interests)

    st.success("AI Recommendation Generated Successfully")

    st.subheader("📌 Recommended Tour")
    st.write(f"**{tour}**")

    st.subheader("💰 Suggested Price")
    st.write(f"**{price} OMR**")

    st.subheader("🧠 Why this recommendation?")
    for r in reasons:
        st.write(f"- {r}")

    st.divider()

    # -----------------------------
    # Step 4: Business Comparison
    # -----------------------------
    st.subheader("📊 Business Impact (Example)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Traditional Offer**")
        st.write("Generic Muscat Tour")
        st.write("Price: 400 OMR")
        st.write("No personalization")

    with col2:
        st.markdown("**AI-Powered Offer**")
        st.write(tour)
        st.write(f"Price: {price} OMR")
        st.write("Personalized & data-driven")

    st.info("This AI approach increases conversion rate and average booking value.")

    # -----------------------------
    # Step 5: Send to WhatsApp (Demo Mode)
    # -----------------------------
    st.subheader("📲 Send Recommendation to WhatsApp")

    phone_number = "968XXXXXXXX"  # Replace with your WhatsApp number

    whatsapp_message = f"AI Recommended Tour:%0A{tour}%0A%0ASuggested Price: {price} OMR%0A%0AReasons:%0A" + "%0A".join(reasons)

    whatsapp_url = f"https://wa.me/{phone_number}?text={whatsapp_message}"

    st.markdown(f"[👉 Send to WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

st.divider()

st.caption("Designed & Developed by Golden Bird LLC – AI Tourism Solutions")
