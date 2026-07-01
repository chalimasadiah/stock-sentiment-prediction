import streamlit as st


def render_news_analysis(headline, sentiment_result):
    """
    Display sentiment analysis result.
    """

    label = sentiment_result["label"]
    score = sentiment_result["score"]

    badge_class = {
        "Positive": "positive",
        "Negative": "negative",
        "Neutral":  "neutral",
    }.get(label, "neutral")

    badge_icon = {
        "Positive": "+",
        "Negative": "-",
        "Neutral":  "~",
    }.get(label, "~")

    score_color = {
        "Positive": "#16A34A",
        "Negative": "#DC2626",
        "Neutral":  "#D97706",
    }.get(label, "#475569")

    # Submitted Headline
    st.markdown(
        f"""
        <div class="card" style="margin-bottom:14px;">
            <div class="card-header">
                <span class="card-header-title">Submitted Headline</span>
            </div>
            <p style="font-size:14px;color:#0F172A;margin:0;line-height:1.6;">{headline}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sentiment + Score
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="kpi-label" style="margin-bottom:8px;">Sentiment</div>
                <span class="sentiment-badge {badge_class}">
                    {badge_icon} {label}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="kpi-label" style="margin-bottom:8px;">Sentiment Score</div>
                <div class="kpi-value" style="font-size:28px;color:{score_color};">{score}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

    # Keywords
    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Positive Keywords</span>
                </div>
            """,
            unsafe_allow_html=True
        )

        if sentiment_result["positive_keywords"]:
            tags = "".join(
                f'<span style="display:inline-block;background:#F0FDF4;'
                f'color:#16A34A;border:1px solid #BBF7D0;border-radius:6px;'
                f'padding:3px 10px;margin:3px 3px 3px 0;font-size:12px;font-weight:600;">'
                f'{kw}</span>'
                for kw in sentiment_result["positive_keywords"]
            )
            st.markdown(tags, unsafe_allow_html=True)
        else:
            st.markdown(
                '<p style="color:#94A3B8;font-size:13px;margin:0;">No positive keywords detected.</p>',
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Negative Keywords</span>
                </div>
            """,
            unsafe_allow_html=True
        )

        if sentiment_result["negative_keywords"]:
            tags = "".join(
                f'<span style="display:inline-block;background:#FEF2F2;'
                f'color:#DC2626;border:1px solid #FECACA;border-radius:6px;'
                f'padding:3px 10px;margin:3px 3px 3px 0;font-size:12px;font-weight:600;">'
                f'{kw}</span>'
                for kw in sentiment_result["negative_keywords"]
            )
            st.markdown(tags, unsafe_allow_html=True)
        else:
            st.markdown(
                '<p style="color:#94A3B8;font-size:13px;margin:0;">No negative keywords detected.</p>',
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
