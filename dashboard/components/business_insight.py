import streamlit as st


def render_business_insight(label):
    """
    Display business interpretation card.
    No emoji.
    """

    st.markdown(
        """
        <p class="section-title">Business Interpretation</p>
        <p class="section-desc">
            Possible economic implication of the submitted headline,
            based on general financial reasoning.
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if label == "Positive":
            body  = (
                "Positive economic news generally indicates improving "
                "macroeconomic conditions and may increase investor "
                "confidence, business optimism, and upward pressure "
                "on stock prices."
            )
            title = "Positive Economic Signal"
            border_color = "#16A34A"
        elif label == "Negative":
            body  = (
                "Negative economic news may signal economic uncertainty, "
                "leading to lower investor confidence, increased selling "
                "pressure, and potential short-term market correction."
            )
            title = "Negative Economic Signal"
            border_color = "#DC2626"
        else:
            body  = (
                "Neutral news usually provides limited market direction. "
                "Investors tend to wait for additional confirmation, "
                "and other economic indicators become more important."
            )
            title = "Neutral Economic Signal"
            border_color = "#D97706"

        st.markdown(
            f"""
            <div class="insight-card" style="border-left:3px solid {border_color};">
                <div class="insight-card-header">
                    <span class="insight-card-title">{title}</span>
                </div>
                <div class="insight-card-body">{body}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="insight-card" style="border-left:3px solid #2563EB;">
                <div class="insight-card-header">
                    <span class="insight-card-title">Forecasting Pipeline</span>
                </div>
                <div class="pipeline-steps">
                    <div class="pipeline-step">
                        <div class="pipeline-step-icon">N</div>
                        <div class="pipeline-step-label">News</div>
                    </div>
                    <div class="pipeline-arrow">&rarr;</div>
                    <div class="pipeline-step">
                        <div class="pipeline-step-icon">S</div>
                        <div class="pipeline-step-label">Sentiment</div>
                    </div>
                    <div class="pipeline-arrow">&rarr;</div>
                    <div class="pipeline-step">
                        <div class="pipeline-step-icon">F</div>
                        <div class="pipeline-step-label">Features</div>
                    </div>
                    <div class="pipeline-arrow">&rarr;</div>
                    <div class="pipeline-step">
                        <div class="pipeline-step-icon">M</div>
                        <div class="pipeline-step-label">Model</div>
                    </div>
                    <div class="pipeline-arrow">&rarr;</div>
                    <div class="pipeline-step">
                        <div class="pipeline-step-icon">P</div>
                        <div class="pipeline-step-label">Predict</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        insight_text = {
            "Positive": (
                "The model predicts IHSG movement for the next "
                "trading day based on news sentiment and historical "
                "patterns. Positive signals may support a bullish outlook."
            ),
            "Negative": (
                "The model predicts IHSG movement for the next "
                "trading day based on news sentiment and historical "
                "patterns. Negative signals may indicate bearish pressure."
            ),
            "Neutral": (
                "The model predicts IHSG movement for the next "
                "trading day based on news sentiment and historical "
                "patterns. Neutral signals provide limited directional guidance."
            ),
        }.get(label, "")

        st.markdown(
            f"""
            <div class="insight-card" style="border-left:3px solid #D97706;">
                <div class="insight-card-header">
                    <span class="insight-card-title">Prediction Insight</span>
                </div>
                <div class="insight-card-body">{insight_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    st.warning(
        "Important: One news headline alone should never be used "
        "as the sole basis for investment decisions. Professional investors "
        "evaluate multiple sources alongside macroeconomic indicators."
    )
