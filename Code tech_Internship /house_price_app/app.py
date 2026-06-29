import streamlit as st

st.set_page_config(
    page_title="House Price Intelligence",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1f4037, #99f2c8);
}
.title {
    text-align: center;
    color: white;
    font-size: 48px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: white;
    font-size: 22px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🏠 House Price Intelligence System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered real estate price prediction</div><br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>📌 What this app does</h3>
<ul>
<li>Predicts house prices using ML</li>
<li>Uses realistic city-wise data</li>
<li>Shows model insights visually</li>
<li>Built like a real product</li>
</ul>
</div>
""", unsafe_allow_html=True)
