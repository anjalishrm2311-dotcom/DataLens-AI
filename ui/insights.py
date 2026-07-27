import streamlit as st


def show_ai_insights(insights):

    st.subheader("🤖 AI Insights")

    for insight in insights:

        st.info(insight)