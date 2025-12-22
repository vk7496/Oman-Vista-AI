# app.py
# OmanVista AI – WhatsApp Smart Tour Recommender Demo
# Designed & Developed by Golden Bird LLC

# =============================
# Imports (must be at top)
# =============================
import streamlit as st
import urllib.parse

# =============================
# Page Configuration
# =============================
st.set_page_config(
    page_title="OmanVista AI | Smart Tourism",
    page_icon="🌍",
    layout="centered"
)

# =============================
# App Header
# =============================
st.title("OmanVista AI – Smart Tour Recommendation")
st.write(
    "This demo shows how AI can increase travel agency sales in Oman through "
    "personalized tour recommendations and smart pricing."
)

st.divider()

# =============================
# Step 1: Traveler Input
# =============================
st.header("1️⃣ Traveler Information")

nationality = st.selectbox(
    "Traveler Nationality",
    ["European", "GCC", "Asian", "Other"]
)

days = st.slider("Trip Duration (days)", min_value=3, max_value=14, value=7)

budget = st.selectbox(
    "Budget Level",
    ["Low", "Medium", "High"]
)

interests = st.multiselect(
    "Travel Interests",
    ["Nature", "Luxury", "Cultural", "Adventure"]
)

st.divider()

# =============================
# AI Recommendation Logic
# =============================
def recommend_tour(nationality, days, budget, interests):
    """Simple, explainable AI logic for demo purposes"""

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
        explanation.append("European travelers prefer experiential tours")

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

    final_price = max(base_price, 300)

    return tour_name, final_price, explanation

# =============================
# Step 2: Generate Recommendation
# =============================
st.header("2️⃣ AI Recommendation")

if st.button("Generate Smart Tour Recommendation"):
    tour, price, reasons = recommend_tour(
        nationality=nationality,
        days=days,
        budget=budget,
        interests=interests
    )

    st.success("AI Recommendation Generated Successfully")

    st.subheader("📌 Recommended Tour")
    st.write(f"**{tour}**")

    st.subheader("💰 Suggested Price")
    st.write(f"**{price} OMR**")

    st.subheader("🧠 Why this recommendation?")
    for reason in reasons:
        st.write(f"- {reason}")

    st.divider()

    # =============================
    # Business Comparison
    # =============================
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

    st.divider()

    # =============================
    # WhatsApp Demo Integration
    # =============================
    st.subheader("📲 Send Recommendation to WhatsApp (Demo)")

    phone_number = "968XXXXXXXX"  # <-- replace with your WhatsApp number

    message_text = f"""
AI Recommended Tour:
{tour}

Suggested Price: {price} OMR

Reasons:
- """ + "\n- ".join(reasons)

    encoded_message = urllib.parse.quote(message_text)

    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    st.markdown(
        f"<a href='{whatsapp_url}' target='_blank'>👉 Send to WhatsApp</a>",
        unsafe_allow_html=True
    )

st.divider()

# =============================
# Footer
# =============================
st.caption("Designed & Developed by Golden Bird LLC – AI Tourism Solutions")
