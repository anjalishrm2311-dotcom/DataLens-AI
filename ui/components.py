import streamlit as st

# Load CSS only once
st.markdown("""
<style>

.kpi-card{
    background: linear-gradient(135deg,#ffffff,#f8fafc);
    border-radius:18px;
    padding:22px;
    text-align:center;
    box-shadow:0px 8px 18px rgba(0,0,0,0.08);
    height:165px;
}

.kpi-icon{
    font-size:34px;
}

.kpi-title{
    color:#6B7280;
    font-size:17px;
    margin-top:8px;
    font-weight:600;
}

.kpi-value{
    font-size:36px;
    font-weight:bold;
    color:#111827;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)


def kpi_card(title, value, icon, color):

    st.markdown(
        f"""
<div class="kpi-card" style="border-top:6px solid {color};">

<div class="kpi-icon">{icon}</div>

<div class="kpi-title">{title}</div>

<div class="kpi-value">{value}</div>

</div>
""",
        unsafe_allow_html=True,
    )