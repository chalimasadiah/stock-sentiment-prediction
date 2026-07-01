import streamlit as st


def render_disclaimer():
    """
    Display project limitations and disclaimer.
    No emoji.
    """

    st.markdown(
        """
        <p class="section-title">Project Disclaimer</p>
        <p class="section-desc">
            This application is intended for educational purposes and
            decision-support only. It should not be interpreted as financial advice.
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Current Limitations</span>
                </div>
                <div class="insight-card-body">
                    Dashboard demonstrates the inference pipeline,
                    not the complete forecasting system.<br><br>
                    Real-time IHSG market indicators are not collected
                    during user interaction.<br><br>
                    The sentiment analyzer is keyword-based and does not
                    yet utilize Transformer-based NLP models.<br><br>
                    Market movements are influenced by many external
                    factors beyond economic news sentiment alone.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Future Improvements</span>
                </div>
                <div class="insight-card-body">
                    FinBERT / IndoBERT sentiment classification<br><br>
                    Multi-headline sentiment aggregation<br><br>
                    Automatic economic news crawling<br><br>
                    Real-time IHSG market integration<br><br>
                    Daily feature generation pipeline<br><br>
                    Cloud deployment using AWS
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    st.warning(
        "The generated prediction should be viewed as an educational demonstration "
        "rather than a production-grade forecast."
    )
