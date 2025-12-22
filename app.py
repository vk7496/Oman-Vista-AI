import streamlit as st
import urllib.parse

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="OmanVista AI – Smart Travel Assistant",
    layout="centered"
)

# -----------------------------------
# Header
# -----------------------------------
st.title("🇴🇲 OmanVista AI")
st.subheader("AI-Powered Travel Recommendation Demo")

st.markdown(
    """
    This demo shows how Artificial Intelligence can help
    travel agencies in Oman increase **sales**, **speed**, and **customer satisfaction**.
    """
)

st.divider()

# -----------------------------------
# User Inputs
# -----------------------------------
travel_type = st.selectbox(
    "Travel Style",
    ["Luxury", "Adventure", "Family", "Romantic"]
)

budget = st.slider(
    "Customer Budget (OMR)",
    min_value=100,
    max_value=2000,
    step=50
)

duration = st.selectbox(
    "Trip Duration",
    ["1–3 days", "4–7 days", "7+ days"]
)

# -----------------------------------
# AI Recommendation Logic (Demo)
# -----------------------------------
if st.button("🔍 Generate AI Recommendation"):

    if travel_type == "Luxury":
        tour = "Luxury Muscat & Salalah Experience"
        price = budget + 200
        reasons = [
            "5-star hotels",
            "Private transport",
            "Premium guided tours"
        ]

    elif travel_type == "Adventure":
        tour = "Desert & Mountain Adventure"
        price = budget + 100
        reasons = [
            "Wadi hiking",
            "Desert camping",
            "Off-road experience"
        ]

    elif travel_type == "Family":
        tour = "Family-Friendly Oman Tour"
        price = budget + 150
        reasons = [
            "Safe locations",
            "Family hotels",
            "Cultural attractions"
        ]

    else:
        tour = "Romantic Escape in Oman"
        price = budget + 180
        reasons = [
            "Beach resorts",
            "Sunset cruises",
            "Private experiences"
        ]

    # -----------------------------------
    # Show AI Result
    # -----------------------------------
    st.success("✅ AI Recommendation Ready")

    st.markdown(f"### 🧠 Recommended Tour: **{tour}**")
    st.markdown(f"💰 **Suggested Price:** {price} OMR")

    st.markdown("**Why this tour?**")
    for r in reasons:
        st.write(f"- {r}")

    st.info(
        "This AI system helps agents upsell tours intelligently based on customer preferences."
    )

    # -----------------------------------
    # WhatsApp Demo (NO API)
    # -----------------------------------
    st.divider()
    st.subheader("📲 WhatsApp Message (Demo – No API)")

    phone_number = "96891278434"  # شماره خودت بدون +

    message_text = (
        f"AI Recommended Tour: {tour}\n"
        f"Suggested Price: {price} OMR\n\n"
        f"Why this tour?\n"
        f"- {reasons[0]}\n"
        f"- {reasons[1]}\n"
        f"- {reasons[2]}"
    )

    # Message preview inside app
    st.text_area(
        "WhatsApp Message Preview",
        message_text,
        height=180
    )

    encoded_message = urllib.parse.quote_plus(message_text)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    st.markdown(
        f"[👉 Open WhatsApp with Message]({whatsapp_url})",
        unsafe_allow_html=True
    )

# -----------------------------------
# Footer
# -----------------------------------
st.divider()
st.caption("Designed & Developed by Golden Bird LLC – AI Solutions for Tourism")
