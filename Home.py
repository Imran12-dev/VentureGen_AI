
import streamlit as st

st.set_page_config(
    page_title="VentureGen AI | NIC",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}
.hero {
    padding: 45px 30px;
    border-radius: 15px;
    background: linear-gradient(120deg, #172554, #2563EB);
    color: white;
    text-align: center;
}
.hero h1 {
    font-size: 48px;
    color: white;
}
.hero p {
    font-size: 19px;
    color: #E0E7FF;
}
.feature {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    min-height: 150px;
}
.footer {
    text-align: center;
    color: gray;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 VentureGen AI")
st.caption("National Incubation Center | Startup Innovation Platform")

st.write("")

# Hero section
st.markdown("""
<div class="hero">
    <h1>Turn Your Ideas Into Businesses</h1>
    <p>
        Discover innovative startup opportunities,
        solve real-world problems and develop
        complete business plans using Generative AI.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Introduction
st.subheader("Welcome to VentureGen AI")

st.write("""
VentureGen AI is an AI-powered startup idea generation
platform designed to help aspiring entrepreneurs transform
their ideas and real-world problems into practical business
opportunities.

Using Generative AI, the platform creates structured startup
plans covering market opportunities, business models,
financial planning, technology requirements and growth strategies.
""")

st.write("")
st.subheader("What Can You Do With VentureGen AI?")

# Feature columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature">
        <h2>💡 Idea Generation</h2>
        <p>Transform your interests, themes and problems
        into innovative startup ideas.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
        <h2>📊 Market Analysis</h2>
        <p>Understand target customers, competitors
        and potential market opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
        <h2>📈 Business Planning</h2>
        <p>Generate structured business plans,
        financial estimates and growth strategies.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# Navigation
st.subheader("Ready to Start Your Entrepreneurial Journey?")

if st.button("🚀 Generate My Startup Idea", type="primary",
             use_container_width=True):
    st.switch_page("pages/1_Startup_Idea_Generator.py")

st.write("")

# Footer
st.markdown("""
<hr>
<div class="footer">
    Developed by Muhammad Imran<br>
    VentureGen AI | National Incubation Center
</div>
""", unsafe_allow_html=True)
