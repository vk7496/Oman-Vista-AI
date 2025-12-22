import streamlit as st
import urllib.parse

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="OmanVista AI – Smart Tourism Assistant",
    layout="centered"
)

# -----------------------------------
# Header
# -----------------------------------
st.title("🇴🇲 OmanVista AI")
st.subheader("AI-Powered Tour Recommendation Demo")

st.markdown(
    """
    This demo shows how Artificial Intelligence can help Omani travel agencies
    increase **conversion rate**, **upselling**, and **customer satisfaction**.
    """
)

st.divider()

# -----------------------------------
# User Inputs
# -----------------------------------
nationality = st.selectbox(
    "🌍 Customer Nationality",
    [
        "Omani",
        "GCC (UAE, Saudi, Qatar, Kuwait, Bahrain)",
        "European",
        "Asian",
        "Other"
    ]
)

travel_type = st.selectbox(
    "🧳 Travel Style",
    ["Luxury", "Adventure", "Family", "Romantic"]
)

budget = st.slider(
    "💰 Customer Budget (OMR)",
    min_value=100,
    max_value=2000,
    step=50
)

duration = st.selectbox(
    "📅 Trip Duration",
    ["1–3 days", "4–7 days", "7+ days"]
)

# -----------------------------------
# Generate Recommendation
# -----------------------------------
if st.button("🔍 Generate AI Recommendation"):

    # -----------------------------
    # Base Tour Logic
    # -----------------------------
    if travel_type == "Luxury":
        tour = "Luxury Muscat & Salalah Experience"
        reasons = [
            "Premium hotels and resorts",
            "Private transportation",
            "Exclusive guided experiences"
        ]

    elif travel_type == "Adventure":
        tour = "Desert & Mountain Adventure"
        reasons = [
            "Wadi hiking and nature exploration",
            "Desert safari experience",
            "Off-road mountain routes"
        ]

    elif travel_type == "Family":
        tour = "Family-Friendly Oman Tour"
        reasons = [
            "Safe and comfortable locations",
            "Family-oriented hotels",
            "Cultural and educational attractions"
        ]

    else:
        tour = "Romantic Escape in Oman"
        reasons = [
            "Beach resorts",
            "Sunset experiences",
            "Private and peaceful locations"
        ]

    # -----------------------------
    # Nationality-Based Optimization
    # -----------------------------
    if nationality in ["European", "Asian", "Other"]:
        price = int(budget * 0.95)
        nationality_note = "Optimized for international travelers"
    else:
        price = int(budget * 0.9)
        nationality_note = "Optimized for regional travelers"

    # Safety check (never exceed budget)
    if price > budget:
        price = budget

    # -----------------------------
    # Display Result
    # -----------------------------
    st.success("✅ AI Recommendation Generated")

    st.markdown(f"### 🧠 Recommended Package")
    st.markdown(f"**Tour:** {tour}")
    st.markdown(f"**Suggested Price:** {price} OMR")

    st.markdown("**Why this package?**")
    for r in reasons:
        st.write(f"- {r}")

    st.info(f"AI Note: {nationality_note}. Package optimized to stay within budget.")

    # -----------------------------------
    # WhatsApp Demo (No Paid API)
    # -----------------------------------
    st.divider()
    st.subheader("📲 WhatsApp Message (Demo)")

    phone_number = "968XXXXXXXX"  # شماره خودت بدون +

    message_text = (
        f"AI Recommended Tour:\n"
        f"{tour}\n\n"
        f"Customer Nationality: {nationality}\n"
        f"Trip Duration: {duration}\n"
        f"Budget: {budget} OMR\n\n"
        f"Suggested Package Price: {price} OMR\n\n"
        f"Why this package?\n"
        f"- {reasons[0]}\n"
        f"- {reasons[1]}\n"
        f"- {reasons[2]}"
    )

    st.text_area(
        "WhatsApp Message Preview",
        message_text,
        height=220
    )

    encoded_message = urllib.parse.quote_plus(message_text)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    st.markdown(
        f"[👉 Open WhatsApp with Message]({whatsapp_url})",
        unsafe_allow_html=True
    )

# -----------------------------------
# Instagram QR Section (Brand Trust)
# -----------------------------------
st.divider()
st.subheader("📸 Official Instagram")

st.markdown(
    """
    Scan the official Instagram QR code of the travel agency  
    to verify brand identity and explore real tour content.
    """
)

st.image("instagram_qr.png", width=220)

# -----------------------------------
# Footer
# -----------------------------------
st.divider()
st.caption("Designed & Developed by Golden Bird LLC – AI Solutions for Tourism")
