"""
Stock Market Intelligence Dashboard
Economic News Sentiment Analysis for IHSG Forecasting
"""

from pathlib import Path
import streamlit as st

from config import APP_TITLE
from data_loader import (
    load_news_dataset,
    load_forecasting_dataset,
    load_feature_importance,
    load_model,
)
from sentiment_service import analyze_news
from components import (
    render_header,
    render_kpi,
    render_news_analysis,
    render_business_insight,
    render_prediction,
    render_price_chart,
    render_sentiment_donut,
    render_feature_importance,
    render_dataset_information,
    render_disclaimer,
)


# ======================================================
# Page Config
# ======================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ======================================================
# Load CSS
# ======================================================

css_path = Path(__file__).parent / "assets" / "style.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================================================
# Load Resources
# ======================================================

@st.cache_resource
def load_resources():
    return (
        load_news_dataset(),
        load_forecasting_dataset(),
        load_feature_importance(),
        load_model(),
    )

news_df, forecasting_df, feature_df, model = load_resources()

# ======================================================
# Sidebar
# ======================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-brand-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                     stroke="white" stroke-width="2.5"
                     stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/>
                    <polyline points="16 7 22 7 22 13"/>
                </svg>
            </div>
            <div class="sidebar-brand-text">
                <div class="sidebar-brand-title">Stock Sentiment</div>
                <div class="sidebar-brand-sub">Dashboard</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-nav-label">Menu</div>', unsafe_allow_html=True)

    pages = [
        "Overview",
        "Sentiment Analysis",
        "Business Insights",
        "Forecasting",
        "Feature Importance",
        "Dataset Overview",
    ]

    if "active_page" not in st.session_state:
        st.session_state.active_page = "Overview"

    for page_name in pages:
        if st.button(page_name, key=f"nav_{page_name}", use_container_width=True):
            st.session_state.active_page = page_name
            st.rerun()

    st.markdown(
        """
        <div class="sidebar-about">
            Dashboard for analyzing economic news sentiment
            and predicting IHSG movement using Machine Learning.
            <div class="sidebar-built">Built with Streamlit</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ======================================================
# Main Content
# ======================================================

page = st.session_state.active_page

# ── Overview ──────────────────────────────────────────
if page == "Overview":

    render_header()
    render_kpi()

    st.divider()

    col_left, col_right = st.columns([1.1, 0.9])

    with col_left:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">
                    <span class="card-header-title">Analyze News Sentiment</span>
                </div>
                <p class="section-desc" style="margin-bottom:12px;">
                    Enter news text to analyze its sentiment and potential
                    impact on IHSG movement.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        headline = st.text_area(
            label="Economic News Headline",
            placeholder="Enter news text here...",
            height=120,
            max_chars=2000,
            label_visibility="collapsed",
        )

        st.caption(f"{len(headline)} / 2000")

        analyze_btn = st.button("Analyze News", use_container_width=True)

        st.caption("Supports up to 2000 characters")

    with col_right:
        render_sentiment_donut(news_df)

    st.divider()

    if analyze_btn:

        if not headline.strip():
            st.warning("Please enter an economic news headline first.")
            st.stop()

        result = analyze_news(headline)
        st.session_state.last_result   = result
        st.session_state.last_headline = headline

        render_news_analysis(headline, result)
        render_business_insight(result["label"])

    elif "last_result" in st.session_state:

        st.markdown(
            """
            <div class="card" style="border-left:3px solid #2563EB;">
                <div class="insight-card-body">
                    Showing results from your last analysis.
                    Submit a new headline to update.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_news_analysis(
            st.session_state.last_headline,
            st.session_state.last_result,
        )
        render_business_insight(st.session_state.last_result["label"])

    st.divider()

    col_a, col_b = st.columns([1, 1])

    with col_a:
        st.markdown(
            """
            <p class="section-title">Recent Analysis Results</p>
            <p class="section-desc">Latest sentiment analysis results.</p>
            """,
            unsafe_allow_html=True,
        )

        if "sentiment_label" in news_df.columns:
            sample = (
                news_df[["title", "sentiment_label", "sentiment_score"]]
                .dropna()
                .tail(5)
                .iloc[::-1]
                .reset_index(drop=True)
            )


            badge_map = {
                "Positive": ("positive", "+"),
                "Negative": ("negative", "-"),
                "Neutral":  ("neutral",  "~"),
            }

            rows_html = ""

            for _, row in sample.iterrows():
                label_cls, icon = badge_map.get(row["sentiment_label"], ("neutral", "~"))
                headline_short  = (
                    str(row["title"])[:60] + "..."
                    if len(str(row["title"])) > 60
                    else row["title"]
                )

                rows_html += f"""<tr>
                <td style="max-width:200px;">{headline_short}</td>
                <td>
                <span class="sentiment-badge {label_cls}">
                {icon} {row["sentiment_label"]}
                </span>
                </td>
                <td>{row["sentiment_score"]}</td>
                </tr>
                """

            st.markdown(
                f"""
            <table border="1">

            <thead>
            <tr>
            <th>News Text</th>
            <th>Sentiment</th>
            <th>Score</th>
            </tr>
            </thead>

            <tbody>

            {rows_html}

            </tbody>

            </table>
            """,
            unsafe_allow_html=True)

        else:
            st.info("No sentiment label column found in the news dataset.")

    with col_b:
        render_price_chart(forecasting_df)

# ── Sentiment Analysis ────────────────────────────────
elif page == "Sentiment Analysis":

    st.markdown(
        '<h2 style="font-size:22px;font-weight:800;margin-bottom:4px;">Sentiment Analysis</h2>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="section-desc">Analyze economic news headline sentiment.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    headline = st.text_area(
        "Economic News Headline",
        placeholder="Enter a news headline...",
        height=140,
    )

    if st.button("Analyze News", use_container_width=True):
        if not headline.strip():
            st.warning("Please enter a headline first.")
        else:
            result = analyze_news(headline)
            st.session_state.last_result   = result
            st.session_state.last_headline = headline
            render_news_analysis(headline, result)

# ── Business Insights ─────────────────────────────────
elif page == "Business Insights":

    st.markdown(
        '<h2 style="font-size:22px;font-weight:800;margin-bottom:4px;">Business Insights</h2>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="section-desc">Economic interpretation of sentiment signals.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    if "last_result" in st.session_state:
        render_business_insight(st.session_state.last_result["label"])
    else:
        st.info("Run a sentiment analysis first from the Overview or Sentiment Analysis page.")

# ── Forecasting ───────────────────────────────────────
elif page == "Forecasting":

    st.markdown(
        '<h2 style="font-size:22px;font-weight:800;margin-bottom:4px;">Forecasting</h2>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="section-desc">How sentiment feeds into the forecasting pipeline.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    if "last_result" in st.session_state:
        render_prediction(st.session_state.last_result)
    else:
        st.info("Run a sentiment analysis first from the Overview or Sentiment Analysis page.")

    st.divider()

    render_price_chart(forecasting_df)

# ── Feature Importance ────────────────────────────────
elif page == "Feature Importance":

    st.markdown(
        '<h2 style="font-size:22px;font-weight:800;margin-bottom:4px;">Feature Importance</h2>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="section-desc">Which features drive the Random Forest predictions.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    render_feature_importance(feature_df)

# ── Dataset Overview ──────────────────────────────────
elif page == "Dataset Overview":

    st.markdown(
        '<h2 style="font-size:22px;font-weight:800;margin-bottom:4px;">Dataset Overview</h2>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="section-desc">Summary of datasets used during model development.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    render_dataset_information(news_df, forecasting_df)

    st.divider()

    render_disclaimer()

