import streamlit as st
from datetime import datetime


def render_header():
    """
    Render professional page header.
    No emoji — clean text only.
    """

    now = datetime.now().strftime("%d %b %Y, %H:%M")

    st.markdown(
        f"""
        <div class="page-header">
            <div class="page-header-left">
                <h1>Stock Market Movement Prediction</h1>
                <p>Economic News Sentiment Analysis for IHSG Forecasting</p>
            </div>
            <div class="page-header-badge">
                Last updated: {now}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
