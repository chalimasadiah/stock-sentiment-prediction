import streamlit as st


def render_prediction(sentiment_result):
    """
    Explain how the forecasting model
    uses sentiment information.
    No emoji.
    """

    label = sentiment_result["label"]
    score = sentiment_result["score"]

    st.markdown(
        """
        <p class="section-title">Forecasting Model</p>
        <p class="section-desc">
            This sentiment becomes one component in the feature engineering
            process. The Random Forest model was trained on 19 engineered
            features — not a single headline.
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        badge_class = {
            "Positive": "positive",
            "Negative": "negative",
            "Neutral":  "neutral",
        }.get(label, "neutral")

        score_color = {
            "Positive": "#16A34A",
            "Negative": "#DC2626",
            "Neutral":  "#D97706",
        }.get(label, "#475569")

        badge_icon = {"Positive": "+", "Negative": "-", "Neutral": "~"}.get(label, "~")

        st.markdown(
            f"""
            <div class="card" style="margin-bottom:12px;">
                <div class="kpi-label" style="margin-bottom:6px;">Detected Sentiment</div>
                <span class="sentiment-badge {badge_class}" style="font-size:14px;padding:6px 16px;">
                    {badge_icon} {label}
                </span>
            </div>

            <div class="card">
                <div class="kpi-label" style="margin-bottom:6px;">Sentiment Score</div>
                <div class="kpi-value" style="font-size:32px;color:{score_color};">
                    {score}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        if label == "Positive":
            interp       = (
                "Positive news contributes to a higher daily average sentiment. "
                "If similar positive news dominates the day, sentiment features "
                "used by the forecasting model may increase, potentially "
                "signalling a bullish direction."
            )
            bg    = "#F0FDF4"
            color = "#16A34A"
            arrow = "+"
        elif label == "Negative":
            interp = (
                "Negative news contributes to a lower daily average sentiment. "
                "If similar negative news dominates the day, sentiment features "
                "used by the forecasting model may decrease, potentially "
                "signalling a bearish direction."
            )
            bg    = "#FEF2F2"
            color = "#DC2626"
            arrow = "-"
        else:
            interp = (
                "Neutral news contributes only a small change to daily "
                "aggregated sentiment. Usually additional news is required "
                "before meaningful market sentiment changes occur."
            )
            bg    = "#FFFBEB"
            color = "#D97706"
            arrow = "~"

        st.markdown(
            f"""
            <div class="card" style="background:{bg};border-color:{color}30;height:100%;">
                <div class="card-header">
                    <span class="card-header-title" style="color:{color};">
                        Model Interpretation
                    </span>
                </div>
                <div class="insight-card-body">{interp}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    st.caption(
        "The actual Random Forest model was trained on 19 engineered features "
        "including historical IHSG prices, volume, technical indicators, and "
        "aggregated daily sentiment — not a single news headline."
    )
